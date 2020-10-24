const staticCacheName = "django-pwa-v" + new Date().getTime();
const filesToCache = [
    '/offline/',
    '/static/icons/16.png',
    '/static/icons/32.png',
    '/static/icons/64.png',
    '/static/icons/128.png',
    // '/static/icons/splash-640x1136.png',
    // '/static/icons/splash-750x1334.png',
    // '/static/icons/splash-1242x2208.png',
    // '/static/icons/splash-1125x2436.png',
    // '/static/icons/splash-828x1792.png',
    // '/static/icons/splash-1242x2688.png',
    // '/static/icons/splash-1536x2048.png',
    // '/static/icons/splash-1668x2224.png',
    // '/static/icons/splash-1668x2388.png',
    // '/static/icons/splash-2048x2732.png'
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});