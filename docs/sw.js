// Offline cache for the VC Lab companion.
// Bump CACHE when the site content changes so clients refetch.
const CACHE = 'vc-lab-v9';
const ASSETS = [
  './',
  'index.html',
  'thesis.html',
  'glossary.html',
  'notes.html',
  'structure.html',
  'drills.html',
  'pipeline.html',
  'memo.html',
  'impact.html',
  'proof.html',
  'assignments.html',
  'style.css',
  'favicon.svg',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE).then((c) => c.addAll(ASSETS)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

// Network first so content stays fresh, falling back to cache when offline.
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    fetch(event.request)
      .then((res) => {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(event.request, copy)).catch(() => {});
        return res;
      })
      .catch(() => caches.match(event.request).then((hit) => hit || caches.match('glossary.html')))
  );
});
