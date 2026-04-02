/**
 * C5iSR Dashboard — Frontend Logic v3.0
 *
 * Features:
 *   - Dual mode: Backend FastAPI or CoinGecko demo
 *   - localStorage caching with TTL to reduce API hits
 *   - Sparkline mini-charts on price cards
 *   - Market cap top 10 rankings
 *   - Chart timeframe selector (7D/30D/90D/180D)
 *   - Persistent alert history
 *   - ETH gas price display
 *   - Fear & Greed with yesterday comparison
 *   - Retry with exponential backoff + rate limit handling
 *   - Market Intelligence Brief (regime + F&G + signal tally + top pick + assessment + Stewardship Score)
 *   - Signal cards show current price, stop-loss & take-profit targets
 *   - Backtest uses full 5-indicator computeSignal (consistent with live signals)
 *   - Structured Telegram report with full SL/TP/price data (no DOM scraping)
 *   - Keyboard shortcuts: R = refresh, C = copy report
 *   - Header flash on fresh data load
 *   - Gold (XAU) & Silver (XAG) live spot prices via metals.live (no key required)
 *   - [v2.8] Prediction Tracker: logs BUY/SELL signals, evaluates WIN/LOSS/PENDING vs SL/TP
 *   - [v2.8] Weekly Report Archive: daily intelligence brief snapshots with accordion view
 *   - [v2.9] Portfolio allocation bars: visual % breakdown + signal-alignment highlights
 *   - [v2.9] Metals: 3rd fallback via fawazahmed0 CDN + XAU:BTC ratio display
 *   - [v3.0] Sticky Key Price Ticker: always-visible BTC/ETH/NEO/XAU/XAG strip below header
 *   - [v3.0] Prediction Range Bars: visual SL→current→TP progress bar for PENDING signals
 */

// ── Config ──
const API_BASE = localStorage.getItem('c5isr_api') || '';
const COINGECKO = 'https://api.coingecko.com/api/v3';
const REFRESH_INTERVAL = 30;
const MAX_RETRIES = 3;
const RETRY_DELAY_MS = 1000;
const CACHE_TTL_MS = 25000; // 25s cache (refresh is 30s)
const CACHE_TTL_LONG = 120000; // 2 min for trending/rankings
const ASSETS = {
  bitcoin:            { symbol: 'BTC', name: 'Bitcoin',  color: '#f7931a' },
  ethereum:           { symbol: 'ETH', name: 'Ethereum', color: '#627eea' },
  neo:                { symbol: 'NEO', name: 'NEO',      color: '#00e599' },
  'flamingo-finance': { symbol: 'FLM', name: 'Flamingo', color: '#fc5c7d' },
  solana:             { symbol: 'SOL', name: 'Solana',   color: '#9945ff' },
};

let backendOnline = false;
let refreshCountdown = REFRESH_INTERVAL;
let refreshInterval = null;
let chart = null;
let candleSeries = null;
let volumeSeries = null;
let currentChartAsset = 'bitcoin';
let currentChartDays = 30;

// ── Auth Check ──
if (localStorage.getItem('c5isr_auth') !== 'true') {
  window.location.href = 'index.html';
}

// ── Cache Layer ──
const cache = {
  set(key, data, ttl = CACHE_TTL_MS) {
    try {
      localStorage.setItem(`c5_cache_${key}`, JSON.stringify({
        data, expires: Date.now() + ttl
      }));
    } catch { /* quota exceeded — ignore */ }
  },
  get(key) {
    try {
      const raw = localStorage.getItem(`c5_cache_${key}`);
      if (!raw) return null;
      const { data, expires } = JSON.parse(raw);
      if (Date.now() > expires) {
        localStorage.removeItem(`c5_cache_${key}`);
        return null;
      }
      return data;
    } catch { return null; }
  }
};

// ── Retry Fetch with Exponential Backoff ──
async function fetchWithRetry(url, options = {}, retries = MAX_RETRIES) {
  for (let i = 0; i < retries; i++) {
    try {
      const r = await fetch(url, { signal: AbortSignal.timeout(12000), ...options });
      if (r.status === 429) {
        const retryAfter = r.headers.get('Retry-After');
        const wait = retryAfter ? parseInt(retryAfter) * 1000 : Math.min(RETRY_DELAY_MS * Math.pow(2, i), 15000);
        showToast(`Rate limited — retrying in ${(wait/1000).toFixed(0)}s`, 'info');
        await new Promise(res => setTimeout(res, wait));
        continue;
      }
      if (!r.ok && i < retries - 1) {
        await new Promise(res => setTimeout(res, RETRY_DELAY_MS * Math.pow(2, i)));
        continue;
      }
      return r;
    } catch (e) {
      if (i === retries - 1) throw e;
      await new Promise(res => setTimeout(res, RETRY_DELAY_MS * Math.pow(2, i)));
    }
  }
  throw new Error('Max retries exceeded');
}

// Cached fetch helper
async function cachedFetch(cacheKey, url, ttl = CACHE_TTL_MS) {
  const cached = cache.get(cacheKey);
  if (cached) return cached;
  const r = await fetchWithRetry(url);
  const data = await r.json();
  cache.set(cacheKey, data, ttl);
  return data;
}

// ── Toast Notifications ──
function showToast(msg, type = 'info') {
  const existing = document.querySelectorAll('.toast');
  existing.forEach(t => t.remove());
  const t = document.createElement('div');
  t.className = `toast toast-${type}`;
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 3500);
}

// ── Init ──
document.addEventListener('DOMContentLoaded', async () => {
  loadScripture();
  await checkBackend();
  initChart();
  setupChartButtons();
  setupTimeframeButtons();

  // Load in parallel, stagger CoinGecko calls slightly to avoid rate limits
  await Promise.allSettled([
    loadPrices(),
    loadGlobalStats(),
    loadFearGreed(),
  ]);
  // Second batch after a brief pause
  await new Promise(r => setTimeout(r, 500));
  await Promise.allSettled([
    loadSignals(),
    loadChartData(currentChartAsset, currentChartDays),
    loadBacktest(),
  ]);
  await new Promise(r => setTimeout(r, 500));
  await Promise.allSettled([
    loadTrending(),
    loadMarketRankings(),
    loadMetals(),
  ]);

  startRefreshTimer();
  updateLastUpdated();
  setupKeyboardShortcuts();
});

// ── Keyboard Shortcuts ──
// R = force refresh now, C = copy signal report
function setupKeyboardShortcuts() {
  document.addEventListener('keydown', (e) => {
    // Ignore when typing in inputs
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 'r' || e.key === 'R') {
      showToast('⚡ Refreshing…', 'info');
      Promise.allSettled([loadPrices(), loadSignals(), loadFearGreed(), loadGlobalStats()]).then(() => {
        updateLastUpdated();
        flashHeader();
      });
    } else if (e.key === 'c' || e.key === 'C') {
      copySignalReport();
    }
  });
}

// ── Header Flash (visual feedback on data refresh) ──
function flashHeader() {
  const header = document.querySelector('.header');
  if (!header) return;
  header.style.transition = 'box-shadow 0.2s ease';
  header.style.boxShadow = '0 0 20px rgba(0,255,136,0.4)';
  setTimeout(() => { header.style.boxShadow = ''; }, 800);
}

// ── Backend Check ──
async function checkBackend() {
  if (!API_BASE) { setStatus(false); return; }
  try {
    const r = await fetch(`${API_BASE}/api/health`, { signal: AbortSignal.timeout(5000) });
    backendOnline = r.ok;
  } catch { backendOnline = false; }
  setStatus(backendOnline);
}

function setStatus(online) {
  const dot = document.getElementById('statusDot');
  const txt = document.getElementById('statusText');
  if (online) {
    dot.style.background = 'var(--green)';
    dot.classList.add('status-online');
    txt.textContent = 'Backend Online';
  } else {
    dot.style.background = 'var(--amber)';
    dot.classList.remove('status-online');
    txt.textContent = 'Demo Mode (CoinGecko)';
  }
}

function updateLastUpdated() {
  const el = document.getElementById('lastUpdated');
  if (el) el.textContent = `Updated ${new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' })}`;
}

