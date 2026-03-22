/**
 * C5iSR Dashboard — Frontend Logic v2.0
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
  ]);

  startRefreshTimer();
  updateLastUpdated();
});

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
      <div class="card card-animate price-card" data-asset="${p.id}">
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
      </div>`;
  }).join('');
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
    renderSignals(signals);
    updateRegime(signals);
    updateDCA(signals);
    updateRisk(signals);
    updateAlertLog(signals);
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
  grid.innerHTML = signals.map(s => {
    const cls = s.signal === 'BUY' ? 'signal-buy' : s.signal === 'SELL' ? 'signal-sell' : 'signal-hold';
    const rsi = s.rsi != null ? s.rsi.toFixed(1) : '—';
    const rsiColor = s.rsi < 35 ? 'var(--green)' : s.rsi > 70 ? 'var(--red)' : 'var(--amber)';
    const rsiWidth = s.rsi != null ? s.rsi : 50;
    const confColor = s.confidence >= 70 ? 'var(--green)' : s.confidence >= 40 ? 'var(--amber)' : 'var(--red)';
    const pills = buildIndicatorPills(s);
    return `
      <div class="card card-animate">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <span style="font-family:var(--font-mono);font-weight:700;font-size:16px;color:${ASSETS[s.asset_id]?.color || '#fff'}">${s.symbol}</span>
          <span class="signal-badge ${cls}">${s.signal}</span>
        </div>
        <div style="margin-top:12px">
          <div class="rsi-value">RSI: <span style="color:${rsiColor}">${rsi}</span></div>
          <div class="rsi-gauge"><div class="rsi-gauge-fill" style="width:${rsiWidth}%;background:${rsiColor}"></div></div>
        </div>
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
      const r = await fetch(`${API_BASE}/api/backtest/${assetId}`, { headers: { Authorization: `Bearer ${token}` } });
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
  const closes = ohlc.map(c => c[4]);
  let capital = 10000, position = 0, entryPrice = 0;
  let trades = 0, wins = 0, maxDD = 0, peak = capital;
  for (let i = 50; i < closes.length; i++) {
    const price = closes[i];
    const equity = capital + position * price;
    if (equity > peak) peak = equity;
    const dd = (peak - equity) / peak * 100;
    if (dd > maxDD) maxDD = dd;
    const slice = closes.slice(0, i + 1);
    const rsiVal = calcRSI(slice);
    let buy = 0, sell = 0;
    if (rsiVal < 35) buy++; if (rsiVal > 70) sell++;
    const ema200 = calcEMA(slice, 200);
    if (ema200 && price > ema200) buy++; else if (ema200) sell++;
    if (buy >= 2 && position === 0) { position = capital / price; entryPrice = price; capital = 0; }
    else if (sell >= 2 && position > 0) { capital = position * price; trades++; if (price > entryPrice) wins++; position = 0; }
  }
  if (position > 0) { capital = position * closes[closes.length - 1]; trades++; if (closes[closes.length - 1] > entryPrice) wins++; }
  return {
    symbol: ASSETS[assetId]?.symbol || '???',
    total_return_pct: round2((capital - 10000) / 100),
    win_rate_pct: trades > 0 ? round2(wins / trades * 100) : 0,
    max_drawdown_pct: round2(maxDD), total_trades: trades, final_capital: round2(capital),
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
      if (!window._refreshCycle) window._refreshCycle = 0;
      window._refreshCycle++;
      if (window._refreshCycle % 2 === 0) { loadFearGreed(); loadGlobalStats(); }
      if (window._refreshCycle % 4 === 0) { loadTrending(); loadMarketRankings(); }
    }
  }, 1000);
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

  // Total row
  const totalPnl = totalValue - totalCost;
  const totalPnlPct = totalCost > 0 ? (totalPnl / totalCost) * 100 : 0;
  const totalColor = totalPnl >= 0 ? 'var(--green)' : 'var(--red)';
  if (totalValue > 0) {
    totalEl.innerHTML = `
      <div style="display:flex;justify-content:flex-end;gap:24px;padding:12px 0 4px;border-top:1px solid var(--border);margin-top:8px">
        <div style="font-size:12px;color:var(--text-muted)">Total Value: <span style="color:var(--text-primary);font-family:var(--font-mono)">$${formatPrice(totalValue)}</span></div>
        <div style="font-size:12px;color:var(--text-muted)">P&L: <span style="color:${totalColor};font-family:var(--font-mono)">${totalPnl >= 0 ? '+' : ''}$${Math.abs(totalPnl).toFixed(2)} (${totalPnlPct >= 0 ? '+' : ''}${totalPnlPct.toFixed(1)}%)</span></div>
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

// Patch into renderPrices to also update portfolio
const _origRenderPrices = renderPrices;
function renderPrices(prices) {
  _origRenderPrices(prices);
  _lastPriceMap = {};
  prices.forEach(p => { _lastPriceMap[p.id] = p.price; });
  renderPortfolio(_lastPriceMap);
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
  { text: "The plans of the diligent lead surely to abundance, but everyone who is hasty comes only to poverty.", ref: "Proverbs 21:5" },
  { text: "For God gave us a spirit not of fear but of power and love and self-control.", ref: "2 Timothy 1:7" },
  { text: "Trust in the LORD with all your heart, and do not lean on your own understanding.", ref: "Proverbs 3:5" },
  { text: "But seek first the kingdom of God and his righteousness, and all these things will be added to you.", ref: "Matthew 6:33" },
  { text: "Commit your work to the LORD, and your plans will be established.", ref: "Proverbs 16:3" },
  { text: "I can do all things through him who strengthens me.", ref: "Philippians 4:13" },
  { text: "The earth is the LORD's, and everything in it, the world, and all who live in it.", ref: "Psalm 24:1" },
  { text: "Honor the LORD with your wealth and with the firstfruits of all your produce.", ref: "Proverbs 3:9" },
  { text: "Do not be conformed to this world, but be transformed by the renewal of your mind.", ref: "Romans 12:2" },
  { text: "Whatever you do, work heartily, as for the Lord and not for men.", ref: "Colossians 3:23" },
  { text: "The blessing of the LORD makes rich, and he adds no sorrow with it.", ref: "Proverbs 10:22" },
  { text: "Wealth gained hastily will dwindle, but whoever gathers little by little will increase it.", ref: "Proverbs 13:11" },
  { text: "A good man leaves an inheritance to his children's children.", ref: "Proverbs 13:22" },
  { text: "The steadfast love of the LORD never ceases; his mercies never come to an end.", ref: "Lamentations 3:22" },
  { text: "For I know the plans I have for you, declares the LORD, plans for welfare and not for evil, to give you a future and a hope.", ref: "Jeremiah 29:11" },
  { text: "He who is faithful in a very little thing is faithful also in much.", ref: "Luke 16:10" },
  { text: "The heart of man plans his way, but the LORD establishes his steps.", ref: "Proverbs 16:9" },
  { text: "Be strong and courageous. Do not be frightened, and do not be dismayed, for the LORD your God is with you.", ref: "Joshua 1:9" },
  { text: "Now faith is the assurance of things hoped for, the conviction of things not seen.", ref: "Hebrews 11:1" },
  { text: "If any of you lacks wisdom, let him ask God, who gives generously to all without reproach.", ref: "James 1:5" },
  { text: "And my God will supply every need of yours according to his riches in glory in Christ Jesus.", ref: "Philippians 4:19" },
  { text: "No one can serve two masters. You cannot serve God and money.", ref: "Matthew 6:24" },
  { text: "Whoever can be trusted with very little can also be trusted with much.", ref: "Luke 16:10 (NIV)" },
  { text: "But godliness with contentment is great gain.", ref: "1 Timothy 6:6" },
  { text: "The LORD is my shepherd; I shall not want.", ref: "Psalm 23:1" },
  { text: "Keep your life free from love of money, and be content with what you have.", ref: "Hebrews 13:5" },
  { text: "Bring the full tithe into the storehouse, and thereby put me to the test, says the LORD.", ref: "Malachi 3:10" },
  { text: "Each one must give as he has decided in his heart, not reluctantly or under compulsion, for God loves a cheerful giver.", ref: "2 Corinthians 9:7" },
  { text: "Where your treasure is, there your heart will be also.", ref: "Matthew 6:21" },
  { text: "The fear of the LORD is the beginning of wisdom.", ref: "Proverbs 9:10" },
  { text: "Better is a little with righteousness than great revenues with injustice.", ref: "Proverbs 16:8" },
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
