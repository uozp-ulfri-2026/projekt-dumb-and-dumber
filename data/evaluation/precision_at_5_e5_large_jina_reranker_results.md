# Precision@5 evaluation with Jina reranker v2

Created: 2026-05-31T21:07:00
Relevance rule: largely related
Embedding model: `intfloat/multilingual-e5-large`
Query embedding method: `transformers AutoModel mean pooling, query prefix, L2 normalized`
Reranker model: `jinaai/jina-reranker-v2-base-multilingual`
Retrieval: FAISS top 50 candidates, Jina reranked, evaluated top 5 results
Full labeled JSON output: `data/evaluation/precision_at_5_e5_large_jina_reranker_decisions.json`
Raw Jina reranker output: `data/evaluation/precision_at_5_e5_large_jina_reranker_raw_outputs.json`

## Overall result

- Total relevant results: 86/100
- Micro precision@5: 0.86
- Macro precision@5: 0.86

## Per-prompt summary

| # | Prompt | Relevant@5 | Precision@5 |
|---:|---|---:|---:|
| 1 | Vpis v srednje šole | 5/5 | 1.00 |
| 2 | Zakoni glede generativne umetne inteligence | 5/5 | 1.00 |
| 3 | Cene kart na nogometnem svetovnem prvenstvu | 3/5 | 0.60 |
| 4 | Tožba slovenskih avtoprevoznikov | 3/5 | 0.60 |
| 5 | Vojna Zvezd v Sloveniji | 1/5 | 0.20 |
| 6 | Ogromni zastoji na Slovenskih cestah | 5/5 | 1.00 |
| 7 | Višanje temperatur | 3/5 | 0.60 |
| 8 | Višanje cen nepremičnin v Sloveniji | 5/5 | 1.00 |
| 9 | Rogljič in Pogačar na tekmi | 5/5 | 1.00 |
| 10 | Donald Trump novi zakoni | 5/5 | 1.00 |
| 11 | Evropska Unija in zveza NATO | 5/5 | 1.00 |
| 12 | Velika Britanija Brexit | 4/5 | 0.80 |
| 13 | Vojna v Ukrajini in Zelenski | 5/5 | 1.00 |
| 14 | Kitajska proti ZDA | 5/5 | 1.00 |
| 15 | Korupcija v slovenski politiki | 4/5 | 0.80 |
| 16 | Izstrelitev rakete v vesolje | 5/5 | 1.00 |
| 17 | Delnice Tesle padajo | 5/5 | 1.00 |
| 18 | Nova verzija umetne inteligence | 4/5 | 0.80 |
| 19 | Najbolj prodajan avtomobil | 5/5 | 1.00 |
| 20 | Obisk tujega predsednika | 4/5 | 0.80 |

## Detailed decisions

### 1. Vpis v srednje šole

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Končane prijave za vpis v srednje šole, največ zanimanja za srednje strokovno izobraževanje
- Decision: relevant
- Rationale: Direct secondary-school enrolment result.
- Category/date: slovenija / 2025-04-09T09:14:45
- URL: https://www.rtvslo.si/slovenija/koncane-prijave-za-vpis-v-srednje-sole-najvec-zanimanja-za-srednje-strokovno-izobrazevanje/742171
- FAISS rank/score: 1 / 0.8696
- Jina reranker score: 0.7344
- Keywords: Gimnazijski programi, Strokovno izobraževanje, Srednje šole, Vpis
- Excerpt: Končane prijave za vpis v srednje šole, največ zanimanja za srednje strokovno izobraževanje Ključne besede: Gimnazijski programi, Strokovno izobraževanje, Srednje šole, Vpis V prve letnike srednjih šol v prihodnjem šolskem letu se je na 26.008 razpisanih prostih mest prijavilo 23.933 kandidatov. Rok za prijave je potekel 2. aprila. Ministrstvo za vzgojo in izobraževanje je objavilo podatke o vpisu v srednje šole v šolskem letu 2025/2026. Na programe nižjega poklicnega izobraževanja, kjer je razp...

#### Rank 2: RELEVANT

- Title: Vpis v srednje šole: največ zanimanja za srednje strokovne šole
- Decision: relevant
- Rationale: Direct secondary-school enrolment result.
- Category/date: slovenija / 2023-04-25T17:29:00
- URL: https://www.rtvslo.si/slovenija/vpis-v-srednje-sole-najvec-zanimanja-za-srednje-strokovne-sole/666150
- FAISS rank/score: 4 / 0.8626
- Jina reranker score: 0.7344
- Keywords: vpis, šolsko leto, srednje šole, kandidati, mesta, prijavnica, izobraževalni programi, ministrstvo, poklicno izobraževanje, gimnazije, strokovno izobraževanje, razpisana mesta, podatki, statistika, sprejem, vpisni postopek, razporeditev, sposobnosti, prvi krog, programi, prosti poklice, želeni poklic, osnovno šolanje.
- Excerpt: Vpis v srednje šole: največ zanimanja za srednje strokovne šole Ključne besede: vpis, šolsko leto, srednje šole, kandidati, mesta, prijavnica, izobraževalni programi, ministrstvo, poklicno izobraževanje, gimnazije, strokovno izobraževanje, razpisana mesta, podatki, statistika, sprejem, vpisni postopek, razporeditev, sposobnosti, prvi krog, programi, prosti poklice, želeni poklic, osnovno šolanje. Za vpis novincev v srednje šole za prihodnje šolsko leto se je v roku na skupno 25.560 prvotno razpi...

#### Rank 3: RELEVANT

- Title: Vpis je omejen na 58 srednjih šolah, povečal se je vpis v srednje in nižje poklicne šole
- Decision: relevant
- Rationale: Direct secondary-school enrolment result.
- Category/date: slovenija / 2024-05-23T11:08:23
- URL: https://www.rtvslo.si/slovenija/vpis-je-omejen-na-58-srednjih-solah-povecal-se-je-vpis-v-srednje-in-nizje-poklicne-sole/709285
- FAISS rank/score: 2 / 0.8641
- Jina reranker score: 0.7031
- Keywords: Ministrstvo za vzgojo in izobraževanje, Gimnazijski programi, Poklicno izobraževanje, Srednje šole, Vpis
- Excerpt: Vpis je omejen na 58 srednjih šolah, povečal se je vpis v srednje in nižje poklicne šole Ključne besede: Ministrstvo za vzgojo in izobraževanje, Gimnazijski programi, Poklicno izobraževanje, Srednje šole, Vpis Prihodnje šolsko leto bo srednje šole obiskovalo 22.971 kandidatov, največ, 42,7 odstotka, se jih je vpisalo v srednje strokovne šole, sledijo gimnazije, srednje poklicne in nižje poklicne šole. Vpis bo omejen na 58 šolah, medtem ko je bil lani na 70. Vpis je omejen v 12 programih poklicne...

#### Rank 4: RELEVANT

- Title: V srednje šole sprejetih 22.127 bodočih dijakov, na voljo je bilo 25.444 vpisnih mest
- Decision: relevant
- Rationale: Direct secondary-school enrolment result.
- Category/date: slovenija / 2023-07-03T08:56:03
- URL: https://www.rtvslo.si/slovenija/v-srednje-sole-sprejetih-22-127-bodocih-dijakov-na-voljo-je-bilo-25-444-vpisnih-mest/673860
- FAISS rank/score: 8 / 0.8603
- Jina reranker score: 0.6914
- Keywords: Srednje šole, dijaki, vpis, prosta mesta, ministrstvo, vzgoja, izobraževanje, srednješolski programi, prijavno-vpisni postopek, novinci, razpisana mesta, poklicno izobraževanje, gimnazije, omejitev vpisa, izbirni postopek, želeno šolo, drugi krog, mest, šole
- Excerpt: V srednje šole sprejetih 22.127 bodočih dijakov, na voljo je bilo 25.444 vpisnih mest Ključne besede: Srednje šole, dijaki, vpis, prosta mesta, ministrstvo, vzgoja, izobraževanje, srednješolski programi, prijavno-vpisni postopek, novinci, razpisana mesta, poklicno izobraževanje, gimnazije, omejitev vpisa, izbirni postopek, želeno šolo, drugi krog, mest, šole Ministrstvo za vzgojo in izobraževanje je objavilo število še prostih mest za vpis v 1. letnik posameznih srednješolskih programov. Kandida...

#### Rank 5: RELEVANT

- Title: V srednje šole vpisanih skoraj 23.000 učencev. Vse več zanimanja za nižje poklicno izobraževanje.
- Decision: relevant
- Rationale: Direct secondary-school enrolment result.
- Category/date: slovenija / 2024-04-08T16:37:29
- URL: https://www.rtvslo.si/slovenija/v-srednje-sole-vpisanih-skoraj-23-000-ucencev-vse-vec-zanimanja-za-nizje-poklicno-izobrazevanje/704324
- FAISS rank/score: 10 / 0.8596
- Jina reranker score: 0.6914
- Keywords: vpis, srednje šole, program, prijava, izobraževanje, ministrstvo, šolsko leto, razpis, kandidati, učenci, trend, število mest, poklicno izobraževanje, gimnazija, srednje strokovno izobraževanje, vajeništvo, osnovnošolci, rok za prijavo, šolski programi, razpisana mesta
- Excerpt: V srednje šole vpisanih skoraj 23.000 učencev. Vse več zanimanja za nižje poklicno izobraževanje. Ključne besede: vpis, srednje šole, program, prijava, izobraževanje, ministrstvo, šolsko leto, razpis, kandidati, učenci, trend, število mest, poklicno izobraževanje, gimnazija, srednje strokovno izobraževanje, vajeništvo, osnovnošolci, rok za prijavo, šolski programi, razpisana mesta Do 2. aprila, ko je potekel rok za prijavo za vpis novincev v srednje šole za šolsko leto 2024/2025, se je na 26.066...


### 2. Zakoni glede generativne umetne inteligence

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: "Umetniška dela ustvarjajo izključno ljudje": poziv evropskega knjižnega sektorja za zaščito knjig
- Decision: relevant
- Rationale: Generative AI and legal/copyright protection.
- Category/date: kultura / 2025-04-23T17:02:00
- URL: https://www.rtvslo.si/kultura/knjige/umetniska-dela-ustvarjajo-izkljucno-ljudje-poziv-evropskega-knjiznega-sektorja-za-zascito-knjig/743658
- FAISS rank/score: 19 / 0.8383
- Jina reranker score: 0.5469
- Keywords: Evropski knjižni sektor, Generativna UI, Kulturni ekosistem, Avtorske pravice, Umetna inteligenca
- Excerpt: "Umetniška dela ustvarjajo izključno ljudje": poziv evropskega knjižnega sektorja za zaščito knjig Ključne besede: Evropski knjižni sektor, Generativna UI, Kulturni ekosistem, Avtorske pravice, Umetna inteligenca Ob vse večjem pojavu knjig, ki jih generira umetna inteligenca, evropski knjižni sektor poziva evropske politične odločevalce, da zaščitijo avtorska dela z jasnimi oznakami, finančno pa naj strojnega dela ne podpirajo z javnimi sredstvi. " Strojno izdelani proizvodi, ki z uporabo genera...

#### Rank 2: RELEVANT

- Title: Nezadovoljstvo imetnikov pravic z implementacijo meril EU-akta o umetni inteligenci
- Decision: relevant
- Rationale: Direct EU AI Act / rights-holder criteria result.
- Category/date: kultura / 2025-07-31T15:07:04
- URL: https://www.rtvslo.si/kultura/drugo/nezadovoljstvo-imetnikov-pravic-z-implementacijo-meril-eu-akta-o-umetni-inteligenci/753436
- FAISS rank/score: 8 / 0.8423
- Jina reranker score: 0.5273
- Keywords: Kodeks ravnanja, Intelektualna lastnina, EU-akt, Imetniki pravic, Umetna inteligenca
- Excerpt: Nezadovoljstvo imetnikov pravic z implementacijo meril EU-akta o umetni inteligenci Ključne besede: Kodeks ravnanja, Intelektualna lastnina, EU-akt, Imetniki pravic, Umetna inteligenca Predstavniki nezadovoljnih imetnikov pravic v kulturnih in ustvarjalnih sektorjih EU-ja so v povezavi z implementacijo meril Akta EU-ja o umetni inteligenci, ki jih je sprejela Evropska komisija, objavili protestno izjavo. Predstavniki evropskih in svetovnih avtorjev, izvajalcev, založnikov, producentov in drugih...

#### Rank 3: RELEVANT

- Title: Ob koncu kampanje UIzi prevedeno. UIzi zgrešeno: "UI naj v etični rabi podpira človečnost"
- Decision: relevant
- Rationale: AI ethics/transparency/copyright regulation.
- Category/date: kultura / 2025-11-03T17:49:11
- URL: https://www.rtvslo.si/kultura/jezik/ob-koncu-kampanje-uizi-prevedeno-uizi-zgreseno-ui-naj-v-eticni-rabi-podpira-clovecnost/762817
- FAISS rank/score: 43 / 0.8288
- Jina reranker score: 0.4961
- Keywords: Jezikovni poklici, Transparentnost, Etična raba, Avtorska pravica, Umetna inteligenca
- Excerpt: Ob koncu kampanje UIzi prevedeno. UIzi zgrešeno: "UI naj v etični rabi podpira človečnost" Ključne besede: Jezikovni poklici, Transparentnost, Etična raba, Avtorska pravica, Umetna inteligenca Organizatorji kampanje UIzi prevedeno. UIzi zgrešeno so ob njenem zaključku na javnost in odločevalce naslovili več zahtev, ki se dotikajo avtorskih pravic, transparentnosti glede rabe UI-ja ter ohranitve in razvoja jezikovnih poklicev. Glede avtorske pravice so zahteve podali v osmih točkah. Med drugim za...

#### Rank 4: RELEVANT

- Title: Vlada sprejela predlog, ki prinaša enotna pravila za razvoj in uporabo umetne inteligence v EU-ju
- Decision: relevant
- Rationale: Direct AI law/rules result.
- Category/date: slovenija / 2025-08-21T15:32:29
- URL: https://www.rtvslo.si/slovenija/vlada-sprejela-predlog-ki-prinasa-enotna-pravila-za-razvoj-in-uporabo-umetne-inteligence-v-eu-ju/755310
- FAISS rank/score: 20 / 0.8375
- Jina reranker score: 0.4668
- Keywords: UI, zakon, evropska uredba
- Excerpt: Vlada sprejela predlog, ki prinaša enotna pravila za razvoj in uporabo umetne inteligence v EU-ju Ključne besede: UI, zakon, evropska uredba Vlada je sprejela predlog zakona o izvajanju evropske uredbe o določitvi harmoniziranih pravil o umetni inteligenci oz. akta o umetni inteligenci. Predlog med drugim določa nadzorne organe in uvaja možnost imenovanja komisarja za etiko umetne inteligence. Akt o umetni inteligenci, katerega namen je izboljšati delovanje notranjega trga z uvedbo enotnih pravi...

#### Rank 5: RELEVANT

- Title: ZPS: Umetna inteligenca prinaša tudi negativne posledice – kršenje zasebnosti in osebne integritete
- Decision: relevant
- Rationale: Generative AI rights/legislation/regulation result.
- Category/date: gospodarstvo / 2023-06-20T13:58:03
- URL: https://www.rtvslo.si/gospodarstvo/zps-umetna-inteligenca-prinasa-tudi-negativne-posledice-krsenje-zasebnosti-in-osebne-integritete/672448
- FAISS rank/score: 5 / 0.8465
- Jina reranker score: 0.4590
- Keywords: Generativna umetna inteligenca, ZPS, Chat GPT, umetna inteligenca, potrošniki, tehnologija, aplikacija, pravice, zaupanje, varnost, kršenje zasebnosti, internet, digitalna politika, zakonodaja, Evropska unija, regulativa, ozaveščanje, opolnomočenje, lobiranje
- Excerpt: ZPS: Umetna inteligenca prinaša tudi negativne posledice – kršenje zasebnosti in osebne integritete Ključne besede: Generativna umetna inteligenca, ZPS, Chat GPT, umetna inteligenca, potrošniki, tehnologija, aplikacija, pravice, zaupanje, varnost, kršenje zasebnosti, internet, digitalna politika, zakonodaja, Evropska unija, regulativa, ozaveščanje, opolnomočenje, lobiranje V zadnjih mesecih je prišlo do bliskovite rasti ponudbe storitev, ki jih poganja generativna umetna inteligenca, ta pa ogrož...


### 3. Cene kart na nogometnem svetovnem prvenstvu

Precision@5: 3/5 = 0.60

#### Rank 1: RELEVANT

- Title: Tožba proti Fifi zaradi visokih cen vstopnic na SP 2026
- Decision: relevant
- Rationale: Direct World Cup ticket price lawsuit.
- Category/date: sport / 2026-03-24T11:22:40
- URL: https://www.rtvslo.si/sport/nogomet/tozba-proti-fifi-zaradi-visokih-cen-vstopnic-na-sp-2026/777332
- FAISS rank/score: 3 / 0.8608
- Jina reranker score: 0.3906
- Keywords: vstopnice, cene, svetovno prvenstvo, nogomet
- Excerpt: Tožba proti Fifi zaradi visokih cen vstopnic na SP 2026 Ključne besede: vstopnice, cene, svetovno prvenstvo, nogomet Združenje nogometnih navijačev Evrope (FSE) je pri Evropski komisiji vložilo tožbo proti Mednarodni nogometni zvezi (Fifa) zaradi previsokih cen vstopnic na letošnjem svetovnem prvenstvu, ki bo v ZDA, Kanadi in Mehiki. "Fifa ima monopol nad prodajo vstopnic za svetovno prvenstvo 2026 in to moč je izkoristila za vsiljevanje pogojev nogometnim privržencem, ki v konkurenčnem tržnem o...