// ── Price Loading with Sparklines ──
async function loadPrices() {
  try {
    let prices;
    if (backendOnline) {
      const token = localStorage.getItem('c5isr_token') || '';
      const r = await fetch(`${API_BASE}/api/prices`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      const data = await r.json();
      prices = data.prices;
    } else {
      prices = await fetchCoinGeckoPrices();
    }
    renderPrices(prices);
    // Load sparklines in background
    loadSparklines();
  } catch (e) {
    console.error('Price load failed:', e);
    try {
      const prices = await fetchCoinGeckoPrices();
      renderPrices(prices);
    } catch {
      document.getElementById('priceGrid').innerHTML = '<div class="card error-card">⚠️ Failed to load prices. Retrying...</div>';
    }
  }
}

async function fetchCoinGeckoPrices() {
  const ids = Object.keys(ASSETS).join(',');
  const data = await cachedFetch('prices', `${COINGECKO}/simple/price?ids=${ids}&vs_currencies=usd&include_24hr_change=true&include_24hr_vol=true&include_market_cap=true`);
  return Object.entries(ASSETS).map(([id, info]) => ({
    id,
    symbol: info.symbol,
    name: info.name,
    price: data[id]?.usd || 0,
    change_24h: data[id]?.usd_24h_change || 0,
    volume_24h: data[id]?.usd_24h_vol || 0,
    market_cap: data[id]?.usd_market_cap || 0,
  }));
}

function renderPrices(prices) {
  const grid = document.getElementById('priceGrid');
  grid.innerHTML = prices.map(p => {
    const change = p.change_24h || 0;
    const isUp = change >= 0;
    const arrow = isUp ? '▲' : '▼';
    const cls = isUp ? 'positive' : 'negative';
    const mcap = p.market_cap ? formatCompact(p.market_cap) : '';
    return `
      <div class="card card-animate price-card price-card-clickable" data-asset="${p.id}" title="Click to view ${ASSETS[p.id]?.name || p.name} chart" onclick="switchChartFromCard('${p.id}')">
        <div style="display:flex;justify-content:space-between;align-items:flex-start">
          <div>
            <div class="price-symbol" style="color:${ASSETS[p.id]?.color || '#fff'}">${ASSETS[p.id]?.symbol || p.symbol}</div>
            <div class="price-name">${ASSETS[p.id]?.name || p.name}</div>
          </div>
          <div class="sparkline-container" id="sparkline-${p.id}"></div>
        </div>
        <div class="price-value">$${formatPrice(p.price)}</div>
        <div style="display:flex;justify-content:space-between;align-items:center">
          <div class="price-change ${cls}">${arrow} ${Math.abs(change).toFixed(2)}%</div>
          <div class="price-mcap">${mcap}</div>
        </div>
        <div class="price-card-hint">📈 tap for chart</div>
      </div>`;
  }).join('');
}

function switchChartFromCard(assetId) {
  if (!ASSETS[assetId]) return;
  // Update chart asset buttons
  document.querySelectorAll('.chart-asset-btn').forEach(b => {
    b.classList.remove('active'); b.style.borderColor = ''; b.style.color = '';
  });
  const assetBtn = document.querySelector(`.chart-asset-btn[data-asset="${assetId}"]`);
  if (assetBtn) { assetBtn.classList.add('active'); assetBtn.style.borderColor = 'var(--green)'; assetBtn.style.color = 'var(--green)'; }
  currentChartAsset = assetId;
  loadChartData(currentChartAsset, currentChartDays);
  // Highlight the active price card
  document.querySelectorAll('.price-card-clickable').forEach(c => c.classList.remove('price-card-active'));
  const card = document.querySelector(`.price-card-clickable[data-asset="${assetId}"]`);
  if (card) card.classList.add('price-card-active');
  // Scroll smoothly to chart
  const chartSection = document.getElementById('mainChart');
  if (chartSection) { chartSection.closest('.card')?.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
}

// ── Sparklines ──
async function loadSparklines() {
  for (const id of Object.keys(ASSETS)) {
    try {
      const data = cache.get(`spark_${id}`) || await (async () => {
        const r = await fetchWithRetry(`${COINGECKO}/coins/${id}/market_chart?vs_currency=usd&days=7&interval=daily`);
        const d = await r.json();
        cache.set(`spark_${id}`, d.prices, CACHE_TTL_LONG);
        return d.prices;
      })();
      const prices = Array.isArray(data) ? data.map(p => Array.isArray(p) ? p[1] : p) : [];
      if (prices.length >= 2) drawSparkline(`sparkline-${id}`, prices, ASSETS[id]?.color || '#00ff88');
    } catch { /* sparkline is non-critical */ }
    await new Promise(r => setTimeout(r, 200)); // stagger
  }
}

function drawSparkline(containerId, prices, color) {
  const container = document.getElementById(containerId);
  if (!container) return;
  const w = 80, h = 32;
  const min = Math.min(...prices);
  const max = Math.max(...prices);
  const range = max - min || 1;
  const points = prices.map((p, i) => {
    const x = (i / (prices.length - 1)) * w;
    const y = h - ((p - min) / range) * h;
    return `${x.toFixed(1)},${y.toFixed(1)}`;
  }).join(' ');
  const isUp = prices[prices.length - 1] >= prices[0];
  const lineColor = isUp ? 'var(--green)' : 'var(--red)';
  container.innerHTML = `<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}"><polyline points="${points}" fill="none" stroke="${lineColor}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
}

// ── Signal Loading ──
async function loadSignals() {
  try {
    let signals;
    if (backendOnline) {
      const token = localStorage.getItem('c5isr_token') || '';
      const r = await fetch(`${API_BASE}/api/signals`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      const data = await r.json();
      signals = data.signals;
    } else {
      signals = await generateDemoSignals();
    }
    window._lastSignals = signals; // cache for structured report
    renderSignals(signals);
    updateRegime(signals);
    updateDCA(signals);
    updateRisk(signals);
    updateAlertLog(signals);
    updateIntelBrief(signals, null);
  } catch (e) {
    console.error('Signal load failed:', e);
    document.getElementById('signalGrid').innerHTML = '<div class="card error-card">⚠️ Signal computation failed</div>';
  }
}

async function generateDemoSignals() {
  const signals = [];
  for (const [id, info] of Object.entries(ASSETS)) {
    try {
      const cacheKey = `ohlc_${id}_30`;
      const ohlc = await cachedFetch(cacheKey, `${COINGECKO}/coins/${id}/ohlc?vs_currency=usd&days=30`, CACHE_TTL_MS);
      if (!Array.isArray(ohlc) || ohlc.length < 30) {
        signals.push({ asset_id: id, symbol: info.symbol, signal: 'HOLD', confidence: 50, reason: 'Insufficient data' });
        continue;
      }
      const closes = ohlc.map(c => c[4]);
      signals.push(computeSignal(closes, id, info.symbol, ohlc));
    } catch {
      signals.push({ asset_id: id, symbol: info.symbol, signal: 'HOLD', confidence: 50, reason: 'Fetch error' });
    }
    await new Promise(r => setTimeout(r, 150)); // stagger
  }
  return signals;
}

// ── Client-Side Signal Computation ──
function computeSignal(prices, assetId, symbol, ohlc = null) {
  const rsiVal = calcRSI(prices, 14);
  const macdData = calcMACD(prices);
  const bb = calcBB(prices);
  const ema20 = calcEMA(prices, 20);
  const ema50 = calcEMA(prices, 50);
  const ema200 = calcEMA(prices, 200);
  const stochRSI = calcStochRSI(prices);
  const atr = ohlc ? calcATR(ohlc) : null;
  const currentPrice = prices[prices.length - 1];

  const buySignals = [];
  const sellSignals = [];

  if (rsiVal !== null) {
    if (rsiVal < 35) buySignals.push(`RSI oversold (${rsiVal.toFixed(1)})`);
    else if (rsiVal > 70) sellSignals.push(`RSI overbought (${rsiVal.toFixed(1)})`);
  }

  if (macdData.bullishCross) buySignals.push('MACD bullish crossover');
  if (macdData.bearishCross) sellSignals.push('MACD bearish crossover');

  if (bb.position === 'below_lower') buySignals.push('Price at lower BB');
  else if (bb.position === 'above_upper') sellSignals.push('Price at upper BB');

  if (ema200 !== null) {
    if (currentPrice > ema200) buySignals.push('Above EMA 200');
    else sellSignals.push('Below EMA 200');
  }

  // StochRSI: 5th confluence indicator
  if (stochRSI.k !== null) {
    if (stochRSI.k < 20 && stochRSI.k > stochRSI.d) buySignals.push(`StochRSI oversold+cross (${stochRSI.k.toFixed(0)})`);
    else if (stochRSI.k > 80 && stochRSI.k < stochRSI.d) sellSignals.push(`StochRSI overbought+cross (${stochRSI.k.toFixed(0)})`);
  }

  let regime = 'SIDEWAYS';
  if (ema20 && ema50 && ema200) {
    if (ema20 > ema50 && ema50 > ema200) regime = 'BULL';
    else if (ema20 < ema50 && ema50 < ema200) regime = 'BEAR';
  }

  // Scale confidence over 5 indicators now
  let signal, confidence;
  if (buySignals.length >= 2 && buySignals.length > sellSignals.length) {
    signal = 'BUY'; confidence = Math.min((buySignals.length / 5) * 100, 100);
  } else if (sellSignals.length >= 2 && sellSignals.length > buySignals.length) {
    signal = 'SELL'; confidence = Math.min((sellSignals.length / 5) * 100, 100);
  } else {
    signal = 'HOLD'; confidence = 50;
  }

  // ATR-based dynamic stop-loss (1.5× ATR) vs fixed pct fallback
  const isVolatile = ['BTC', 'ETH', 'SOL'].includes(symbol);
  let slPrice, slPct, tpPrice;
  if (atr !== null && atr > 0) {
    slPrice = round2(currentPrice - 1.5 * atr);
    slPct = round2(((currentPrice - slPrice) / currentPrice) * 100);
    tpPrice = round2(currentPrice + 3 * atr); // 1:2 risk/reward
  } else {
    slPct = isVolatile ? 8 : 5;
    slPrice = currentPrice * (1 - slPct / 100);
    tpPrice = currentPrice * (1 + (slPct * 2) / 100);
  }

  const result = {
    asset_id: assetId, symbol, signal,
    confidence: Math.round(confidence * 10) / 10,
    reason: [...buySignals, ...sellSignals].join(' | ') || 'No strong confluence',
    buy_signals: buySignals, sell_signals: sellSignals,
    rsi: rsiVal, macd: macdData.line, macd_signal: macdData.signal,
    bb_position: bb.position,
    stoch_rsi: stochRSI,
    atr: atr ? round2(atr) : null,
    ema_trend: ema200 ? (currentPrice > ema200 ? 'uptrend' : 'downtrend') : 'unknown',
    market_regime: regime,
    indicators: {
      current_price: currentPrice, rsi: rsiVal,
      macd: { macd_line: macdData.line, signal_line: macdData.signal, histogram: macdData.histogram },
      bollinger: { upper: bb.upper, middle: bb.middle, lower: bb.lower },
      ema: { ema_20: ema20, ema_50: ema50, ema_200: ema200, regime },
      stoch_rsi: stochRSI,
      atr: atr ? round2(atr) : null,
    },
    risk: {
      stop_loss_pct: slPct, stop_loss_price: round2(slPrice),
      take_profit_price: round2(tpPrice), max_position_usd: 2500, risk_reward_ratio: '1:2',
      atr_based: atr !== null,
    },
  };

  if (signal === 'BUY') {
    result.dca_plan = {
      strategy: '3-Tranche DCA', total_position_usd: 2500,
      tranches: [
        { tranche: 1, entry_price: round2(currentPrice), amount_usd: 833, pct_of_position: 33.3 },
        { tranche: 2, entry_price: round2(currentPrice * 0.98), amount_usd: 833, pct_of_position: 33.3 },
        { tranche: 3, entry_price: round2(currentPrice * 0.96), amount_usd: 834, pct_of_position: 33.3 },
      ],
      avg_entry_price: round2(currentPrice * 0.98),
    };
  }
  return result;
}

// ── Technical Indicator Functions ──
function calcRSI(prices, period = 14) {
  if (prices.length < period + 1) return null;
  let avgGain = 0, avgLoss = 0;
  for (let i = 1; i <= period; i++) {
    const d = prices[i] - prices[i - 1];
    if (d > 0) avgGain += d; else avgLoss -= d;
  }
  avgGain /= period; avgLoss /= period;
  for (let i = period + 1; i < prices.length; i++) {
    const d = prices[i] - prices[i - 1];
    avgGain = (avgGain * (period - 1) + Math.max(d, 0)) / period;
    avgLoss = (avgLoss * (period - 1) + Math.max(-d, 0)) / period;
  }
  if (avgLoss === 0) return 100;
  return 100 - (100 / (1 + avgGain / avgLoss));
}

function calcEMA(prices, period) {
  if (prices.length < period) return null;
  let ema = prices.slice(0, period).reduce((a, b) => a + b) / period;
  const m = 2 / (period + 1);
  for (let i = period; i < prices.length; i++) ema = (prices[i] - ema) * m + ema;
  return ema;
}

function calcMACD(prices) {
  const fast = 12, slow = 26, sig = 9;
  if (prices.length < slow + sig) return { line: null, signal: null, histogram: null, bullishCross: false, bearishCross: false };
  function emaArr(p, per) {
    const r = [];
    let e = p.slice(0, per).reduce((a, b) => a + b) / per;
    for (let i = 0; i < per; i++) r.push(null);
    r[per - 1] = e;
    const m = 2 / (per + 1);
    for (let i = per; i < p.length; i++) { e = (p[i] - e) * m + e; r.push(e); }
    return r;
  }
  const ef = emaArr(prices, fast), es = emaArr(prices, slow);
  const ml = ef.map((f, i) => f !== null && es[i] !== null ? f - es[i] : null);
  const valid = ml.filter(v => v !== null);
  const sl = valid.length >= sig ? (() => {
    let e = valid.slice(0, sig).reduce((a, b) => a + b) / sig;
    const r = Array(sig - 1).fill(null); r.push(e);
    const m = 2 / (sig + 1);
    for (let i = sig; i < valid.length; i++) { e = (valid[i] - e) * m + e; r.push(e); }
    return r;
  })() : [];
  const line = valid.length ? valid[valid.length - 1] : null;
  const signal = sl.length ? sl[sl.length - 1] : null;
  const histogram = line !== null && signal !== null ? line - signal : null;
  let bullishCross = false, bearishCross = false;
  if (valid.length >= 2 && sl.length >= 2) {
    const m1 = valid[valid.length - 2], m2 = valid[valid.length - 1];
    const s1 = sl[sl.length - 2], s2 = sl[sl.length - 1];
    if (s1 !== null && s2 !== null) {
      if (m1 < s1 && m2 > s2) bullishCross = true;
      if (m1 > s1 && m2 < s2) bearishCross = true;
    }
  }
  return { line, signal, histogram, bullishCross, bearishCross };
}

function calcBB(prices, period = 20) {
  if (prices.length < period) return { upper: null, middle: null, lower: null, position: 'unknown' };
  const slice = prices.slice(-period);
  const middle = slice.reduce((a, b) => a + b) / period;
  const std = Math.sqrt(slice.reduce((s, v) => s + (v - middle) ** 2, 0) / period);
  const upper = middle + 2 * std, lower = middle - 2 * std;
  const price = prices[prices.length - 1];
  let position = 'upper_half';
  if (price >= upper) position = 'above_upper';
  else if (price <= lower) position = 'below_lower';
  else if (price < middle) position = 'lower_half';
  return { upper, middle, lower, position };
}

// ── Stochastic RSI ──
function calcRSIArray(prices, period = 14) {
  if (prices.length < period + 1) return [];
  const result = [];
  let avgGain = 0, avgLoss = 0;
  for (let i = 1; i <= period; i++) {
    const d = prices[i] - prices[i - 1];
    if (d > 0) avgGain += d; else avgLoss -= d;
  }
  avgGain /= period; avgLoss /= period;
  result.push(avgLoss === 0 ? 100 : 100 - (100 / (1 + avgGain / avgLoss)));
  for (let i = period + 1; i < prices.length; i++) {
    const d = prices[i] - prices[i - 1];
    avgGain = (avgGain * (period - 1) + Math.max(d, 0)) / period;
    avgLoss = (avgLoss * (period - 1) + Math.max(-d, 0)) / period;
    result.push(avgLoss === 0 ? 100 : 100 - (100 / (1 + avgGain / avgLoss)));
  }
  return result;
}

function calcStochRSI(prices, rsiPeriod = 14, stochPeriod = 14) {
  const rsiArr = calcRSIArray(prices, rsiPeriod);
  if (rsiArr.length < stochPeriod) return { k: null, d: null };
  const recent = rsiArr.slice(-stochPeriod);
  const minR = Math.min(...recent), maxR = Math.max(...recent);
  const range = maxR - minR;
  const lastRSI = rsiArr[rsiArr.length - 1];
  const k = range === 0 ? 50 : ((lastRSI - minR) / range) * 100;
  let d = k;
  if (rsiArr.length >= stochPeriod + 2) {
    const k3 = rsiArr.slice(-3).map(r => range === 0 ? 50 : ((r - minR) / range) * 100);
    d = k3.reduce((a, b) => a + b) / k3.length;
  }
  return { k: Math.round(k * 10) / 10, d: Math.round(d * 10) / 10 };
}

// ── ATR (Average True Range) for dynamic stop-loss ──
function calcATR(ohlc, period = 14) {
  if (!ohlc || ohlc.length < period + 1) return null;
  const tr = [];
  for (let i = 1; i < ohlc.length; i++) {
    const high = ohlc[i][2], low = ohlc[i][3], prevClose = ohlc[i - 1][4];
    tr.push(Math.max(high - low, Math.abs(high - prevClose), Math.abs(low - prevClose)));
  }
  if (tr.length < period) return null;
  let atr = tr.slice(0, period).reduce((a, b) => a + b) / period;
  for (let i = period; i < tr.length; i++) atr = (atr * (period - 1) + tr[i]) / period;
  return atr;
}

// ── Render Functions ──
// ── Indicator Pill Builder ──
function buildIndicatorPills(s) {
  const pills = [];

  // RSI pill
  if (s.rsi != null) {
    const v = s.rsi.toFixed(0);
    if (s.rsi < 35) pills.push({ label: `RSI ${v}`, type: 'bull' });
    else if (s.rsi > 70) pills.push({ label: `RSI ${v}`, type: 'bear' });
    else pills.push({ label: `RSI ${v}`, type: 'neutral' });
  }

  // MACD pill
  if (s.macd != null && s.macd_signal != null) {
    const bullCross = s.buy_signals?.some(b => b.includes('MACD'));
    const bearCross = s.sell_signals?.some(b => b.includes('MACD'));
    if (bullCross) pills.push({ label: 'MACD ↑', type: 'bull' });
    else if (bearCross) pills.push({ label: 'MACD ↓', type: 'bear' });
    else pills.push({ label: `MACD ${s.macd > 0 ? '+' : ''}${s.macd.toFixed(0)}`, type: s.macd > 0 ? 'bull-dim' : 'bear-dim' });
  }

  // Bollinger pill
  if (s.bb_position) {
    const bbMap = {
      below_lower: { label: 'BB Low ✓', type: 'bull' },
      above_upper: { label: 'BB High ✗', type: 'bear' },
      lower_half:  { label: 'BB Mid-Low', type: 'neutral' },
      upper_half:  { label: 'BB Mid-High', type: 'neutral' },
    };
    const p = bbMap[s.bb_position];
    if (p) pills.push(p);
  }

  // EMA Trend pill
  if (s.ema_trend) {
    pills.push({ label: s.ema_trend === 'uptrend' ? 'EMA ↑' : 'EMA ↓', type: s.ema_trend === 'uptrend' ? 'bull-dim' : 'bear-dim' });
  }

  // StochRSI pill
  if (s.stoch_rsi?.k != null) {
    const k = s.stoch_rsi.k;
    if (k < 20) pills.push({ label: `StochRSI ${k.toFixed(0)}`, type: 'bull' });
    else if (k > 80) pills.push({ label: `StochRSI ${k.toFixed(0)}`, type: 'bear' });
    else pills.push({ label: `StochRSI ${k.toFixed(0)}`, type: 'neutral' });
  }

  const typeStyles = {
    bull:     'background:rgba(0,255,136,0.18);color:#00ff88;border:1px solid rgba(0,255,136,0.35)',
    bear:     'background:rgba(255,51,85,0.18);color:#ff3355;border:1px solid rgba(255,51,85,0.35)',
    'bull-dim': 'background:rgba(0,255,136,0.08);color:rgba(0,255,136,0.6);border:1px solid rgba(0,255,136,0.15)',
    'bear-dim': 'background:rgba(255,51,85,0.08);color:rgba(255,51,85,0.6);border:1px solid rgba(255,51,85,0.15)',
    neutral:  'background:rgba(255,255,255,0.05);color:rgba(255,255,255,0.4);border:1px solid rgba(255,255,255,0.1)',
  };

  return pills.map(p =>
    `<span style="display:inline-block;padding:2px 7px;border-radius:4px;font-size:10px;font-family:var(--font-mono);margin:2px 2px 0 0;${typeStyles[p.type] || typeStyles.neutral}">${p.label}</span>`
  ).join('');
}

function renderSignals(signals) {
  const grid = document.getElementById('signalGrid');
  // Build a price lookup from currently rendered price cards
  const priceMap = {};
  document.querySelectorAll('.price-card-clickable').forEach(card => {
    const assetId = card.dataset.asset;
    const valEl = card.querySelector('.price-value');
    if (assetId && valEl) priceMap[assetId] = valEl.textContent.trim();
  });
  // Also pull from cached window state if set
  if (window._lastPrices) {
    window._lastPrices.forEach(p => {
      if (p.id && p.price) priceMap[p.id] = '$' + formatPrice(p.price);
    });
  }

  grid.innerHTML = signals.map(s => {
    const cls = s.signal === 'BUY' ? 'signal-buy' : s.signal === 'SELL' ? 'signal-sell' : 'signal-hold';
    const rsi = s.rsi != null ? s.rsi.toFixed(1) : '—';
    const rsiColor = s.rsi < 35 ? 'var(--green)' : s.rsi > 70 ? 'var(--red)' : 'var(--amber)';
    const rsiWidth = s.rsi != null ? s.rsi : 50;
    const confColor = s.confidence >= 70 ? 'var(--green)' : s.confidence >= 40 ? 'var(--amber)' : 'var(--red)';
    const pills = buildIndicatorPills(s);

    // Current price: prefer live indicator data, then priceMap, then stop-loss back-calc
    let currentPrice = s.indicators?.current_price || null;
    const priceDisplay = currentPrice
      ? `<span style="font-family:var(--font-mono);font-size:13px;color:var(--text-secondary)">$${formatPrice(currentPrice)}</span>`
      : (priceMap[s.asset_id]
          ? `<span style="font-family:var(--font-mono);font-size:13px;color:var(--text-secondary)">${priceMap[s.asset_id]}</span>`
          : '');

    // Stop-loss & take-profit mini row (only when relevant)
    const risk = s.risk;
    const riskHtml = (risk && s.signal !== 'HOLD' && risk.stop_loss_price > 0)
      ? `<div style="display:flex;gap:10px;margin-top:6px;font-family:var(--font-mono);font-size:10px;flex-wrap:wrap">
           <span style="color:var(--red)">SL $${formatPrice(risk.stop_loss_price)}</span>
           <span style="color:var(--green)">TP $${formatPrice(risk.take_profit_price)}</span>
           <span style="color:var(--text-muted)">${risk.risk_reward_ratio}</span>
         </div>`
      : '';

    return `
      <div class="card card-animate">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <div>
            <span style="font-family:var(--font-mono);font-weight:700;font-size:16px;color:${ASSETS[s.asset_id]?.color || '#fff'}">${s.symbol}</span>
            ${priceDisplay ? `<div style="margin-top:2px">${priceDisplay}</div>` : ''}
          </div>
          <span class="signal-badge ${cls}">${s.signal}</span>
        </div>
        <div style="margin-top:10px">
          <div class="rsi-value">RSI: <span style="color:${rsiColor}">${rsi}</span></div>
          <div class="rsi-gauge"><div class="rsi-gauge-fill" style="width:${rsiWidth}%;background:${rsiColor}"></div></div>
        </div>
        ${riskHtml}
        <div style="margin-top:8px;line-height:1.6">${pills}</div>
        <div class="confidence-bar" style="margin-top:8px"><div class="confidence-fill" style="width:${s.confidence}%;background:${confColor}"></div></div>
        <div style="text-align:right;font-size:11px;color:var(--text-muted);margin-top:4px">${s.confidence}% confidence</div>
      </div>`;
  }).join('');
}

function updateRegime(signals) {
  const btc = signals.find(s => s.symbol === 'BTC') || signals[0];
  const regime = btc?.market_regime || btc?.indicators?.ema?.regime || 'SIDEWAYS';
  const badge = document.getElementById('regimeBadge');
  const emoji = regime === 'BULL' ? '🐂' : regime === 'BEAR' ? '🐻' : '↔️';
  const cls = regime === 'BULL' ? 'regime-bull' : regime === 'BEAR' ? 'regime-bear' : 'regime-sideways';
  badge.className = `regime-badge ${cls}`;
  badge.textContent = `${emoji} ${regime}`;
  const emaInfo = btc?.indicators?.ema;
  const align = document.getElementById('emaAlignment');
  if (emaInfo) {
    align.innerHTML = `EMA20: $${formatPrice(emaInfo.ema_20)} | EMA50: $${formatPrice(emaInfo.ema_50)} | EMA200: $${formatPrice(emaInfo.ema_200)}`;
  }
}

function updateDCA(signals) {
  const buySignal = signals.find(s => s.signal === 'BUY' && s.dca_plan);
  const el = document.getElementById('dcaContent');
  if (!buySignal) {
    el.innerHTML = '<div style="text-align:center;padding:20px;color:var(--text-muted)">No active BUY signal — DCA inactive</div>';
    return;
  }
  const dca = buySignal.dca_plan;
  el.innerHTML = `
    <div style="font-family:var(--font-mono);font-size:14px;color:var(--green);margin-bottom:12px">${buySignal.symbol} — ${dca.strategy}</div>
    ${dca.tranches.map(t => `
      <div class="dca-tranche">
        <span class="dca-label">T${t.tranche}</span>
        <span class="dca-price">$${formatPrice(t.entry_price)}</span>
        <span class="dca-amount">$${t.amount_usd.toLocaleString()}</span>
        <span style="color:var(--text-muted)">${t.pct_of_position}%</span>
      </div>`).join('')}
    <div style="margin-top:12px;font-size:12px;color:var(--text-muted)">
      Avg Entry: $${formatPrice(dca.avg_entry_price)} | Total: $${dca.total_position_usd.toLocaleString()}
    </div>`;
}

function updateRisk(signals) {
  const el = document.getElementById('riskContent');
  const sig = signals.find(s => s.signal !== 'HOLD' && s.risk) || signals.find(s => s.symbol === 'BTC');
  if (!sig?.risk) { el.innerHTML = '<div style="color:var(--text-muted)">No risk data</div>'; return; }
  const r = sig.risk;
  el.innerHTML = `
    <div style="font-family:var(--font-mono);font-size:14px;margin-bottom:12px">${sig.symbol} Risk Profile</div>
    <div class="risk-row"><span class="risk-label">Stop-Loss${r.atr_based ? ' <span style="font-size:9px;color:var(--amber)">(ATR)</span>' : ''}</span><span class="risk-value risk-stop">$${formatPrice(r.stop_loss_price)} (${r.stop_loss_pct}%)</span></div>
    <div class="risk-row"><span class="risk-label">Take-Profit</span><span class="risk-value risk-target">$${formatPrice(r.take_profit_price)}</span></div>
    <div class="risk-row"><span class="risk-label">Max Position</span><span class="risk-value">$${r.max_position_usd?.toLocaleString() || '—'}</span></div>
    <div class="risk-row"><span class="risk-label">Risk/Reward</span><span class="risk-value">${r.risk_reward_ratio}</span></div>
    <div class="risk-row"><span class="risk-label">Max Portfolio Risk</span><span class="risk-value">${r.max_portfolio_risk_pct || 5}%</span></div>`;
}

// ── Alert History (Persistent) ──
function getAlertHistory() {
  try {
    return JSON.parse(localStorage.getItem('c5_alert_history') || '[]');
  } catch { return []; }
}

function saveAlertHistory(alerts) {
  try {
    localStorage.setItem('c5_alert_history', JSON.stringify(alerts.slice(0, 50))); // keep last 50
  } catch {}
}

function clearAlertHistory() {
  localStorage.removeItem('c5_alert_history');
  document.getElementById('alertLog').innerHTML = '<div style="color:var(--text-muted);padding:12px;text-align:center">Alert history cleared</div>';
}

// ── Market Intelligence Brief ──
function updateIntelBrief(signals, fearGreedValue) {
  const el = document.getElementById('intelBriefContent');
  if (!el) return;

  // Tally signals
  const buys = signals.filter(s => s.signal === 'BUY');
  const sells = signals.filter(s => s.signal === 'SELL');
  const holds = signals.filter(s => s.signal === 'HOLD');

  // Best buy candidate (highest confidence)
  const topBuy = buys.sort((a, b) => b.confidence - a.confidence)[0];
  const topSell = sells.sort((a, b) => b.confidence - a.confidence)[0];

  // Determine market bias
  const btcSignal = signals.find(s => s.symbol === 'BTC');
  const regime = btcSignal?.market_regime || btcSignal?.indicators?.ema?.regime || 'SIDEWAYS';
  const regimeEmoji = regime === 'BULL' ? '🐂' : regime === 'BEAR' ? '🐻' : '↔️';

  // Fear & Greed from current state
  const fgEl = document.getElementById('fearGreedValue');
  const fgText = fgEl ? fgEl.textContent.trim() : '—';
  const fgVal = fearGreedValue ?? (parseInt(fgText) || 50);
  const fgLabel = fgVal <= 25 ? 'Extreme Fear' : fgVal <= 45 ? 'Fear' : fgVal <= 55 ? 'Neutral' : fgVal <= 75 ? 'Greed' : 'Extreme Greed';
  const fgColor = fgVal <= 25 ? 'var(--red)' : fgVal <= 45 ? '#ff6644' : fgVal <= 55 ? 'var(--amber)' : fgVal <= 75 ? '#88dd44' : 'var(--green)';

  // Average confidence
  const allConf = signals.map(s => s.confidence);
  const avgConf = Math.round(allConf.reduce((a, b) => a + b, 0) / allConf.length);

  // ── Stewardship Score (0-100) ──
  // Composite of: regime (30pts) + F&G neutrality (20pts) + signal balance (30pts) + avg confidence (20pts)
  let ssRegime = regime === 'BULL' ? 30 : regime === 'BEAR' ? 10 : 20;
  // F&G: score peaks near neutral (50), drops at extremes
  const fgNeutral = 50 - Math.abs(fgVal - 50); // 0-50 → rescale to 0-20
  const ssFG = Math.round((fgNeutral / 50) * 20);
  // Signal balance: more BUYs = higher (max 30), net neutral = 15, all SELL = 0
  const total = signals.length || 1;
  const ssSignals = Math.round(((buys.length / total) * 30));
  // Confidence component (0-20)
  const ssConf = Math.round((avgConf / 100) * 20);
  const stewScore = Math.min(100, ssRegime + ssFG + ssSignals + ssConf);
  const stewGrade = stewScore >= 80 ? 'A' : stewScore >= 65 ? 'B' : stewScore >= 50 ? 'C' : stewScore >= 35 ? 'D' : 'F';
  const stewColor = stewScore >= 70 ? 'var(--green)' : stewScore >= 50 ? 'var(--amber)' : stewScore >= 35 ? '#ff6644' : 'var(--red)';
  const stewLabel = stewScore >= 80 ? 'Strong' : stewScore >= 65 ? 'Favorable' : stewScore >= 50 ? 'Neutral' : stewScore >= 35 ? 'Caution' : 'Risk-Off';

  // Build assessment
  let assessment = '';
  let assessColor = 'var(--text-muted)';
  if (buys.length >= 3 && regime === 'BULL') {
    assessment = '🟢 Strong bull confluence — broad BUY signals in uptrend. Consider scaling in with DCA.';
    assessColor = 'var(--green)';
  } else if (buys.length >= 2) {
    assessment = '🟡 Moderate bullish setup — selective entries. Prioritize highest-confidence signals.';
    assessColor = 'var(--amber)';
  } else if (sells.length >= 3 && regime === 'BEAR') {
    assessment = '🔴 Strong bear confluence — broad SELL signals in downtrend. Risk-off posture advised.';
    assessColor = 'var(--red)';
  } else if (sells.length >= 2) {
    assessment = '🟠 Bearish pressure building — reduce exposure or wait for reversal confirmation.';
    assessColor = '#ff6644';
  } else if (fgVal <= 20) {
    assessment = '💡 Extreme Fear often precedes reversals. Watch for BUY signal confluence before entering.';
    assessColor = '#88dd44';
  } else if (fgVal >= 80) {
    assessment = '⚠️ Extreme Greed — market likely overbought. Tighten stops, avoid chasing.';
    assessColor = 'var(--amber)';
  } else {
    assessment = '⏸ Mixed signals — no clear edge. Hold positions, wait for cleaner setups.';
    assessColor = 'var(--text-muted)';
  }

  // Top pick
  const topPick = topBuy || topSell;
  const topPickHtml = topPick
    ? `<div style="display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border-radius:6px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08)">
        <span style="font-family:var(--font-mono);font-weight:700;color:${ASSETS[topPick.asset_id]?.color || '#fff'}">${topPick.symbol}</span>
        <span class="signal-badge ${topPick.signal === 'BUY' ? 'signal-buy' : 'signal-sell'}" style="font-size:10px;padding:2px 7px">${topPick.signal}</span>
        <span style="font-size:11px;color:var(--text-muted)">${topPick.confidence}% conf</span>
      </div>`
    : '<span style="color:var(--text-muted);font-size:12px">No actionable picks</span>';

  el.innerHTML = `
    <div style="display:flex;flex-wrap:wrap;gap:16px;align-items:flex-start">
      <!-- Stats Row -->
      <div style="display:flex;gap:16px;flex-wrap:wrap;flex:1;min-width:280px">
        <div style="text-align:center;min-width:60px">
          <div style="font-family:var(--font-mono);font-size:20px;font-weight:700;color:var(--green)">${buys.length}</div>
          <div style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">BUY</div>
        </div>
        <div style="text-align:center;min-width:60px">
          <div style="font-family:var(--font-mono);font-size:20px;font-weight:700;color:var(--amber)">${holds.length}</div>
          <div style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">HOLD</div>
        </div>
        <div style="text-align:center;min-width:60px">
          <div style="font-family:var(--font-mono);font-size:20px;font-weight:700;color:var(--red)">${sells.length}</div>
          <div style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">SELL</div>
        </div>
        <div style="text-align:center;min-width:70px">
          <div style="font-family:var(--font-mono);font-size:20px;font-weight:700">${regimeEmoji} ${regime}</div>
          <div style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">Regime</div>
        </div>
        <div style="text-align:center;min-width:70px">
          <div style="font-family:var(--font-mono);font-size:20px;font-weight:700;color:${fgColor}">${fgVal}</div>
          <div style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">${fgLabel}</div>
        </div>
        <div style="text-align:center;min-width:70px">
          <div style="font-family:var(--font-mono);font-size:20px;font-weight:700;color:var(--text-secondary)">${avgConf}%</div>
          <div style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">Avg Conf</div>
        </div>
        <div style="text-align:center;min-width:80px;border-left:1px solid var(--border);padding-left:16px">
          <div style="font-family:var(--font-mono);font-size:22px;font-weight:700;color:${stewColor}">${stewScore}<span style="font-size:14px;opacity:0.7">/${stewGrade}</span></div>
          <div style="font-size:10px;color:${stewColor};text-transform:uppercase;letter-spacing:1px">Stewardship</div>
          <div style="font-size:9px;color:var(--text-muted);margin-top:2px">${stewLabel}</div>
        </div>
      </div>

      <!-- Top Pick + Assessment -->
      <div style="flex:2;min-width:260px;display:flex;flex-direction:column;gap:10px">
        <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
          <span style="font-size:11px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">Top Pick:</span>
          ${topPickHtml}
        </div>
        <div style="font-size:13px;color:${assessColor};line-height:1.5">${assessment}</div>
      </div>
    </div>`;

  document.getElementById('intelBriefTime').textContent = new Date().toLocaleTimeString();
}

function updateAlertLog(signals) {
  const el = document.getElementById('alertLog');
  const now = new Date();
  const newAlerts = signals
    .filter(s => s.signal !== 'HOLD')
    .map(s => ({
      time: now.toISOString(),
      timeStr: now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' }),
      dateStr: now.toLocaleDateString('en-US', { month: 'short', day: 'numeric' }),
      symbol: s.symbol,
      type: s.signal,
      msg: s.reason,
    }));

  // Merge with history (deduplicate by symbol+type within last 5 minutes)
  let history = getAlertHistory();
  for (const a of newAlerts) {
    const isDuplicate = history.some(h =>
      h.symbol === a.symbol && h.type === a.type &&
      (now - new Date(h.time)) < 300000
    );
    if (!isDuplicate) history.unshift(a);
  }
  history = history.slice(0, 50);
  saveAlertHistory(history);

  const display = history.slice(0, 10);
  if (display.length === 0) {
    el.innerHTML = '<div style="color:var(--text-muted);padding:12px;text-align:center">All clear — no actionable signals right now</div>';
    return;
  }

  el.innerHTML = display.map(a => {
    const color = a.type === 'BUY' ? 'var(--green)' : 'var(--red)';
    return `
      <div class="alert-item">
        <span class="alert-time">${a.dateStr} ${a.timeStr}</span>
        <span class="alert-symbol" style="color:${color}">${a.symbol}</span>
        <span class="signal-badge ${a.type === 'BUY' ? 'signal-buy' : 'signal-sell'}">${a.type}</span>
        <span class="alert-msg">${a.msg}</span>
      </div>`;
  }).join('');
}

// ── Backtest ──
async function loadBacktest() {
  const assetId = document.getElementById('backtestAsset').value;
  const el = document.getElementById('backtestContent');
  el.innerHTML = '<div class="spinner"></div>';
  try {
    let result;
    if (backendOnline) {
      const token = localStorage.getItem('c5isr_token') || '';
      const r = await fetch(`${API_BASE}/api/backtest/${assetId}?days=90`, { headers: { Authorization: `Bearer ${token}` } });
      result = await r.json();
    } else {
      const ohlc = await cachedFetch(`ohlc_${assetId}_90`, `${COINGECKO}/coins/${assetId}/ohlc?vs_currency=usd&days=90`, CACHE_TTL_LONG);
      if (!Array.isArray(ohlc) || ohlc.length < 50) {
        el.innerHTML = '<div style="color:var(--text-muted)">Insufficient data for backtest</div>';
        return;
      }
      result = runClientBacktest(ohlc, assetId);
    }
    renderBacktest(result);
  } catch (e) {
    el.innerHTML = `<div style="color:var(--red);font-size:12px">Backtest failed: ${e.message}</div>`;
  }
}

function runClientBacktest(ohlc, assetId) {
  const info = ASSETS[assetId] || { symbol: '???' };
  const closes = ohlc.map(c => c[4]);
  // Need sufficient history for all indicators (EMA-200 needs 200 points)
  const startIdx = Math.min(Math.max(50, ohlc.length - 90), ohlc.length - 10);
  if (closes.length < startIdx + 5) {
    return { symbol: info.symbol, error: 'Insufficient history for full backtest' };
  }

  let capital = 10000, position = 0, entryPrice = 0;
  let trades = 0, wins = 0, maxDD = 0, peak = capital;
  let lastSignal = 'HOLD';

  for (let i = startIdx; i < closes.length; i++) {
    const price = closes[i];
    const equity = capital + position * price;
    if (equity > peak) peak = equity;
    const dd = (peak - equity) / peak * 100;
    if (dd > maxDD) maxDD = dd;

    // Use the same full 5-indicator computeSignal used for live signals
    const slicePrices = closes.slice(0, i + 1);
    const sliceOhlc = ohlc.slice(0, i + 1);
    const sig = computeSignal(slicePrices, assetId, info.symbol, sliceOhlc);

    if (sig.signal === 'BUY' && lastSignal !== 'BUY' && position === 0 && capital > 0) {
      position = capital / price;
      entryPrice = price;
      capital = 0;
      lastSignal = 'BUY';
    } else if (sig.signal === 'SELL' && lastSignal !== 'SELL' && position > 0) {
      capital = position * price;
      trades++;
      if (price > entryPrice) wins++;
      position = 0;
      lastSignal = 'SELL';
    }
  }
  // Close any open position at last candle
  if (position > 0) {
    capital = position * closes[closes.length - 1];
    trades++;
    if (closes[closes.length - 1] > entryPrice) wins++;
  }
  return {
    symbol: info.symbol,
    total_return_pct: round2((capital - 10000) / 100),
    win_rate_pct: trades > 0 ? round2(wins / trades * 100) : 0,
    max_drawdown_pct: round2(maxDD),
    total_trades: trades,
    final_capital: round2(capital),
  };
}

function renderBacktest(bt) {
  if (bt.error) { document.getElementById('backtestContent').innerHTML = `<div style="color:var(--text-muted)">${bt.error}</div>`; return; }
  const retColor = bt.total_return_pct >= 0 ? 'var(--green)' : 'var(--red)';
  document.getElementById('backtestContent').innerHTML = `
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px">
      <div class="bt-stat"><div class="bt-stat-value" style="color:${retColor}">${bt.total_return_pct >= 0 ? '+' : ''}${bt.total_return_pct}%</div><div class="bt-stat-label">Total Return</div></div>
      <div class="bt-stat"><div class="bt-stat-value">${bt.win_rate_pct}%</div><div class="bt-stat-label">Win Rate</div></div>
      <div class="bt-stat"><div class="bt-stat-value" style="color:var(--red)">${bt.max_drawdown_pct}%</div><div class="bt-stat-label">Max Drawdown</div></div>
      <div class="bt-stat"><div class="bt-stat-value">${bt.total_trades}</div><div class="bt-stat-label">Total Trades</div></div>
    </div>
    <div style="text-align:center;margin-top:12px;font-size:12px;color:var(--text-muted)">
      Final: $${(bt.final_capital || 0).toLocaleString(undefined, {maximumFractionDigits: 2})}
    </div>`;
}

// ── Chart with Timeframe Selector ──
function initChart() {
  const container = document.getElementById('mainChart');
  chart = LightweightCharts.createChart(container, {
    width: container.clientWidth, height: 350,
    layout: { background: { type: 'solid', color: 'transparent' }, textColor: 'rgba(255,255,255,0.5)', fontFamily: 'JetBrains Mono' },
    grid: { vertLines: { color: 'rgba(255,255,255,0.03)' }, horzLines: { color: 'rgba(255,255,255,0.03)' } },
    crosshair: { mode: LightweightCharts.CrosshairMode.Normal },
    rightPriceScale: { borderColor: 'rgba(255,255,255,0.08)' },
    timeScale: { borderColor: 'rgba(255,255,255,0.08)', timeVisible: true },
  });
  candleSeries = chart.addCandlestickSeries({
    upColor: '#00ff88', downColor: '#ff3355',
    borderUpColor: '#00ff88', borderDownColor: '#ff3355',
    wickUpColor: '#00ff88', wickDownColor: '#ff3355',
  });
  volumeSeries = chart.addHistogramSeries({
    color: '#26a69a33', priceFormat: { type: 'volume' },
    priceScaleId: '', scaleMargins: { top: 0.85, bottom: 0 },
  });
  new ResizeObserver(() => { chart.applyOptions({ width: container.clientWidth }); }).observe(container);

  // Crosshair legend
  chart.subscribeCrosshairMove(param => {
    const legend = document.getElementById('chartLegend');
    if (!param.time || !param.seriesData) { legend.textContent = ''; return; }
    const ohlc = param.seriesData.get(candleSeries);
    if (ohlc) {
      const cls = ohlc.close >= ohlc.open ? 'positive' : 'negative';
      legend.innerHTML = `<span style="color:var(--text-muted)">O</span> $${formatPrice(ohlc.open)} <span style="color:var(--text-muted)">H</span> $${formatPrice(ohlc.high)} <span style="color:var(--text-muted)">L</span> $${formatPrice(ohlc.low)} <span style="color:var(--text-muted)">C</span> <span class="${cls}">$${formatPrice(ohlc.close)}</span>`;
    }
  });
}

async function loadChartData(assetId, days = 30) {
  try {
    const cacheKey = `chart_${assetId}_${days}`;
    const ohlc = await cachedFetch(cacheKey, `${COINGECKO}/coins/${assetId}/ohlc?vs_currency=usd&days=${days}`, CACHE_TTL_MS);
    if (!Array.isArray(ohlc)) return;
    const data = ohlc.map(c => ({ time: Math.floor(c[0] / 1000), open: c[1], high: c[2], low: c[3], close: c[4] }));
    // Estimate volume from price range
    const volData = data.map(d => ({
      time: d.time,
      value: Math.abs(d.high - d.low) * 1000,
      color: d.close >= d.open ? 'rgba(0,255,136,0.15)' : 'rgba(255,51,85,0.15)',
    }));
    candleSeries.setData(data);
    volumeSeries.setData(volData);
    chart.timeScale().fitContent();
    const titleEl = document.querySelector('.chart-container').closest('.card').querySelector('.card-title');
    if (titleEl) titleEl.textContent = `${ASSETS[assetId]?.symbol || '???'}/USD`;
  } catch (e) { console.error('Chart load failed:', e); }
}

function setupChartButtons() {
  document.querySelectorAll('.chart-asset-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.chart-asset-btn').forEach(b => { b.classList.remove('active'); b.style.borderColor = ''; b.style.color = ''; });
      btn.classList.add('active');
      btn.style.borderColor = 'var(--green)'; btn.style.color = 'var(--green)';
      currentChartAsset = btn.dataset.asset;
      loadChartData(currentChartAsset, currentChartDays);
    });
  });
  const active = document.querySelector('.chart-asset-btn.active');
  if (active) { active.style.borderColor = 'var(--green)'; active.style.color = 'var(--green)'; }
}

function setupTimeframeButtons() {
  document.querySelectorAll('.chart-tf-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.chart-tf-btn').forEach(b => { b.classList.remove('active'); b.style.borderColor = ''; b.style.color = ''; });
      btn.classList.add('active');
      btn.style.borderColor = 'var(--blue)'; btn.style.color = 'var(--blue)';
      currentChartDays = parseInt(btn.dataset.days);
      loadChartData(currentChartAsset, currentChartDays);
    });
  });
  const active = document.querySelector('.chart-tf-btn.active');
  if (active) { active.style.borderColor = 'var(--blue)'; active.style.color = 'var(--blue)'; }
}

// ── Refresh Timer ──
function startRefreshTimer() {
  refreshCountdown = REFRESH_INTERVAL;
  if (refreshInterval) clearInterval(refreshInterval);
  refreshInterval = setInterval(() => {
    refreshCountdown--;
    document.getElementById('refreshTimer').textContent = `${refreshCountdown}s`;
    if (refreshCountdown <= 0) {
      refreshCountdown = REFRESH_INTERVAL;
      loadPrices();
      loadSignals();
      loadChartData(currentChartAsset, currentChartDays);
      updateLastUpdated();
      flashHeader();
      if (!window._refreshCycle) window._refreshCycle = 0;
      window._refreshCycle++;
      if (window._refreshCycle % 2 === 0) { loadFearGreed(); loadGlobalStats(); }
      if (window._refreshCycle % 4 === 0) { loadTrending(); loadMarketRankings(); }
      if (window._refreshCycle % 8 === 0) { loadMetals(); } // Metals refresh every ~4 min (less volatile)
    }
  }, 1000);
}

// ── Gold & Silver Live Spot Prices ──
// Uses metals.live free public API (no key required)
// Falls back to frankfurter.app currency endpoint for XAU/XAG in USD
async function loadMetals() {
  const el = document.getElementById('metalsCard');
  if (!el) return;

  try {
    // metals.live provides XAU (oz) and XAG (oz) in USD — free, CORS-friendly
    const data = await cachedFetch('metals', 'https://metals.live/api/spot', 120000);
    // Response: [{ metal: "gold", price: 3123.45, currency: "USD", weight: "troy_ounce", change: 12.3, change_percentage: 0.4 }, ...]
    const gold = Array.isArray(data) ? data.find(m => m.metal === 'gold') : null;
    const silver = Array.isArray(data) ? data.find(m => m.metal === 'silver') : null;

    if (gold || silver) {
      renderMetals(gold, silver);
      return;
    }
  } catch (e) { /* fall through to backup */ }

  // Fallback: frankfurter.app converts XAU/XAG via ECB rates (less precise for metals but free)
  try {
    const [xauRes, xagRes] = await Promise.all([
      cachedFetch('xau_usd', 'https://api.frankfurter.app/latest?from=XAU&to=USD', 120000),
      cachedFetch('xag_usd', 'https://api.frankfurter.app/latest?from=XAG&to=USD', 120000),
    ]);
    const xauUsd = xauRes?.rates?.USD || null;
    const xagUsd = xagRes?.rates?.USD || null;
    if (xauUsd || xagUsd) {
      renderMetals(
        xauUsd ? { metal: 'gold',   price: xauUsd, currency: 'USD', change: null, change_percentage: null } : null,
        xagUsd ? { metal: 'silver', price: xagUsd, currency: 'USD', change: null, change_percentage: null } : null,
      );
      return;
    }
  } catch (e) { /* silent fallback failure */ }

  // 3rd fallback: fawazahmed0 currency API (daily rates, free CDN)
  try {
    const xauData = await cachedFetch('xau_fawaz', 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/xau.json', 120000);
    const xagData = await cachedFetch('xag_fawaz', 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/xag.json', 120000);
    const xauUsd = xauData?.xau?.usd ? (1 / xauData.xau.usd) : null;
    const xagUsd = xagData?.xag?.usd ? (1 / xagData.xag.usd) : null;
    if (xauUsd || xagUsd) {
      renderMetals(
        xauUsd ? { metal: 'gold',   price: xauUsd, currency: 'USD', change: null, change_percentage: null } : null,
        xagUsd ? { metal: 'silver', price: xagUsd, currency: 'USD', change: null, change_percentage: null } : null,
      );
      return;
    }
  } catch (e) { /* silent */ }

  // All sources failed — show graceful degraded state
  el.innerHTML = `
    <div class="metals-item">
      <div class="metals-symbol" style="color:#ffd700">XAU</div>
      <div class="metals-name">Gold</div>
      <div class="metals-price" style="color:var(--text-muted)">Unavailable</div>
    </div>
    <div class="metals-item">
      <div class="metals-symbol" style="color:#c0c0c0">XAG</div>
      <div class="metals-name">Silver</div>
      <div class="metals-price" style="color:var(--text-muted)">Unavailable</div>
    </div>`;
  const updEl = document.getElementById('metalsUpdated');
  if (updEl) updEl.textContent = 'API unavailable';
}

function renderMetals(gold, silver) {
  const el = document.getElementById('metalsCard');
  const updEl = document.getElementById('metalsUpdated');
  if (!el) return;

  const renderItem = (item, symbol, label, color) => {
    if (!item) return '';
    const price = item.price;
    const change = item.change_percentage;
    const isUp = change != null ? change >= 0 : null;
    const arrow = isUp === true ? '▲' : isUp === false ? '▼' : '';
    const changeStr = change != null
      ? `<div class="metals-change ${isUp ? 'positive' : 'negative'}">${arrow} ${Math.abs(change).toFixed(2)}%</div>`
      : '';
    const absDollarChange = item.change != null
      ? `<div style="font-size:10px;color:var(--text-muted);margin-top:2px">${item.change >= 0 ? '+' : ''}$${Math.abs(item.change).toFixed(2)}/oz</div>`
      : '';
    return `
      <div class="metals-item">
        <div>
          <div class="metals-symbol" style="color:${color}">${symbol}</div>
          <div class="metals-name">${label}</div>
        </div>
        <div style="text-align:right">
          <div class="metals-price">$${price >= 1000 ? price.toLocaleString(undefined, {minimumFractionDigits:2,maximumFractionDigits:2}) : price.toFixed(2)}</div>
          ${changeStr}
          ${absDollarChange}
        </div>
      </div>`;
  };

  // XAU:BTC ratio — how many oz of gold to buy 1 BTC
  const btcPrice = (_lastPriceMap && _lastPriceMap['bitcoin']) || (window._lastPrices && window._lastPrices.find(p => p.id === 'bitcoin')?.price) || null;
  let ratioHtml = '';
  if (gold && gold.price > 0 && btcPrice && btcPrice > 0) {
    const ratio = (btcPrice / gold.price).toFixed(1);
    ratioHtml = `
      <div class="metals-item" style="border-left:1px solid var(--border);padding-left:16px;margin-left:8px">
        <div>
          <div class="metals-symbol" style="color:#f7931a">BTC</div>
          <div class="metals-name">oz of Gold</div>
        </div>
        <div style="text-align:right">
          <div class="metals-price" style="color:#f7931a">${ratio} oz</div>
          <div style="font-size:10px;color:var(--text-muted);margin-top:2px">XAU:BTC ratio</div>
        </div>
      </div>`;
  }

  el.innerHTML = `
    ${renderItem(gold,   'XAU', 'Gold (troy oz)',   '#ffd700')}
    ${renderItem(silver, 'XAG', 'Silver (troy oz)', '#c0c0c0')}
    ${ratioHtml}`;

  if (updEl) updEl.textContent = new Date().toLocaleTimeString();

  // Update sticky price ticker with metals data
  updateTickerMetals(gold, silver);
}

// ── MetaMask ──
async function connectMetaMask() {
  if (typeof window.ethereum === 'undefined') {
    showToast('MetaMask not detected. Install the extension first.', 'error');
    return;
  }
  try {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const addr = accounts[0];
    const short = addr.slice(0, 6) + '...' + addr.slice(-4);
    document.getElementById('metamaskBtn').textContent = `🦊 ${short}`;
    document.getElementById('metamaskBtn').style.borderColor = 'var(--green)';
    document.getElementById('metamaskBtn').style.color = 'var(--green)';
    const walletInfo = document.getElementById('walletInfo');
    walletInfo.style.display = 'block';
    const balance = await window.ethereum.request({ method: 'eth_getBalance', params: [addr, 'latest'] });
    const ethBalance = parseInt(balance, 16) / 1e18;
    walletInfo.textContent = `${short} | ${ethBalance.toFixed(4)} ETH`;
    showToast(`Connected: ${short}`, 'success');
  } catch (e) { showToast('MetaMask connection failed', 'error'); }
}

// ── Portfolio Tracker ──
const PORTFOLIO_ASSETS = [
  { id: 'bitcoin',          symbol: 'BTC', color: '#f7931a' },
  { id: 'ethereum',         symbol: 'ETH', color: '#627eea' },
  { id: 'neo',              symbol: 'NEO', color: '#00e599' },
  { id: 'flamingo-finance', symbol: 'FLM', color: '#fc5c7d' },
  { id: 'solana',           symbol: 'SOL', color: '#9945ff' },
];

function getHoldings() {
  try { return JSON.parse(localStorage.getItem('c5_holdings') || '{}'); } catch { return {}; }
}
function saveHoldings(h) {
  try { localStorage.setItem('c5_holdings', JSON.stringify(h)); } catch {}
}

function updateHolding(assetId, qty, avgCost) {
  const h = getHoldings();
  if (!qty || isNaN(parseFloat(qty))) {
    delete h[assetId];
  } else {
    h[assetId] = { qty: parseFloat(qty), avgCost: parseFloat(avgCost) || 0 };
  }
  saveHoldings(h);
  renderPortfolio(null); // re-render with current prices if available
}

function clearHoldings() {
  localStorage.removeItem('c5_holdings');
  renderPortfolio(null);
}

// Call with live prices map { assetId -> price }
function renderPortfolio(pricesMap) {
  const holdings = getHoldings();
  const el = document.getElementById('portfolioContent');
  const totalEl = document.getElementById('portfolioTotal');

  let totalValue = 0, totalCost = 0;

  const rows = PORTFOLIO_ASSETS.map(asset => {
    const h = holdings[asset.id];
    const price = pricesMap ? (pricesMap[asset.id] || 0) : 0;
    const qty = h?.qty || '';
    const avgCost = h?.avgCost || '';
    const currentValue = h ? (h.qty * price) : 0;
    const costBasis = h ? (h.qty * (h.avgCost || 0)) : 0;
    const pnl = currentValue - costBasis;
    const pnlPct = costBasis > 0 ? (pnl / costBasis) * 100 : 0;
    const pnlColor = pnl >= 0 ? 'var(--green)' : 'var(--red)';

    if (h) { totalValue += currentValue; totalCost += costBasis; }

    const pnlStr = h && price
      ? `<span style="color:${pnlColor};font-family:var(--font-mono);font-size:12px">${pnl >= 0 ? '+' : ''}$${Math.abs(pnl).toFixed(2)} (${pnlPct >= 0 ? '+' : ''}${pnlPct.toFixed(1)}%)</span>`
      : '<span style="color:var(--text-muted);font-size:12px">—</span>';

    const valueStr = h && price
      ? `<span style="font-family:var(--font-mono);font-size:13px;color:var(--text-secondary)">$${formatPrice(currentValue)}</span>`
      : '<span style="color:var(--text-muted);font-size:12px">—</span>';

    return `
      <div class="portfolio-row">
        <div class="portfolio-asset">
          <span style="font-family:var(--font-mono);font-weight:700;color:${asset.color}">${asset.symbol}</span>
          ${price ? `<span style="font-size:11px;color:var(--text-muted)">@$${formatPrice(price)}</span>` : ''}
        </div>
        <div class="portfolio-inputs">
          <input class="portfolio-input" type="number" placeholder="Qty" step="any" min="0"
            value="${qty}" data-asset="${asset.id}" data-field="qty"
            onchange="onHoldingChange(this)" onblur="onHoldingChange(this)" />
          <input class="portfolio-input" type="number" placeholder="Avg cost" step="any" min="0"
            value="${avgCost}" data-asset="${asset.id}" data-field="cost"
            onchange="onHoldingChange(this)" onblur="onHoldingChange(this)" />
        </div>
        <div class="portfolio-pnl">
          ${valueStr}
          ${pnlStr}
        </div>
      </div>`;
  }).join('');

  el.innerHTML = `<div class="portfolio-table">${rows}</div>`;

  // Total row + allocation bars
  const totalPnl = totalValue - totalCost;
  const totalPnlPct = totalCost > 0 ? (totalPnl / totalCost) * 100 : 0;
  const totalColor = totalPnl >= 0 ? 'var(--green)' : 'var(--red)';

  // Current signals for alignment highlights
  const activeSignals = window._lastSignals || [];
  const signalMap = {};
  activeSignals.forEach(s => { signalMap[s.asset_id] = s.signal; });

  if (totalValue > 0) {
    // Build allocation bar segments
    const allocations = PORTFOLIO_ASSETS
      .filter(a => holdings[a.id] && (holdings[a.id].qty * ((pricesMap && pricesMap[a.id]) || 0)) > 0)
      .map(a => {
        const val = holdings[a.id].qty * (pricesMap[a.id] || 0);
        const pct = (val / totalValue * 100).toFixed(1);
        const sig = signalMap[a.id];
        const sigBorder = sig === 'BUY' ? `outline:2px solid var(--green);` : sig === 'SELL' ? `outline:2px solid var(--red);` : '';
        return `<div title="${a.symbol}: ${pct}% ($${formatPrice(val)})" style="flex:${pct};background:${a.color};height:100%;border-radius:2px;${sigBorder}transition:flex 0.4s"></div>`;
      })
      .join('');

    const allocLegend = PORTFOLIO_ASSETS
      .filter(a => holdings[a.id] && (holdings[a.id].qty * ((pricesMap && pricesMap[a.id]) || 0)) > 0)
      .map(a => {
        const val = holdings[a.id].qty * (pricesMap[a.id] || 0);
        const pct = (val / totalValue * 100).toFixed(1);
        const sig = signalMap[a.id];
        const sigBadge = sig && sig !== 'HOLD'
          ? `<span style="font-size:9px;padding:0 4px;border-radius:3px;background:${sig === 'BUY' ? 'var(--green-dim,rgba(0,255,136,0.15))' : 'rgba(255,68,68,0.15)'};color:${sig === 'BUY' ? 'var(--green)' : 'var(--red)'};">${sig}</span>`
          : '';
        return `<span style="display:inline-flex;align-items:center;gap:4px;font-size:11px;color:var(--text-muted)"><span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:${a.color}"></span>${a.symbol} ${pct}%${sigBadge}</span>`;
      })
      .join('<span style="color:var(--border);padding:0 4px">·</span>');

    totalEl.innerHTML = `
      <div style="margin-top:12px;border-top:1px solid var(--border);padding-top:10px">
        <div style="display:flex;gap:4px;height:8px;border-radius:4px;overflow:hidden;margin-bottom:8px">${allocations || '<div style="flex:1;background:var(--border);height:100%"></div>'}</div>
        <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:10px">${allocLegend}</div>
        <div style="display:flex;justify-content:flex-end;gap:24px">
          <div style="font-size:12px;color:var(--text-muted)">Total Value: <span style="color:var(--text-primary);font-family:var(--font-mono)">$${formatPrice(totalValue)}</span></div>
          <div style="font-size:12px;color:var(--text-muted)">P&L: <span style="color:${totalColor};font-family:var(--font-mono)">${totalPnl >= 0 ? '+' : ''}$${Math.abs(totalPnl).toFixed(2)} (${totalPnlPct >= 0 ? '+' : ''}${totalPnlPct.toFixed(1)}%)</span></div>
        </div>
      </div>`;
  } else {
    totalEl.innerHTML = '<div style="font-size:11px;color:var(--text-muted);text-align:center;padding-top:8px">Enter your holdings above to track live P&L</div>';
  }

  document.getElementById('portfolioUpdated').textContent = pricesMap ? new Date().toLocaleTimeString() : '—';
}

