/* The Husband Course — installable, offline-capable service worker.
 *
 *   - Precaches the course shell so every module works offline.
 *   - HTML: network-first (fresh when online) -> cache -> offline fallback.
 *   - CSS/JS: stale-while-revalidate (fast, self-updating).
 *   - other assets: cache-first.
 *   - Lives at /tmc-husband/sw.js so its default scope is /tmc-husband/ —
 *     it never fights the civic root worker; longest-scope-match wins here.
 *
 * Course progress lives in localStorage (usmcmin:tmc-husband:v1:*). This worker
 * NEVER touches it, so a cache wipe or version bump never erases progress.
 *
 * Bump SW_VERSION when the shell changes so installs refresh on next launch.
 */
const SW_VERSION = 'v1-2026-08-01';
const CORE_CACHE = 'tmc-core-' + SW_VERSION;
const RUNTIME_CACHE = 'tmc-runtime-' + SW_VERSION;
const OFFLINE_FALLBACK = '/tmc-husband/index.html';

const CORE_ASSETS = [
  '/tmc-husband/index.html',
  '/tmc-husband/about.html',
  '/tmc-husband/progress.html',
  '/tmc-husband/module-01.html',
  '/tmc-husband/module-02.html',
  '/tmc-husband/module-03.html',
  '/tmc-husband/module-04.html',
  '/tmc-husband/module-05.html',
  '/tmc-husband/module-06.html',
  '/tmc-husband/module-07.html',
  '/assets/css/tmc-husband.v1.css',
  '/assets/js/tmc-husband.v1.js',
  '/assets/icons/icon-192.png',
  '/assets/icons/icon-512.png',
  '/assets/icons/apple-touch-icon.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CORE_CACHE).then((cache) =>
      // Don't fail the whole install if a single asset 404s.
      cache.addAll(CORE_ASSETS).catch((err) => console.warn('[tmc-sw] some core assets failed to cache', err))
    )
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((k) => k.startsWith('tmc-core-') || k.startsWith('tmc-runtime-'))
          .filter((k) => !k.endsWith(SW_VERSION))
          .map((k) => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

function isHTML(request) {
  return request.mode === 'navigate' ||
    (request.headers.get('accept') || '').includes('text/html');
}

function isAsset(url) {
  return /\.(css|js)$/.test(url.pathname);
}

self.addEventListener('fetch', (event) => {
  const request = event.request;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);
  if (url.origin !== self.location.origin) return;

  // HTML: network-first -> cache -> offline fallback.
  if (isHTML(request)) {
    event.respondWith(
      fetch(request)
        .then((response) => {
          const copy = response.clone();
          caches.open(RUNTIME_CACHE).then((cache) => cache.put(request, copy));
          return response;
        })
        .catch(() => caches.match(request).then((hit) => hit || caches.match(OFFLINE_FALLBACK)))
    );
    return;
  }

  // CSS/JS: stale-while-revalidate.
  if (isAsset(url)) {
    event.respondWith(
      caches.match(request).then((cached) => {
        const network = fetch(request).then((response) => {
          const copy = response.clone();
          caches.open(RUNTIME_CACHE).then((cache) => cache.put(request, copy));
          return response;
        }).catch(() => cached);
        return cached || network;
      })
    );
    return;
  }

  // Everything else (images, fonts, media): cache-first.
  event.respondWith(
    caches.match(request).then((cached) => cached || fetch(request).then((response) => {
      const copy = response.clone();
      caches.open(RUNTIME_CACHE).then((cache) => cache.put(request, copy));
      return response;
    }).catch(() => cached))
  );
});
