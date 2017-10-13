
# Lab 3: URL Shortener


A url shortener is a web service that can take long urls (`https://www.google.com/search?source=hp&q=this+is+a+long+url&oq=this+is+a+long+url&gs_l=psy-ab.3..0i22i30k1.1095.3196.0.3437.19.18.0.0.0.0.137.1480.14j4.18.0....0...1.1.64.psy-ab..1.18.1477.0..0j35i39k1j0i131k1j0i67k1j0i20i264k1j33i22i29i30k1.0.aJvctrIr-Ds`) and create a short url (`goo.gl/pEc4vt`). When the shortener url is activated, the service will take the specific id associated with that url (`pEc4vt`) and look up the url associated with it in the database. If that URL is found, it then redirects to that URL.

| id | code | url |
| ---|---|---|
| `1` | `pEc4vt` | `https://www.google.com/search?s...`|
| `2` | `fso3Fs` | `https://www..`


You *could* use the ID in the url, instead of some code, but that then exposes some details about your database to the public.