const _holdingChangeBuf = {};
function onHoldingChange(input) {
  const assetId = input.dataset.asset;
  if (!_holdingChangeBuf[assetId]) _holdingChangeBuf[assetId] = {};
  _holdingChangeBuf[assetId][input.dataset.field] = input.value;
  const row = _holdingChangeBuf[assetId];
  updateHolding(assetId, row.qty ?? '', row.cost ?? '');
}

// Expose for price refresh integration
let _lastPriceMap = {};

// Patch into renderPrices to also update portfolio + ticker
const _origRenderPrices = renderPrices;
function renderPrices(prices) {
  _origRenderPrices(prices);
  _lastPriceMap = {};
  prices.forEach(p => { _lastPriceMap[p.id] = p.price; });
  // Cache for signal card price display
  window._lastPrices = prices;
  renderPortfolio(_lastPriceMap);
  // Update sticky price ticker
  updateTicker(prices);
}

// ── Copy Signal Report (Telegram-ready) ──
// v2.6: Uses structured window._lastSignals instead of fragile DOM scraping
// Produces full-fidelity report with price, SL, TP, RSI, and confidence per signal
function copySignalReport() {
  const signals = window._lastSignals;
  if (!signals || !signals.length) {
    showToast('No signals loaded yet — wait for data', 'error');
    return;
  }

  const now = new Date();
  const dateStr = now.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' });
  const timeStr = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', timeZoneName: 'short' });

  // Regime from BTC signal data
  const btcSig = signals.find(s => s.symbol === 'BTC');
  const regime = btcSig?.market_regime || btcSig?.indicators?.ema?.regime || 'SIDEWAYS';
  const regimeEmoji = regime === 'BULL' ? '🐂' : regime === 'BEAR' ? '🐻' : '↔️';

  // Fear & Greed (display string only — not in structured signal data)
  const fgEl = document.getElementById('fearGreedValue');
  const fgTxt = fgEl ? fgEl.textContent.replace(/\s+/g, ' ').trim() : '—';

  // Market cap
  const mcap = document.getElementById('globalMarketCap')?.textContent?.trim() || '—';
  const mcapChange = document.getElementById('globalMarketCapChange')?.textContent?.trim() || '';

  // Stewardship score from rendered brief HTML
  const stewScore = (() => {
    const el = document.querySelector('#intelBriefContent');
    if (!el) return null;
    const match = el.innerHTML.match(/(\d{1,3})<span[^>]*>\/([A-F][+-]?)</);
    if (match) return `${match[1]}/${match[2]}`;
    return null;
  })();

  // Signal lines — built from structured data for full accuracy
  const signalLines = signals.map(s => {
    const emoji = s.signal === 'BUY' ? '🟢' : s.signal === 'SELL' ? '🔴' : '⚪';
    const price = s.indicators?.current_price
      ? ` @ $${formatPrice(s.indicators.current_price)}`
      : (_lastPriceMap[s.asset_id] ? ` @ $${formatPrice(_lastPriceMap[s.asset_id])}` : '');
    const rsi = s.rsi != null ? `RSI ${s.rsi.toFixed(0)}` : null;
    const conf = `${s.confidence}% conf`;
    const meta = [rsi, conf].filter(Boolean).join(', ');

    let line = `${emoji} *${s.symbol}*${price} — ${s.signal}  (${meta})`;

    // Add SL/TP for actionable signals
    if (s.signal !== 'HOLD' && s.risk?.stop_loss_price > 0) {
      const atrNote = s.risk.atr_based ? ' ⚡ATR' : '';
      line += `\n   └ SL $${formatPrice(s.risk.stop_loss_price)} → TP $${formatPrice(s.risk.take_profit_price)}  ${s.risk.risk_reward_ratio || '1:2'}${atrNote}`;
    }

    // Key confluence reasons (max 2)
    if (s.signal !== 'HOLD' && s.reason && s.reason !== 'No strong confluence') {
      const shortReason = s.reason.split(' | ').slice(0, 2).join(' | ');
      line += `\n   ↳ _${shortReason}_`;
    }

    return line;
  });

  // Assessment derived from signal data
  const buys = signals.filter(s => s.signal === 'BUY');
  const sells = signals.filter(s => s.signal === 'SELL');
  let assessment = '';
  if (buys.length >= 3 && regime === 'BULL') assessment = '🟢 Strong bull confluence — broad BUY signals in uptrend.';
  else if (buys.length >= 2) assessment = '🟡 Moderate bullish setup — selective entries advised.';
  else if (sells.length >= 3 && regime === 'BEAR') assessment = '🔴 Strong bear confluence — risk-off posture advised.';
  else if (sells.length >= 2) assessment = '🟠 Bearish pressure — reduce exposure or await reversal.';
  else assessment = '⏸ Mixed signals — no clear edge. Hold and wait for confluence.';

  const report = [
    `✝️ *C5iSR Market Brief* — ${dateStr} ${timeStr}`,
    ``,
    `📊 *Regime:* ${regimeEmoji} ${regime}  |  😱 *F&G:* ${fgTxt}`,
    `🌍 *Market Cap:* ${mcap}${mcapChange ? '  ' + mcapChange : ''}`,
    stewScore ? `🏅 *Stewardship Score:* ${stewScore}` : null,
    ``,
    `*── Signals ──*`,
    ...signalLines,
    ``,
    `💡 ${assessment}`,
    ``,
    `_"The plans of the diligent lead surely to abundance." — Prov 21:5_`,
    `📈 usmcmin.com/c5isr/dashboard.html`,
  ].filter(l => l !== null).join('\n');

  navigator.clipboard.writeText(report).then(() => {
    const btn = document.getElementById('copyReportBtn');
    if (btn) { btn.textContent = '✅ Copied!'; setTimeout(() => { btn.textContent = '📋 Copy Report'; }, 2500); }
    showToast('Signal report copied — ready to paste into Telegram!', 'success');
  }).catch(() => {
    window.prompt('Copy this report:', report);
  });
}
// ── Sticky Key Price Ticker (v3.0) ──
// Updates BTC/ETH/NEO/XAU/XAG in the always-visible strip below the header.
// Called by renderPrices (crypto) and renderMetals (metals).
let _tickerMetals = {}; // { xau: { price, change_pct }, xag: {...} }

