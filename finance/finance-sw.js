/* Johns Family Financial Command — installable dashboard service worker
 *
 *   - Precaches the finance suite shell so the dashboard opens offline
 *   - HTML: network-first (fresh numbers when online) -> cache -> offline fallback
 *   - CSS/JS: stale-while-revalidate (fast, self-updating)
 *   - other assets: cache-first
 *   - Lives at /finance/finance-sw.js so its scope defaults to /finance/ —
 *     narrower than the civic /sw.js scope "/", so this worker wins for
 *     finance pages via longest-scope-match; everything else stays civic.
 *     (Same pattern as /family-captain-sw.js.)
 *
 * Steward auth lives in localStorage (moop_steward_auth / moop_finance_auth)
 * — the worker never touches it, so a cache wipe or SW_VERSION bump never
 * re-locks the dashboard.
 *
 * Live-data caveat: the CoinGecko BTC fetch is cross-origin and passes
 * through untouched (no caching); financial-command.html's /snapshot fetch
 * only resolves on Adam's Mac or once intake.usmcmin.com is tunneled — the
 * page's own error state handles that honestly.
 *
 * Bump SW_VERSION when the shell changes so installs refresh on next launch.
 */
const SW_VERSION = 'v6-2026-07-11';
const CORE_CACHE = 'fin-core-' + SW_VERSION;
const RUNTIME_CACHE = 'fin-runtime-' + SW_VERSION;
const OFFLINE_FALLBACK = '/finance/finance.html';

const CORE_ASSETS = [
  '/finance/finance.html',
  '/finance/review.html',
  '/finance/debt.html',
  '/finance/forecast.html',
  '/finance/assets.html',
  '/finance/trading.html',
  '/finance/financial-command.html',
  '/finance/stewardship-dashboard.html',
  '/finance/financial-intake.html',
  '/finance/index.html',
  '/finance/consulting.html',
  '/finance/financial-onboarding.html',
  '/assets/css/main.min.css',
  '/assets/icons/finance-icon-192.png',
  '/assets/icons/finance-icon-512.png',
  '/assets/icons/finance-apple-touch-icon.png',
  '/assets/icons/favicon-32.png',
  '/assets/icons/favicon-16.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CORE_CACHE).then((cache) =>
      cache.addAll(CORE_ASSETS).catch((err) => {
        // Don't fail install on a single missing asset — log and move on.
        console.warn('[fin-sw] some core assets failed to cache', err);
      })
    )
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          // only retire OUR old caches; never touch other workers' caches
          .filter((k) => k.startsWith('fin-core-') || k.startsWith('fin-runtime-'))
          .filter((k) => !k.endsWith(SW_VERSION))
          .map((k) => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  const isHTML =
    req.mode === 'navigate' ||
    (req.headers.get('accept') || '').includes('text/html') ||
    url.pathname.endsWith('.html');

  if (isHTML) {
    event.respondWith(
      fetch(req)
        .then((res) => {
          if (res && res.ok) {
            const clone = res.clone();
            caches.open(RUNTIME_CACHE).then((c) => c.put(req, clone)).catch(() => {});
          }
          return res;
        })
        .catch(() =>
          caches.match(req).then((cached) => cached || caches.match(OFFLINE_FALLBACK))
        )
    );
    return;
  }

  const isStyleOrScript = /\.(css|js)$/i.test(url.pathname);
  if (isStyleOrScript) {
    event.respondWith(
      caches.match(req).then((cached) => {
        const networkFetch = fetch(req).then((res) => {
          if (res && res.ok && res.type === 'basic') {
            const clone = res.clone();
            caches.open(RUNTIME_CACHE).then((c) => c.put(req, clone)).catch(() => {});
          }
          return res;
        }).catch(() => cached);
        return cached || networkFetch;
      })
    );
    return;
  }

  // Other static assets (images, fonts, json): cache-first.
  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;
      return fetch(req).then((res) => {
        if (res && res.ok && res.type === 'basic') {
          const clone = res.clone();
          caches.open(RUNTIME_CACHE).then((c) => c.put(req, clone)).catch(() => {});
        }
        return res;
      }).catch(() => cached);
    })
  );
});
