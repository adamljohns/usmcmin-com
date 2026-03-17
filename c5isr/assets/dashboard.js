/**
 * C5iSR Dashboard — Frontend Logic
 * 
 * Works in two modes:
 *   1. Backend mode: Pulls from FastAPI at API_BASE
 *   2. Demo mode: Falls back to CoinGecko direct API if backend offline
 */

// ── Config ──
const API_BASE = localStorage.getItem('c5isr_api') || '';  // empty = demo mode
const COINGECKO = 'https://api.coingecko.com/api/v3';
const COINGECKO_FALLBACK = 'https://pro-api.coingecko.com/api/v3'; // fallback endpoint
const REFRESH_INTERVAL = 30; // seconds
const MAX_RETRIES = 3;
const RETRY_DELAY_MS = 1000;
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
let currentChartAsset = 'bitcoin';

// ── Auth Check ──
if (localStorage.getItem('c5isr_auth') !== 'true') {
  window.location.href = 'index.html';
}

// ── Retry Fetch with Exponential Backoff ──
async function fetchWithRetry(url, options = {}, retries = MAX_RETRIES) {
  for (let i = 0; i < retries; i++) {
    try {
      const r = await fetch(url, { signal: AbortSignal.timeout(10000), ...options });
      if (r.status === 429) {
        const wait = Math.min(RETRY_DELAY_MS * Math.pow(2, i), 10000);
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

// ── Toast Notifications ──
function showToast(msg, type = 'info') {
  const existing = document.querySelectorAll('.toast');
  existing.forEach(t => t.remove());
  const t = document.createElement('div');
  t.className = `toast toast-${type}`;
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 3000);
}

// ── Init ──
document.addEventListener('DOMContentLoaded', async () => {
  await checkBackend();
  initChart();
  await Promise.all([
    loadPrices(),
    loadSignals(),
    loadChartData(currentChartAsset),
    loadBacktest(),
    loadFearGreed(),
    loadTrending(),
    loadGlobalStats(),
  ]);
  startRefreshTimer();
  setupChartButtons();
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
    txt.textContent = 'Backend Online';
  } else {
    dot.style.background = 'var(--amber)';
    txt.textContent = 'Demo Mode (CoinGecko)';
  }
}

// ── Price Loading ──
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
  } catch (e) {
    console.error('Price load failed:', e);
    // Try CoinGecko fallback
    try {
      const prices = await fetchCoinGeckoPrices();
      renderPrices(prices);
    } catch { }
  }
}

async function fetchCoinGeckoPrices() {
  const ids = Object.keys(ASSETS).join(',');
  const r = await fetchWithRetry(`${COINGECKO}/simple/price?ids=${ids}&vs_currencies=usd&include_24hr_change=true&include_24hr_vol=true&include_market_cap=true`);
  const data = await r.json();
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
    return `
      <div class="card">
        <div class="price-symbol">${ASSETS[p.id]?.symbol || p.symbol}</div>
        <div class="price-name">${ASSETS[p.id]?.name || p.name}</div>
        <div class="price-value">$${formatPrice(p.price)}</div>
        <div class="price-change ${cls}">${arrow} ${Math.abs(change).toFixed(2)}%</div>
      </div>`;
  }).join('');
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
    try {
      const signals = await generateDemoSignals();
      renderSignals(signals);
    } catch {}
  }
}

async function generateDemoSignals() {
  // Fetch OHLC from CoinGecko and compute signals client-side
  const signals = [];
  for (const [id, info] of Object.entries(ASSETS)) {
    try {
      const r = await fetchWithRetry(`${COINGECKO}/coins/${id}/ohlc?vs_currency=usd&days=30`);
      const ohlc = await r.json();
      if (!Array.isArray(ohlc) || ohlc.length < 30) {
        signals.push({ asset_id: id, symbol: info.symbol, signal: 'HOLD', confidence: 50, reason: 'Insufficient data' });
        continue;
      }
      const closes = ohlc.map(c => c[4]);
      const signal = computeSignal(closes, id, info.symbol);
      signals.push(signal);
    } catch {
      signals.push({ asset_id: id, symbol: info.symbol, signal: 'HOLD', confidence: 50, reason: 'Fetch error' });
    }
  }
  return signals;
}

