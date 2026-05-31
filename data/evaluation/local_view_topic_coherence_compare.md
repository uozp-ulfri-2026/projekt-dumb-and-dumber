# Local View Topic Coherence Comparison

- Scope: local view candidate sets
- Gemini API: not called
- Queries: 20
- Mean agglomerative coherence: 0.8272
- Mean kmeans coherence: 0.8257
- Mean hdbscan coherence: 0.8244
- Best count: 8
- Agglomerative wins: 7
- KMeans wins: 8
- HDBSCAN wins: 4

| # | Query | Agglomerative | KMeans | HDBSCAN | Winner |
| --- | --- | --- | --- | --- | --- |
| 1 | Vpis v srednje šole | 0.8350 | 0.8356 | 0.8301 | kmeans |
| 2 | Zakoni glede generativne umetne inteligence | 0.8336 | 0.8301 | 0.8229 | agglomerative |
| 3 | Cene kart na nogometnem svetovnem prvenstvu | 0.8231 | 0.8231 | 0.8140 | tie |
| 4 | Tožba slovenskih avtoprevoznikov | 0.8301 | 0.8282 | 0.8312 | hdbscan |
| 5 | Vojna Zvezd v Sloveniji | 0.8389 | 0.8423 | 0.8390 | kmeans |
| 6 | Ogromni zastoji na Slovenskih cestah | 0.8283 | 0.8252 | 0.8362 | hdbscan |
| 7 | Višanje temperatur | 0.8383 | 0.8191 | 0.8296 | agglomerative |
| 8 | Višanje cen nepremičnin v Sloveniji | 0.8501 | 0.8515 | 0.8441 | kmeans |
| 9 | Rogljič in Pogačar na tekmi | 0.8148 | 0.8137 | 0.8090 | agglomerative |
| 10 | Donald Trump novi zakoni | 0.8112 | 0.8113 | 0.8086 | kmeans |
| 11 | Evropska Unija in zveza NATO | 0.8276 | 0.8165 | 0.8278 | hdbscan |
| 12 | Velika Britanija Brexit | 0.8248 | 0.8261 | 0.8251 | kmeans |
| 13 | Vojna v Ukrajini in Zelenski | 0.8230 | 0.8267 | 0.8262 | kmeans |
| 14 | Kitajska proti ZDA | 0.8203 | 0.8192 | 0.8160 | agglomerative |
| 15 | Korupcija v slovenski politiki | 0.8195 | 0.8215 | 0.8201 | kmeans |
| 16 | Izstrelitev rakete v vesolje | 0.8179 | 0.8146 | 0.8151 | agglomerative |
| 17 | Delnice Tesle padajo | 0.8385 | 0.8353 | 0.8227 | agglomerative |
| 18 | Nova verzija umetne inteligence | 0.8231 | 0.8262 | 0.8212 | kmeans |
| 19 | Najbolj prodajan avtomobil | 0.8239 | 0.8295 | 0.8324 | hdbscan |
| 20 | Obisk tujega predsednika | 0.8214 | 0.8171 | 0.8167 | agglomerative |
