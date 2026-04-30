/* RESOLUTE Citizen Scorecard — service worker
 *
 * Provides:
 *   - Offline fallback for the main civic-stack pages
 *   - Cache-first delivery of static assets (CSS, JS, images, JSON
 *     lookups) for sub-50ms repeat-visit loads
 *   - Network-first for HTML so visitors always see fresh data when online
 *
 * Bump SW_VERSION when shipping a major change so existing visitors
 * pick up the new shell on their next page navigation.
 */
const SW_VERSION = 'v1-2026-04-30';
const CORE_CACHE = `usmcmin-core-${SW_VERSION}`;
const RUNTIME_CACHE = `usmcmin-runtime-${SW_VERSION}`;

// Hand-picked shell — the first three pages a returning RESOLUTE
// citizen is most likely to hit, plus the assets they share. This
// list is stable; bump SW_VERSION above when it changes.
const CORE_ASSETS = [
  '/',
  '/citizen.html',
  '/find-my-reps.html',
  '/citizen-table.html',
  '/citizen-issues.html',
  '/assets/css/main.min.css',
  '/assets/css/profile.min.css',
  '/assets/js/profile.min.js',
  '/assets/img/logo.png',
  '/assets/img/favicon.png',
  '/assets/og/og-citizen.jpg',
  '/data/index.json',
  '/data/places.json',
];

self.addEventListener('install', (event) => {
  // Pre-cache the shell so first offline load works.
  event.waitUntil(
    caches.open(CORE_CACHE).then((cache) =>
      cache.addAll(CORE_ASSETS).catch((err) => {
        // Don't fail install on a single asset miss — log and move on.
        console.warn('[sw] Some core assets failed to cache', err);
      })
    )
  );
  // Activate immediately on first install.
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  // Wipe old-version caches.
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((k) => !k.endsWith(SW_VERSION))
          .map((k) => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

// Fetch strategy:
//   - HTML / navigation:   network-first, fall back to cache, then to /citizen.html
//   - Static assets:       cache-first, populate runtime cache on miss
//   - Same-origin only:    pass cross-origin straight through to the browser
self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  const isHTML =
    req.mode === 'navigate' ||
    req.headers.get('accept')?.includes('text/html') ||
    url.pathname.endsWith('.html');

  if (isHTML) {
    // Network-first for navigations. Lets fresh scorecard data reach
    // online visitors immediately. On failure, falls back to cache.
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
          caches.match(req).then((cached) => cached || caches.match('/citizen.html'))
        )
    );
    return;
  }

  // Static assets: cache-first.
  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;
      return fetch(req).then((res) => {
        // Don't cache opaque or non-200 responses.
        if (res && res.ok && res.type === 'basic') {
          const clone = res.clone();
          caches.open(RUNTIME_CACHE).then((c) => c.put(req, clone)).catch(() => {});
        }
        return res;
      }).catch(() => cached);
    })
  );
});