#### Rank 2: RELEVANT

- Title: Infantino zagovarja visoke cene vstopnic in pravi, da bodo ves denar vložili spet v nogomet
- Decision: relevant
- Rationale: Direct World Cup ticket price result.
- Category/date: sport / 2025-12-30T08:47:57
- URL: https://www.rtvslo.si/sport/nogomet/infantino-zagovarja-visoke-cene-vstopnic-in-pravi-da-bodo-ves-denar-vlozili-spet-v-nogomet/768669
- FAISS rank/score: 2 / 0.8611
- Jina reranker score: 0.3164
- Keywords: Gianni Infantino, Fifa, SP, vstopnice
- Excerpt: Infantino zagovarja visoke cene vstopnic in pravi, da bodo ves denar vložili spet v nogomet Ključne besede: Gianni Infantino, Fifa, SP, vstopnice Predsednik Mednarodne nogometne zveze Fife Gianni Infantino zagovarja visoke cene vstopnic za prihajajoče svetovno prvenstvo. Infantino je dejal, da cene vstopnic zgolj odražajo trenutno povpraševanje po njih. Združenje nogometnih navijačev (FSA) je od začetka prodaje vstopnic za tekmovanje, ki bo med 11. junijem in 19. julijem prihodnje leto potekalo...

#### Rank 3: NOT RELEVANT

- Title: Šeško zatresel mrežo nemočnega Kölna, Kane poskrbel za šov ob vrnitvi Neuerja
- Decision: not_relevant
- Rationale: Football match article, not World Cup ticket prices.
- Category/date: sport / 2023-10-28T18:29:20
- URL: https://www.rtvslo.si/sport/nogomet/nemsko-nogometno-prvenstvo/sesko-zatresel-mrezo-nemocnega-koelna-kane-poskrbel-za-sov-ob-vrnitvi-neuerja/686496
- FAISS rank/score: 37 / 0.8249
- Jina reranker score: 0.2832
- Keywords: Harry Kane, Manuel Neuer, Benjamin Šeško, Oliver Baumann, rdeči kartoni, hat-trick, Bayern, Allianz Arena, Darmstadt, Bundesliga, Nemčija, Katar, svetovno prvenstvo, zlom noge, okrevanje, Sven Ulreich, Joshua Kimmich, derbi, Dortmund, Konrad Laimer, Klaus Gjasula, Matej Maglica, videosodnik, Blancosljed, gol.
- Excerpt: Šeško zatresel mrežo nemočnega Kölna, Kane poskrbel za šov ob vrnitvi Neuerja Ključne besede: Harry Kane, Manuel Neuer, Benjamin Šeško, Oliver Baumann, rdeči kartoni, hat-trick, Bayern, Allianz Arena, Darmstadt, Bundesliga, Nemčija, Katar, svetovno prvenstvo, zlom noge, okrevanje, Sven Ulreich, Joshua Kimmich, derbi, Dortmund, Konrad Laimer, Klaus Gjasula, Matej Maglica, videosodnik, Blancosljed, gol. Trije rdeči kartoni v prvem polčasu, osem golov v drugem polčasu, hat-trick Harryja Kana z mojs...

#### Rank 4: NOT RELEVANT

- Title: Zasoljene cene vstopnic za slovenske tekme v Zagrebu
- Decision: not_relevant
- Rationale: Handball World Cup tickets, not football World Cup tickets.
- Category/date: sport / 2025-01-13T15:29:38
- URL: https://www.rtvslo.si/sport/rokomet/sp-v-rokometu-2025/zasoljene-cene-vstopnic-za-slovenske-tekme-v-zagrebu/733223
- FAISS rank/score: 4 / 0.8465
- Jina reranker score: 0.2695
- Keywords: Cene, Slovenija, Svetovno prvenstvo, Zagreb, Vstopnice
- Excerpt: Zasoljene cene vstopnic za slovenske tekme v Zagrebu Ključne besede: Cene, Slovenija, Svetovno prvenstvo, Zagreb, Vstopnice Slovenski rokometaši bodo skupinski del svetovnega prvenstva ter morebitna četrtfinale in polfinale odigrali v Zagrebu. Pričakuje se veliko slovenskih navijačev, a vstopnice nikakor niso poceni. Še več, zagrebška Arena bo imela v prvem delu najdražje vstopnice, dražje tudi od tistih na Danskem in Norveškem, ki sta soorganizatorici svetovnega prvenstva. Slovenija se bo v prv...

#### Rank 5: RELEVANT

- Title: Ogromno povpraševanje za nogometni spektakel leta
- Decision: relevant
- Rationale: World Cup ticket demand/sales result.
- Category/date: sport / 2026-01-15T16:54:35
- URL: https://www.rtvslo.si/sport/nogomet/svetovno-prvenstvo-v-nogometu/ogromno-povprasevanje-za-nogometni-spektakel-leta/770262
- FAISS rank/score: 1 / 0.8636
- Jina reranker score: 0.2578
- Keywords: Fifa, Navijači, Prodaja vstopnic, Nogometni dogodek
- Excerpt: Ogromno povpraševanje za nogometni spektakel leta Ključne besede: Fifa, Navijači, Prodaja vstopnic, Nogometni dogodek V zadnjem delu prodaje je mednarodna nogometna zveza (Fifa) prejela več kot pol milijarde zahtevkov za vstopnice za ogled tekem letošnjega svetovnega prvenstva, ki bo poleti potekalo v ZDA, Kanadi in Mehiki. Prodaja vstopnic se je začela 11. decembra in je trajala do 13. januarja. Prvič so bile naprodaj posamezne vstopnice za določene tekme. Navijači bodo o morebitnem uspehu v na...


### 4. Tožba slovenskih avtoprevoznikov

Precision@5: 3/5 = 0.60

#### Rank 1: NOT RELEVANT

- Title: Kampanja PreVWara - Pomembna zmaga za potrošnike ali precejšnje razočaranje?
- Decision: not_relevant
- Rationale: VW consumer campaign, not Slovenian hauliers.
- Category/date: gospodarstvo / 2024-11-21T16:19:56
- URL: https://www.rtvslo.si/gospodarstvo/kampanja-prevwara-pomembna-zmaga-za-potrosnike-ali-precejsnje-razocaranje/728165
- FAISS rank/score: 46 / 0.8377
- Jina reranker score: 0.5273
- Keywords: ZPS, Volkswagen, Potrošniki, Poravnava, Dieselgate
- Excerpt: Kampanja PreVWara - Pomembna zmaga za potrošnike ali precejšnje razočaranje? Ključne besede: ZPS, Volkswagen, Potrošniki, Poravnava, Dieselgate Volkswagen je privolil v poravnavo s slovenskimi lastniki njegovih vozil, ki so bili oškodovani v t. i. aferi Dieselgate. A so odškodnine slovenskim potrošnikom očitno precej nižje, kot so bile dosežene v nekaterih drugih poravnavah v evropskih državah. Zveza potrošnikov Slovenije (ZPS), ki je leta 2017 v kampanji PreVWara zbrala zainteresirane slovenske...

#### Rank 2: RELEVANT

- Title: Avtoprevozniki zaradi kolapsa prometa čez Fernetiče grozijo tudi z zaprtjem avtocestnega križa
- Decision: relevant
- Rationale: Slovenian hauliers and traffic disruption; largely related.
- Category/date: gospodarstvo / 2025-08-26T13:18:22
- URL: https://www.rtvslo.si/gospodarstvo/avtoprevozniki-zaradi-kolapsa-prometa-cez-fernetice-grozijo-tudi-z-zaprtjem-avtocestnega-kriza/755699
- FAISS rank/score: 13 / 0.8460
- Jina reranker score: 0.5195
- Keywords: Primorska avtocesta, Prometni kolaps, Avtoprevozniki
- Excerpt: Avtoprevozniki zaradi kolapsa prometa čez Fernetiče grozijo tudi z zaprtjem avtocestnega križa Ključne besede: Primorska avtocesta, Prometni kolaps, Avtoprevozniki Avtoprevozniki zaradi posledic zaprtja vipavske hitre ceste proti Vrtojbi opozarjajo na neprevoznost na avtocesti A1 in pozivajo k takojšnjemu ukrepanju. Pred Fernetiči nastajajo kolone tovornjakov, ki segajo tudi na primorsko avtocesto. Avtoprevozniki so se danes zbrali na Razdrtem in pozvali odgovorne k takojšnjim ukrepom. Razmišlja...

#### Rank 3: RELEVANT

- Title: Avtoprevozniki zaradi kolapsa prometa čez Fernetiče grozijo tudi z zaprtjem avtocestnega križa
- Decision: relevant
- Rationale: Duplicate Slovenian hauliers result; largely related.
- Category/date: gospodarstvo / 2025-08-26T13:18:22
- URL: https://www.rtvslo.si/gospodarstvo/avtoprevozniki-zaradi-kolapsa-na-primorski-avtocesti-zahtevajo-od-pristojnih-takojsnje-ukrepanje/755699
- FAISS rank/score: 14 / 0.8460
- Jina reranker score: 0.5195
- Keywords: Primorska avtocesta, Prometni kolaps, Avtoprevozniki
- Excerpt: Avtoprevozniki zaradi kolapsa prometa čez Fernetiče grozijo tudi z zaprtjem avtocestnega križa Ključne besede: Primorska avtocesta, Prometni kolaps, Avtoprevozniki Avtoprevozniki zaradi posledic zaprtja vipavske hitre ceste proti Vrtojbi opozarjajo na neprevoznost na avtocesti A1 in pozivajo k takojšnjemu ukrepanju. Pred Fernetiči nastajajo kolone tovornjakov, ki segajo tudi na primorsko avtocesto. Avtoprevozniki so se danes zbrali na Razdrtem in pozvali odgovorne k takojšnjim ukrepom. Razmišlja...

#### Rank 4: RELEVANT

- Title: Avtoprevozniki na zboru državi postavili zahteve, sicer lahko sledi zaprtje najpomembnejših cest
- Decision: relevant
- Rationale: Slovenian hauliers and demands; largely related.
- Category/date: gospodarstvo / 2025-10-18T15:03:41
- URL: https://www.rtvslo.si/gospodarstvo/avtoprevozniki-na-zboru-drzavi-postavili-zahteve-sicer-lahko-sledi-zaprtje-najpomembnejsih-cest/761263
- FAISS rank/score: 1 / 0.8628
- Jina reranker score: 0.5078
- Keywords: Digitalizacija, Kadrovska kriza, Zeleni prehod, Zaprtje cest, Avtoprevozniki
- Excerpt: Avtoprevozniki na zboru državi postavili zahteve, sicer lahko sledi zaprtje najpomembnejših cest Ključne besede: Digitalizacija, Kadrovska kriza, Zeleni prehod, Zaprtje cest, Avtoprevozniki Avtoprevozniki so na zboru v Celju na vlado naslovili zahteve, za katere pričakujejo, da jih izpolni do decembra oz. do marca 2026. V nasprotnem bodo decembra pripravili protest, za marec pa so napovedali zaprtje pomembnih cest v Sloveniji. Zbor sta organizirala sekcija za promet pri Obrtno-podjetniški zborni...

#### Rank 5: NOT RELEVANT

- Title: Med predlogi za rešitev zastojev na primorski avtocesti tudi dvosmerni promet proti Razdrtemu
- Decision: not_relevant
- Rationale: Traffic-flow proposal, not haulier lawsuit/dispute.
- Category/date: slovenija / 2025-08-28T07:55:43
- URL: https://www.rtvslo.si/slovenija/med-predlogi-za-resitev-zastojev-na-primorski-avtocesti-tudi-dvosmerni-promet-proti-razdrtemu/755864
- FAISS rank/score: 7 / 0.8492
- Jina reranker score: 0.4746
- Keywords: zastoji, avtoprevozniki, Alenka Bratušek, sestanek
- Excerpt: Med predlogi za rešitev zastojev na primorski avtocesti tudi dvosmerni promet proti Razdrtemu Ključne besede: zastoji, avtoprevozniki, Alenka Bratušek, sestanek Ministrica Alenka Bratušek se je sestala s predstavniki avtoprevoznikov, ki zaradi zastojev na primorski avtocesti zahtevajo takojšnje ukrepanje. Med predlogi je ureditev dvosmernega prometa po smernem vozišču vipavske hitre ceste v smeri Razdrtega. Ob zapori vipavske hitre ceste med Razdrtim in Vipavo v smeri Nove Gorice je tovorni tran...


### 5. Vojna Zvezd v Sloveniji

Precision@5: 1/5 = 0.20

#### Rank 1: NOT RELEVANT

- Title: Na čelu Zveze veteranov vojne za Slovenijo ostaja Ladislav Lipič
- Decision: not_relevant
- Rationale: False match on war veterans.
- Category/date: slovenija / 2024-04-06T19:27:44
- URL: https://www.rtvslo.si/slovenija/preberite-tudi/na-celu-zveze-veteranov-vojne-za-slovenijo-ostaja-ladislav-lipic/704146
- FAISS rank/score: 26 / 0.8176
- Jina reranker score: 0.5156
- Keywords: Mandatno obdobje, Ladislav Lipič, Zveza veteranov, Veterani, vojna, Slovenija, zveza, mandat, volitve, zbor, obrambni minister, Marjan Šarec, vrednote, domoljubje, pogum, Laško, epidemija, covid-19, poplave, izzivi, 30-letnica, teritorialna obramba, slavnostni govor, general Rudolf Maister, žrtve, politična opcija, društvo, ministrstvo, vojaški poklic, mladi, čast, zvestoba, poštenost, poročila, načrti, organe, volitve.
- Excerpt: Na čelu Zveze veteranov vojne za Slovenijo ostaja Ladislav Lipič Ključne besede: Mandatno obdobje, Ladislav Lipič, Zveza veteranov, Veterani, vojna, Slovenija, zveza, mandat, volitve, zbor, obrambni minister, Marjan Šarec, vrednote, domoljubje, pogum, Laško, epidemija, covid-19, poplave, izzivi, 30-letnica, teritorialna obramba, slavnostni govor, general Rudolf Maister, žrtve, politična opcija, društvo, ministrstvo, vojaški poklic, mladi, čast, zvestoba, poštenost, poročila, načrti, organe, voli...

#### Rank 2: RELEVANT

- Title: Po svetu praznujejo dan Vojne zvezd
- Decision: relevant
- Rationale: Direct Star Wars result.
- Category/date: zabava-in-slog / 2023-05-04T17:09:00
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/po-svetu-praznujejo-dan-vojne-zvezd/667027
- FAISS rank/score: 1 / 0.8381
- Jina reranker score: 0.3750
- Keywords: Vojna zvezd, Star Wars, May the fourth be with you, franšiza, filmi, kultura, popularni, datum, praznovanje, Luka Skywalker, George Lucas, animirani, igralci, televizijske serije, igrače, videoigre, Lego, BioWare, Slovenija, otroci, liki, imena
- Excerpt: Po svetu praznujejo dan Vojne zvezd Ključne besede: Vojna zvezd, Star Wars, May the fourth be with you, franšiza, filmi, kultura, popularni, datum, praznovanje, Luka Skywalker, George Lucas, animirani, igralci, televizijske serije, igrače, videoigre, Lego, BioWare, Slovenija, otroci, liki, imena Ljubitelji ene največjih znanstvenofantastičnih franšiz na svetu že od leta 2011 četrtega maja praznujejo dan Vojne zvezd. Kultni filmi so vse od prvenca leta 1977 premikali meje žanra in se zasidrali gl...

#### Rank 3: NOT RELEVANT

- Title: General Brieger: Slovenski prispevek k misijam je cenjen. SV dobil šest e-motorjev.
- Decision: not_relevant
- Rationale: Slovenian army result, not Star Wars.
- Category/date: slovenija / 2024-06-13T14:51:30
- URL: https://www.rtvslo.si/slovenija/general-brieger-slovenski-prispevek-k-misijam-je-cenjen-sv-dobil-sest-e-motorjev/711678
- FAISS rank/score: 23 / 0.8192
- Jina reranker score: 0.2852
- Keywords: e-motorji, SV, STRiX eMotors
- Excerpt: General Brieger: Slovenski prispevek k misijam je cenjen. SV dobil šest e-motorjev. Ključne besede: e-motorji, SV, STRiX eMotors Obrambno ministrstvo in SV sta v Kočevski Reki predstavila električne vojaške motorje, ki jih je ob pomoči strokovnjakov ministrstva posebej za vojsko razvilo slovensko podjetje STRiX eMotors in so z izjemo nekaj delov v celoti slovenski izdelek. Po besedah generalnega direktorja direktorata za logistiko Željka Kralja obrambno ministrstvo v zadnjem letu intenzivno vlag...

#### Rank 4: NOT RELEVANT