function updateTicker(priceArr) {
  // priceArr: array of { id, symbol, price, change_24h }
  if (priceArr) {
    priceArr.forEach(p => {
      const id = p.id || '';
      const sym = (id === 'bitcoin' ? 'btc' : id === 'ethereum' ? 'eth' : id === 'neo' ? 'neo' : null);
      if (!sym) return;
      _setTickerCell(sym, p.price, p.change_24h);
    });
  }
  // Also flush cached metals
  if (_tickerMetals.xau) _setTickerCell('xau', _tickerMetals.xau.price, _tickerMetals.xau.change_pct);
  if (_tickerMetals.xag) _setTickerCell('xag', _tickerMetals.xag.price, _tickerMetals.xag.change_pct);
  const tsEl = document.getElementById('tickerTs');
  if (tsEl) tsEl.textContent = new Date().toLocaleTimeString();
}

function updateTickerMetals(gold, silver) {
  if (gold)   _tickerMetals.xau = { price: gold.price,   change_pct: gold.change_percentage };
  if (silver) _tickerMetals.xag = { price: silver.price, change_pct: silver.change_percentage };
  if (gold)   _setTickerCell('xau', gold.price,   gold.change_percentage);
  if (silver) _setTickerCell('xag', silver.price, silver.change_percentage);
  const tsEl = document.getElementById('tickerTs');
  if (tsEl) tsEl.textContent = new Date().toLocaleTimeString();
}

