/* fit20 Liberty Studio Command PWA · V4.0 · cache shell only, never data/ */
const CACHE = "sc-liberty-v4";
const PRECACHE = ["./","./index.html","./manifest.webmanifest","./assets/favicon.png","./assets/fit20-logo.png",
  "./assets/fit20-mark-192.png","./assets/icon-192.png","./assets/icon-512.png","./assets/apple-touch-icon.png"];
self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(PRECACHE)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
    .then(() => self.clients.claim()));
});
self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.pathname.includes("/data/")) return;          // never cache data/ (PII)
  if (url.origin !== self.location.origin) return;      // same-origin shell only
  // Network first so a new pack shows up on refresh; cache is the offline fallback.
  e.respondWith(fetch(req).then((res) => {
    if (res && res.ok && res.type === "basic") { const copy = res.clone(); caches.open(CACHE).then((c) => c.put(req, copy)); }
    return res;
  }).catch(() => caches.match(req).then((hit) => hit || caches.match("./index.html"))));
});