- Title: Roskozmos v vojni, fosfor v Enkeladu in slovenska vesoljska strategija
- Decision: not_relevant
- Rationale: Space/war/strategy false match, not Star Wars.
- Category/date: znanost-in-tehnologija / 2023-06-24T15:16:18
- URL: https://www.rtvslo.si/znanost-in-tehnologija/roskozmos-v-vojni-fosfor-v-enkeladu-in-slovenska-vesoljska-strategija/665675
- FAISS rank/score: 4 / 0.8284
- Jina reranker score: 0.2363
- Keywords: Vesolje, Vesoljski tednik, Raziskovanje vesolja, vesoljska tehnologija, raketa, izstrelitev, satelit, orbita, vesoljska agencija, vesoljski sektor, Evropska vesoljska agencija, SpaceX, falcon 9, tirnica, Cape Canaveral, Starlink, posnetek izstrelitve, United Launch Alliance, Delta IV Heavy, eksoplanet, teleskop James Webb, Amerika
- Excerpt: Roskozmos v vojni, fosfor v Enkeladu in slovenska vesoljska strategija Ključne besede: Vesolje, Vesoljski tednik, Raziskovanje vesolja, vesoljska tehnologija, raketa, izstrelitev, satelit, orbita, vesoljska agencija, vesoljski sektor, Evropska vesoljska agencija, SpaceX, falcon 9, tirnica, Cape Canaveral, Starlink, posnetek izstrelitve, United Launch Alliance, Delta IV Heavy, eksoplanet, teleskop James Webb, Amerika Ruska vesoljska korporacija sestavlja vojaško enoto za boj v Ukrajini, mogočna a...

#### Rank 5: NOT RELEVANT

- Title: Pirc Musar: Naši vojski moramo zagotoviti kakovostno opremo za obrambo in zaščito vseh nas
- Decision: not_relevant
- Rationale: Slovenian army result, not Star Wars.
- Category/date: slovenija / 2025-05-24T16:24:29
- URL: https://www.rtvslo.si/slovenija/pirc-musar-nasi-vojski-moramo-zagotoviti-kakovostno-opremo-za-obrambo-in-zascito-vseh-nas/746788
- FAISS rank/score: 40 / 0.8155
- Jina reranker score: 0.1826
- Keywords: Teritorialna obramba, Vojaška oprema, Koper, Praznovanje, Slovenska vojska
- Excerpt: Pirc Musar: Naši vojski moramo zagotoviti kakovostno opremo za obrambo in zaščito vseh nas Ključne besede: Teritorialna obramba, Vojaška oprema, Koper, Praznovanje, Slovenska vojska "Nedopustno je, da bi bila vojska, kot temelj državnosti, predmet politizacije ali morebitnih političnih zlorab. Če jo imamo, moramo zanjo tudi ustrezno skrbeti. In te skrbnosti ne moremo izkazovati selektivno," je ob dnevu SV opozorila Nataša Pirc Musar. Slovenska vojska svoj praznik uradno praznuje 15. maja, ko se...


### 6. Ogromni zastoji na Slovenskih cestah

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Na avtocestah nastajajo zastoji, pot od Razdrtega do Ljubljane se podaljša za 45 minut
- Decision: relevant
- Rationale: Direct highway traffic jams.
- Category/date: slovenija / 2023-07-29T12:30:06
- URL: https://www.rtvslo.si/slovenija/na-avtocestah-nastajajo-zastoji-pot-od-razdrtega-do-ljubljane-se-podaljsa-za-45-minut/676502
- FAISS rank/score: 3 / 0.8632
- Jina reranker score: 0.6211
- Keywords: Potovalni čas, Gneča na cestah, Zastoji na avtocestah, promet, zastoji, avtocesta, hitra cesta, ceste, prometnoinformacijski center, zamuda, gneča, zapora, Jesenice, Avstrija, Postojna, Logatec, Vrhnika, Izola, Strunjan, Škofije, Koper, Karavanke, Štajerska
- Excerpt: Na avtocestah nastajajo zastoji, pot od Razdrtega do Ljubljane se podaljša za 45 minut Ključne besede: Potovalni čas, Gneča na cestah, Zastoji na avtocestah, promet, zastoji, avtocesta, hitra cesta, ceste, prometnoinformacijski center, zamuda, gneča, zapora, Jesenice, Avstrija, Postojna, Logatec, Vrhnika, Izola, Strunjan, Škofije, Koper, Karavanke, Štajerska Promet na slovenskih cestah je zgoščen. Zastoji tako nastajajo na primorski avtocesti v obe smeri in na gorenjski avtocesti v smeri Karavan...

#### Rank 2: RELEVANT

- Title: Pred Karavankami in Šentiljem dolgi zastoji
- Decision: relevant
- Rationale: Direct traffic jams result.
- Category/date: slovenija / 2024-08-17T07:57:05
- URL: https://www.rtvslo.si/slovenija/pred-karavankami-in-sentiljem-dolgi-zastoji/718223
- FAISS rank/score: 4 / 0.8621
- Jina reranker score: 0.6094
- Keywords: Reševalni pas, Varna vožnja, Preventivna akcija, Vročinski val, Prometna varnost
- Excerpt: Pred Karavankami in Šentiljem dolgi zastoji Ključne besede: Reševalni pas, Varna vožnja, Preventivna akcija, Vročinski val, Prometna varnost Na slovenskih cestah je tudi ta konec tedna zgoščen promet, gneča je tako v smeri proti morju kot proti notranjosti. Pred predorom Karavanke je kolona dolga 11 kilometrov, predor občasno zapirajo. Na primorski avtocesti je promet upočasnjen v smeri proti Primorski, pa tudi proti Ljubljani, in sicer na posameznih odsekih med Razdrtim in Brezovico. Zastoji so...

#### Rank 3: RELEVANT

- Title: Pred Karavankami in Šentiljem dolgi zastoji
- Decision: relevant
- Rationale: Duplicate direct traffic jams result.
- Category/date: slovenija / 2024-08-17T07:57:05
- URL: https://www.rtvslo.si/slovenija/pred-karavankami-11-kilometrski-zastoj-gneca-tudi-pred-prehodoma-sentilj-in-ljubelj/718223
- FAISS rank/score: 5 / 0.8621
- Jina reranker score: 0.6094
- Keywords: Reševalni pas, Varna vožnja, Preventivna akcija, Vročinski val, Prometna varnost
- Excerpt: Pred Karavankami in Šentiljem dolgi zastoji Ključne besede: Reševalni pas, Varna vožnja, Preventivna akcija, Vročinski val, Prometna varnost Na slovenskih cestah je tudi ta konec tedna zgoščen promet, gneča je tako v smeri proti morju kot proti notranjosti. Pred predorom Karavanke je kolona dolga 11 kilometrov, predor občasno zapirajo. Na primorski avtocesti je promet upočasnjen v smeri proti Primorski, pa tudi proti Ljubljani, in sicer na posameznih odsekih med Razdrtim in Brezovico. Zastoji so...

#### Rank 4: RELEVANT

- Title: Ob številnih tujih turistih na slovenskih cestah ves dan pričakovana gneča in zastoji
- Decision: relevant
- Rationale: Direct Slovenian road congestion result.
- Category/date: slovenija / 2023-05-18T10:36:00
- URL: https://www.rtvslo.si/slovenija/ob-stevilnih-tujih-turistih-na-slovenskih-cestah-ves-dan-pricakovana-gneca-in-zastoji/668570
- FAISS rank/score: 9 / 0.8549
- Jina reranker score: 0.6055
- Keywords: promet, zastoji, Dars, cesta, zastoj, avtocesta, turist, praznik, dela prost dan, gneča, prometno-informacijski center, prometna informacija, mestno središče, obvoznica, Ljubljana, štajerska avtocesta, število kolone, gorenjska avtocesta, primorska avtocesta, vzdrževanje ceste
- Excerpt: Ob številnih tujih turistih na slovenskih cestah ves dan pričakovana gneča in zastoji Ključne besede: promet, zastoji, Dars, cesta, zastoj, avtocesta, turist, praznik, dela prost dan, gneča, prometno-informacijski center, prometna informacija, mestno središče, obvoznica, Ljubljana, štajerska avtocesta, število kolone, gorenjska avtocesta, primorska avtocesta, vzdrževanje ceste Na slovenskih cestah je močno zgoščen promet, na številnih avtocestnih odsekih so tudi zastoji. Veliko je predvsem turis...

#### Rank 5: RELEVANT

- Title: Bratušek: Čudežnih rešitev za trenutno stanje na slovenskih avtocestah ne more biti
- Decision: relevant
- Rationale: Slovenian highway congestion result.
- Category/date: slovenija / 2024-08-27T08:45:56
- URL: https://www.rtvslo.si/slovenija/bratusek-cudeznih-resitev-za-trenutno-stanje-na-slovenskih-avtocestah-ne-more-biti/719127
- FAISS rank/score: 19 / 0.8508
- Jina reranker score: 0.5938
- Keywords: promet, zastoji, Alenka Bratušek, Matej Ogrin, Marcel Štefančič, oddaja Marcel
- Excerpt: Bratušek: Čudežnih rešitev za trenutno stanje na slovenskih avtocestah ne more biti Ključne besede: promet, zastoji, Alenka Bratušek, Matej Ogrin, Marcel Štefančič, oddaja Marcel "Mislim, da ni realnih možnosti, da bo v naslednjih petih letih bolje," glede stanja na slovenskih avtocestah priznava ministrica Alenka Bratušek. Da hitrih rešitev za zastoje ni, poudarja tudi Matej Ogrin. "Na to se bomo morali navaditi," je dejal. Na slovenskih cestah je vse več osebnih in tovornih vozil, gneča in pro...


### 7. Višanje temperatur

Precision@5: 3/5 = 0.60

#### Rank 1: RELEVANT

- Title: Z višanjem temperatur se "facekiniji" prodajajo kot vroče žemljice
- Decision: relevant
- Rationale: Explicitly about rising temperatures and heat effects.
- Category/date: zabava-in-slog / 2023-07-21T12:05:56
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/z-visanjem-temperatur-se-facekiniji-prodajajo-kot-vroce-zemljice/675739
- FAISS rank/score: 43 / 0.8109
- Jina reranker score: 0.6250
- Keywords: vročina, Kitajska, sonce, facekini, zaščita pred soncem, pokrivala, vročinski rekordi, UV-žarki, bela polt, kozmetični izdelki, sončne bolezni, turizem, Peking, maska za obraz, prodaja, prodajalna, pandemija, zaščitna sredstva, ventilatorji, klasična lepota, pokrivala za obraz, koža
- Excerpt: Z višanjem temperatur se "facekiniji" prodajajo kot vroče žemljice Ključne besede: vročina, Kitajska, sonce, facekini, zaščita pred soncem, pokrivala, vročinski rekordi, UV-žarki, bela polt, kozmetični izdelki, sončne bolezni, turizem, Peking, maska za obraz, prodaja, prodajalna, pandemija, zaščitna sredstva, ventilatorji, klasična lepota, pokrivala za obraz, koža Ob podiranju vročinskih rekordov se vse več ljudi na Kitajskem odloči za nakup posebnega pokrivala, imenovanega "facekini". Z njim pr...

#### Rank 2: RELEVANT

- Title: Napovedane visoke temperature, do 37 stopinj Celzija. Velika toplotna obremenitev.
- Decision: relevant
- Rationale: Direct high-temperature/weather result.
- Category/date: okolje / 2022-06-26T18:54:14
- URL: https://www.rtvslo.si/okolje/napovedane-visoke-temperature-do-37-stopinj-celzija-velika-toplotna-obremenitev/632320
- FAISS rank/score: 29 / 0.8127
- Jina reranker score: 0.4102
- Keywords: vreme, vročina, napoved, toplotna obremenitev, temperatura, veter, zrak, Agencija RS za okolje, nevihta, delo na prostem, hrana, senco, gozd, suša, vročinski val, Slovenija
- Excerpt: Napovedane visoke temperature, do 37 stopinj Celzija. Velika toplotna obremenitev. Ključne besede: vreme, vročina, napoved, toplotna obremenitev, temperatura, veter, zrak, Agencija RS za okolje, nevihta, delo na prostem, hrana, senco, gozd, suša, vročinski val, Slovenija Po podatkih urada za meteorološko napoved bo po nižinah sredi dneva in popoldne velika toplotna obremenitev. Najvišje dnevne temperature bodo od 30 do 37 stopinj Celzija. V višinah s šibkim vetrom zahodnih smeri priteka nad naše...

#### Rank 3: RELEVANT

- Title: Ob dvigu temperature lahko pričakujemo več komarjev
- Decision: relevant
- Rationale: Effect of temperature rise.
- Category/date: slovenija / 2025-08-07T13:24:43
- URL: https://www.rtvslo.si/slovenija/ob-dvigu-temperature-lahko-pricakujemo-vec-komarjev/754077
- FAISS rank/score: 2 / 0.8248
- Jina reranker score: 0.3926
- Keywords: Repelenti, Preventivni ukrepi, Komarji
- Excerpt: Ob dvigu temperature lahko pričakujemo več komarjev Ključne besede: Repelenti, Preventivni ukrepi, Komarji Začetek poletja je bil sušen, zato je bilo komarjev manj. Zadnje deževje in višja temperatura bosta vplivala na njihovo številčnost. Odstranjevanje vode iz okolja in pravilno odlaganje odpadkov ter urejanje zelenih zmanjšujejo možnosti za razmnoževanje. Za razvoj komarjev sta ključni stoječa voda in zadostna toplota. Vodja kustodiata za nevretenčarje v Prirodoslovnem muzeju Slovenije Tea Kn...

#### Rank 4: NOT RELEVANT

- Title: Zaradi suše zvišanje cen italijanskega riža, paradižnikove mezge in oljčnega olja
- Decision: not_relevant
- Rationale: Drought-related food prices, not mainly rising temperatures.
- Category/date: okolje / 2022-07-13T11:34:20
- URL: https://www.rtvslo.si/okolje/zaradi-suse-zvisanje-cen-italijanskega-riza-paradiznikove-mezge-in-oljcnega-olja/634072
- FAISS rank/score: 40 / 0.8115
- Jina reranker score: 0.3398
- Keywords: vročina, poletje, suša, Italija, Portugalska, zvišanje cen, vročinski val, Španija, Francija, Kitajska, Združeno kraljestvo, temperatura, zdravstvene težave, Lizbona, gozdni požari, proizvodnja, oljčno olje, riž, paradižnikova mezga, kmetje, sneženje
- Excerpt: Zaradi suše zvišanje cen italijanskega riža, paradižnikove mezge in oljčnega olja Ključne besede: vročina, poletje, suša, Italija, Portugalska, zvišanje cen, vročinski val, Španija, Francija, Kitajska, Združeno kraljestvo, temperatura, zdravstvene težave, Lizbona, gozdni požari, proizvodnja, oljčno olje, riž, paradižnikova mezga, kmetje, sneženje Zaradi suše v Italiji se napoveduje zvišanje cen riža, oljčnega olja in paradižnikove mezge za do 50 odstotkov. Že drugi vročinski val bo zajel Španijo...

#### Rank 5: NOT RELEVANT

- Title: Povpraševanje po toplotnih kamerah strmo narašča
- Decision: not_relevant
- Rationale: Thermal camera demand, not rising temperatures.
- Category/date: znanost-in-tehnologija / 2020-03-25T14:01:05
- URL: https://www.rtvslo.si/znanost-in-tehnologija/povprasevanje-po-toplotnih-kamerah-strmo-narasca/518329
- FAISS rank/score: 1 / 0.8252
- Jina reranker score: 0.3320
- Keywords: Termalna kamera, Toplotna kamera, Infrardeča kamera, Termovizijska kamera, termovizijske kamere, merjenje temperature, infrardeče valovanje, pregrevanje, vzdrževanje, zdravstvo, imunski sistem, koronavirus, pandemija, dobavne poti, brezstičnost, industrija, gradbeništvo, elektroindustrija, gasilci, meteorologi, astronomi, bolezni, sars, prašičja gripa, umerjanje.
- Excerpt: Povpraševanje po toplotnih kamerah strmo narašča Ključne besede: Termalna kamera, Toplotna kamera, Infrardeča kamera, Termovizijska kamera, termovizijske kamere, merjenje temperature, infrardeče valovanje, pregrevanje, vzdrževanje, zdravstvo, imunski sistem, koronavirus, pandemija, dobavne poti, brezstičnost, industrija, gradbeništvo, elektroindustrija, gasilci, meteorologi, astronomi, bolezni, sars, prašičja gripa, umerjanje. Med širjenjem novega koronavirusa narašča tudi povpraševanje po termo...


### 8. Višanje cen nepremičnin v Sloveniji

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Cene stanovanj so se lani zvišale za 8,5 odstotka
- Decision: relevant
- Rationale: Direct real-estate price rise.
- Category/date: gospodarstvo / 2025-03-24T11:15:44
- URL: https://www.rtvslo.si/gospodarstvo/cene-stanovanj-so-se-lani-zvisale-za-8-5-odstotka/740422
- FAISS rank/score: 9 / 0.8640
- Jina reranker score: 0.7109
- Keywords: Nove družinske hiše, Rabljena stanovanja, Prodaja nepremičnin, Zvišanje cen, Cene stanovanj
- Excerpt: Cene stanovanj so se lani zvišale za 8,5 odstotka Ključne besede: Nove družinske hiše, Rabljena stanovanja, Prodaja nepremičnin, Zvišanje cen, Cene stanovanj Cene stanovanjskih nepremičnin v Sloveniji so se lani zvišale deseto leto zapored, tokrat za 8,5 odstotka. Skupaj je bilo prodanih za približno 1,3 milijarde evrov stanovanjskih nepremičnin, kar je 14,7 odstotka manj kot leto prej. Lani se je zmanjšalo tudi število transakcij s stanovanjskimi nepremičninami. Potem ko je leta 2023 novega las...