function _setTickerCell(sym, price, changePct) {
  const priceEl = document.getElementById(`tick-${sym}-price`);
  const chgEl   = document.getElementById(`tick-${sym}-chg`);
  if (!priceEl) return;
  if (price == null) return;
  // Format price
  let priceStr;
  if (price >= 1000)      priceStr = '$' + price.toLocaleString(undefined, {minimumFractionDigits:0, maximumFractionDigits:0});
  else if (price >= 10)   priceStr = '$' + price.toFixed(2);
  else if (price >= 1)    priceStr = '$' + price.toFixed(3);
  else                    priceStr = '$' + price.toFixed(4);
  priceEl.textContent = priceStr;
  if (chgEl && changePct != null) {
    const isUp = changePct >= 0;
    chgEl.textContent = (isUp ? '▲' : '▼') + Math.abs(changePct).toFixed(2) + '%';
    chgEl.className = 'ticker-chg ' + (isUp ? 'up' : 'down');
  }
}

// ── Logout ──
function logout() {
  localStorage.removeItem('c5isr_auth');
  localStorage.removeItem('c5isr_auth_time');
  localStorage.removeItem('c5isr_token');
  window.location.href = 'index.html';
}

// ── Fear & Greed Index (with yesterday comparison) ──
async function loadFearGreed() {
  try {
    const data = await cachedFetch('fng', 'https://api.alternative.me/fng/?limit=2', CACHE_TTL_LONG);
    const fg = data.data?.[0];
    const fgYesterday = data.data?.[1];
    if (!fg) return;
    const value = parseInt(fg.value);
    const label = fg.value_classification;
    const el = document.getElementById('fearGreedValue');
    const pointer = document.getElementById('fearGreedPointer');
    const update = document.getElementById('fearGreedUpdate');
    const yesterday = document.getElementById('fearGreedYesterday');

    let color;
    if (value <= 25) color = 'var(--red)';
    else if (value <= 45) color = '#ff6644';
    else if (value <= 55) color = 'var(--amber)';
    else if (value <= 75) color = '#88dd44';
    else color = 'var(--green)';

    el.innerHTML = `<span style="color:${color}">${value}</span> <span style="font-size:14px;color:var(--text-secondary)">${label}</span>`;
    pointer.style.left = `${value}%`;
    const fill = document.getElementById('fearGreedFill');
    if (fill) { fill.style.width = `${value}%`; fill.style.background = color; }
    const updated = new Date(parseInt(fg.timestamp) * 1000);
    update.textContent = `Updated: ${updated.toLocaleDateString()}`;

    if (fgYesterday) {
      const yVal = parseInt(fgYesterday.value);
      const diff = value - yVal;
      const diffStr = diff > 0 ? `+${diff}` : `${diff}`;
      const diffColor = diff > 0 ? 'var(--green)' : diff < 0 ? 'var(--red)' : 'var(--text-muted)';
      yesterday.innerHTML = `Yesterday: ${yVal} (<span style="color:${diffColor}">${diffStr}</span>)`;
    }
  } catch (e) {
    console.error('Fear & Greed load failed:', e);
    document.getElementById('fearGreedValue').innerHTML = '<span style="color:var(--text-muted);font-size:14px">Unavailable</span>';
  }
}