// ── Client-Side Signal Computation ──
function computeSignal(prices, assetId, symbol) {
  const rsiVal = calcRSI(prices, 14);
  const macdData = calcMACD(prices);
  const bb = calcBB(prices);
  const ema20 = calcEMA(prices, 20);
  const ema50 = calcEMA(prices, 50);
  const ema200 = calcEMA(prices, 200);
  const currentPrice = prices[prices.length - 1];

  const buySignals = [];
  const sellSignals = [];

  // RSI
  if (rsiVal !== null) {
    if (rsiVal < 35) buySignals.push(`RSI oversold (${rsiVal.toFixed(1)})`);
    else if (rsiVal > 70) sellSignals.push(`RSI overbought (${rsiVal.toFixed(1)})`);
  }

  // MACD
  if (macdData.bullishCross) buySignals.push('MACD bullish crossover');
  if (macdData.bearishCross) sellSignals.push('MACD bearish crossover');

  // Bollinger
  if (bb.position === 'below_lower') buySignals.push('Price at lower BB');
  else if (bb.position === 'above_upper') sellSignals.push('Price at upper BB');

  // EMA trend
  if (ema200 !== null) {
    if (currentPrice > ema200) buySignals.push('Above EMA 200');
    else sellSignals.push('Below EMA 200');
  }

  // Determine regime
  let regime = 'SIDEWAYS';
  if (ema20 && ema50 && ema200) {
    if (ema20 > ema50 && ema50 > ema200) regime = 'BULL';
    else if (ema20 < ema50 && ema50 < ema200) regime = 'BEAR';
  }

  let signal, confidence;
  if (buySignals.length >= 2 && buySignals.length > sellSignals.length) {
    signal = 'BUY';
    confidence = Math.min((buySignals.length / 4) * 100, 100);
  } else if (sellSignals.length >= 2 && sellSignals.length > buySignals.length) {
    signal = 'SELL';
    confidence = Math.min((sellSignals.length / 4) * 100, 100);
  } else {
    signal = 'HOLD';
    confidence = 50;
  }

  // Build risk + DCA
  const isVolatile = ['BTC', 'ETH', 'SOL'].includes(symbol);
  const slPct = isVolatile ? 8 : 5;
  const slPrice = currentPrice * (1 - slPct / 100);
  const tpPrice = currentPrice * (1 + (slPct * 2) / 100);

  const result = {
    asset_id: assetId,
    symbol,
    signal,
    confidence: Math.round(confidence * 10) / 10,
    reason: [...buySignals, ...sellSignals].join(' | ') || 'No strong confluence',
    buy_signals: buySignals,
    sell_signals: sellSignals,
    rsi: rsiVal,
    macd: macdData.line,
    macd_signal: macdData.signal,
    bb_position: bb.position,
    ema_trend: ema200 ? (currentPrice > ema200 ? 'uptrend' : 'downtrend') : 'unknown',
    market_regime: regime,
    indicators: {
      current_price: currentPrice,
      rsi: rsiVal,
      macd: { macd_line: macdData.line, signal_line: macdData.signal, histogram: macdData.histogram },
      bollinger: { upper: bb.upper, middle: bb.middle, lower: bb.lower },
      ema: { ema_20: ema20, ema_50: ema50, ema_200: ema200, regime },
    },
    risk: {
      stop_loss_pct: slPct,
      stop_loss_price: Math.round(slPrice * 100) / 100,
      take_profit_price: Math.round(tpPrice * 100) / 100,
      max_position_usd: 2500,
      risk_reward_ratio: '1:2',
    },
  };

  if (signal === 'BUY') {
    result.dca_plan = {
      strategy: '3-Tranche DCA',
      total_position_usd: 2500,
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

// ── Technical Indicator Functions (Client-Side) ──
function calcRSI(prices, period = 14) {
  if (prices.length < period + 1) return null;
  let avgGain = 0, avgLoss = 0;
  for (let i = 1; i <= period; i++) {
    const d = prices[i] - prices[i - 1];
    if (d > 0) avgGain += d; else avgLoss -= d;
  }
  avgGain /= period;
  avgLoss /= period;
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
  for (let i = period; i < prices.length; i++) {
    ema = (prices[i] - ema) * m + ema;
  }
  return ema;
}

function calcMACD(prices) {
  const fast = 12, slow = 26, sig = 9;
  if (prices.length < slow + sig) return { line: null, signal: null, histogram: null, bullishCross: false, bearishCross: false };

  // Compute full EMA arrays
  function emaArr(p, per) {
    const r = [];
    let e = p.slice(0, per).reduce((a, b) => a + b) / per;
    for (let i = 0; i < per; i++) r.push(null);
    r[per - 1] = e;
    const m = 2 / (per + 1);
    for (let i = per; i < p.length; i++) {
      e = (p[i] - e) * m + e;
      r.push(e);
    }
    return r;
  }

  const ef = emaArr(prices, fast);
  const es = emaArr(prices, slow);
  const ml = ef.map((f, i) => f !== null && es[i] !== null ? f - es[i] : null);
  const valid = ml.filter(v => v !== null);
  const sl = valid.length >= sig ? (() => {
    let e = valid.slice(0, sig).reduce((a, b) => a + b) / sig;
    const r = Array(sig - 1).fill(null);
    r.push(e);
    const m = 2 / (sig + 1);
    for (let i = sig; i < valid.length; i++) {
      e = (valid[i] - e) * m + e;
      r.push(e);
    }
    return r;
  })() : [];

  const line = valid.length ? valid[valid.length - 1] : null;
  const signal = sl.length ? sl[sl.length - 1] : null;
  const histogram = line !== null && signal !== null ? line - signal : null;

  // Crossover check
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
  const upper = middle + 2 * std;
  const lower = middle - 2 * std;
  const price = prices[prices.length - 1];
  let position = 'upper_half';
  if (price >= upper) position = 'above_upper';
  else if (price <= lower) position = 'below_lower';
  else if (price < middle) position = 'lower_half';
  return { upper, middle, lower, position };
}

// ── Render Functions ──
function renderSignals(signals) {
  const grid = document.getElementById('signalGrid');
  grid.innerHTML = signals.map(s => {
    const cls = s.signal === 'BUY' ? 'signal-buy' : s.signal === 'SELL' ? 'signal-sell' : 'signal-hold';
    const rsi = s.rsi != null ? s.rsi.toFixed(1) : '—';
    const rsiColor = s.rsi < 35 ? 'var(--green)' : s.rsi > 70 ? 'var(--red)' : 'var(--amber)';
    const rsiWidth = s.rsi != null ? s.rsi : 50;
    const confColor = s.confidence >= 70 ? 'var(--green)' : s.confidence >= 40 ? 'var(--amber)' : 'var(--red)';
    return `
      <div class="card">
        <div style="display:flex;justify-content:space-between;align-items:center">
          <span style="font-family:var(--font-mono);font-weight:700;font-size:16px">${s.symbol}</span>
          <span class="signal-badge ${cls}">${s.signal}</span>
        </div>
        <div style="margin-top:12px">
          <div class="rsi-value">RSI: <span style="color:${rsiColor}">${rsi}</span></div>
          <div class="rsi-gauge">
            <div class="rsi-gauge-fill" style="width:${rsiWidth}%;background:${rsiColor}"></div>
          </div>
        </div>
        <div style="margin-top:8px;font-size:12px;color:var(--text-muted)">
          MACD: ${s.macd != null ? s.macd.toFixed(4) : '—'}
        </div>
        <div style="margin-top:4px;font-size:11px;color:var(--text-muted)">${s.reason || '—'}</div>
        <div class="confidence-bar">
          <div class="confidence-fill" style="width:${s.confidence}%;background:${confColor}"></div>
        </div>
        <div style="text-align:right;font-size:11px;color:var(--text-muted);margin-top:4px">${s.confidence}% confidence</div>
      </div>`;
  }).join('');
}

function updateRegime(signals) {
  // Use BTC's regime as the overall market indicator
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
  // Show risk for first non-HOLD signal, or BTC
  const sig = signals.find(s => s.signal !== 'HOLD' && s.risk) || signals.find(s => s.symbol === 'BTC');
  if (!sig?.risk) {
    el.innerHTML = '<div style="color:var(--text-muted)">No risk data</div>';
    return;
  }
  const r = sig.risk;
  el.innerHTML = `
    <div style="font-family:var(--font-mono);font-size:14px;margin-bottom:12px">${sig.symbol} Risk Profile</div>
    <div class="risk-row"><span class="risk-label">Stop-Loss</span><span class="risk-value risk-stop">$${formatPrice(r.stop_loss_price)} (${r.stop_loss_pct}%)</span></div>
    <div class="risk-row"><span class="risk-label">Take-Profit</span><span class="risk-value risk-target">$${formatPrice(r.take_profit_price)}</span></div>
    <div class="risk-row"><span class="risk-label">Max Position</span><span class="risk-value">$${r.max_position_usd?.toLocaleString() || '—'}</span></div>
    <div class="risk-row"><span class="risk-label">Risk/Reward</span><span class="risk-value">${r.risk_reward_ratio}</span></div>
    <div class="risk-row"><span class="risk-label">Max Portfolio Risk</span><span class="risk-value">${r.max_portfolio_risk_pct || 5}%</span></div>`;
}

function updateAlertLog(signals) {
  const el = document.getElementById('alertLog');
  const now = new Date();
  const alerts = signals
    .filter(s => s.signal !== 'HOLD')
    .map(s => ({
      time: now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' }),
      symbol: s.symbol,
      type: s.signal,
      msg: s.reason,
    }));

  if (alerts.length === 0) {
    el.innerHTML = '<div style="color:var(--text-muted);padding:12px;text-align:center">All clear — no actionable signals right now</div>';
    return;
  }

  el.innerHTML = alerts.map(a => {
    const color = a.type === 'BUY' ? 'var(--green)' : 'var(--red)';
    return `
      <div class="alert-item">
        <span class="alert-time">${a.time}</span>
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
      const r = await fetch(`${API_BASE}/api/backtest/${assetId}`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      result = await r.json();
    } else {
      // Demo backtest using CoinGecko data
      const r = await fetchWithRetry(`${COINGECKO}/coins/${assetId}/ohlc?vs_currency=usd&days=90`);
      const ohlc = await r.json();
      if (!Array.isArray(ohlc) || ohlc.length < 50) {
        el.innerHTML = '<div style="color:var(--text-muted)">Insufficient data for backtest</div>';
        return;
      }
      result = runClientBacktest(ohlc, assetId);
    }
    renderBacktest(result);
  } catch (e) {
    el.innerHTML = `<div style="color:var(--red)">Backtest failed: ${e.message}</div>`;
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
    if (rsiVal < 35) buy++;
    if (rsiVal > 70) sell++;

    const ema200 = calcEMA(slice, 200);
    if (ema200 && price > ema200) buy++; else if (ema200) sell++;

    if (buy >= 2 && position === 0) {
      position = capital / price;
      entryPrice = price;
      capital = 0;
    } else if (sell >= 2 && position > 0) {
      capital = position * price;
      trades++;
      if (price > entryPrice) wins++;
      position = 0;
    }
  }
  // Close open position
  if (position > 0) {
    capital = position * closes[closes.length - 1];
    trades++;
    if (closes[closes.length - 1] > entryPrice) wins++;
  }

  return {
    symbol: ASSETS[assetId]?.symbol || '???',
    total_return_pct: round2((capital - 10000) / 100),
    win_rate_pct: trades > 0 ? round2(wins / trades * 100) : 0,
    max_drawdown_pct: round2(maxDD),
    total_trades: trades,
    final_capital: round2(capital),
  };
}

function renderBacktest(bt) {
  if (bt.error) {
    document.getElementById('backtestContent').innerHTML = `<div style="color:var(--text-muted)">${bt.error}</div>`;
    return;
  }
  const retColor = bt.total_return_pct >= 0 ? 'var(--green)' : 'var(--red)';
  document.getElementById('backtestContent').innerHTML = `
    <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px">
      <div class="bt-stat">
        <div class="bt-stat-value" style="color:${retColor}">${bt.total_return_pct >= 0 ? '+' : ''}${bt.total_return_pct}%</div>
        <div class="bt-stat-label">Total Return</div>
      </div>
      <div class="bt-stat">
        <div class="bt-stat-value">${bt.win_rate_pct}%</div>
        <div class="bt-stat-label">Win Rate</div>
      </div>
      <div class="bt-stat">
        <div class="bt-stat-value" style="color:var(--red)">${bt.max_drawdown_pct}%</div>
        <div class="bt-stat-label">Max Drawdown</div>
      </div>
      <div class="bt-stat">
        <div class="bt-stat-value">${bt.total_trades}</div>
        <div class="bt-stat-label">Total Trades</div>
      </div>
    </div>
    <div style="text-align:center;margin-top:12px;font-size:12px;color:var(--text-muted)">
      Final: $${(bt.final_capital || 0).toLocaleString(undefined, {maximumFractionDigits: 2})}
    </div>`;
}

// ── Chart ──
function initChart() {
  const container = document.getElementById('mainChart');
  chart = LightweightCharts.createChart(container, {
    width: container.clientWidth,
    height: 300,
    layout: {
      background: { type: 'solid', color: 'transparent' },
      textColor: 'rgba(255,255,255,0.5)',
      fontFamily: 'JetBrains Mono',
    },
    grid: {
      vertLines: { color: 'rgba(255,255,255,0.03)' },
      horzLines: { color: 'rgba(255,255,255,0.03)' },
    },
    crosshair: {
      mode: LightweightCharts.CrosshairMode.Normal,
    },
    rightPriceScale: {
      borderColor: 'rgba(255,255,255,0.08)',
    },
    timeScale: {
      borderColor: 'rgba(255,255,255,0.08)',
      timeVisible: true,
    },
  });

  candleSeries = chart.addCandlestickSeries({
    upColor: '#00ff88',
    downColor: '#ff3355',
    borderUpColor: '#00ff88',
    borderDownColor: '#ff3355',
    wickUpColor: '#00ff88',
    wickDownColor: '#ff3355',
  });

  // Responsive resize
  new ResizeObserver(() => {
    chart.applyOptions({ width: container.clientWidth });
  }).observe(container);
}

async function loadChartData(assetId) {
  try {
    const r = await fetchWithRetry(`${COINGECKO}/coins/${assetId}/ohlc?vs_currency=usd&days=30`);
    const ohlc = await r.json();
    if (!Array.isArray(ohlc)) return;

    const data = ohlc.map(c => ({
      time: Math.floor(c[0] / 1000),
      open: c[1],
      high: c[2],
      low: c[3],
      close: c[4],
    }));

    candleSeries.setData(data);
    chart.timeScale().fitContent();

    // Update chart title
    const titleEl = document.querySelector('.chart-container').closest('.card').querySelector('.card-title');
    if (titleEl) titleEl.textContent = `${ASSETS[assetId]?.symbol || '???'}/USD`;
  } catch (e) {
    console.error('Chart load failed:', e);
  }
}

function setupChartButtons() {
  document.querySelectorAll('.chart-asset-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.chart-asset-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      btn.style.borderColor = 'var(--green)';
      btn.style.color = 'var(--green)';
      document.querySelectorAll('.chart-asset-btn:not(.active)').forEach(b => {
        b.style.borderColor = '';
        b.style.color = '';
      });
      currentChartAsset = btn.dataset.asset;
      loadChartData(currentChartAsset);
    });
  });
  // Style initial active
  const active = document.querySelector('.chart-asset-btn.active');
  if (active) { active.style.borderColor = 'var(--green)'; active.style.color = 'var(--green)'; }
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
      loadChartData(currentChartAsset);
      // Refresh these less frequently (every 2 cycles = 60s)
      if (!window._refreshCycle) window._refreshCycle = 0;
      window._refreshCycle++;
      if (window._refreshCycle % 2 === 0) {
        loadFearGreed();
        loadTrending();
        loadGlobalStats();
      }
    }
  }, 1000);
}

// ── MetaMask ──
async function connectMetaMask() {
  if (typeof window.ethereum === 'undefined') {
    alert('MetaMask not detected. Install MetaMask to connect your wallet.');
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
    walletInfo.textContent = `Connected: ${short}`;
    // Get balance
    const balance = await window.ethereum.request({
      method: 'eth_getBalance',
      params: [addr, 'latest']
    });
    const ethBalance = parseInt(balance, 16) / 1e18;
    walletInfo.textContent = `${short} | ${ethBalance.toFixed(4)} ETH`;
  } catch (e) {
    console.error('MetaMask connect failed:', e);
  }
}

// ── Logout ──
function logout() {
  localStorage.removeItem('c5isr_auth');
  localStorage.removeItem('c5isr_auth_time');
  localStorage.removeItem('c5isr_token');
  window.location.href = 'index.html';
}

// ── Fear & Greed Index ──
async function loadFearGreed() {
  try {
    const r = await fetchWithRetry('https://api.alternative.me/fng/?limit=1');
    const data = await r.json();
    const fg = data.data?.[0];
    if (!fg) return;

    const value = parseInt(fg.value);
    const label = fg.value_classification;
    const el = document.getElementById('fearGreedValue');
    const pointer = document.getElementById('fearGreedPointer');
    const update = document.getElementById('fearGreedUpdate');

    // Color based on value
    let color;
    if (value <= 25) color = 'var(--red)';
    else if (value <= 45) color = '#ff6644';
    else if (value <= 55) color = 'var(--amber)';
    else if (value <= 75) color = '#88dd44';
    else color = 'var(--green)';

    el.innerHTML = `<span style="color:${color}">${value}</span> <span style="font-size:14px;color:var(--text-secondary)">${label}</span>`;
    pointer.style.left = `${value}%`;

    const updated = new Date(parseInt(fg.timestamp) * 1000);
    update.textContent = `Updated: ${updated.toLocaleDateString()}`;
  } catch (e) {
    console.error('Fear & Greed load failed:', e);
    document.getElementById('fearGreedValue').innerHTML = '<span style="color:var(--text-muted);font-size:14px">Unavailable</span>';
  }
}

// ── Trending Coins ──
async function loadTrending() {
  try {
    const r = await fetchWithRetry(`${COINGECKO}/search/trending`);
    const data = await r.json();
    const coins = data.coins?.slice(0, 7) || [];
    const el = document.getElementById('trendingCoins');

    if (coins.length === 0) {
      el.innerHTML = '<div style="color:var(--text-muted)">No trending data available</div>';
      return;
    }

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
          <div class="trending-coin-price">
            <div>${priceStr}</div>
            ${changeStr}
          </div>
        </div>`;
    }).join('');

    document.getElementById('trendingUpdate').textContent = new Date().toLocaleTimeString();
  } catch (e) {
    console.error('Trending load failed:', e);
    document.getElementById('trendingCoins').innerHTML = '<div style="color:var(--text-muted)">Failed to load trending coins</div>';
  }
}

// ── Global Market Stats ──
async function loadGlobalStats() {
  try {
    const r = await fetchWithRetry(`${COINGECKO}/global`);
    const data = await r.json();
    const g = data.data;
    if (!g) return;

    const fmt = (n) => {
      if (n >= 1e12) return `$${(n / 1e12).toFixed(2)}T`;
      if (n >= 1e9) return `$${(n / 1e9).toFixed(1)}B`;
      if (n >= 1e6) return `$${(n / 1e6).toFixed(0)}M`;
      return `$${n.toLocaleString()}`;
    };

    document.getElementById('globalMarketCap').textContent = fmt(g.total_market_cap?.usd || 0);
    document.getElementById('global24hVol').textContent = fmt(g.total_volume?.usd || 0);
    document.getElementById('btcDominance').textContent = `${(g.market_cap_percentage?.btc || 0).toFixed(1)}%`;
    document.getElementById('ethDominance').textContent = `${(g.market_cap_percentage?.eth || 0).toFixed(1)}%`;
    document.getElementById('activeCryptos').textContent = (g.active_cryptocurrencies || 0).toLocaleString();
  } catch (e) {
    console.error('Global stats load failed:', e);
  }
}

// ── Helpers ──
function formatPrice(n) {
  if (n == null) return '—';
  if (n >= 1000) return n.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  if (n >= 1) return n.toFixed(2);
  if (n >= 0.01) return n.toFixed(4);
  return n.toFixed(6);
}

function round2(n) { return Math.round(n * 100) / 100; }