#### Rank 2: RELEVANT

- Title: Najemniška kriza: "Za polkletno stanovanje nas je bilo na ogled hkrati naročenih 20"
- Decision: relevant
- Rationale: Housing affordability/rental crisis related to rising property costs.
- Category/date: slovenija / 2024-02-19T06:46:25
- URL: https://www.rtvslo.si/slovenija/najemniska-kriza-za-polkletno-stanovanje-nas-je-bilo-na-ogled-hkrati-narocenih-20/697334
- FAISS rank/score: 18 / 0.8573
- Jina reranker score: 0.6367
- Keywords: Obdavčenje najemnin, Kratkoročni najemi, Cene nepremičnin, Ponudba in povpraševanje, Najemniška kriza, skit scena, najemnine, stanovanja, nepremičnine, tržišče, mladi zaposleni, najem, cene, Ljubljana, najemodajalci, trg, Airbnb, Booking, premier, obdavčenje, spremembe, oglas, Maribor, Kranj, Celje, Istra, iskanje stanovanja
- Excerpt: Najemniška kriza: "Za polkletno stanovanje nas je bilo na ogled hkrati naročenih 20" Ključne besede: Obdavčenje najemnin, Kratkoročni najemi, Cene nepremičnin, Ponudba in povpraševanje, Najemniška kriza, skit scena, najemnine, stanovanja, nepremičnine, tržišče, mladi zaposleni, najem, cene, Ljubljana, najemodajalci, trg, Airbnb, Booking, premier, obdavčenje, spremembe, oglas, Maribor, Kranj, Celje, Istra, iskanje stanovanja Višina najemnin je zlasti za mlade zaposlene vedno večja težava. Porast...

#### Rank 3: RELEVANT

- Title: Prodaja nepremičnin upada, cene pa še naprej rastejo
- Decision: relevant
- Rationale: Direct real-estate prices rising.
- Category/date: gospodarstvo / 2024-12-23T15:25:02
- URL: https://www.rtvslo.si/gospodarstvo/prodaja-nepremicnin-upada-cene-pa-se-naprej-rastejo/731459
- FAISS rank/score: 5 / 0.8694
- Jina reranker score: 0.6289
- Keywords: nepremičnine, prodaja, cene
- Excerpt: Prodaja nepremičnin upada, cene pa še naprej rastejo Ključne besede: nepremičnine, prodaja, cene Prodaja stanovanjskih nepremičnin v Sloveniji upada. V tretjem četrtletju je bilo prodanih celo najmanj rabljenih nepremičnin v zadnjih 14 letih. Cene nepremičnin medtem še naprej rastejo, najbolj prav za rabljena stanovanja in hiše. Po izračunih Statističnega urada RS (Surs) je bilo v tretjem četrtletju letošnjega leta skupno prodnih 1737 stanovanjskih nepremičnin. To je 16 odstotkov manj kot v četr...

#### Rank 4: RELEVANT

- Title: Gurs: V Sloveniji lani prodanih manj hiš in stanovanj. Cene zrasle za devet oz. deset odstotkov.
- Decision: relevant
- Rationale: Direct Slovenian housing price rise.
- Category/date: gospodarstvo / 2025-04-15T06:31:30
- URL: https://www.rtvslo.si/gospodarstvo/gurs-v-sloveniji-lani-prodanih-manj-his-in-stanovanj-cene-zrasle-za-devet-oz-deset-odstotkov/742731
- FAISS rank/score: 2 / 0.8742
- Jina reranker score: 0.6250
- Keywords: Cene stanovanj, Nepremičninski trg, Gurs
- Excerpt: Gurs: V Sloveniji lani prodanih manj hiš in stanovanj. Cene zrasle za devet oz. deset odstotkov. Ključne besede: Cene stanovanj, Nepremičninski trg, Gurs Po podatkih Gursa je lani precej upadla prodaja vseh vrst nepremičnin. Na drugi strani pa so se denimo v Ljubljani cene stanovanj zvišale za kar 500 evrov/m2. "Povpraševanje še vedno močno presega ponudbo," pravi Boštjan Udovič iz GZS-ja. Geodetska uprava (Gurs) je na začetku aprila objavila poročilo o slovenskem nepremičninskem trgu za leto 20...

#### Rank 5: RELEVANT

- Title: Gurs: Večji del populacije si tržnega nakupa stanovanja ne more več privoščiti
- Decision: relevant
- Rationale: Housing affordability result tied to property prices.
- Category/date: gospodarstvo / 2024-10-15T15:54:10
- URL: https://www.rtvslo.si/gospodarstvo/gurs-vecji-del-populacije-si-trznega-nakupa-stanovanja-ne-more-vec-privosciti/724389
- FAISS rank/score: 14 / 0.8609
- Jina reranker score: 0.6250
- Keywords: Cene stanovanj, Nepremičninski trg, Gurs
- Excerpt: Gurs: Večji del populacije si tržnega nakupa stanovanja ne more več privoščiti Ključne besede: Cene stanovanj, Nepremičninski trg, Gurs Na slovenskem nepremičninskem trgu se je tudi v prvem letošnjem polletju nadaljevalo upadanje števila sklenjenih kupoprodajnih pogodb. Kljub temu pa so cene nepremičnin še naprej rasle, ugotavlja Gurs. V prvih šestih mesecih je bilo po podatkih z vsemi kategorijami nepremičnin sklenjenih okoli 12.000 kupoprodajnih pogodb v skupni vrednosti 1,2 milijarde evrov, v...


### 9. Rogljič in Pogačar na tekmi

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Na Emiliji in Lombardiji prvo in drugo letošnje soočenje Pogačarja in Rogliča
- Decision: relevant
- Rationale: Direct Pogacar/Roglic race result.
- Category/date: sport / 2023-09-18T20:40:51
- URL: https://www.rtvslo.si/sport/kolesarstvo/na-emiliji-in-lombardiji-prvo-in-drugo-letosnje-soocenje-pogacarja-in-roglica/681833
- FAISS rank/score: 4 / 0.8470
- Jina reranker score: 0.7070
- Keywords: kolesarstvo, Dirka po Lombardiji, Tadej Pogačar, Primož Roglič, Marc Hirschi, ekipa UAE, slovenski državni prvak, Joxean Matxin Fernandez, Dirka po Emiliji, Dirka tri doline Vareseja, Vuelta, San Luco, Bologna, Dirka po Franciji, 2024, tritedenske dirke, enodnevne dirke, Madrid, kraljevska etapa, Angliru, Remco Evenepoel
- Excerpt: Na Emiliji in Lombardiji prvo in drugo letošnje soočenje Pogačarja in Rogliča Ključne besede: kolesarstvo, Dirka po Lombardiji, Tadej Pogačar, Primož Roglič, Marc Hirschi, ekipa UAE, slovenski državni prvak, Joxean Matxin Fernandez, Dirka po Emiliji, Dirka tri doline Vareseja, Vuelta, San Luco, Bologna, Dirka po Franciji, 2024, tritedenske dirke, enodnevne dirke, Madrid, kraljevska etapa, Angliru, Remco Evenepoel Tadej Pogačar je ob Marcu Hirschiju iz ekipe UAE že na startni listi Dirke po Lomba...

#### Rank 2: RELEVANT