// ── Trending Coins ──
async function loadTrending() {
  try {
    const data = await cachedFetch('trending', `${COINGECKO}/search/trending`, CACHE_TTL_LONG);
    const coins = data.coins?.slice(0, 7) || [];
    const el = document.getElementById('trendingCoins');
    if (coins.length === 0) { el.innerHTML = '<div style="color:var(--text-muted)">No trending data</div>'; return; }
    el.innerHTML = coins.map((c, i) => {
      const item = c.item;
      const priceChange = item.data?.price_change_percentage_24h?.usd;
      const changeStr = priceChange != null
        ? `<span class="price-change ${priceChange >= 0 ? 'positive' : 'negative'}">${priceChange >= 0 ? '▲' : '▼'} ${Math.abs(priceChange).toFixed(1)}%</span>`
        : '';
      const priceStr = item.data?.price ? `$${parseFloat(item.data.price).toFixed(item.data.price < 1 ? 6 : 2)}` : '';
      return `
        <div class="trending-coin">
          <span class="trending-rank">#${i + 1}</span>
          <img class="trending-coin-img" src="${item.small}" alt="${item.name}" loading="lazy" onerror="this.style.display='none'">
          <div class="trending-coin-info">
            <div class="trending-coin-name">${item.name}</div>
            <div class="trending-coin-symbol">${item.symbol}</div>
          </div>
          <div class="trending-coin-price"><div>${priceStr}</div>${changeStr}</div>
        </div>`;
    }).join('');
    document.getElementById('trendingUpdate').textContent = new Date().toLocaleTimeString();
  } catch (e) {
    console.error('Trending load failed:', e);
    document.getElementById('trendingCoins').innerHTML = '<div style="color:var(--text-muted)">Failed to load trending coins</div>';
  }
}

// ── Top 10 Market Cap Rankings ──
async function loadMarketRankings() {
  try {
    const data = await cachedFetch('rankings', `${COINGECKO}/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=true&price_change_percentage=1h,24h,7d`, CACHE_TTL_LONG);
    const el = document.getElementById('marketRankings');
    if (!Array.isArray(data) || data.length === 0) { el.innerHTML = '<div style="color:var(--text-muted)">No ranking data</div>'; return; }

    el.innerHTML = `
      <div class="rankings-header">
        <span class="rank-col">#</span>
        <span class="rank-name-col">Name</span>
        <span class="rank-price-col">Price</span>
        <span class="rank-change-col">1h</span>
        <span class="rank-change-col">24h</span>
        <span class="rank-change-col">7d</span>
        <span class="rank-mcap-col">Market Cap</span>
        <span class="rank-spark-col">7D Chart</span>
      </div>
      ${data.map(coin => {
        const h1 = coin.price_change_percentage_1h_in_currency;
        const h24 = coin.price_change_percentage_24h_in_currency;
        const d7 = coin.price_change_percentage_7d_in_currency;
        const sparkPrices = coin.sparkline_in_7d?.price || [];
        const sparkId = `rank-spark-${coin.id}`;
        return `
          <div class="rankings-row">
            <span class="rank-col">${coin.market_cap_rank}</span>
            <span class="rank-name-col">
              <img src="${coin.image}" alt="" class="rank-coin-img" loading="lazy" onerror="this.style.display='none'">
              <span class="rank-coin-name">${coin.symbol.toUpperCase()}</span>
            </span>
            <span class="rank-price-col">$${formatPrice(coin.current_price)}</span>
            <span class="rank-change-col ${h1 >= 0 ? 'positive' : 'negative'}">${h1 != null ? (h1 >= 0 ? '+' : '') + h1.toFixed(1) + '%' : '—'}</span>
            <span class="rank-change-col ${h24 >= 0 ? 'positive' : 'negative'}">${h24 != null ? (h24 >= 0 ? '+' : '') + h24.toFixed(1) + '%' : '—'}</span>
            <span class="rank-change-col ${d7 >= 0 ? 'positive' : 'negative'}">${d7 != null ? (d7 >= 0 ? '+' : '') + d7.toFixed(1) + '%' : '—'}</span>
            <span class="rank-mcap-col">${formatCompact(coin.market_cap)}</span>
            <span class="rank-spark-col" id="${sparkId}"></span>
          </div>`;
      }).join('')}`;

    // Draw mini sparklines for each
    data.forEach(coin => {
      const sparkPrices = coin.sparkline_in_7d?.price || [];
      if (sparkPrices.length > 5) {
        // Downsample to ~20 points for perf
        const step = Math.max(1, Math.floor(sparkPrices.length / 20));
        const sampled = sparkPrices.filter((_, i) => i % step === 0);
        const isUp = sampled[sampled.length - 1] >= sampled[0];
        drawSparkline(`rank-spark-${coin.id}`, sampled, isUp ? '#00ff88' : '#ff3355');
      }
    });

    document.getElementById('rankingsUpdate').textContent = new Date().toLocaleTimeString();
  } catch (e) {
    console.error('Rankings load failed:', e);
    document.getElementById('marketRankings').innerHTML = '<div style="color:var(--text-muted)">Failed to load rankings</div>';
  }
}

// ── Global Market Stats ──
async function loadGlobalStats() {
  try {
    const data = await cachedFetch('global', `${COINGECKO}/global`, CACHE_TTL_MS);
    const g = data.data;
    if (!g) return;
    document.getElementById('globalMarketCap').textContent = formatCompact(g.total_market_cap?.usd || 0);
    document.getElementById('global24hVol').textContent = formatCompact(g.total_volume?.usd || 0);
    document.getElementById('btcDominance').textContent = `${(g.market_cap_percentage?.btc || 0).toFixed(1)}%`;
    document.getElementById('ethDominance').textContent = `${(g.market_cap_percentage?.eth || 0).toFixed(1)}%`;
    document.getElementById('activeCryptos').textContent = (g.active_cryptocurrencies || 0).toLocaleString();

    // Market cap 24h change
    const mcChange = g.market_cap_change_percentage_24h_usd;
    if (mcChange != null) {
      const changeEl = document.getElementById('globalMarketCapChange');
      if (changeEl) {
        changeEl.className = `market-stat-change ${mcChange >= 0 ? 'positive' : 'negative'}`;
        changeEl.textContent = `${mcChange >= 0 ? '▲' : '▼'} ${Math.abs(mcChange).toFixed(1)}%`;
      }
    }
  } catch (e) { console.error('Global stats load failed:', e); }

  // ETH Gas (separate endpoint — Etherscan free API or estimate)
  try {
    const gasEl = document.getElementById('ethGas');
    // Use a free gas estimate — Etherscan public, no key needed for basic
    const gasData = await cachedFetch('ethgas', 'https://api.etherscan.io/api?module=gastracker&action=gasoracle', 60000);
    if (gasData.status === '1' && gasData.result) {
      const gas = gasData.result;
      gasEl.innerHTML = `<span style="color:var(--green)">${gas.SafeGasPrice}</span>/<span style="color:var(--amber)">${gas.ProposeGasPrice}</span>`;
    }
  } catch { /* gas is non-critical */ }
}

