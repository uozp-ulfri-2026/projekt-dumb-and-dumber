# Local View Silhouette Comparison

- Scope: local view candidate sets
- Gemini API: not called
- Queries: 20
- Mean agglomerative silhouette: 0.6050
- Mean kmeans silhouette: 0.6118
- Mean delta (kmeans - agglomerative): 0.0068
- KMeans wins: 13
- Agglomerative wins: 6
- Ties: 1

| # | Query | Candidates | Clusters | Agglomerative | KMeans | Delta | Winner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Vpis v srednje šole | 100 | 6 | 0.6349 | 0.6435 | 0.0087 | kmeans |
| 2 | Zakoni glede generativne umetne inteligence | 100 | 6 | 0.5900 | 0.5510 | -0.0390 | agglomerative |
| 3 | Cene kart na nogometnem svetovnem prvenstvu | 100 | 6 | 0.6977 | 0.6977 | 0.0000 | tie |
| 4 | Tožba slovenskih avtoprevoznikov | 100 | 6 | 0.6059 | 0.6275 | 0.0217 | kmeans |
| 5 | Vojna Zvezd v Sloveniji | 100 | 6 | 0.5574 | 0.5799 | 0.0225 | kmeans |
| 6 | Ogromni zastoji na Slovenskih cestah | 100 | 6 | 0.6411 | 0.6337 | -0.0073 | agglomerative |
| 7 | Višanje temperatur | 100 | 6 | 0.5852 | 0.6309 | 0.0457 | kmeans |
| 8 | Višanje cen nepremičnin v Sloveniji | 100 | 6 | 0.7875 | 0.7862 | -0.0013 | agglomerative |
| 9 | Rogljič in Pogačar na tekmi | 100 | 6 | 0.5933 | 0.6053 | 0.0120 | kmeans |
| 10 | Donald Trump novi zakoni | 100 | 6 | 0.6964 | 0.6999 | 0.0035 | kmeans |
| 11 | Evropska Unija in zveza NATO | 100 | 6 | 0.5393 | 0.4963 | -0.0431 | agglomerative |
| 12 | Velika Britanija Brexit | 100 | 6 | 0.5109 | 0.5470 | 0.0361 | kmeans |
| 13 | Vojna v Ukrajini in Zelenski | 100 | 6 | 0.4604 | 0.5403 | 0.0799 | kmeans |
| 14 | Kitajska proti ZDA | 100 | 6 | 0.5317 | 0.5081 | -0.0236 | agglomerative |
| 15 | Korupcija v slovenski politiki | 100 | 6 | 0.5246 | 0.5659 | 0.0413 | kmeans |
| 16 | Izstrelitev rakete v vesolje | 100 | 6 | 0.6328 | 0.6419 | 0.0091 | kmeans |
| 17 | Delnice Tesle padajo | 100 | 6 | 0.7620 | 0.6664 | -0.0956 | agglomerative |
| 18 | Nova verzija umetne inteligence | 100 | 6 | 0.5135 | 0.5159 | 0.0023 | kmeans |
| 19 | Najbolj prodajan avtomobil | 100 | 6 | 0.6106 | 0.6515 | 0.0409 | kmeans |
| 20 | Obisk tujega predsednika | 100 | 6 | 0.6255 | 0.6473 | 0.0218 | kmeans |

## 1. Vpis v srednje šole
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.6349
- KMeans silhouette: 0.6435
- Delta: 0.0087
- Winner: kmeans

## 2. Zakoni glede generativne umetne inteligence
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.5900
- KMeans silhouette: 0.5510
- Delta: -0.0390
- Winner: agglomerative

## 3. Cene kart na nogometnem svetovnem prvenstvu
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.6977
- KMeans silhouette: 0.6977
- Delta: 0.0000
- Winner: tie

## 4. Tožba slovenskih avtoprevoznikov
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.6059
- KMeans silhouette: 0.6275
- Delta: 0.0217
- Winner: kmeans

## 5. Vojna Zvezd v Sloveniji
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.5574
- KMeans silhouette: 0.5799
- Delta: 0.0225
- Winner: kmeans

## 6. Ogromni zastoji na Slovenskih cestah
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.6411
- KMeans silhouette: 0.6337
- Delta: -0.0073
- Winner: agglomerative

## 7. Višanje temperatur
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.5852
- KMeans silhouette: 0.6309
- Delta: 0.0457
- Winner: kmeans

## 8. Višanje cen nepremičnin v Sloveniji
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.7875
- KMeans silhouette: 0.7862
- Delta: -0.0013
- Winner: agglomerative

## 9. Rogljič in Pogačar na tekmi
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.5933
- KMeans silhouette: 0.6053
- Delta: 0.0120
- Winner: kmeans

## 10. Donald Trump novi zakoni
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.6964
- KMeans silhouette: 0.6999
- Delta: 0.0035
- Winner: kmeans

## 11. Evropska Unija in zveza NATO
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.5393
- KMeans silhouette: 0.4963
- Delta: -0.0431
- Winner: agglomerative

## 12. Velika Britanija Brexit
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.5109
- KMeans silhouette: 0.5470
- Delta: 0.0361
- Winner: kmeans

## 13. Vojna v Ukrajini in Zelenski
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.4604
- KMeans silhouette: 0.5403
- Delta: 0.0799
- Winner: kmeans

## 14. Kitajska proti ZDA
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.5317
- KMeans silhouette: 0.5081
- Delta: -0.0236
- Winner: agglomerative

## 15. Korupcija v slovenski politiki
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.5246
- KMeans silhouette: 0.5659
- Delta: 0.0413
- Winner: kmeans

## 16. Izstrelitev rakete v vesolje
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.6328
- KMeans silhouette: 0.6419
- Delta: 0.0091
- Winner: kmeans

## 17. Delnice Tesle padajo
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.7620
- KMeans silhouette: 0.6664
- Delta: -0.0956
- Winner: agglomerative

## 18. Nova verzija umetne inteligence
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.5135
- KMeans silhouette: 0.5159
- Delta: 0.0023
- Winner: kmeans

## 19. Najbolj prodajan avtomobil
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.6106
- KMeans silhouette: 0.6515
- Delta: 0.0409
- Winner: kmeans

## 20. Obisk tujega predsednika
- Candidates: 100
- Clusters: 6
- Agglomerative silhouette: 0.6255
- KMeans silhouette: 0.6473
- Delta: 0.0218
- Winner: kmeans