- Title: Slovenci po medaljo tako na cestni dirki kot na kronometru
- Decision: relevant
- Rationale: Slovenian cycling road-race result; largely related.
- Category/date: sport / 2024-09-13T18:25:25
- URL: https://www.rtvslo.si/sport/kolesarstvo/svetovno-prvenstvo-v-kolesarstvu/slovenci-po-medaljo-tako-na-cestni-dirki-kot-na-kronometru/720972
- FAISS rank/score: 7 / 0.8447
- Jina reranker score: 0.6992
- Keywords: kolesarstvo, svetovno prvenstvo, Uroš Murn, Tadej Pogačar, Primož Roglič
- Excerpt: Slovenci po medaljo tako na cestni dirki kot na kronometru Ključne besede: kolesarstvo, svetovno prvenstvo, Uroš Murn, Tadej Pogačar, Primož Roglič Slovenija bo na svetovnem prvenstvu v kolesarstvu nastopila z najmočnejšo ekipo. "Na cestni dirki bodo nastopili vsi fantje, ki nastopajo v ekipah svetovne serije, Primož Roglič pa bo nastopil na cestni dirki in kronometru," je potrdil selektor Uroš Murn. Ob Pogačarju in Rogliču so se selektorjevemu pozivu za nastop na SP-ju v Švici (od 21. do 29. se...

#### Rank 3: RELEVANT

- Title: Pogačar kraljuje na svetovni lestvici, Roglič peti
- Decision: relevant
- Rationale: Direct Pogacar/Roglic ranking result.
- Category/date: sport / 2025-08-12T09:27:36
- URL: https://www.rtvslo.si/sport/kolesarstvo/pogacar-kraljuje-na-svetovni-lestvici-roglic-peti/754455
- FAISS rank/score: 44 / 0.8345
- Jina reranker score: 0.6680
- Keywords: Tadej Pogačar, UCI-lestvica, kolesarstvo
- Excerpt: Pogačar kraljuje na svetovni lestvici, Roglič peti Ključne besede: Tadej Pogačar, UCI-lestvica, kolesarstvo Tadej Pogačar ima na svetovni lestvici Mednarodne kolesarske zveze (Uci) z 11.465 točkami pred prvim zasledovalcem, Dancem Madsom Pedersenom (4486 točk) skoraj sedem tisoč točk naskoka. Primož Roglič je na petem mestu (3841 točk). Med najboljšo peterico najdemo na tretjem mestu Nizozemca Mathieuja Van der Poela (4261 točk), četrti je Belgijec Wout Van Aert (3847). V najboljši deseterici je...

#### Rank 4: RELEVANT

- Title: Roglič v Andori dobil prestižno dirko 'pokra asov'
- Decision: relevant
- Rationale: Roglic race result; largely related.
- Category/date: sport / 2025-10-19T15:52:32
- URL: https://www.rtvslo.si/sport/kolesarstvo/roglic-v-andori-dobil-prestizno-dirko-pokra-asov/761326
- FAISS rank/score: 3 / 0.8473
- Jina reranker score: 0.6602
- Keywords: Primož Roglič, Tadej Pogačar, Jonas Vingegaard, Isaac del Toro
- Excerpt: Roglič v Andori dobil prestižno dirko 'pokra asov' Ključne besede: Primož Roglič, Tadej Pogačar, Jonas Vingegaard, Isaac del Toro Primož Roglič je zmagovalec dvodelne revijalne preizkušnje v Andori. Zasavec je bil dopoldne najhitrejši v gorskem kronometru, na mestnem kriteriju pa je bil drugi, kar je bilo dovolj za skupno zmago. Med štirimi tekmovalci je nastopal tudi Tadej Pogačar. Preizkušnja z imenom Andorra Cycling Masters je združila štiri zvezdnike kolesarstva. Ob Primožu Rogliču in Tadeju...

#### Rank 5: RELEVANT

- Title: Selektor Murn: Nimamo česa skrivati. Cilj je vsaj medalja na cestni dirki.
- Decision: relevant
- Rationale: Slovenian cycling race/medal context.
- Category/date: sport / 2024-09-18T14:10:18
- URL: https://www.rtvslo.si/sport/kolesarstvo/svetovno-prvenstvo-v-kolesarstvu/selektor-murn-nimamo-cesa-skrivati-cilj-je-vsaj-medalja-na-cestni-dirki/721400
- FAISS rank/score: 2 / 0.8473
- Jina reranker score: 0.6562
- Keywords: kolesarstvo, SP v kolesarstvu, Jaka Primožič, Tadej Pogačar, Primož Roglič
- Excerpt: Selektor Murn: Nimamo česa skrivati. Cilj je vsaj medalja na cestni dirki. Ključne besede: kolesarstvo, SP v kolesarstvu, Jaka Primožič, Tadej Pogačar, Primož Roglič Slovenija na 97. svetovno prvenstvo v cestnem kolesarstvu odhaja kot favorizirana ekipa za osrednji dogodek – cestno dirko moške elite. Primož Roglič in Tadej Pogačar bosta skušala poskrbeti za še eno redkih manjkajočih lovorik – mavrično majico. V nedeljo se začenja letošnje, že 97. svetovno prvenstvo v cestnem kolesarstvu, ki ga m...


### 10. Donald Trump novi zakoni

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Trump z novim zakonom uvedel višje kazni za trgovino s fentanilom
- Decision: relevant
- Rationale: Direct new Trump law result.
- Category/date: svet / 2025-07-17T10:37:53
- URL: https://www.rtvslo.si/svet/preberite-tudi/trump-z-novim-zakonom-uvedel-visje-kazni-za-trgovino-s-fentanilom/752186
- FAISS rank/score: 4 / 0.8404
- Jina reranker score: 0.6992
- Keywords: Nezakonito, Trgovina, Višje kazni, Fentanil, Trump
- Excerpt: Trump z novim zakonom uvedel višje kazni za trgovino s fentanilom Ključne besede: Nezakonito, Trgovina, Višje kazni, Fentanil, Trump Ameriški predsednik Donald Trump je v sredo podpisal zakon, ki sintetično drogo fentanil uvršča med najhujša prepovedana mamila v ZDA. Ob podpisu zakona je dejal, da bodo s tem zadali velik udarec mamilarskim kartelom, saj so za trgovino s fentanilom zdaj predvidene višje kazni. Fentanil je sredstvo, ki ga ameriški zdravniki včasih predpisujejo za lajšanje hudih bo...

#### Rank 2: RELEVANT

- Title: Trump podpisal prvi ameriški zakon o kriptovalutah
- Decision: relevant
- Rationale: Direct Trump-signed crypto law.
- Category/date: svet / 2025-07-19T14:19:39
- URL: https://www.rtvslo.si/svet/preberite-tudi/trump-podpisal-prvi-ameriski-zakon-o-kriptovalutah/752400
- FAISS rank/score: 5 / 0.8401
- Jina reranker score: 0.6094
- Keywords: Industrija kriptovalut, Stabilni kovanci, Zakon Genius, Kriptovalute, Trump
- Excerpt: Trump podpisal prvi ameriški zakon o kriptovalutah Ključne besede: Industrija kriptovalut, Stabilni kovanci, Zakon Genius, Kriptovalute, Trump Ameriški predsednik Donald Trump je podpisal prvi zakon o kriptovalutah v ZDA. Zadeva t. i. stabilne kovance – vrsto kriptovalut, katerih vrednost je vezana na stabilen zunanji vir, kot so dolar, evro ali zlato. Namen zakona je okrepiti zaupanje v industrijo kriptovalut, ki je z donacijami Trumpu postala pomemben političen igralec v Washingtonu. Zakon z i...

#### Rank 3: RELEVANT

- Title: Trump podpisal zakon, ki zahteva objavo dosjejev o Epsteinu
- Decision: relevant
- Rationale: Direct Trump law result.
- Category/date: svet / 2025-11-20T07:28:28
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/trump-podpisal-zakon-ki-zahteva-objavo-dosjejev-o-epsteinu/764647
- FAISS rank/score: 11 / 0.8376
- Jina reranker score: 0.5742
- Keywords: ZDA, Jeffrey Epstein, Donald Trump, Dokumenti, Dosjeji
- Excerpt: Trump podpisal zakon, ki zahteva objavo dosjejev o Epsteinu Ključne besede: ZDA, Jeffrey Epstein, Donald Trump, Dokumenti, Dosjeji Predsednik ZDA Donald Trump je podpisal zakon, po katerem mora pravosodno ministrstvo v 30 dneh objaviti vse dosjeje o spolnem prestopniku Jeffreyju Epsteinu. Z ministrstva pa že sporočajo, da dosjejev, ki so predmet tekočih preiskav, ne bodo objavili. "Demokrati so zlorabili vprašanje Epstein, ki jih zadeva veliko bolj kot republikansko stranko, da bi poskušali odvr...

#### Rank 4: RELEVANT

- Title: Trump najprej uvedel nove 10-odstotne carine, nato jih je dvignil na 15 odstotkov
- Decision: relevant
- Rationale: Trump tariff/policy result.
- Category/date: svet / 2026-02-21T09:59:57
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/trump-najprej-uvedel-nove-10-odstotne-carine-nato-jih-je-dvignil-na-15-odstotkov/774153
- FAISS rank/score: 12 / 0.8375
- Jina reranker score: 0.5430
- Keywords: Zakon o trgovini, Uvoz, Vrhovno sodišče, Carine, Trump
- Excerpt: Trump najprej uvedel nove 10-odstotne carine, nato jih je dvignil na 15 odstotkov Ključne besede: Zakon o trgovini, Uvoz, Vrhovno sodišče, Carine, Trump Ameriški predsednik Donald Trump je v petek ostro kritiziral sodnike vrhovnega sodišča, ki so razveljavili njegove t. i. vzajemne carine. Takoj je podpisal izvršni ukaz in uvedel nove splošne 10-odstotne carine, nato pa jih je povišal na 15 odstotkov. V odzivu na odločitev vrhovnega sodišča je Donald Trump napovedal, da bo nemudoma podpisal ukaz...

#### Rank 5: RELEVANT

- Title: S Trumpovim podpisom končana delna blokada ameriške vlade
- Decision: relevant
- Rationale: Trump-signed government measure.
- Category/date: svet / 2026-02-04T07:05:07
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/s-trumpovim-podpisom-koncana-delna-blokada-ameriske-vlade/772270
- FAISS rank/score: 49 / 0.8285
- Jina reranker score: 0.5352
- Keywords: ZDA, Donald Trump, financiranje vlade
- Excerpt: S Trumpovim podpisom končana delna blokada ameriške vlade Ključne besede: ZDA, Donald Trump, financiranje vlade Ameriški predsednik Donald Trump je podpisal zakone o nadaljevanju financiranja agencij svoje vlade, potem ko jih je nekaj ur prej tesno z 217 proti 214 glasovom potrdil predstavniški dom kongresa, s čimer se je po štirih dneh končala delna blokada vlade. Že lani je bilo potrjenih šest zakonov o proračunski porabi za razna ministrstva, tokrat jih je bilo prav tako do konca proračunskeg...


### 11. Evropska Unija in zveza NATO

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Premier Golob na srečanju z veleposlaniki držav članic o pomenu enotnosti EU-ja
- Decision: relevant
- Rationale: EU unity/security context; related to EU/NATO topic.
- Category/date: slovenija / 2023-06-28T16:34:12
- URL: https://www.rtvslo.si/slovenija/preberite-tudi/premier-golob-na-srecanju-z-veleposlaniki-drzav-clanic-o-pomenu-enotnosti-eu-ja/673405
- FAISS rank/score: 26 / 0.8372
- Jina reranker score: 0.3594
- Keywords: Robert Golob, EU, veleposlanik, Predsednik vlade, Ljubljana, Veleposlaniki, Evropska unija, Dnevni red, Vrh, Bruselj, Enotnost, Hiša EU-ja, Slovenija, Jedrna Evropa, Voditelji, Ruska agresija, Ukrajina, Varnost, Obramba, Zavezništvo, Migracije, Gospodarstvo
- Excerpt: Premier Golob na srečanju z veleposlaniki držav članic o pomenu enotnosti EU-ja Ključne besede: Robert Golob, EU, veleposlanik, Predsednik vlade, Ljubljana, Veleposlaniki, Evropska unija, Dnevni red, Vrh, Bruselj, Enotnost, Hiša EU-ja, Slovenija, Jedrna Evropa, Voditelji, Ruska agresija, Ukrajina, Varnost, Obramba, Zavezništvo, Migracije, Gospodarstvo Predsednik vlade Robert Golob se je danes v Ljubljani z veleposlaniki držav članic Evropske unije pogovarjal o aktualnih temah, ki bodo na dnevnem...

#### Rank 2: RELEVANT

- Title: Golob ob 30-letnici Sove pozval k samozavestni zadržanosti, budnosti in nenehni pripravljenosti
- Decision: relevant
- Rationale: EU and NATO/security architecture context.
- Category/date: slovenija / 2023-06-13T18:25:17
- URL: https://www.rtvslo.si/slovenija/golob-ob-30-letnici-sove-pozval-k-samozavestni-zadrzanosti-budnosti-in-nenehni-pripravljenosti/671692
- FAISS rank/score: 23 / 0.8376
- Jina reranker score: 0.3496
- Keywords: Sova, 30 let, Robert Golob, Evropa, prihodnost, vrednote, obveščevalna agencija, varnost, Jugoslavija, Evropska unija, NATO, Partnerstvo za mir, varnostna arhitektura, pariška listina, Rusija, Ukrajina, konflikt, begunska kriza, nacionalna varnost, suverenost, življenjski slog, tujina, partnerstvo, promet z občutljivim blagom, migracijski tokovi, informacijska varnost, protiobveščevalna dejavnost.
- Excerpt: Golob ob 30-letnici Sove pozval k samozavestni zadržanosti, budnosti in nenehni pripravljenosti Ključne besede: Sova, 30 let, Robert Golob, Evropa, prihodnost, vrednote, obveščevalna agencija, varnost, Jugoslavija, Evropska unija, NATO, Partnerstvo za mir, varnostna arhitektura, pariška listina, Rusija, Ukrajina, konflikt, begunska kriza, nacionalna varnost, suverenost, življenjski slog, tujina, partnerstvo, promet z občutljivim blagom, migracijski tokovi, informacijska varnost, protiobveščevaln...

#### Rank 3: RELEVANT

- Title: Kallas pozvala h krepitvi evropskega stebra Nata
- Decision: relevant
- Rationale: Direct EU/NATO result.
- Category/date: svet / 2026-01-28T12:14:40
- URL: https://www.rtvslo.si/svet/preberite-tudi/kallas-pozvala-h-krepitvi-evropskega-stebra-nata/771518
- FAISS rank/score: 8 / 0.8420
- Jina reranker score: 0.3477
- Keywords: kaja kallas, eu, nato
- Excerpt: Kallas pozvala h krepitvi evropskega stebra Nata Ključne besede: kaja kallas, eu, nato Evropa mora okrepiti lastno obrambo in prevzeti večjo vlogo znotraj zveze Nato, je danes dejala visoka zunanjepolitična predstavnica EU-ja Kaja Kallas. Dodala je, da so spremembe na drugi strani Atlantika pretresle čezatlantske odnose do temeljev, a hkrati zagotovila, da bodo ZDA ostale partnerica in zaveznica Evrope. "Naj bom jasna: želimo si močne čezatlantske odnose. ZDA bodo ostale partnerica in zaveznica...

#### Rank 4: RELEVANT

- Title: Rutte: Če mislite, da se lahko Evropa brani sama, kar sanjajte naprej
- Decision: relevant
- Rationale: Direct Europe/NATO defence result.
- Category/date: svet / 2026-01-26T18:46:29
- URL: https://www.rtvslo.si/svet/rutte-ce-mislite-da-se-lahko-evropa-brani-sama-kar-sanjajte-naprej/771341
- FAISS rank/score: 4 / 0.8428
- Jina reranker score: 0.3418
- Keywords: ZDA, Nato, Mark Rutte
- Excerpt: Rutte: Če mislite, da se lahko Evropa brani sama, kar sanjajte naprej Ključne besede: ZDA, Nato, Mark Rutte Evropa se ne more braniti brez ZDA, potrebujemo drug drugega, je ob zadnjih napetosti v čezatlantskih odnosih dejal generalni sekretar zveze Nato Mark Rutte. "Kar sanjajte naprej," je odvrnil tistim, ki menijo, da se lahko Evropa brani sama. " Če kdor koli tu misli, da se lahko Evropska unija ali Evropa kot celota brani brez ZDA, naj kar sanja naprej. Tega ne morete, tega ne moremo, potreb...

#### Rank 5: RELEVANT

- Title: Francoski minister Barrot: Evropejci lahko in morajo prevzeti odgovornost za svojo varnost
- Decision: relevant
- Rationale: Direct European/NATO security result.
- Category/date: svet / 2026-01-27T19:42:38
- URL: https://www.rtvslo.si/svet/evropa/francoski-minister-barrot-evropejci-lahko-in-morajo-prevzeti-odgovornost-za-svojo-varnost/771458
- FAISS rank/score: 16 / 0.8395
- Jina reranker score: 0.3223
- Keywords: Neodvisnost, Nato, ZDA, Varnost, Evropa
- Excerpt: Francoski minister Barrot: Evropejci lahko in morajo prevzeti odgovornost za svojo varnost Ključne besede: Neodvisnost, Nato, ZDA, Varnost, Evropa Evropa lahko prevzame in mora prevzeti odgovornost za svojo varnost, je v odzivu na izjave generalnega sekretarja zveze Nato Marka Rutteja, da se Evropa ne more braniti brez ZDA, dejal francoski zunanji minister Jean-Noel Barrot. "Ne, dragi Mark Rutte. Evropejci lahko prevzamejo in morajo prevzeti odgovornost za svojo varnost. Celo ZDA se strinjajo s...


### 12. Velika Britanija Brexit

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: Velika Britanija hoče preoblikovati severnoirski protokol
- Decision: relevant
- Rationale: Direct Brexit/Northern Ireland protocol result.
- Category/date: svet / 2021-07-21T18:44:51
- URL: https://www.rtvslo.si/svet/evropa/velika-britanija-hoce-preoblikovati-severnoirski-protokol/588379
- FAISS rank/score: 3 / 0.8314
- Jina reranker score: 0.6406
- Keywords: Brexit, Velika Britanija, Bruselj, Britanska vlada, Evropska unija, Severnoirski protokol, Irski otok, Brandon Lewis, Parlament, London, Blago, Združeno kraljestvo, Enotni trg, David Frost, Gospodarska škoda, Severna Irska, Protesti, Maroš Šefčovič, Evropska komisija, Izstopni sporazum, Odbor
- Excerpt: Velika Britanija hoče preoblikovati severnoirski protokol Ključne besede: Brexit, Velika Britanija, Bruselj, Britanska vlada, Evropska unija, Severnoirski protokol, Irski otok, Brandon Lewis, Parlament, London, Blago, Združeno kraljestvo, Enotni trg, David Frost, Gospodarska škoda, Severna Irska, Protesti, Maroš Šefčovič, Evropska komisija, Izstopni sporazum, Odbor Britanska vlada se želi z Evropsko unijo znova pogajati o severnoirskem protokolu in ga spremeniti. Pozvala je tudi k moratoriju za...

#### Rank 2: RELEVANT

- Title: Kljub brexitu Oxford postal električna tovarna za znamko Mini
- Decision: relevant
- Rationale: Brexit/electric vehicle production result.
- Category/date: zabava-in-slog / 2023-09-12T07:40:54
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/kljub-brexitu-oxford-postal-elektricna-tovarna-za-znamko-mini/681082
- FAISS rank/score: 23 / 0.8167
- Jina reranker score: 0.5352
- Keywords: Mini, cooper, aceman, BMW Group, Oxford, električni avtomobili, Velika Britanija, investicija, proizvodnja, modeli, elektrifikacija, električna vozila, naložba, proizvodnja vozil, tradicionalna tovarna, subvencija, delovna mesta, premier, Združeno kraljestvo, znamka Mini, zgodovina, srce znamke
- Excerpt: Kljub brexitu Oxford postal električna tovarna za znamko Mini Ključne besede: Mini, cooper, aceman, BMW Group, Oxford, električni avtomobili, Velika Britanija, investicija, proizvodnja, modeli, elektrifikacija, električna vozila, naložba, proizvodnja vozil, tradicionalna tovarna, subvencija, delovna mesta, premier, Združeno kraljestvo, znamka Mini, zgodovina, srce znamke BMW Group je uradno potrdil, da bo tovarna Mini v Oxfordu od leta 2030 izdelovala samo električne avtomobile. BMW bo v tovarno...

#### Rank 3: RELEVANT

- Title: Brexit pričakovanj ni upravičil, britanska javnost pa ga skoraj ne omenja več
- Decision: relevant
- Rationale: Direct Brexit result.
- Category/date: svet / 2025-01-31T06:20:23
- URL: https://www.rtvslo.si/svet/evropa/brexit-pricakovanj-ni-upravicil-britanska-javnost-pa-ga-skoraj-ne-omenja-vec/735075
- FAISS rank/score: 1 / 0.8510
- Jina reranker score: 0.5312
- Keywords: Gospodarske posledice, Evropska unija, Združeno kraljestvo, Brexit, Jan Grobovšek
- Excerpt: Brexit pričakovanj ni upravičil, britanska javnost pa ga skoraj ne omenja več Ključne besede: Gospodarske posledice, Evropska unija, Združeno kraljestvo, Brexit, Jan Grobovšek Pred petimi leti je Združeno kraljestvo izstopilo iz Evropske unije. Ekonomist z univerze v Edinburgu Jan Grobovšek pravi, da je s tem država dobila "najslabše od obeh svetov" – postala je manjše gospodarstvo in ni ujela gospodarskih priložnosti. Združeno kraljestvo je 31. januarja 2020 po 47 letih članstva kot prva članic...

#### Rank 4: RELEVANT

- Title: Brexit je postal težava za e-mobilnost
- Decision: relevant
- Rationale: Direct Brexit result.
- Category/date: zabava-in-slog / 2023-06-05T07:45:00
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/brexit-je-postal-tezava-za-e-mobilnost/670651
- FAISS rank/score: 5 / 0.8287
- Jina reranker score: 0.5273
- Keywords: Brexit, Stellantis, carina, električni avtomobili, Velika Britanija, dajatve na izvoz, avtomobilska industrija, Aston Martin Lagonda, Unite, Carlos Tavares, električna vozila, BMW, Kitajska, Opel/Vauxhall, Ellesmere Port, dostavna vozila, investicije, zaposlovanje, gospodarstvo, kriza, blagovne znamke
- Excerpt: Brexit je postal težava za e-mobilnost Ključne besede: Brexit, Stellantis, carina, električni avtomobili, Velika Britanija, dajatve na izvoz, avtomobilska industrija, Aston Martin Lagonda, Unite, Carlos Tavares, električna vozila, BMW, Kitajska, Opel/Vauxhall, Ellesmere Port, dostavna vozila, investicije, zaposlovanje, gospodarstvo, kriza, blagovne znamke Morebitne dajatve na izvoz električnih avtomobilov iz Velike Britanije vznemirjajo avtomobilske proizvajalce. Stellantis odkrito grozi z zaprt...

#### Rank 5: NOT RELEVANT

- Title: Britanska vlada bo prepovedala islamistično gibanje Hizb ut-Tahrir
- Decision: not_relevant
- Rationale: UK domestic security ban, not Brexit.
- Category/date: svet / 2024-01-15T21:10:18
- URL: https://www.rtvslo.si/svet/preberite-tudi/britanska-vlada-bo-prepovedala-islamisticno-gibanje-hizb-ut-tahrir/694926
- FAISS rank/score: 45 / 0.8128
- Jina reranker score: 0.5039
- Keywords: Združeno kraljestvo, islamisti, Hizb ut-Tahrir, Velika Britanija, radikalno, panislamistično, islamski kalifat, muslimanska skupnost, šeriatsko pravo, terorizem, Hamas, antisemitizem, Izrael, teroristična organizacija, Londonsko notranje ministrstvo, panislamistična politična organizacija, Jeruzalem, Kitajska, Nemčija, Pakistan, Bangladeš, Indonezija
- Excerpt: Britanska vlada bo prepovedala islamistično gibanje Hizb ut-Tahrir Ključne besede: Združeno kraljestvo, islamisti, Hizb ut-Tahrir, Velika Britanija, radikalno, panislamistično, islamski kalifat, muslimanska skupnost, šeriatsko pravo, terorizem, Hamas, antisemitizem, Izrael, teroristična organizacija, Londonsko notranje ministrstvo, panislamistična politična organizacija, Jeruzalem, Kitajska, Nemčija, Pakistan, Bangladeš, Indonezija Oblasti v Veliki Britaniji so danes sporočile, da nameravajo pre...


### 13. Vojna v Ukrajini in Zelenski

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Zelenski: V Rusijo prihaja vojna. Papež pozval k obnovitvi sporazuma o žitu.
- Decision: relevant
- Rationale: Direct Zelensky/Ukraine war result.
- Category/date: svet / 2023-07-30T09:43:53
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-v-rusijo-prihaja-vojna-papez-pozval-k-obnovitvi-sporazuma-o-zitu/676560
- FAISS rank/score: 40 / 0.8606
- Jina reranker score: 0.6992
- Keywords: vojna v Ukrajini, Vladimir Putin, pogajanja, Ukrajina, Rusija, napadi, vojna, letalniki, predsednik, obramba, teroristi, energetska infrastruktura, napad, uničenje, umrli, ranjeni, raketa, ruske sile, Sumi, Zaporožje, Ministrstvo, BBC
- Excerpt: Zelenski: V Rusijo prihaja vojna. Papež pozval k obnovitvi sporazuma o žitu. Ključne besede: vojna v Ukrajini, Vladimir Putin, pogajanja, Ukrajina, Rusija, napadi, vojna, letalniki, predsednik, obramba, teroristi, energetska infrastruktura, napad, uničenje, umrli, ranjeni, raketa, ruske sile, Sumi, Zaporožje, Ministrstvo, BBC V napadih po Ukrajini so bili ponoči ubiti najmanj trije ljudje, Rusija pa je nad Moskvo sestrelila ukrajinske letalnike. Ukrajinski predsednik Zelenski je dejal, da so nap...

#### Rank 2: RELEVANT

- Title: Zelenski: Putin želi nadaljevati vojno in nihče se ne more počutiti varnega
- Decision: relevant
- Rationale: Direct Zelensky/war result.
- Category/date: svet / 2025-09-24T18:15:11
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-putin-zeli-nadaljevati-vojno-in-nihce-se-ne-more-pocutiti-varnega/758633
- FAISS rank/score: 29 / 0.8624
- Jina reranker score: 0.6875
- Keywords: Ukrajina, Rusija, vojna, Volodimir Zelenski
- Excerpt: Zelenski: Putin želi nadaljevati vojno in nihče se ne more počutiti varnega Ključne besede: Ukrajina, Rusija, vojna, Volodimir Zelenski Ukrajinski predsednik Volodimir Zelenski je v govoru pred Generalno skupščino ZN-a ponovil, da premirja v Ukrajini še ni, ker ga Rusija zavrača. Ocenil je, da je lažje ustaviti predsednika Vladimirja Putina, kot se spustiti v oboroževalno tekmo. "Ne molčite, medtem ko Rusija nadaljuje to vojno, prosim, izrazite svoje mnenje in jo obsodite," je zbrane pozval Zele...

#### Rank 3: RELEVANT

- Title: Zelenski: V vojni umrlo 31.000 ukrajinskih vojakov. Moskva poroča o napredku ruskih sil.
- Decision: relevant
- Rationale: Direct Zelensky/Ukraine war result.
- Category/date: svet / 2024-02-25T12:39:38
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-v-vojni-umrlo-31-000-ukrajinskih-vojakov-moskva-poroca-o-napredku-ruskih-sil/699466
- FAISS rank/score: 34 / 0.8609
- Jina reranker score: 0.6797
- Keywords: Ukrajina, Rusija, Avdijivka, Doneck, Volodimir Zelenski, vojna, žrtve, pomoč Zahoda, Putin, Vladimir Putin, žrtve vojne, civilisti, dejstva, podpora, vojaška pomoč, ofenziva, protiofenziva, Kremlj, informacije, strategija, končanje vojne, zmaga, poraz.
- Excerpt: Zelenski: V vojni umrlo 31.000 ukrajinskih vojakov. Moskva poroča o napredku ruskih sil. Ključne besede: Ukrajina, Rusija, Avdijivka, Doneck, Volodimir Zelenski, vojna, žrtve, pomoč Zahoda, Putin, Vladimir Putin, žrtve vojne, civilisti, dejstva, podpora, vojaška pomoč, ofenziva, protiofenziva, Kremlj, informacije, strategija, končanje vojne, zmaga, poraz. Ukrajinski predsednik Volodimir Zelenski je sporočil, da je bilo v dveh letih vojne ubitih 31.000 ukrajinskih vojakov. Medtem pa so ruske sile...

#### Rank 4: RELEVANT

- Title: Zelenski: Ukrajinska vojska zajela kitajska državljana
- Decision: relevant
- Rationale: Zelensky/Ukraine war result.
- Category/date: svet / 2025-04-08T15:56:40
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-ukrajinska-vojska-zajela-kitajska-drzavljana/742110
- FAISS rank/score: 11 / 0.8658
- Jina reranker score: 0.6641
- Keywords: Ruske sile, Doneck, Kitajski državljani, Ukrajinska vojska, Zelenski
- Excerpt: Zelenski: Ukrajinska vojska zajela kitajska državljana Ključne besede: Ruske sile, Doneck, Kitajski državljani, Ukrajinska vojska, Zelenski Ukrajinska vojska je v Doneški oblasti na ukrajinskem ozemlju zajela kitajska državljana, ki sta se bojevala v vrstah ruskih sil, je zatrdil ukrajinski predsednik Volodimir Zelenski. Dodal je, da bodo v zvezi s tem stopili v stik s Pekingom. "Naša vojska je zajela kitajska državljana, ki sta se bojevala v ruski vojski. To se je zgodilo na ozemlju Ukrajine –...

#### Rank 5: RELEVANT

- Title: Zelenski se je srečal z vojaki, ki se borijo v Kursku: Ukrajinci so lahko močnejši od sovražnika
- Decision: relevant
- Rationale: Direct Zelensky/Ukrainian soldiers result.
- Category/date: svet / 2024-10-04T09:53:55
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-se-je-srecal-z-vojaki-ki-se-borijo-v-kursku-ukrajinci-so-lahko-mocnejsi-od-sovraznika/723177
- FAISS rank/score: 38 / 0.8607
- Jina reranker score: 0.6445
- Keywords: Ukrajina, Rusija, vojna, Vugledar, Pokrovsk
- Excerpt: Zelenski se je srečal z vojaki, ki se borijo v Kursku: Ukrajinci so lahko močnejši od sovražnika Ključne besede: Ukrajina, Rusija, vojna, Vugledar, Pokrovsk Ukrajinski predsednik Volodimir Zelenski je sporočil, da je obiskal Sumsko oblast ob meji z Rusijo in se srečal z vojaki, ki sodelujejo v ofenzivi v ruski obmejni Kurski oblasti. Zelenski se je srečal z vojaki iz 82. zračno-jurišne brigade, ki se bori v Rusiji, in se seznanil s poročilom njenega poveljnika Dmitra Vološina, ki je govoril o op...


### 14. Kitajska proti ZDA

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Kitajska na področju umetne inteligence prehiteva ZDA
- Decision: relevant
- Rationale: China vs US in AI.
- Category/date: znanost-in-tehnologija / 2019-03-19T08:39:25
- URL: https://www.rtvslo.si/znanost-in-tehnologija/kitajska-na-podrocju-umetne-inteligence-prehiteva-zda/483019
- FAISS rank/score: 18 / 0.8516
- Jina reranker score: 0.6250
- Keywords: AI, UI, Umetna inteligenca, Kitajska, Allen Institute for Artificial Intelligence, ZDA, raziskava, inštitut, tehnologija, avtonomna vozila, navidezna resničnost, 5G, naložbe, Peking, priseljevanje, strategija, Donald Trump, administracija, inovacije, nacionalna strategija, analitiki, Washington, raziskovalec
- Excerpt: Kitajska na področju umetne inteligence prehiteva ZDA Ključne besede: AI, UI, Umetna inteligenca, Kitajska, Allen Institute for Artificial Intelligence, ZDA, raziskava, inštitut, tehnologija, avtonomna vozila, navidezna resničnost, 5G, naložbe, Peking, priseljevanje, strategija, Donald Trump, administracija, inovacije, nacionalna strategija, analitiki, Washington, raziskovalec Kitajska je na dobri poti, da na področju umetne inteligence prehiti ZDA, kaže analiza, ki jo je v sredo objavil amerišk...

#### Rank 2: RELEVANT

- Title: Kitajska po napovedi novih ameriških carin zagrozila s protiukrepi
- Decision: relevant
- Rationale: Direct China response to US tariffs.
- Category/date: gospodarstvo / 2025-10-12T13:10:13
- URL: https://www.rtvslo.si/gospodarstvo/kitajska-po-napovedi-novih-ameriskih-carin-zagrozila-s-protiukrepi/760526
- FAISS rank/score: 3 / 0.8605
- Jina reranker score: 0.5977
- Keywords: ZDA, Kitajska, carine
- Excerpt: Kitajska po napovedi novih ameriških carin zagrozila s protiukrepi Ključne besede: ZDA, Kitajska, carine Potem ko je predsednik ZDA Donald Trump z novembrom napovedal nove carine na uvoz iz Kitajske, je ta zagrozila s protiukrepi. V Pekingu ob tem Washingtonu očitajo dvojna merila in mu očitajo zlorabe načela nacionalne varnosti. S kitajskega ministrstva za trgovino so sporočili, da ameriška administracija že dolgo pretirava z uporabo načela nacionalne varnosti in ga zlorablja za nadzor nad izvo...

#### Rank 3: RELEVANT

- Title: Kitajski obrambni minister: Spopad Kitajske in ZDA bi bil neznosna katastrofa za svet
- Decision: relevant
- Rationale: Direct China-US conflict result.
- Category/date: svet / 2023-06-04T09:05:31
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/kitajski-obrambni-minister-spopad-kitajske-in-zda-bi-bil-neznosna-katastrofa-za-svet/670585
- FAISS rank/score: 13 / 0.8523
- Jina reranker score: 0.5703
- Keywords: Kitajska, ZDA, Li Šangfu, konflikt, dialog, sodelovanje, varnost, vojska, politika, mednarodni odnosi, Sovjetska zveza, sankcije, orožje, Tajvan, Singapur, Azija, vrh, geopolitika, hladna vojna, hegemonija, diplomatski odnosi
- Excerpt: Kitajski obrambni minister: Spopad Kitajske in ZDA bi bil neznosna katastrofa za svet Ključne besede: Kitajska, ZDA, Li Šangfu, konflikt, dialog, sodelovanje, varnost, vojska, politika, mednarodni odnosi, Sovjetska zveza, sankcije, orožje, Tajvan, Singapur, Azija, vrh, geopolitika, hladna vojna, hegemonija, diplomatski odnosi Kitajski obrambni minister Li Šangfu je v nedeljo dejal, da bi bil spopad z ZDA "neznosna katastrofa" za svet, in da si njegova država želi dialog namesto spopada. Li, ki j...

#### Rank 4: RELEVANT

- Title: Peking sporoča Trumpu: Pritisk, prisila in grožnje niso pravi način ravnanja s Kitajsko
- Decision: relevant
- Rationale: Direct China-US pressure/tension result.
- Category/date: svet / 2025-02-28T10:06:04
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/peking-sporoca-trumpu-pritisk-prisila-in-groznje-niso-pravi-nacin-ravnanja-s-kitajsko/737947
- FAISS rank/score: 37 / 0.8472
- Jina reranker score: 0.5664
- Keywords: ZDA, Kitajska, carine
- Excerpt: Peking sporoča Trumpu: Pritisk, prisila in grožnje niso pravi način ravnanja s Kitajsko Ključne besede: ZDA, Kitajska, carine Kitajska je obtožila ZDA izsiljevanja, potem ko je ameriški predsednik Donald Trump napovedal dodatne carine na uvoz kitajskega blaga, saj po njegovih besedah Peking prispeva k zasvojenosti Američanov s fentanilom. ZDA so dodatne 10-odstotne carine na uvoz iz Kitajske uvedle ta mesec, zdaj pa je Trump zagrozil s še dodatnimi, za 10 odstotnih točk. Kitajska je napovedala,...

#### Rank 5: RELEVANT

- Title: Peking sporoča, da ne bo sprejel "izsiljevalske narave" ZDA
- Decision: relevant
- Rationale: Direct China-US pressure/tension result.
- Category/date: svet / 2025-04-08T07:23:25
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/peking-sporoca-da-ne-bo-sprejel-izsiljevalske-narave-zda/742022
- FAISS rank/score: 4 / 0.8554
- Jina reranker score: 0.5586
- Keywords: ZDA, Carine, Kitajska
- Excerpt: Peking sporoča, da ne bo sprejel "izsiljevalske narave" ZDA Ključne besede: ZDA, Carine, Kitajska Potem ko so ZDA Kitajski zagrozile z dodatnimi, 50-odstotnimi carinami, če ta ne bo umaknila povračilnih carin na uvoz ameriškega blaga, je kitajsko ministrstvo za trgovino sporočilo, da ne bodo sprejeli "izsiljevalske narave" ZDA. Ministrstvo je dodalo, da se bodo proti carinam borili "do konca", poroča BBC. Grožnjo ameriškega predsednika Donalda Trumpa z dodatnimi 50-odstotnimi carinami na kitajsk...


### 15. Korupcija v slovenski politiki

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: Koalicija in opozicija sta se obmetavali z obtožbami korupcije
- Decision: relevant
- Rationale: Direct Slovenian political corruption accusations.
- Category/date: slovenija / 2024-02-20T20:53:47
- URL: https://www.rtvslo.si/slovenija/koalicija-in-opozicija-sta-se-obmetavali-z-obtozbami-korupcije/698992
- FAISS rank/score: 5 / 0.8487
- Jina reranker score: 0.7148
- Keywords: Politika, Slovenska politika, korupcija, pravosodje, DZ, Odbor za pravosodje, Litijska, afere, opozicija, koalicija, nakup, stavba, Litijska cesta, živahna razprava, SDS, priporočila, seja, poslanec, očitki, milijonski nakup, lastništvo, integriteta, javne funkcije, obljube.
- Excerpt: Koalicija in opozicija sta se obmetavali z obtožbami korupcije Ključne besede: Politika, Slovenska politika, korupcija, pravosodje, DZ, Odbor za pravosodje, Litijska, afere, opozicija, koalicija, nakup, stavba, Litijska cesta, živahna razprava, SDS, priporočila, seja, poslanec, očitki, milijonski nakup, lastništvo, integriteta, javne funkcije, obljube. Na razpravi o stanju na področju korupcije je opozicija poudarila zlasti afere spornega nakupa stavbe na Litijski cesti, koalicija pa je izpostav...

#### Rank 2: RELEVANT

- Title: Neža Grasselli: Korupciji lahko rečemo "ne" na volitvah
- Decision: relevant
- Rationale: Corruption and elections/politics in Slovenia.
- Category/date: slovenija / 2024-12-12T08:35:44
- URL: https://www.rtvslo.si/slovenija/ob-osmih/neza-grasselli-korupciji-lahko-recemo-ne-na-volitvah/730332
- FAISS rank/score: 16 / 0.8449
- Jina reranker score: 0.6523
- Keywords: korupcija, KPK, javna naročila, politične stranke
- Excerpt: Neža Grasselli: Korupciji lahko rečemo "ne" na volitvah Ključne besede: korupcija, KPK, javna naročila, politične stranke Slovenija ima težave s korupcijo. Kot pravi predsednica upravnega odbora Transparency International Slovenija Neža Grasselli, država sicer dela nekakšne premike, ampak na področju boja proti korupciji ni preboja. Na indeksu zaznave korupcije, ki ga vsako leto objavi Transparency International (TI), smo na lanski meritvi s 56 točkami od možnih sto izenačili zdajšnji najslabši...

#### Rank 3: RELEVANT

- Title: KPK: V Sloveniji manjka ustrezno prevzemanje odgovornosti najvišjih predstavnikov oblasti
- Decision: relevant
- Rationale: Slovenian public-official accountability/corruption context.
- Category/date: slovenija / 2026-02-10T10:23:44
- URL: https://www.rtvslo.si/slovenija/kpk-v-sloveniji-manjka-ustrezno-prevzemanje-odgovornosti-najvisjih-predstavnikov-oblasti/772947
- FAISS rank/score: 25 / 0.8423
- Jina reranker score: 0.5977
- Keywords: korupcija, CPI, Slovenija
- Excerpt: KPK: V Sloveniji manjka ustrezno prevzemanje odgovornosti najvišjih predstavnikov oblasti Ključne besede: korupcija, CPI, Slovenija Slovenija je v Indeksu zaznave korupcije za leto 2025 dosegla 58 od 100 točk in se uvrstila na 41. mesto med 182 državami. Slovenija je v primerjavi z lani padla za pet mest. Premier Golob: "Morda smo bili uspavani z odličnimi rezultati v letu 2024" Po lanskem skoku navzgor, ko je Slovenija na lestvici zaznave korupcije za leto 2024 dosegla 60 točk, je letos indeks...

#### Rank 4: NOT RELEVANT

- Title: Šumi: Politika zelo težko dopusti, da bi najvišje funkcije zasedali samo kompetentni strokovni kadri
- Decision: not_relevant
- Rationale: Political appointments/competence, not mainly corruption.
- Category/date: slovenija / 2025-01-23T22:49:38
- URL: https://www.rtvslo.si/slovenija/sumi-politika-zelo-tezko-dopusti-da-bi-najvisje-funkcije-zasedali-samo-kompetentni-strokovni-kadri/734378
- FAISS rank/score: 11 / 0.8458
- Jina reranker score: 0.5898
- Keywords: KPK, Šumi, Spirit, Korupcija, Integriteta, Preprečevanje korupcije
- Excerpt: Šumi: Politika zelo težko dopusti, da bi najvišje funkcije zasedali samo kompetentni strokovni kadri Ključne besede: KPK, Šumi, Spirit, Korupcija, Integriteta, Preprečevanje korupcije Ne smemo se slepiti, da politika ne bo vplivala na to, kdo je imenovan na najvišje funkcije podjetij v državni lasti, je zadevo Črnčec posredno komentiral predsednik Komisije za preprečevanje korupcije Robert Šumi. Komisija za preprečevanje korupcije (KPK) je v primeru nakupa sodne stavbe na Litijski zaznala več ko...

#### Rank 5: RELEVANT

- Title: Seja komisije za nadzor javnih financ o korupciji prekinjena, padale tudi težke besede
- Decision: relevant
- Rationale: Direct corruption/public finance result.
- Category/date: slovenija / 2026-02-17T10:29:32
- URL: https://www.rtvslo.si/slovenija/seja-komisije-za-nadzor-javnih-financ-o-korupciji-prekinjena-padale-tudi-tezke-besede/773708
- FAISS rank/score: 13 / 0.8456
- Jina reranker score: 0.5781
- Keywords: Komisija DZ za nadzor javnih finan, korupcija, prekinitev
- Excerpt: Seja komisije za nadzor javnih financ o korupciji prekinjena, padale tudi težke besede Ključne besede: Komisija DZ za nadzor javnih finan, korupcija, prekinitev Nujna seja komisije za nadzor javnih financ je bila ob odsotnosti poslancev Levice in SD-ja prekinjena zaradi nesklepčnosti. Predsednik komisije Jernej Vrtovec je sicer zavrnil predlog Svobode, da bi obravnavali tudi trgovino z orožjem in druge afere. Sejo, na kateri bi obravnavali sume sistemske korupcije v Sloveniji, so zahtevali posla...


### 16. Izstrelitev rakete v vesolje

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Video: Tako je iz vesolja videti izstrelitev rakete
- Decision: relevant
- Rationale: Direct rocket launch from space.
- Category/date: znanost-in-tehnologija / 2018-11-25T11:06:09
- URL: https://www.rtvslo.si/znanost-in-tehnologija/video-tako-je-iz-vesolja-videti-izstrelitev-rakete/472829
- FAISS rank/score: 4 / 0.8705
- Jina reranker score: 0.7109
- Keywords: ISS, Mednarodna vesoljska postaja, Alexander Gerst, Poleti s posadko, Progress, Sojuz, raketa, vesolje, izstrelitev, vesoljsko plovilo, zaloge, Evropska vesoljska agencija, Esa, astronavt, poveljnik, kozmodrom, orbite, gorivo, kisik, preizkus, nesreča, senzor, Rusija, posadke, kupola, fotoaparat, fotografiranje.
- Excerpt: Video: Tako je iz vesolja videti izstrelitev rakete Ključne besede: ISS, Mednarodna vesoljska postaja, Alexander Gerst, Poleti s posadko, Progress, Sojuz, raketa, vesolje, izstrelitev, vesoljsko plovilo, zaloge, Evropska vesoljska agencija, Esa, astronavt, poveljnik, kozmodrom, orbite, gorivo, kisik, preizkus, nesreča, senzor, Rusija, posadke, kupola, fotoaparat, fotografiranje. Astronavt Alexander Gerst je posnel izstrelitev rakete z drugačne perspektive, kot smo je vajeni. Ujel je plovilo MS-1...

#### Rank 2: RELEVANT

- Title: SpaceX bo v četrtek zvečer izstrelil mogočno raketo Starship
- Decision: relevant
- Rationale: Direct Starship rocket launch.
- Category/date: znanost-in-tehnologija / 2025-03-03T20:06:34
- URL: https://www.rtvslo.si/znanost-in-tehnologija/spacex-bo-v-cetrtek-zvecer-izstrelil-mogocno-raketo-starship/449493
- FAISS rank/score: 5 / 0.8686
- Jina reranker score: 0.6719
- Keywords: Tehnologija, Izstrelitev, Super Heavy, SpaceX, Starship
- Excerpt: SpaceX bo v četrtek zvečer izstrelil mogočno raketo Starship Ključne besede: Tehnologija, Izstrelitev, Super Heavy, SpaceX, Starship Ameriško podjetje SpaceX bo v četrtek opravilo osmi preizkusni polet rakete Starship. Znova bo poskusilo uloviti stopnjo Super Heavy. Starship je nadgrajen in precej večji, v vesolje pa bo oddal prototipe nove generacije satelitov Starlink. Enourno izstrelitveno okno se bo odprlo v noči s četrtka na petek ob 00.30 po našem času. Izstrelitev bo potekala z Boca Chice...

#### Rank 3: RELEVANT

- Title: Izstrelitev Starshipa prestavljena
- Decision: relevant
- Rationale: Direct Starship launch result.
- Category/date: znanost-in-tehnologija / 2023-04-17T12:03:00
- URL: https://www.rtvslo.si/znanost-in-tehnologija/izstrelitev-starshipa-prestavljena/665061
- FAISS rank/score: 26 / 0.8581
- Jina reranker score: 0.6328
- Keywords: Starship, SpaceX, Raziskovanje vesolja, Vesolje, prva izstrelitev, raketa Starship, poskus, vaja, ventil, Super Heavy, Elon Musk, mokra vaja, polnjenje z gorivom, odštevanje, prižig, video, večkrat uporabna, prototip, potopljena raketa, prva stopnja, druga stopnja, simulacija
- Excerpt: Izstrelitev Starshipa prestavljena Ključne besede: Starship, SpaceX, Raziskovanje vesolja, Vesolje, prva izstrelitev, raketa Starship, poskus, vaja, ventil, Super Heavy, Elon Musk, mokra vaja, polnjenje z gorivom, odštevanje, prižig, video, večkrat uporabna, prototip, potopljena raketa, prva stopnja, druga stopnja, simulacija Prva izstrelitev rakete Starship je zaradi težav na prvi stopnji prestavljena. SpaceX je tokratni poskus spremenil v vajo. Kdaj bo naslednji poskus, še ni znano, zelo verje...

#### Rank 4: RELEVANT

- Title: Anže Slosar razvija Nasin teleskop, ki bo postavljen na oddaljeni strani Lune
- Decision: relevant
- Rationale: Space weekly includes rocket launch; largely related.
- Category/date: znanost-in-tehnologija / 2023-03-25T15:33:00
- URL: https://www.rtvslo.si/znanost-in-tehnologija/anze-slosar-razvija-nasin-teleskop-ki-bo-postavljen-na-oddaljeni-strani-lune/662367
- FAISS rank/score: 8 / 0.8618
- Jina reranker score: 0.6211
- Keywords: Vesolje, Vesoljski tednik, Raziskovanje vesolja, r, raketa, Nasa, 3D-natisnjena, teleskop, Mesec, izstrelitev, Relativity Space, Terran 1, motor, orbita, aerodinamični stres, aditivna proizvodnja, nosilna raketa, konkurenca, Starship, Marsov, robotska misija, pristajalnik.
- Excerpt: Anže Slosar razvija Nasin teleskop, ki bo postavljen na oddaljeni strani Lune Ključne besede: Vesolje, Vesoljski tednik, Raziskovanje vesolja, r, raketa, Nasa, 3D-natisnjena, teleskop, Mesec, izstrelitev, Relativity Space, Terran 1, motor, orbita, aerodinamični stres, aditivna proizvodnja, nosilna raketa, konkurenca, Starship, Marsov, robotska misija, pristajalnik. Polet prve pretežno 3D-natisnjene rakete je bil uspešen neuspeh, Nasa razvija radijski teleskop, ki bo postavljen na oddaljeno stran...

#### Rank 5: RELEVANT

- Title: Elon Musk se zanima tudi za slovensko znanje
- Decision: relevant
- Rationale: Falcon Heavy rocket launch result.
- Category/date: znanost-in-tehnologija / 2018-02-07T19:30:57
- URL: https://www.rtvslo.si/znanost-in-tehnologija/elon-musk-se-zanima-tudi-za-slovensko-znanje/445365
- FAISS rank/score: 30 / 0.8571
- Jina reranker score: 0.6133
- Keywords: Falcon Heavy, SpaceX, Tomaž Zwitter, Zwitter, Frekvenca X, Musk, Elon Musk, Tesla, Matevž Dular, Matt Taylor, Taylor, raketa, izstrelitev, promocija, znanje, tehnološki dosežek, vesolje, satelit, astrofizik, javnost, odgovornost, strokovnjak, vesoljska agencija, spektakel, zanimanje, stroški, misija
- Excerpt: Elon Musk se zanima tudi za slovensko znanje Ključne besede: Falcon Heavy, SpaceX, Tomaž Zwitter, Zwitter, Frekvenca X, Musk, Elon Musk, Tesla, Matevž Dular, Matt Taylor, Taylor, raketa, izstrelitev, promocija, znanje, tehnološki dosežek, vesolje, satelit, astrofizik, javnost, odgovornost, strokovnjak, vesoljska agencija, spektakel, zanimanje, stroški, misija Je izstrelitev rakete Falcon Heavy vrhunski dosežek ali predvsem promocija? Astrofizik Zwitter je do ravnanja podjetja kritičen, zanimanje...


### 17. Delnice Tesle padajo

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Tesla v prvem četrtletju s 13-odstotnim padcem prodaje avtomobilov
- Decision: relevant
- Rationale: Direct Tesla sales fall result.
- Category/date: gospodarstvo / 2025-04-02T17:43:00
- URL: https://www.rtvslo.si/gospodarstvo/preberite-tudi/tesla-v-prvem-cetrtletju-s-13-odstotnim-padcem-prodaje-avtomobilov/741463
- FAISS rank/score: 12 / 0.8338
- Jina reranker score: 0.7344
- Keywords: Padec delnic, Bojkot, Elon Musk, Prodaja avtomobilov, Tesla
- Excerpt: Tesla v prvem četrtletju s 13-odstotnim padcem prodaje avtomobilov Ključne besede: Padec delnic, Bojkot, Elon Musk, Prodaja avtomobilov, Tesla Ameriški proizvajalec električnih avtomobilov Tesla je v prvem letošnjem četrtletju dobavil 336.681 avtomobilov, kar je 13 odstotkov manj kot leto prej, poroča francoska tiskovna agencija AFP. Manjša prodaja je posledica manjše proizvodnje zaradi posodabljanja tovarn in bojkota podjetja zaradi političnega delovanja direktorja Elona Muska. Število dobavlje...

#### Rank 2: RELEVANT

- Title: Tesla izgublja primat na trgu e-vozil; prodajni pritisk pri bitcoinu popušča
- Decision: relevant
- Rationale: Tesla market/sales pressure context.
- Category/date: gospodarstvo / 2024-01-28T06:24:02
- URL: https://www.rtvslo.si/gospodarstvo/borzni-komentar/tesla-izgublja-primat-na-trgu-e-vozil-prodajni-pritisk-pri-bitcoinu-popusca/696349
- FAISS rank/score: 8 / 0.8369
- Jina reranker score: 0.6758
- Keywords: MMC-jev borzni komentar, Intel, Tesla, četrtletni poslovni rezultati, BYD, PCE-inflacija, ameriški BDP, bitcoin, ETF-sklad, Bitcoin Trust, delnice, New York, indeksi, dobiček, čipov, umetna inteligenca, Nvidija, podatkovni centri, Mobileye, samovozeča vozila, konkurenca, Kitajska, električna vozila, prodaja, rezultati, trgovanje, finance
- Excerpt: Tesla izgublja primat na trgu e-vozil; prodajni pritisk pri bitcoinu popušča Ključne besede: MMC-jev borzni komentar, Intel, Tesla, četrtletni poslovni rezultati, BYD, PCE-inflacija, ameriški BDP, bitcoin, ETF-sklad, Bitcoin Trust, delnice, New York, indeksi, dobiček, čipov, umetna inteligenca, Nvidija, podatkovni centri, Mobileye, samovozeča vozila, konkurenca, Kitajska, električna vozila, prodaja, rezultati, trgovanje, finance Čeprav sta Intel in Tesla s črnogledimi napovedmi malce pokvarila r...

#### Rank 3: RELEVANT

- Title: Musk po velikem padcu vrednosti Tesle obljublja, da bo podjetje najvrednejše na svetu
- Decision: relevant
- Rationale: Direct Tesla value drop result.
- Category/date: gospodarstvo / 2022-12-29T16:28:18
- URL: https://www.rtvslo.si/gospodarstvo/musk-po-velikem-padcu-vrednosti-tesle-obljublja-da-bo-podjetje-najvrednejse-na-svetu/652623
- FAISS rank/score: 10 / 0.8354
- Jina reranker score: 0.6758
- Keywords: Tesla, Elon Musk, Avtomobili, delnice, borzni trg, zaposleni, elektronsko pismo, dobave, popusti, analitiki, četrtletje, vrednost, povpraševanje, električni avtomobili, tehnološko podjetje, Twitter, proizvodnja, napoved, družbeno omrežje, direktor
- Excerpt: Musk po velikem padcu vrednosti Tesle obljublja, da bo podjetje najvrednejše na svetu Ključne besede: Tesla, Elon Musk, Avtomobili, delnice, borzni trg, zaposleni, elektronsko pismo, dobave, popusti, analitiki, četrtletje, vrednost, povpraševanje, električni avtomobili, tehnološko podjetje, Twitter, proizvodnja, napoved, družbeno omrežje, direktor Potem ko so delnice avtomobilskega podjetja Tesla letos izgubile 70 odstotkov, je lastnik Elon Musk zatrdil, da bo podjetje na dolgi rok najvrednejše...

#### Rank 4: RELEVANT

- Title: Tesla vse bolj v nemilosti Wall Streeta, bitcoinov "flash crash"
- Decision: relevant
- Rationale: Tesla/Wall Street stock-pressure result.
- Category/date: gospodarstvo / 2024-03-20T06:34:54
- URL: https://www.rtvslo.si/gospodarstvo/borzni-komentar/tesla-vse-bolj-v-nemilosti-wall-streeta-bitcoinov-flash-crash/702135
- FAISS rank/score: 13 / 0.8336
- Jina reranker score: 0.6680
- Keywords: MMC-jev borzni komentar, Tesla, Rivian, Cisco, borzni mehurček, bitcoin, flash crash, naložbe, tveganje, volatilnost, rast, balon, delnice, vrednost, kriptovalute, podjetje, inflacija, avtomobili, Wall Street, tržni delež, dobiček, vrednotenje, električna vozila, Wells Fargo, ciljna cena, banka UBS, portfelj.
- Excerpt: Tesla vse bolj v nemilosti Wall Streeta, bitcoinov "flash crash" Ključne besede: MMC-jev borzni komentar, Tesla, Rivian, Cisco, borzni mehurček, bitcoin, flash crash, naložbe, tveganje, volatilnost, rast, balon, delnice, vrednost, kriptovalute, podjetje, inflacija, avtomobili, Wall Street, tržni delež, dobiček, vrednotenje, električna vozila, Wells Fargo, ciljna cena, banka UBS, portfelj. Neizkušeni vlagatelji verjetno ne razumejo, kaj pomeni, če je neka naložba tvegana in volatilna. Vidijo le p...

#### Rank 5: RELEVANT

- Title: Tehnološko opustošenje stoletja: iz velikanov izpuhtelo 5,4 bilijona dolarjev
- Decision: relevant
- Rationale: Direct Tesla stock/share losses.
- Category/date: gospodarstvo / 2022-12-25T07:40:17
- URL: https://www.rtvslo.si/gospodarstvo/borzni-komentar/tehnolosko-opustosenje-stoletja-iz-velikanov-izpuhtelo-5-4-bilijona-dolarjev/652126
- FAISS rank/score: 2 / 0.8418
- Jina reranker score: 0.6562
- Keywords: MMC-jev borzni komentar, tehnološke delnice, ARK Innovation, Cathie Wood, Tesla, Primož Cencelj, finančni trgi, recesija, Teslina delnica, Fed, inflacija, vlagatelji, izgube, kriza, mladi vlagatelji, ETF-sklad, kapital, Invitae, Coinbase, Twilio, tečaj, rast, spremembe, trg
- Excerpt: Tehnološko opustošenje stoletja: iz velikanov izpuhtelo 5,4 bilijona dolarjev Ključne besede: MMC-jev borzni komentar, tehnološke delnice, ARK Innovation, Cathie Wood, Tesla, Primož Cencelj, finančni trgi, recesija, Teslina delnica, Fed, inflacija, vlagatelji, izgube, kriza, mladi vlagatelji, ETF-sklad, kapital, Invitae, Coinbase, Twilio, tečaj, rast, spremembe, trg Ker Fedov boj proti inflaciji večjih rezultatov še ni prinesel, gospodarstvo pa bo očitno pahnil v recesijo, se finančni trgi od le...


### 18. Nova verzija umetne inteligence

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: OpenAI predstavil najnovejši model umetne inteligence GPT-5 − pametnejši, hitrejši, uporabnejši
- Decision: relevant
- Rationale: Direct latest AI model/version result.
- Category/date: znanost-in-tehnologija / 2025-08-08T08:30:59
- URL: https://www.rtvslo.si/znanost-in-tehnologija/openai-predstavil-najnovejsi-model-umetne-inteligence-gpt-5-pametnejsi-hitrejsi-uporabnejsi/754133
- FAISS rank/score: 1 / 0.8351
- Jina reranker score: 0.7266
- Keywords: GPT-5, OpenAI, UI
- Excerpt: OpenAI predstavil najnovejši model umetne inteligence GPT-5 − pametnejši, hitrejši, uporabnejši Ključne besede: GPT-5, OpenAI, UI Podjetje OpenAI je predstavilo najnovejši in najnaprednejši model umetne inteligence velikega obsega GPT-5. GPT-5, ki je pametnejši, hitrejši in uporabnejši pri pisanju, programiranju in na drugih področjih, bo vsem na voljo brezplačno. OpenAI trdi, da je stopnja halucinacij GPT-5 nižja, kar pomeni, da si model manj pogosto izmišlja odgovore. V podjetju so pojasnili,...

#### Rank 2: RELEVANT

- Title: Google predstavil nov program umetne inteligence Bard
- Decision: relevant
- Rationale: New AI program result.
- Category/date: znanost-in-tehnologija / 2023-02-07T11:00:00
- URL: https://www.rtvslo.si/znanost-in-tehnologija/google-predstavil-nov-program-umetne-inteligence-bard/657070
- FAISS rank/score: 3 / 0.8275
- Jina reranker score: 0.6055
- Keywords: Google, Bard, Umetna inteligenca, jezikovni model, intervju, Sundar Pichai, LaMDA, ChatGPT, OpenAI, Microsoft, investicija, partnerstvo, tehnološko podjetje, aplikacije za dialog, razvoj, napredki, zunanji vplivi, primerjava, inovacija, iskalnik
- Excerpt: Google predstavil nov program umetne inteligence Bard Ključne besede: Google, Bard, Umetna inteligenca, jezikovni model, intervju, Sundar Pichai, LaMDA, ChatGPT, OpenAI, Microsoft, investicija, partnerstvo, tehnološko podjetje, aplikacije za dialog, razvoj, napredki, zunanji vplivi, primerjava, inovacija, iskalnik Ameriški tehnološki velikan Google je uradno predstavil nov program umetne inteligence Bard. Kot poudarjajo v podjetju, gre za pomemben naslednji korak na področju umetne inteligence z...

#### Rank 3: NOT RELEVANT

- Title: Umetna inteligenca se je že sposobna učiti brez človekove pomoči
- Decision: not_relevant
- Rationale: AI capability article, not a new version/model.
- Category/date: znanost-in-tehnologija / 2017-10-19T14:59:55
- URL: https://www.rtvslo.si/znanost-in-tehnologija/umetna-inteligenca-se-je-ze-sposobna-uciti-brez-clovekove-pomoci/435607
- FAISS rank/score: 5 / 0.8237
- Jina reranker score: 0.5352
- Keywords: umetna inteligenca, Go, programska oprema, Google, DeepMind, AlphaGo Zero, igra go, kitajska družabna igra, samoučenje, računalniška moč, podatki, neuronka mreža, algoritmi, profesionalci, razvoj, tehnologija, inovacija, napredek
- Excerpt: Umetna inteligenca se je že sposobna učiti brez človekove pomoči Ključne besede: umetna inteligenca, Go, programska oprema, Google, DeepMind, AlphaGo Zero, igra go, kitajska družabna igra, samoučenje, računalniška moč, podatki, neuronka mreža, algoritmi, profesionalci, razvoj, tehnologija, inovacija, napredek Medmrežni velikan Google razvija umetno inteligenco, ki se je sposobna učiti brez kakršnega koli človeškega posredovanja. Googlova raziskovalna skupina Google DeepMind je naredila velik kor...

#### Rank 4: RELEVANT

- Title: Razvili umetno inteligenco, ki bo nadgradila izkušnjo športnih ljubiteljev
- Decision: relevant
- Rationale: Newly developed AI system result.
- Category/date: zabava-in-slog / 2024-06-24T13:28:46
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/razvili-umetno-inteligenco-ki-bo-nadgradila-izkusnjo-sportnih-ljubiteljev/712824
- FAISS rank/score: 6 / 0.8234
- Jina reranker score: 0.5156
- Keywords: Generativna funkcija, Wimbledon, IBM, Športni podatki, Umetna inteligenca, skit scena
- Excerpt: Razvili umetno inteligenco, ki bo nadgradila izkušnjo športnih ljubiteljev Ključne besede: Generativna funkcija, Wimbledon, IBM, Športni podatki, Umetna inteligenca, skit scena Umetna inteligenca je dodobra vpeta v naš način življenja in je prisotna kot še nikoli doslej. Zdaj bo tehnologija vpeljana še v svet športa, natančneje tenisa, ki bo tako za tekmovalce kot navijače dodala novo dimenzijo. "Vi vidite tenis, mi vidimo podatke. Vi vidite golf, mi vidimo podatke," je za Euronews povedal Jonat...

#### Rank 5: RELEVANT

- Title: Apple bo svoje naprave nadgradil s ChatGPT-jem in glasovni pomočnici Siri dal nove funkcije
- Decision: relevant
- Rationale: New AI features/upgrade result.
- Category/date: znanost-in-tehnologija / 2024-06-11T09:23:51
- URL: https://www.rtvslo.si/znanost-in-tehnologija/apple-bo-svoje-naprave-nadgradil-s-chatgpt-jem-in-glasovni-pomocnici-siri-dal-nove-funkcije/711352
- FAISS rank/score: 2 / 0.8309
- Jina reranker score: 0.5000
- Keywords: Apple, OpenAI, ChatGPT, Tim Cook
- Excerpt: Apple bo svoje naprave nadgradil s ChatGPT-jem in glasovni pomočnici Siri dal nove funkcije Ključne besede: Apple, OpenAI, ChatGPT, Tim Cook Ameriško tehnološko podjetje Apple je predstavilo nove funkcije umetne inteligence za svoje naprave Apple Intelligence in partnerstvo s podjetjem OpenAI, ki bo še letos vključilo storitev ChatGPT v Applove naprave. Glavni izvršni direktor Appla Tim Cook je na sedežu tehnološkega velikana v kalifornijskem mestu Cupertino v Silicijevi dolini odprl letno konfe...


### 19. Najbolj prodajan avtomobil

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Tesla z dvema modeloma na lestvici najbolj prodajanih vozil na svetu
- Decision: relevant
- Rationale: Direct best-selling vehicles result.
- Category/date: zabava-in-slog / 2023-05-10T08:01:00
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/tesla-z-dvema-modeloma-na-lestvici-najbolj-prodajanih-vozil-na-svetu/667586
- FAISS rank/score: 25 / 0.8342
- Jina reranker score: 0.6133
- Keywords: Prodaja vozil, JATO Dynamics, Toyota RAV 4, Toyota, vozilo, prodaja, svet, avtomobili, modeli, Tesla, registracija, trg, razvoj, Severna Amerika, Evropa, Kitajska, padec, dobavna veriga, polprevodniki, motnje, Ukrajina, sankcije, Rusija, Volkswagen, Hyundai-Kia, Stellantis, General Motors, BYD, tržni delež, testiranje, Avtomobilnost.
- Excerpt: Tesla z dvema modeloma na lestvici najbolj prodajanih vozil na svetu Ključne besede: Prodaja vozil, JATO Dynamics, Toyota RAV 4, Toyota, vozilo, prodaja, svet, avtomobili, modeli, Tesla, registracija, trg, razvoj, Severna Amerika, Evropa, Kitajska, padec, dobavna veriga, polprevodniki, motnje, Ukrajina, sankcije, Rusija, Volkswagen, Hyundai-Kia, Stellantis, General Motors, BYD, tržni delež, testiranje, Avtomobilnost. Toyota je leta 2022 prodala največ vozil na svetu. Med desetimi najbolje prodaj...

#### Rank 2: RELEVANT

- Title: Tesla model Y leta 2023 najbolje prodajano vozilo v Evropi
- Decision: relevant
- Rationale: Direct best-selling vehicle result.
- Category/date: zabava-in-slog / 2024-01-21T12:31:47
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/tesla-model-y-leta-2023-najbolje-prodajano-vozilo-v-evropi/695612
- FAISS rank/score: 3 / 0.8537
- Jina reranker score: 0.5469
- Keywords: Tesla, Model Y, Prodaja vozil, električni avtomobil, Evropa, prodaja, Slovenija, leta 2023, registracije, cena, konkurenca, industrija, vozila, strokovnjaki, uspeh, popularnost, Dacia Sandero, Volkswagen T-Roc, Škoda Octavia
- Excerpt: Tesla model Y leta 2023 najbolje prodajano vozilo v Evropi Ključne besede: Tesla, Model Y, Prodaja vozil, električni avtomobil, Evropa, prodaja, Slovenija, leta 2023, registracije, cena, konkurenca, industrija, vozila, strokovnjaki, uspeh, popularnost, Dacia Sandero, Volkswagen T-Roc, Škoda Octavia Električni križanec tesla Y je prvi električni avtomobil, ki je do zdaj postal najbolje prodajano vozilo v Evropi v koledarskem letu. Tesla model Y je bil v Sloveniji sedmi najbolje prodajan model avt...

#### Rank 3: RELEVANT

- Title: Dacia sandero premagala teslo Y
- Decision: relevant
- Rationale: Direct sales ranking result.
- Category/date: zabava-in-slog / 2024-03-23T07:37:23
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/dacia-sandero-premagala-teslo-y/702542
- FAISS rank/score: 9 / 0.8485
- Jina reranker score: 0.5391
- Keywords: Dacia sandero, Tesla model y, Volkswagen golf, Evropa, prodaja avtomobilov, Dataforce, sindikati, prodaja vozil, Teslina tovarna, Grünheide, Berlin, avtomobilska industrija, Peugeot 208, Citroen C3, kombilimuzina, električni avtomobili, avtomobilske tovarne, aktivisti, prodajne uspešnice, prodajne enote
- Excerpt: Dacia sandero premagala teslo Y Ključne besede: Dacia sandero, Tesla model y, Volkswagen golf, Evropa, prodaja avtomobilov, Dataforce, sindikati, prodaja vozil, Teslina tovarna, Grünheide, Berlin, avtomobilska industrija, Peugeot 208, Citroen C3, kombilimuzina, električni avtomobili, avtomobilske tovarne, aktivisti, prodajne uspešnice, prodajne enote Dacia Sandero je ponovno najbolje prodajani avto v Evropi. Premagala je teslo model Y, največjo uspešnico leta 2023. Dacia sandero je na dobri poti...

#### Rank 4: RELEVANT

- Title: Lani največ avtomobilov prodal Volkswagen, najbolj priljubljena škoda octavia
- Decision: relevant
- Rationale: Direct best-selling brand/model result.
- Category/date: gospodarstvo / 2024-01-15T15:52:19
- URL: https://www.rtvslo.si/gospodarstvo/lani-najvec-avtomobilov-prodal-volkswagen-najbolj-priljubljena-skoda-octavia/694894
- FAISS rank/score: 7 / 0.8490
- Jina reranker score: 0.5156
- Keywords: Tržni delež, Električni avtomobili, Škoda Octavia, Volkswagen, avtomobili, Slovenija, registracija, vozilo, gospodarsko, znamka, model, električni avtomobil, hibridni pogon, prodaja, Škoda, Renault, Ford, Toyota, Tesla, ID.4, enyaq, corolla
- Excerpt: Lani največ avtomobilov prodal Volkswagen, najbolj priljubljena škoda octavia Ključne besede: Tržni delež, Električni avtomobili, Škoda Octavia, Volkswagen, avtomobili, Slovenija, registracija, vozilo, gospodarsko, znamka, model, električni avtomobil, hibridni pogon, prodaja, Škoda, Renault, Ford, Toyota, Tesla, ID.4, enyaq, corolla V Sloveniji je bilo lani prvič registriranih 48.923 osebnih avtomobilov, kar je 5,6 odstotka več kot predlani. Število prvič registriranih lahkih gospodarskih vozil...

#### Rank 5: RELEVANT

- Title: Po skromnejšem maju se prodaja vozil v Sloveniji krepi
- Decision: relevant
- Rationale: Vehicle sales with top brands/models; largely related.
- Category/date: zabava-in-slog / 2023-07-08T09:08:41
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/po-skromnejsem-maju-se-prodaja-vozil-v-sloveniji-krepi/674464
- FAISS rank/score: 2 / 0.8546
- Jina reranker score: 0.4980
- Keywords: Prodaja vozil, škoda octavia, Tesla, avtomobilski trg, registracija vozil, rast prodaje, Slovenija, osebna vozila, gospodarska vozila, znamke, modeli vozil, elektrificirana vozila, električna vozila, hibridna vozila, registracije vozil, junij, trendi prodaje, trg vozil, statistika registracij, priključni hibridi, blagi hibridi, Volkswagen, Renault, Toyota, Škoda, Ford, Opel, vozni park
- Excerpt: Po skromnejšem maju se prodaja vozil v Sloveniji krepi Ključne besede: Prodaja vozil, škoda octavia, Tesla, avtomobilski trg, registracija vozil, rast prodaje, Slovenija, osebna vozila, gospodarska vozila, znamke, modeli vozil, elektrificirana vozila, električna vozila, hibridna vozila, registracije vozil, junij, trendi prodaje, trg vozil, statistika registracij, priključni hibridi, blagi hibridi, Volkswagen, Renault, Toyota, Škoda, Ford, Opel, vozni park Medletna rast prodaje novih vozil na avt...


### 20. Obisk tujega predsednika

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: Južnokorejski predsednik pred obiskom ZDA krepil vezi na Japonskem
- Decision: relevant
- Rationale: Foreign president visit result.
- Category/date: svet / 2025-08-23T21:47:21
- URL: https://www.rtvslo.si/svet/preberite-tudi/juznokorejski-predsednik-pred-obiskom-zda-krepil-vezi-na-japonskem/755500
- FAISS rank/score: 28 / 0.8252
- Jina reranker score: 0.4688
- Keywords: Japonska, Južna Koreja, sodelovanje
- Excerpt: Južnokorejski predsednik pred obiskom ZDA krepil vezi na Japonskem Ključne besede: Japonska, Južna Koreja, sodelovanje Japonska in Južna Koreja sta se ob današnjem obisku novega južnokorejskega predsednika Lee Jae Myunga v Tokiu dogovorili za krepitev sodelovanja. Obisk ima zgodovinski pomen, saj se je prvič po normalizaciji odnosov med državama pred 60 leti zgodilo, da je predsednik Južne Koreje za prvo pot v tujino izbral Japonsko. V nedeljo bo odšel še v ZDA. " V vse zahtevnejšem strateškem o...

#### Rank 2: RELEVANT

- Title: Zoran Milanović si je za prvo pot v tujino v drugem predsedniškem mandatu izbral Slovenijo
- Decision: relevant
- Rationale: Direct foreign president visit to Slovenia.
- Category/date: slovenija / 2025-02-19T13:19:48
- URL: https://www.rtvslo.si/slovenija/zoran-milanovic-si-je-za-prvo-pot-v-tujino-v-drugem-predsedniskem-mandatu-izbral-slovenijo/737062
- FAISS rank/score: 8 / 0.8313
- Jina reranker score: 0.4355
- Keywords: Uradni obisk, Slovenija, Zoran Milanović
- Excerpt: Zoran Milanović si je za prvo pot v tujino v drugem predsedniškem mandatu izbral Slovenijo Ključne besede: Uradni obisk, Slovenija, Zoran Milanović Hrvaški predsednik Zoran Milanović, ki je v torek v Zagrebu prisegel za drugi predsedniški petletni mandat, bo prihodnjo sredo na uradnem obisku v Sloveniji. Iz urada predsednice republike Nataše Pirc Musar so sporočili, da gre za prvo uradno pot Zorana Milanovića v tujino po nastopu drugega mandata predsednika republike. " Namen obiska je nadaljevan...

#### Rank 3: RELEVANT

- Title: Putin v Kirgiziji prvič na obisku v tujini po izdaji naloga ICC-ja
- Decision: relevant
- Rationale: Foreign visit by a president.
- Category/date: svet / 2023-10-12T11:03:00
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/putin-v-kirgiziji-prvic-na-obisku-v-tujini-po-izdaji-naloga-icc-ja/684578
- FAISS rank/score: 24 / 0.8259
- Jina reranker score: 0.4316
- Keywords: Rusija, Kirgizistan, Vladimir Putin, ICC, Kirgizija, Mednarodno kazensko sodišče, Haag, Skupnost neodvisnih držav, SND, Aleksander Lukašenko, Sadir Žaparov, Zračna obramba, Ukrajina, Dekleta, Moskva, Marija Lvova-Belova, Pravice otrok, Aretekacija, Preventivni ukrepi, Brics, Južna Afrika
- Excerpt: Putin v Kirgiziji prvič na obisku v tujini po izdaji naloga ICC-ja Ključne besede: Rusija, Kirgizistan, Vladimir Putin, ICC, Kirgizija, Mednarodno kazensko sodišče, Haag, Skupnost neodvisnih držav, SND, Aleksander Lukašenko, Sadir Žaparov, Zračna obramba, Ukrajina, Dekleta, Moskva, Marija Lvova-Belova, Pravice otrok, Aretekacija, Preventivni ukrepi, Brics, Južna Afrika Ruski predsednik Vladimir Putin je prispel na obisk v Kirgizijo, kar je njegova prva pot v tujino, potem ko je Mednarodno kazens...

#### Rank 4: RELEVANT

- Title: Predsednica Nataša Pirc Musar bo prihodnji teden obiskala Kazahstan
- Decision: relevant
- Rationale: Presidential official foreign visit; largely related.
- Category/date: slovenija / 2025-03-26T10:48:19
- URL: https://www.rtvslo.si/slovenija/preberite-tudi/predsednica-natasa-pirc-musar-bo-prihodnji-teden-obiskala-kazahstan/740645
- FAISS rank/score: 47 / 0.8231
- Jina reranker score: 0.4004
- Keywords: Nataša Pirc Musar, obisk, Kazahstan
- Excerpt: Predsednica Nataša Pirc Musar bo prihodnji teden obiskala Kazahstan Ključne besede: Nataša Pirc Musar, obisk, Kazahstan Predsednica republike Nataša Pirc Musar bo v ponedeljek in torek na uradnem obisku v Kazahstanu, kjer jo bo gostil predsednik Kasim-Žomart Tokajev. Predsednico bosta spremljali zunanja ministrica Tanja Fajon in gospodarska delegacija. Predsednica republike Nataša Pirc Musar se bo v Astani srečala s predsednikom Kazahstana Kasim-Žomartom Tokajevom, premierjem Olžasom Bektenovom...

#### Rank 5: NOT RELEVANT

- Title: Tajvan Pekingu sporoča, "naj se sprijazni z realnostjo". Na obisku ameriška delegacija.
- Decision: not_relevant
- Rationale: US delegation visit, not a foreign president visit.
- Category/date: svet / 2024-01-14T13:45:34
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/tajvan-pekingu-sporoca-naj-se-sprijazni-z-realnostjo-na-obisku-ameriska-delegacija/694770
- FAISS rank/score: 21 / 0.8273
- Jina reranker score: 0.3711
- Keywords: Tajvan, Laj Čingte, Kitajska, ZDA, amerika, volitve, predsednik, diplomatski odnosi, varnost, delegacija, politika, vojaške vaje, demokracija, tajvanska ožina, sodelovanje, grožnje, stabilnost, zunanje ministrstvo, Peking, neuradni obisk
- Excerpt: Tajvan Pekingu sporoča, "naj se sprijazni z realnostjo". Na obisku ameriška delegacija. Ključne besede: Tajvan, Laj Čingte, Kitajska, ZDA, amerika, volitve, predsednik, diplomatski odnosi, varnost, delegacija, politika, vojaške vaje, demokracija, tajvanska ožina, sodelovanje, grožnje, stabilnost, zunanje ministrstvo, Peking, neuradni obisk Novoizvoljeni tajvanski predsednik Laj Čingte je po sobotni zmagi dejal, da bo branil otok pred kitajskim "ustrahovanjem". V Tajvan je prišla tudi neuradna am...