// ── Scripture of the Day ──
const SCRIPTURES = [
  // Stewardship & Wealth
  { text: "The plans of the diligent lead surely to abundance, but everyone who is hasty comes only to poverty.", ref: "Proverbs 21:5" },
  { text: "Honor the LORD with your wealth and with the firstfruits of all your produce.", ref: "Proverbs 3:9" },
  { text: "The blessing of the LORD makes rich, and he adds no sorrow with it.", ref: "Proverbs 10:22" },
  { text: "Wealth gained hastily will dwindle, but whoever gathers little by little will increase it.", ref: "Proverbs 13:11" },
  { text: "A good man leaves an inheritance to his children's children.", ref: "Proverbs 13:22" },
  { text: "Better is a little with righteousness than great revenues with injustice.", ref: "Proverbs 16:8" },
  { text: "Bring the full tithe into the storehouse, and thereby put me to the test, says the LORD.", ref: "Malachi 3:10" },
  { text: "Each one must give as he has decided in his heart, not reluctantly or under compulsion, for God loves a cheerful giver.", ref: "2 Corinthians 9:7" },
  { text: "Where your treasure is, there your heart will be also.", ref: "Matthew 6:21" },
  { text: "No one can serve two masters. You cannot serve God and money.", ref: "Matthew 6:24" },
  { text: "But godliness with contentment is great gain.", ref: "1 Timothy 6:6" },
  { text: "Keep your life free from love of money, and be content with what you have.", ref: "Hebrews 13:5" },
  { text: "The earth is the LORD's, and everything in it, the world, and all who live in it.", ref: "Psalm 24:1" },
  { text: "He who is faithful in a very little thing is faithful also in much.", ref: "Luke 16:10" },
  { text: "For the love of money is a root of all kinds of evils.", ref: "1 Timothy 6:10" },
  { text: "Command them to do good, to be rich in good deeds, and to be generous and willing to share.", ref: "1 Timothy 6:18" },
  { text: "One person gives freely, yet gains even more; another withholds unduly, but comes to poverty.", ref: "Proverbs 11:24" },
  { text: "The rich rule over the poor, and the borrower is slave to the lender.", ref: "Proverbs 22:7" },
  { text: "Dishonest money dwindles away, but whoever gathers money little by little makes it grow.", ref: "Proverbs 13:11 (NIV)" },
  { text: "Good will come to those who are generous and lend freely, who conduct their affairs with justice.", ref: "Psalm 112:5" },

  // Faith & Trust
  { text: "Trust in the LORD with all your heart, and do not lean on your own understanding.", ref: "Proverbs 3:5" },
  { text: "But seek first the kingdom of God and his righteousness, and all these things will be added to you.", ref: "Matthew 6:33" },
  { text: "Commit your work to the LORD, and your plans will be established.", ref: "Proverbs 16:3" },
  { text: "Now faith is the assurance of things hoped for, the conviction of things not seen.", ref: "Hebrews 11:1" },
  { text: "The steadfast love of the LORD never ceases; his mercies never come to an end.", ref: "Lamentations 3:22" },
  { text: "For I know the plans I have for you, declares the LORD, plans for welfare and not for evil, to give you a future and a hope.", ref: "Jeremiah 29:11" },
  { text: "And my God will supply every need of yours according to his riches in glory in Christ Jesus.", ref: "Philippians 4:19" },
  { text: "The LORD is my shepherd; I shall not want.", ref: "Psalm 23:1" },
  { text: "The heart of man plans his way, but the LORD establishes his steps.", ref: "Proverbs 16:9" },
  { text: "Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God.", ref: "Philippians 4:6" },
  { text: "Cast your cares on the LORD and he will sustain you; he will never let the righteous be shaken.", ref: "Psalm 55:22" },
  { text: "Blessed is the man who trusts in the LORD, whose trust is the LORD.", ref: "Jeremiah 17:7" },
  { text: "For we live by faith, not by sight.", ref: "2 Corinthians 5:7" },
  { text: "Without faith it is impossible to please God, because anyone who comes to him must believe that he exists and that he rewards those who earnestly seek him.", ref: "Hebrews 11:6" },
  { text: "Those who hope in the LORD will renew their strength. They will soar on wings like eagles.", ref: "Isaiah 40:31" },

  // Courage & Strength
  { text: "For God gave us a spirit not of fear but of power and love and self-control.", ref: "2 Timothy 1:7" },
  { text: "Be strong and courageous. Do not be frightened, and do not be dismayed, for the LORD your God is with you.", ref: "Joshua 1:9" },
  { text: "I can do all things through him who strengthens me.", ref: "Philippians 4:13" },
  { text: "The LORD is my light and my salvation; whom shall I fear?", ref: "Psalm 27:1" },
  { text: "Be strong in the Lord and in his mighty power.", ref: "Ephesians 6:10" },
  { text: "So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you.", ref: "Isaiah 41:10" },
  { text: "The LORD your God is in your midst, a mighty one who will save.", ref: "Zephaniah 3:17" },
  { text: "Have I not commanded you? Be strong and courageous.", ref: "Joshua 1:9" },
  { text: "For nothing will be impossible with God.", ref: "Luke 1:37" },
  { text: "God is our refuge and strength, an ever-present help in trouble.", ref: "Psalm 46:1" },

  // Wisdom & Discernment
  { text: "If any of you lacks wisdom, let him ask God, who gives generously to all without reproach.", ref: "James 1:5" },
  { text: "The fear of the LORD is the beginning of wisdom.", ref: "Proverbs 9:10" },
  { text: "Do not be conformed to this world, but be transformed by the renewal of your mind.", ref: "Romans 12:2" },
  { text: "Get wisdom, and whatever you get, get insight.", ref: "Proverbs 4:7" },
  { text: "The wise person has eyes in his head, but the fool walks in darkness.", ref: "Ecclesiastes 2:14" },
  { text: "Plans fail for lack of counsel, but with many advisers they succeed.", ref: "Proverbs 15:22" },
  { text: "A wise man thinks ahead; a fool doesn't, and even brags about it.", ref: "Proverbs 13:16 (TLB)" },
  { text: "By wisdom a house is built, and through understanding it is established.", ref: "Proverbs 24:3" },
  { text: "The discerning heart seeks knowledge, but the mouth of a fool feeds on folly.", ref: "Proverbs 15:14" },
  { text: "As iron sharpens iron, so one person sharpens another.", ref: "Proverbs 27:17" },

  // Work & Purpose
  { text: "Whatever you do, work heartily, as for the Lord and not for men.", ref: "Colossians 3:23" },
  { text: "For we are God's handiwork, created in Christ Jesus to do good works.", ref: "Ephesians 2:10" },
  { text: "Let your light shine before others, that they may see your good deeds and glorify your Father in heaven.", ref: "Matthew 5:16" },
  { text: "Lazy hands make for poverty, but diligent hands bring wealth.", ref: "Proverbs 10:4" },
  { text: "All hard work brings a profit, but mere talk leads only to poverty.", ref: "Proverbs 14:23" },
  { text: "She sets about her work vigorously; her arms are strong for her tasks.", ref: "Proverbs 31:17" },
  { text: "Do not grow weary in doing good, for in due season you will reap, if you do not give up.", ref: "Galatians 6:9" },
  { text: "Commit to the LORD whatever you do, and he will establish your plans.", ref: "Proverbs 16:3 (NIV)" },
  { text: "The soul of the diligent is richly supplied.", ref: "Proverbs 13:4" },
  { text: "Work willingly at whatever you do, as though you were working for the Lord rather than for people.", ref: "Colossians 3:23 (NLT)" },

  // Peace & Contentment
  { text: "I have learned, in whatever situation I am, to be content.", ref: "Philippians 4:11" },
  { text: "Peace I leave with you; my peace I give to you. Not as the world gives do I give to you.", ref: "John 14:27" },
  { text: "You will keep in perfect peace those whose minds are steadfast, because they trust in you.", ref: "Isaiah 26:3" },
  { text: "The LORD gives strength to his people; the LORD blesses his people with peace.", ref: "Psalm 29:11" },
  { text: "Better is a dry morsel with quiet than a house full of feasting with strife.", ref: "Proverbs 17:1" },
  { text: "Godliness with contentment is great gain. For we brought nothing into the world, and we can take nothing out of it.", ref: "1 Timothy 6:6-7" },
  { text: "May the God of hope fill you with all joy and peace as you trust in him.", ref: "Romans 15:13" },

  // Integrity & Character
  { text: "The integrity of the upright guides them, but the unfaithful are destroyed by their duplicity.", ref: "Proverbs 11:3" },
  { text: "Better a poor person who walks in his integrity than one who is crooked in speech and is a fool.", ref: "Proverbs 19:1" },
  { text: "A good name is more desirable than great riches; to be esteemed is better than silver or gold.", ref: "Proverbs 22:1" },
  { text: "Do to others as you would have them do to you.", ref: "Luke 6:31" },
  { text: "Let your yes be yes and your no be no.", ref: "Matthew 5:37" },
  { text: "He who walks in integrity walks securely.", ref: "Proverbs 10:9" },
  { text: "Do not take advantage of each other, but fear your God.", ref: "Leviticus 25:17" },
  { text: "A false balance is an abomination to the LORD, but a just weight is his delight.", ref: "Proverbs 11:1" },

  // Giving & Generosity
  { text: "Give, and it will be given to you. A good measure, pressed down, shaken together and running over.", ref: "Luke 6:38" },
  { text: "Whoever is generous to the poor lends to the LORD, and he will repay him for his deed.", ref: "Proverbs 19:17" },
  { text: "Remember this: Whoever sows sparingly will also reap sparingly, and whoever sows generously will also reap generously.", ref: "2 Corinthians 9:6" },
  { text: "In all things I have shown you that by working hard in this way we must help the weak.", ref: "Acts 20:35" },
  { text: "The world of the generous gets larger and larger; the world of the stingy gets smaller and smaller.", ref: "Proverbs 11:24 (MSG)" },
];

function loadScripture() {
  const el = document.getElementById('scriptureText');
  const refEl = document.getElementById('scriptureRef');
  if (!el || !refEl) return;
  // Deterministic daily rotation — changes at midnight local time
  const dayOfYear = Math.floor((Date.now() - new Date(new Date().getFullYear(), 0, 0)) / 86400000);
  const verse = SCRIPTURES[dayOfYear % SCRIPTURES.length];
  el.textContent = `"${verse.text}"`;
  refEl.textContent = `— ${verse.ref}`;
}

// ── Helpers ──
function formatPrice(n) {
  if (n == null) return '—';
  if (n >= 1000) return n.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  if (n >= 1) return n.toFixed(2);
  if (n >= 0.01) return n.toFixed(4);
  return n.toFixed(6);
}

function formatCompact(n) {
  if (n >= 1e12) return `$${(n / 1e12).toFixed(2)}T`;
  if (n >= 1e9) return `$${(n / 1e9).toFixed(1)}B`;
  if (n >= 1e6) return `$${(n / 1e6).toFixed(0)}M`;
  return `$${n.toLocaleString()}`;
}

function round2(n) { return Math.round(n * 100) / 100; }

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// ── Prediction Tracker (v1.0) ── Added 2026-03-31 ──
// Logs every BUY/SELL signal with entry price + SL/TP.
// On each refresh, evaluates outcome vs current price.
// Persists to localStorage under 'c5_predictions'.
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

const PRED_KEY = 'c5_predictions';
const MAX_PREDICTIONS = 100;

function getPredictions() {
  try { return JSON.parse(localStorage.getItem(PRED_KEY) || '[]'); }
  catch { return []; }
}

function savePredictions(preds) {
  try { localStorage.setItem(PRED_KEY, JSON.stringify(preds.slice(0, MAX_PREDICTIONS))); }
  catch { /* quota */ }
}

function clearPredictions() {
  if (!confirm('Clear all prediction history?')) return;
  localStorage.removeItem(PRED_KEY);
  renderPredictionTracker([]);
  showToast('Prediction history cleared', 'info');
}

/**
 * Called after each signal load. Logs new BUY/SELL signals, then
 * evaluates pending ones against the latest price map.
 */
function updatePredictionTracker(signals, priceMap) {
  if (!signals || !signals.length) return;
  let preds = getPredictions();
  const now = Date.now();

  // ── 1. Log new actionable signals (deduplicate by symbol+signal within 4h) ──
  signals.forEach(s => {
    if (s.signal === 'HOLD') return;
    const entryPrice = priceMap[s.asset_id] || s.indicators?.current_price;
    if (!entryPrice || entryPrice <= 0) return;
    const slPrice = s.risk?.stop_loss_price;
    const tpPrice = s.risk?.take_profit_price;
    if (!slPrice || !tpPrice) return;

    // Deduplicate: skip if same symbol+signal already logged in last 4h
    const recent = preds.find(p =>
      p.symbol === s.symbol &&
      p.signal === s.signal &&
      p.outcome === 'PENDING' &&
      (now - p.timestamp) < 4 * 3600 * 1000
    );
    if (recent) return;

    preds.unshift({
      id: `${s.symbol}_${s.signal}_${now}`,
      symbol: s.symbol,
      asset_id: s.asset_id,
      signal: s.signal,
      entryPrice,
      slPrice,
      tpPrice,
      confidence: s.confidence,
      reason: s.reason || '',
      timestamp: now,
      dateStr: new Date(now).toLocaleDateString('en-US', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }),
      outcome: 'PENDING',
      outcomePrice: null,
      outcomeTime: null,
    });
  });

  // ── 2. Evaluate pending predictions vs current prices ──
  preds = preds.map(p => {
    if (p.outcome !== 'PENDING') return p;
    const currentPrice = priceMap[p.asset_id];
    if (!currentPrice || currentPrice <= 0) return p;

    let outcome = 'PENDING';
    if (p.signal === 'BUY') {
      if (currentPrice >= p.tpPrice) outcome = 'WIN';
      else if (currentPrice <= p.slPrice) outcome = 'LOSS';
    } else if (p.signal === 'SELL') {
      // For SELL: WIN if price dropped to TP (below entry), LOSS if risen to SL (above entry)
      if (currentPrice <= p.tpPrice) outcome = 'WIN';
      else if (currentPrice >= p.slPrice) outcome = 'LOSS';
    }

    if (outcome !== 'PENDING') {
      return { ...p, outcome, outcomePrice: currentPrice, outcomeTime: Date.now() };
    }
    return p;
  });

  savePredictions(preds);
  renderPredictionTracker(preds, priceMap);
}

function renderPredictionTracker(preds, priceMap = {}) {
  const statsEl = document.getElementById('predictionStats');
  const logEl = document.getElementById('predictionLog');
  const updEl = document.getElementById('predictionUpdated');
  if (!statsEl || !logEl) return;

  if (updEl) updEl.textContent = new Date().toLocaleTimeString();

  // ── Stats summary ──
  const resolved = preds.filter(p => p.outcome !== 'PENDING');
  const wins = resolved.filter(p => p.outcome === 'WIN').length;
  const losses = resolved.filter(p => p.outcome === 'LOSS').length;
  const pending = preds.filter(p => p.outcome === 'PENDING').length;
  const accuracy = resolved.length > 0 ? Math.round((wins / resolved.length) * 100) : null;
  const accColor = accuracy == null ? 'var(--text-muted)' : accuracy >= 60 ? 'var(--green)' : accuracy >= 40 ? 'var(--amber)' : 'var(--red)';

  statsEl.innerHTML = `
    <div style="display:flex;gap:20px;flex-wrap:wrap;padding:8px 0 12px;border-bottom:1px solid var(--border);margin-bottom:12px">
      <div style="text-align:center;min-width:60px">
        <div style="font-family:var(--font-mono);font-size:22px;font-weight:700;color:var(--green)">${wins}</div>
        <div style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">Wins</div>
      </div>
      <div style="text-align:center;min-width:60px">
        <div style="font-family:var(--font-mono);font-size:22px;font-weight:700;color:var(--red)">${losses}</div>
        <div style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">Losses</div>
      </div>
      <div style="text-align:center;min-width:60px">
        <div style="font-family:var(--font-mono);font-size:22px;font-weight:700;color:var(--amber)">${pending}</div>
        <div style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">Pending</div>
      </div>
      <div style="text-align:center;min-width:80px;border-left:1px solid var(--border);padding-left:20px">
        <div style="font-family:var(--font-mono);font-size:22px;font-weight:700;color:${accColor}">
          ${accuracy !== null ? accuracy + '%' : '—'}
        </div>
        <div style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">Accuracy</div>
      </div>
      <div style="text-align:center;min-width:60px">
        <div style="font-family:var(--font-mono);font-size:22px;font-weight:700;color:var(--text-secondary)">${preds.length}</div>
        <div style="font-size:10px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px">Total</div>
      </div>
    </div>`;

  // ── Log entries (show last 20) ──
  const display = preds.slice(0, 20);
  if (display.length === 0) {
    logEl.innerHTML = '<div style="color:var(--text-muted);text-align:center;padding:16px">No predictions logged yet — signals will be tracked automatically on each refresh.</div>';
    return;
  }

  logEl.innerHTML = display.map(p => {
    const signalColor = p.signal === 'BUY' ? 'var(--green)' : 'var(--red)';
    const outcomeColor = p.outcome === 'WIN' ? 'var(--green)' : p.outcome === 'LOSS' ? 'var(--red)' : 'var(--amber)';
    const outcomeIcon = p.outcome === 'WIN' ? '✅' : p.outcome === 'LOSS' ? '❌' : '⏳';
    const currentPrice = priceMap[p.asset_id];

    // Price delta vs entry
    let deltaHtml = '';
    if (currentPrice && p.outcome === 'PENDING') {
      const delta = ((currentPrice - p.entryPrice) / p.entryPrice * 100);
      const sign = p.signal === 'BUY' ? 1 : -1;
      const pnl = delta * sign;
      const pnlColor = pnl >= 0 ? 'var(--green)' : 'var(--red)';
      deltaHtml = `<span style="font-size:10px;color:${pnlColor};font-family:var(--font-mono)">${pnl >= 0 ? '+' : ''}${pnl.toFixed(1)}%</span>`;
    }

    const slPct = p.entryPrice > 0 ? Math.abs((p.slPrice - p.entryPrice) / p.entryPrice * 100).toFixed(1) : '?';
    const tpPct = p.entryPrice > 0 ? Math.abs((p.tpPrice - p.entryPrice) / p.entryPrice * 100).toFixed(1) : '?';
    const elapsed = formatElapsed(Date.now() - p.timestamp);

    // ── Range bar for PENDING predictions ──
    let rangeBarHtml = '';
    if (p.outcome === 'PENDING' && currentPrice && p.slPrice && p.tpPrice && p.entryPrice) {
      const lo = Math.min(p.slPrice, p.tpPrice, p.entryPrice, currentPrice);
      const hi = Math.max(p.slPrice, p.tpPrice, p.entryPrice, currentPrice);
      const span = hi - lo || 1;
      const toPos = v => Math.max(0, Math.min(100, ((v - lo) / span) * 100));

      const slPos      = toPos(p.slPrice);
      const tpPos      = toPos(p.tpPrice);
      const entryPos   = toPos(p.entryPrice);
      const curPos     = toPos(currentPrice);
      const cursorColor = p.signal === 'BUY'
        ? (currentPrice >= p.entryPrice ? 'var(--green)' : 'var(--amber)')
        : (currentPrice <= p.entryPrice ? 'var(--green)' : 'var(--amber)');

      // For a BUY: sl is left, tp is right. SELL: reversed visually.
      const dangerLeft  = p.signal === 'BUY' ? `${slPos}%`  : `${tpPos}%`;
      const dangerWidth = p.signal === 'BUY' ? `${entryPos - slPos}%` : `${entryPos - tpPos}%`;
      const gainLeft    = p.signal === 'BUY' ? `${entryPos}%` : `${slPos}%`;
      const gainWidth   = p.signal === 'BUY' ? `${tpPos - entryPos}%` : `${entryPos - slPos}%`;

      rangeBarHtml = `
        <div class="pred-range-wrap">
          <div class="pred-range-track">
            <div class="pred-range-sl"  style="left:${dangerLeft};width:${dangerWidth}"></div>
            <div class="pred-range-tp"  style="left:${gainLeft};width:${gainWidth}"></div>
            <div class="pred-range-cursor" style="left:${curPos}%;background:${cursorColor}" title="Current: $${formatPrice(currentPrice)}"></div>
          </div>
          <div class="pred-range-labels">
            <span style="color:var(--red)">SL $${formatPrice(p.slPrice)}</span>
            <span style="color:var(--text-muted)">Entry $${formatPrice(p.entryPrice)}</span>
            <span style="color:var(--green)">TP $${formatPrice(p.tpPrice)}</span>
          </div>
        </div>`;
    }

    return `
      <div style="padding:10px 4px;border-bottom:1px solid rgba(255,255,255,0.04)">
        <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
          <span style="font-size:15px">${outcomeIcon}</span>
          <span style="font-family:var(--font-mono);font-weight:700;color:${signalColor};min-width:36px">${p.symbol}</span>
          <span class="signal-badge ${p.signal === 'BUY' ? 'signal-buy' : 'signal-sell'}" style="font-size:10px;padding:2px 6px">${p.signal}</span>
          <span style="font-family:var(--font-mono);font-size:11px;color:var(--text-secondary)">@ $${formatPrice(p.entryPrice)}</span>
          ${deltaHtml}
          <span style="margin-left:auto;font-size:10px;color:${outcomeColor};font-weight:600">${p.outcome}</span>
          <span style="font-size:10px;color:var(--text-muted)">${elapsed} · ${p.confidence}% conf</span>
        </div>
        ${rangeBarHtml}
      </div>`;
  }).join('');
}

function formatElapsed(ms) {
  const s = Math.floor(ms / 1000);
  if (s < 60) return `${s}s ago`;
  const m = Math.floor(s / 60);
  if (m < 60) return `${m}m ago`;
  const h = Math.floor(m / 60);
  if (h < 24) return `${h}h ago`;
  return `${Math.floor(h / 24)}d ago`;
}

// Hook into renderPrices to evaluate predictions when new prices arrive
const _origRenderPricesForPred = renderPrices;
// renderPrices already overridden once for portfolio — chain it
const _prevRenderPrices = renderPrices;
// Use a post-render hook via patching _lastPriceMap updates:
// We'll call updatePredictionTracker from loadSignals instead (after signals available)
// See: patchLoadSignals below


// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// ── Weekly Report Archive (v1.0) ── Added 2026-03-31 ──
// Snapshots the full intelligence brief + signal data once
// per session (or when signals change significantly).
// Archives last 28 entries in localStorage.
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

const ARCHIVE_KEY = 'c5_report_archive';
const MAX_ARCHIVE = 28;
let _lastArchiveSnapshot = null;

function getReportArchive() {
  try { return JSON.parse(localStorage.getItem(ARCHIVE_KEY) || '[]'); }
  catch { return []; }
}

function saveReportArchive(entries) {
  try { localStorage.setItem(ARCHIVE_KEY, JSON.stringify(entries.slice(0, MAX_ARCHIVE))); }
  catch { /* quota */ }
}

function clearReportArchive() {
  if (!confirm('Clear all archived reports?')) return;
  localStorage.removeItem(ARCHIVE_KEY);
  _lastArchiveSnapshot = null;
  renderReportArchive([]);
  showToast('Report archive cleared', 'info');
}

/**
 * Saves a snapshot of the current market brief to the archive.
 * Deduplicates by day — only one snapshot per calendar day.
 * Called after signals + intel brief are rendered.
 */
function archiveCurrentReport(signals, priceMap, fearGreedValue) {
  if (!signals || !signals.length) return;
  const now = new Date();
  const dayKey = now.toISOString().slice(0, 10); // YYYY-MM-DD

  let archive = getReportArchive();

  // Skip if we already snapshotted today
  if (archive.length > 0 && archive[0].dayKey === dayKey) {
    // Update the existing today entry (refresh it to latest data)
    archive[0] = buildSnapshot(signals, priceMap, fearGreedValue, now, dayKey);
  } else {
    // New day — prepend
    archive.unshift(buildSnapshot(signals, priceMap, fearGreedValue, now, dayKey));
  }

  saveReportArchive(archive);
  renderReportArchive(archive);
}

function buildSnapshot(signals, priceMap, fgValue, now, dayKey) {
  const buys = signals.filter(s => s.signal === 'BUY');
  const sells = signals.filter(s => s.signal === 'SELL');
  const holds = signals.filter(s => s.signal === 'HOLD');
  const btcSig = signals.find(s => s.symbol === 'BTC');
  const regime = btcSig?.market_regime || btcSig?.indicators?.ema?.regime || 'SIDEWAYS';
  const avgConf = signals.length > 0
    ? Math.round(signals.reduce((a, s) => a + s.confidence, 0) / signals.length)
    : 0;

  const prices = {};
  signals.forEach(s => {
    const p = priceMap[s.asset_id] || s.indicators?.current_price;
    if (p) prices[s.symbol] = p;
  });

  // Stewardship score from DOM (best effort)
  const stewEl = document.querySelector('#intelBriefContent');
  const stewMatch = stewEl ? stewEl.innerHTML.match(/(\d{1,3})<span[^>]*>\/([A-F][+-]?)/) : null;
  const stewScore = stewMatch ? `${stewMatch[1]}/${stewMatch[2]}` : null;

  return {
    dayKey,
    timestamp: now.getTime(),
    dateStr: now.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' }),
    timeStr: now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' }),
    regime,
    fearGreed: fgValue,
    buys: buys.length,
    holds: holds.length,
    sells: sells.length,
    avgConf,
    stewScore,
    prices,
    signals: signals.map(s => ({
      symbol: s.symbol,
      signal: s.signal,
      confidence: s.confidence,
      reason: s.reason,
      slPrice: s.risk?.stop_loss_price,
      tpPrice: s.risk?.take_profit_price,
      price: priceMap[s.asset_id] || s.indicators?.current_price,
    })),
  };
}

function renderReportArchive(archive) {
  const el = document.getElementById('reportArchive');
  const countEl = document.getElementById('archiveCount');
  if (!el) return;

  if (countEl) countEl.textContent = `${archive.length} snapshot${archive.length !== 1 ? 's' : ''} stored`;

  if (archive.length === 0) {
    el.innerHTML = '<div style="color:var(--text-muted);text-align:center;padding:16px">No reports archived yet — snapshots are saved automatically once per day.</div>';
    return;
  }

  el.innerHTML = archive.map((entry, idx) => {
    const regimeEmoji = entry.regime === 'BULL' ? '🐂' : entry.regime === 'BEAR' ? '🐻' : '↔️';
    const buySellBadge = entry.buys > 0
      ? `<span style="color:var(--green);font-weight:600">${entry.buys}B</span>`
      : '';
    const sellBadge = entry.sells > 0
      ? `<span style="color:var(--red);font-weight:600">${entry.sells}S</span>`
      : '';
    const holdBadge = entry.holds > 0
      ? `<span style="color:var(--amber);font-weight:600">${entry.holds}H</span>`
      : '';

    const isToday = idx === 0;
    const signalDetails = (entry.signals || []).map(s => {
      const emoji = s.signal === 'BUY' ? '🟢' : s.signal === 'SELL' ? '🔴' : '⚪';
      const priceStr = s.price ? ` @ $${formatPrice(s.price)}` : '';
      return `<div style="font-size:11px;color:var(--text-secondary);padding:2px 0">
        ${emoji} <b>${s.symbol}</b>${priceStr} — <span style="color:${s.signal === 'BUY' ? 'var(--green)' : s.signal === 'SELL' ? 'var(--red)' : 'var(--text-muted)'}">${s.signal}</span>
        <span style="color:var(--text-muted)">${s.confidence}% · ${(s.reason || '').split(' | ').slice(0,2).join(' | ')}</span>
      </div>`;
    }).join('');

    return `
      <div style="border:1px solid var(--border);border-radius:8px;margin-bottom:8px;overflow:hidden">
        <div style="display:flex;align-items:center;gap:10px;padding:10px 14px;background:rgba(255,255,255,0.02);cursor:pointer;flex-wrap:wrap"
             onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==='none'?'block':'none'">
          <span style="font-weight:600;font-size:13px;color:${isToday ? 'var(--green)' : 'var(--text-primary)'}">${entry.dateStr}</span>
          ${isToday ? '<span style="font-size:10px;background:var(--green);color:#000;padding:1px 6px;border-radius:4px;font-weight:700">TODAY</span>' : ''}
          <span style="font-size:11px;color:var(--text-muted)">${entry.timeStr}</span>
          <span style="font-family:var(--font-mono);font-size:12px">${regimeEmoji} ${entry.regime}</span>
          <span style="font-size:11px;display:flex;gap:6px">${buySellBadge}${holdBadge}${sellBadge}</span>
          ${entry.stewScore ? `<span style="font-size:11px;color:var(--text-muted)">🏅 ${entry.stewScore}</span>` : ''}
          ${entry.fearGreed != null ? `<span style="font-size:11px;color:var(--text-muted)">F&G: ${entry.fearGreed}</span>` : ''}
          <span style="margin-left:auto;font-size:11px;color:var(--text-muted)">${entry.avgConf}% avg conf ▾</span>
        </div>
        <div style="display:none;padding:12px 14px;border-top:1px solid var(--border)">
          ${signalDetails}
          ${entry.prices && Object.keys(entry.prices).length > 0
            ? `<div style="margin-top:8px;padding-top:8px;border-top:1px solid rgba(255,255,255,0.04);font-size:10px;color:var(--text-muted)">
                Prices: ${Object.entries(entry.prices).map(([sym, p]) => `${sym} $${formatPrice(p)}`).join(' · ')}
               </div>`
            : ''}
        </div>
      </div>`;
  }).join('');
}

// ── Integration hook: called from loadSignals after signals render ──
// Patches the existing loadSignals flow to trigger prediction + archive updates
(function patchSignalFlow() {
  // Intercept window._lastSignals assignment via a setter
  let _signals = null;
  Object.defineProperty(window, '_lastSignals', {
    get() { return _signals; },
    set(v) {
      _signals = v;
      // After a short delay to let prices settle
      setTimeout(() => {
        if (_signals && _signals.length && _lastPriceMap && Object.keys(_lastPriceMap).length) {
          updatePredictionTracker(_signals, _lastPriceMap);
          // Get F&G value from DOM
          const fgEl = document.getElementById('fearGreedValue');
          const fgText = fgEl ? fgEl.textContent.trim().match(/\d+/) : null;
          const fgValue = fgText ? parseInt(fgText[0]) : null;
          archiveCurrentReport(_signals, _lastPriceMap, fgValue);
        }
      }, 1500);
    },
    configurable: true,
  });
})();

// ── Load archived data on boot ──
document.addEventListener('DOMContentLoaded', () => {
  // Show existing prediction & archive data immediately on load
  setTimeout(() => {
    const preds = getPredictions();
    renderPredictionTracker(preds, {});
    const archive = getReportArchive();
    renderReportArchive(archive);
  }, 500);
});
