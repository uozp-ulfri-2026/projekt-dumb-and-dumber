# Precision@5 evaluation without reranker - intfloat/multilingual-e5-large

Created: 2026-05-31T20:37:02
Relevance rule: largely related
Embedding model: `intfloat/multilingual-e5-large`
Reranker: disabled
Retrieval: direct FAISS top 5 results
Raw output source: `data/evaluation/precision_at_5_e5_large_no_reranker_raw_outputs.json`

## Overall result

- Total relevant results: 78/100
- Precision@5: 0.78

## Per-prompt summary

| # | Prompt | Relevant@5 | Precision@5 |
|---:|---|---:|---:|
| 1 | Vpis v srednje šole | 5/5 | 1.00 |
| 2 | Zakoni glede generativne umetne inteligence | 2/5 | 0.40 |
| 3 | Cene kart na nogometnem svetovnem prvenstvu | 3/5 | 0.60 |
| 4 | Tožba slovenskih avtoprevoznikov | 2/5 | 0.40 |
| 5 | Vojna Zvezd v Sloveniji | 1/5 | 0.20 |
| 6 | Ogromni zastoji na Slovenskih cestah | 5/5 | 1.00 |
| 7 | Višanje temperatur | 4/5 | 0.80 |
| 8 | Višanje cen nepremičnin v Sloveniji | 5/5 | 1.00 |
| 9 | Rogljič in Pogačar na tekmi | 5/5 | 1.00 |
| 10 | Donald Trump novi zakoni | 3/5 | 0.60 |
| 11 | Evropska Unija in zveza NATO | 5/5 | 1.00 |
| 12 | Velika Britanija Brexit | 5/5 | 1.00 |
| 13 | Vojna v Ukrajini in Zelenski | 5/5 | 1.00 |
| 14 | Kitajska proti ZDA | 5/5 | 1.00 |
| 15 | Korupcija v slovenski politiki | 4/5 | 0.80 |
| 16 | Izstrelitev rakete v vesolje | 5/5 | 1.00 |
| 17 | Delnice Tesle padajo | 3/5 | 0.60 |
| 18 | Nova verzija umetne inteligence | 3/5 | 0.60 |
| 19 | Najbolj prodajan avtomobil | 4/5 | 0.80 |
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
- Reranker score: n/a
- Keywords: Gimnazijski programi, Strokovno izobraževanje, Srednje šole, Vpis
- Excerpt: Končane prijave za vpis v srednje šole, največ zanimanja za srednje strokovno izobraževanje Ključne besede: Gimnazijski programi, Strokovno izobraževanje, Srednje šole, Vpis V prve letnike srednjih šol v prihodnjem šolskem letu se je na 26.008 razpisanih prostih mest prijavilo 23.933 kandidatov. Rok za prijave je potekel 2. aprila. Ministrstvo za vzgojo in izobraževanje je objavilo podatke o vpisu v srednje šole v šolskem letu 2025/2026. Na programe nižjega poklicnega izobraževanja, kjer je razp...

#### Rank 2: RELEVANT

- Title: Vpis je omejen na 58 srednjih šolah, povečal se je vpis v srednje in nižje poklicne šole
- Decision: relevant
- Rationale: Direct secondary-school enrolment result.
- Category/date: slovenija / 2024-05-23T11:08:23
- URL: https://www.rtvslo.si/slovenija/vpis-je-omejen-na-58-srednjih-solah-povecal-se-je-vpis-v-srednje-in-nizje-poklicne-sole/709285
- FAISS rank/score: 2 / 0.8641
- Reranker score: n/a
- Keywords: Ministrstvo za vzgojo in izobraževanje, Gimnazijski programi, Poklicno izobraževanje, Srednje šole, Vpis
- Excerpt: Vpis je omejen na 58 srednjih šolah, povečal se je vpis v srednje in nižje poklicne šole Ključne besede: Ministrstvo za vzgojo in izobraževanje, Gimnazijski programi, Poklicno izobraževanje, Srednje šole, Vpis Prihodnje šolsko leto bo srednje šole obiskovalo 22.971 kandidatov, največ, 42,7 odstotka, se jih je vpisalo v srednje strokovne šole, sledijo gimnazije, srednje poklicne in nižje poklicne šole. Vpis bo omejen na 58 šolah, medtem ko je bil lani na 70. Vpis je omejen v 12 programih poklicne...

#### Rank 3: RELEVANT

- Title: Zadnji dan za vpis na izbrano srednjo šolo
- Decision: relevant
- Rationale: Direct secondary-school enrolment result.
- Category/date: slovenija / 2024-04-02T09:39:24
- URL: https://www.rtvslo.si/slovenija/zadnji-dan-za-vpis-na-izbrano-srednjo-solo/703604
- FAISS rank/score: 3 / 0.8638
- Reranker score: n/a
- Keywords: Regija, Prijavnica, Mest, Gimnazija, Izobraževanje, skit scena, vpis, srednješolski programi, Ministrstvo za vzgojo in izobraževanje, prijave, izobraževalni programi, prijavni rok, srednja šola, vpisovanje, izbirni postopek, osnovno šolstvo, osrednjeslovenska regija, šolsko leto, gimnazije, poklicno izobraževanje, regije, dijaki, dijakinje, mesta za vpis, razpisana mesta, 9. razred
- Excerpt: Zadnji dan za vpis na izbrano srednjo šolo Ključne besede: Regija, Prijavnica, Mest, Gimnazija, Izobraževanje, skit scena, vpis, srednješolski programi, Ministrstvo za vzgojo in izobraževanje, prijave, izobraževalni programi, prijavni rok, srednja šola, vpisovanje, izbirni postopek, osnovno šolstvo, osrednjeslovenska regija, šolsko leto, gimnazije, poklicno izobraževanje, regije, dijaki, dijakinje, mesta za vpis, razpisana mesta, 9. razred Danes se izteče rok za prijavo za vpis v srednješolske p...

#### Rank 4: RELEVANT

- Title: Vpis v srednje šole: največ zanimanja za srednje strokovne šole
- Decision: relevant
- Rationale: Direct secondary-school enrolment result.
- Category/date: slovenija / 2023-04-25T17:29:00
- URL: https://www.rtvslo.si/slovenija/vpis-v-srednje-sole-najvec-zanimanja-za-srednje-strokovne-sole/666150
- FAISS rank/score: 4 / 0.8626
- Reranker score: n/a
- Keywords: vpis, šolsko leto, srednje šole, kandidati, mesta, prijavnica, izobraževalni programi, ministrstvo, poklicno izobraževanje, gimnazije, strokovno izobraževanje, razpisana mesta, podatki, statistika, sprejem, vpisni postopek, razporeditev, sposobnosti, prvi krog, programi, prosti poklice, želeni poklic, osnovno šolanje.
- Excerpt: Vpis v srednje šole: največ zanimanja za srednje strokovne šole Ključne besede: vpis, šolsko leto, srednje šole, kandidati, mesta, prijavnica, izobraževalni programi, ministrstvo, poklicno izobraževanje, gimnazije, strokovno izobraževanje, razpisana mesta, podatki, statistika, sprejem, vpisni postopek, razporeditev, sposobnosti, prvi krog, programi, prosti poklice, želeni poklic, osnovno šolanje. Za vpis novincev v srednje šole za prihodnje šolsko leto se je v roku na skupno 25.560 prvotno razpi...

#### Rank 5: RELEVANT

- Title: Zadnji dan za prijavo v srednje šole in dijaške domove
- Decision: relevant
- Rationale: Direct secondary-school application/enrolment result.
- Category/date: slovenija / 2025-04-02T09:43:41
- URL: https://www.rtvslo.si/slovenija/zadnji-dan-za-prijavo-v-srednje-sole-in-dijaske-domove/741401
- FAISS rank/score: 5 / 0.8624
- Reranker score: n/a
- Keywords: Izbirni postopek, Vpisna mesta, Dijaški domovi, Srednje šole, Prijave
- Excerpt: Zadnji dan za prijavo v srednje šole in dijaške domove Ključne besede: Izbirni postopek, Vpisna mesta, Dijaški domovi, Srednje šole, Prijave Izteka se rok za oddajo prijavnice za vpis novincev v srednje šole in dijaške domove za šolsko leto 2025/26. Letos jo je po novem mogoče oddati elektronsko. Stanje prijav po posameznih programih oz. šolah bo ministrstvo objavilo najpozneje do 8. aprila, do 6. maja pa bodo lahko nato učenci svojo prijavo prenesli v drug program. Osnovno šolo v letošnjem šols...


### 2. Zakoni glede generativne umetne inteligence

Precision@5: 2/5 = 0.40

#### Rank 1: RELEVANT

- Title: Vizualni umetniki pridobivajo v pravni bitki proti umetni inteligenci. Bo z glasbo drugače?
- Decision: relevant
- Rationale: Legal battle around generative AI/copyright.
- Category/date: kultura / 2024-08-14T21:03:41
- URL: https://www.rtvslo.si/kultura/glasba/vizualni-umetniki-pridobivajo-v-pravni-bitki-proti-umetni-inteligenci-bo-z-glasbo-drugace/718051
- FAISS rank/score: 1 / 0.8586
- Reranker score: n/a
- Keywords: Poštena uporaba, Generativna orodja, Umetniška tožba, Avtorske pravice, Generirana umetnost
- Excerpt: Vizualni umetniki pridobivajo v pravni bitki proti umetni inteligenci. Bo z glasbo drugače? Ključne besede: Poštena uporaba, Generativna orodja, Umetniška tožba, Avtorske pravice, Generirana umetnost Pravno urejanje uporabe vizualnih ali glasbenih del za učenje umetne inteligence postaja vse bolj zapleteno, kar dokazujejo tudi zadnji sodni primeri v ZDA. V prihodnjih mesecih bo jasno, ali gre za pošteno uporabo ali kršitve avtorskih pravic. Na začetku letošnjega leta smo poročali o dolgem seznam...

#### Rank 2: NOT RELEVANT

- Title: Razpis za nacionalno platformo za umetno inteligenco deli mnenja v stroki
- Decision: not_relevant
- Rationale: AI platform procurement, not mainly laws.
- Category/date: znanost-in-tehnologija / 2025-12-15T08:03:13
- URL: https://www.rtvslo.si/znanost-in-tehnologija/razpis-za-nacionalno-platformo-za-umetno-inteligenco-deli-mnenja-v-stroki/767256
- FAISS rank/score: 2 / 0.8517
- Reranker score: n/a
- Keywords: Licenciranje, Tehnološka suverenost, Razpis, ChatGPT, Generativna umetna inteligenca
- Excerpt: Razpis za nacionalno platformo za umetno inteligenco deli mnenja v stroki Ključne besede: Licenciranje, Tehnološka suverenost, Razpis, ChatGPT, Generativna umetna inteligenca Končalo se je razpisno zbiranje ponudb za nacionalno platformo umetne inteligence, s katero naj bi državljanom omogočili dostop do najzmogljivejših modelov umetne inteligence. Mnenja o upravičenosti takšne naložbe so različna. Danes marsikdo že uporablja orodja generativne umetne inteligence, kot je ChatGPT, predvsem brezpl...

#### Rank 3: NOT RELEVANT

- Title: Največja glasbena založba sklenila dogovor s podjetjem generativne umetne inteligence
- Decision: not_relevant
- Rationale: Business agreement with AI company, not laws.
- Category/date: kultura / 2025-10-30T13:39:44
- URL: https://www.rtvslo.si/kultura/glasba/najvecja-glasbena-zalozba-sklenila-dogovor-s-podjetjem-generativne-umetne-inteligence/762476
- FAISS rank/score: 3 / 0.8473
- Reranker score: n/a
- Keywords: Poravnava, Generativna umetna inteligenca, Avtorske pravice, Udio, Universal Music Group
- Excerpt: Največja glasbena založba sklenila dogovor s podjetjem generativne umetne inteligence Ključne besede: Poravnava, Generativna umetna inteligenca, Avtorske pravice, Udio, Universal Music Group Največja glasbena založba na svetu, Universal Music Group, je umaknila tožbo proti podjetju generativne umetne inteligence Udio in napovedala skupno sodelovanje pri razvoju novih kreativnih storitev. Universal Music Group je sporočil, da je umaknil tožbo proti podjetju Udio, katerega program generira glasbo...

#### Rank 4: NOT RELEVANT

- Title: Umetna inteligenca: od zabave do zlorabe
- Decision: not_relevant
- Rationale: General AI abuse article, not mainly laws.
- Category/date: znanost-in-tehnologija / 2024-04-12T07:35:34
- URL: https://www.rtvslo.si/znanost-in-tehnologija/umetna-inteligenca-od-zabave-do-zlorabe/704734
- FAISS rank/score: 4 / 0.8466
- Reranker score: n/a
- Keywords: umetna inteligenca, deepfake, zloraba, AI, globoki ponaredki, deepfakes, generativna umetna inteligenca, podobe, avdio, videoposnetki, papež, Taylor Swift, Donald Trump, Joe Biden, nevronske mreže, splet, laž, računalništvo, tehnologija, socialna omrežja, dezinformacije, umetno ustvarjanje
- Excerpt: Umetna inteligenca: od zabave do zlorabe Ključne besede: umetna inteligenca, deepfake, zloraba, AI, globoki ponaredki, deepfakes, generativna umetna inteligenca, podobe, avdio, videoposnetki, papež, Taylor Swift, Donald Trump, Joe Biden, nevronske mreže, splet, laž, računalništvo, tehnologija, socialna omrežja, dezinformacije, umetno ustvarjanje Priča smo izjemnemu vzponu umetno generiranih podob ter avdio- in videoposnetkov. Kaj so globoki ponaredki in kako bi lahko umetna inteligenca vplivala...

#### Rank 5: RELEVANT

- Title: ZPS: Umetna inteligenca prinaša tudi negativne posledice – kršenje zasebnosti in osebne integritete
- Decision: relevant
- Rationale: Generative AI rights/legislation/regulation result.
- Category/date: gospodarstvo / 2023-06-20T13:58:03
- URL: https://www.rtvslo.si/gospodarstvo/zps-umetna-inteligenca-prinasa-tudi-negativne-posledice-krsenje-zasebnosti-in-osebne-integritete/672448
- FAISS rank/score: 5 / 0.8465
- Reranker score: n/a
- Keywords: Generativna umetna inteligenca, ZPS, Chat GPT, umetna inteligenca, potrošniki, tehnologija, aplikacija, pravice, zaupanje, varnost, kršenje zasebnosti, internet, digitalna politika, zakonodaja, Evropska unija, regulativa, ozaveščanje, opolnomočenje, lobiranje
- Excerpt: ZPS: Umetna inteligenca prinaša tudi negativne posledice – kršenje zasebnosti in osebne integritete Ključne besede: Generativna umetna inteligenca, ZPS, Chat GPT, umetna inteligenca, potrošniki, tehnologija, aplikacija, pravice, zaupanje, varnost, kršenje zasebnosti, internet, digitalna politika, zakonodaja, Evropska unija, regulativa, ozaveščanje, opolnomočenje, lobiranje V zadnjih mesecih je prišlo do bliskovite rasti ponudbe storitev, ki jih poganja generativna umetna inteligenca, ta pa ogrož...


### 3. Cene kart na nogometnem svetovnem prvenstvu

Precision@5: 3/5 = 0.60

#### Rank 1: RELEVANT

- Title: Ogromno povpraševanje za nogometni spektakel leta
- Decision: relevant
- Rationale: World Cup ticket demand/sales result.
- Category/date: sport / 2026-01-15T16:54:35
- URL: https://www.rtvslo.si/sport/nogomet/svetovno-prvenstvo-v-nogometu/ogromno-povprasevanje-za-nogometni-spektakel-leta/770262
- FAISS rank/score: 1 / 0.8636
- Reranker score: n/a
- Keywords: Fifa, Navijači, Prodaja vstopnic, Nogometni dogodek
- Excerpt: Ogromno povpraševanje za nogometni spektakel leta Ključne besede: Fifa, Navijači, Prodaja vstopnic, Nogometni dogodek V zadnjem delu prodaje je mednarodna nogometna zveza (Fifa) prejela več kot pol milijarde zahtevkov za vstopnice za ogled tekem letošnjega svetovnega prvenstva, ki bo poleti potekalo v ZDA, Kanadi in Mehiki. Prodaja vstopnic se je začela 11. decembra in je trajala do 13. januarja. Prvič so bile naprodaj posamezne vstopnice za določene tekme. Navijači bodo o morebitnem uspehu v na...

#### Rank 2: RELEVANT

- Title: Infantino zagovarja visoke cene vstopnic in pravi, da bodo ves denar vložili spet v nogomet
- Decision: relevant
- Rationale: Direct World Cup ticket price result.
- Category/date: sport / 2025-12-30T08:47:57
- URL: https://www.rtvslo.si/sport/nogomet/infantino-zagovarja-visoke-cene-vstopnic-in-pravi-da-bodo-ves-denar-vlozili-spet-v-nogomet/768669
- FAISS rank/score: 2 / 0.8611
- Reranker score: n/a
- Keywords: Gianni Infantino, Fifa, SP, vstopnice
- Excerpt: Infantino zagovarja visoke cene vstopnic in pravi, da bodo ves denar vložili spet v nogomet Ključne besede: Gianni Infantino, Fifa, SP, vstopnice Predsednik Mednarodne nogometne zveze Fife Gianni Infantino zagovarja visoke cene vstopnic za prihajajoče svetovno prvenstvo. Infantino je dejal, da cene vstopnic zgolj odražajo trenutno povpraševanje po njih. Združenje nogometnih navijačev (FSA) je od začetka prodaje vstopnic za tekmovanje, ki bo med 11. junijem in 19. julijem prihodnje leto potekalo...

#### Rank 3: RELEVANT

- Title: Tožba proti Fifi zaradi visokih cen vstopnic na SP 2026
- Decision: relevant
- Rationale: Direct World Cup ticket price lawsuit.
- Category/date: sport / 2026-03-24T11:22:40
- URL: https://www.rtvslo.si/sport/nogomet/tozba-proti-fifi-zaradi-visokih-cen-vstopnic-na-sp-2026/777332
- FAISS rank/score: 3 / 0.8608
- Reranker score: n/a
- Keywords: vstopnice, cene, svetovno prvenstvo, nogomet
- Excerpt: Tožba proti Fifi zaradi visokih cen vstopnic na SP 2026 Ključne besede: vstopnice, cene, svetovno prvenstvo, nogomet Združenje nogometnih navijačev Evrope (FSE) je pri Evropski komisiji vložilo tožbo proti Mednarodni nogometni zvezi (Fifa) zaradi previsokih cen vstopnic na letošnjem svetovnem prvenstvu, ki bo v ZDA, Kanadi in Mehiki. "Fifa ima monopol nad prodajo vstopnic za svetovno prvenstvo 2026 in to moč je izkoristila za vsiljevanje pogojev nogometnim privržencem, ki v konkurenčnem tržnem o...

#### Rank 4: NOT RELEVANT

- Title: Zasoljene cene vstopnic za slovenske tekme v Zagrebu
- Decision: not_relevant
- Rationale: Handball World Cup tickets, not football World Cup.
- Category/date: sport / 2025-01-13T15:29:38
- URL: https://www.rtvslo.si/sport/rokomet/sp-v-rokometu-2025/zasoljene-cene-vstopnic-za-slovenske-tekme-v-zagrebu/733223
- FAISS rank/score: 4 / 0.8465
- Reranker score: n/a
- Keywords: Cene, Slovenija, Svetovno prvenstvo, Zagreb, Vstopnice
- Excerpt: Zasoljene cene vstopnic za slovenske tekme v Zagrebu Ključne besede: Cene, Slovenija, Svetovno prvenstvo, Zagreb, Vstopnice Slovenski rokometaši bodo skupinski del svetovnega prvenstva ter morebitna četrtfinale in polfinale odigrali v Zagrebu. Pričakuje se veliko slovenskih navijačev, a vstopnice nikakor niso poceni. Še več, zagrebška Arena bo imela v prvem delu najdražje vstopnice, dražje tudi od tistih na Danskem in Norveškem, ki sta soorganizatorici svetovnega prvenstva. Slovenija se bo v prv...

#### Rank 5: NOT RELEVANT

- Title: Nova navijaška evforija? Čarterski polet na Dansko razprodan v manj kot enem dnevu.
- Decision: not_relevant
- Rationale: Fan flight/travel, not ticket prices.
- Category/date: zabava-in-slog / 2023-11-15T14:56:21
- URL: https://www.rtvslo.si/zabava-in-slog/popkultura/druzabno/nova-navijaska-evforija-carterski-polet-na-dansko-razprodan-v-manj-kot-enem-dnevu/688266
- FAISS rank/score: 5 / 0.8445
- Reranker score: n/a
- Keywords: Evropsko prvenstvo, Slovenska nogometna izbrana vrsta, Danska, Čarterski polet, Navijaška evforija, nogomet, navijači, evforija, tekma, Slovenija, Finska, Kazahstan, navijaška skupina, organizacija, turneja, Nemčija, stadion, srečanje, potovalna agencija, Kompas, Ljubljana, cena.
- Excerpt: Nova navijaška evforija? Čarterski polet na Dansko razprodan v manj kot enem dnevu. Ključne besede: Evropsko prvenstvo, Slovenska nogometna izbrana vrsta, Danska, Čarterski polet, Navijaška evforija, nogomet, navijači, evforija, tekma, Slovenija, Finska, Kazahstan, navijaška skupina, organizacija, turneja, Nemčija, stadion, srečanje, potovalna agencija, Kompas, Ljubljana, cena. Se v Sloveniji že začenja nova nogometna navijaška evforija? Po nedavni razprodani tekmi Slovenije in Finske v Stožicah...


### 4. Tožba slovenskih avtoprevoznikov

Precision@5: 2/5 = 0.40

#### Rank 1: RELEVANT

- Title: Avtoprevozniki na zboru državi postavili zahteve, sicer lahko sledi zaprtje najpomembnejših cest
- Decision: relevant
- Rationale: Hauliers and demands; largely related.
- Category/date: gospodarstvo / 2025-10-18T15:03:41
- URL: https://www.rtvslo.si/gospodarstvo/avtoprevozniki-na-zboru-drzavi-postavili-zahteve-sicer-lahko-sledi-zaprtje-najpomembnejsih-cest/761263
- FAISS rank/score: 1 / 0.8628
- Reranker score: n/a
- Keywords: Digitalizacija, Kadrovska kriza, Zeleni prehod, Zaprtje cest, Avtoprevozniki
- Excerpt: Avtoprevozniki na zboru državi postavili zahteve, sicer lahko sledi zaprtje najpomembnejših cest Ključne besede: Digitalizacija, Kadrovska kriza, Zeleni prehod, Zaprtje cest, Avtoprevozniki Avtoprevozniki so na zboru v Celju na vlado naslovili zahteve, za katere pričakujejo, da jih izpolni do decembra oz. do marca 2026. V nasprotnem bodo decembra pripravili protest, za marec pa so napovedali zaprtje pomembnih cest v Sloveniji. Zbor sta organizirala sekcija za promet pri Obrtno-podjetniški zborni...

#### Rank 2: NOT RELEVANT

- Title: V pravni boj proti Bookingu tudi slovenski hoteli
- Decision: not_relevant
- Rationale: Hotels vs Booking legal case, not hauliers.
- Category/date: zabava-in-slog / 2025-08-12T12:05:54
- URL: https://www.rtvslo.si/zabava-in-slog/ture-avanture/v-pravni-boj-proti-bookingu-tudi-slovenski-hoteli/754468
- FAISS rank/score: 2 / 0.8614
- Reranker score: n/a
- Keywords: Odškodnina, Slovenski hoteli, Množična tožba, Booking
- Excerpt: V pravni boj proti Bookingu tudi slovenski hoteli Ključne besede: Odškodnina, Slovenski hoteli, Množična tožba, Booking V množični tožbi proti platformi za rezervacijo nastanitev Booking, v kateri ji več kot 10.000 evropskih hotelov očita, da je preprečevala ponudbo nižjih cen, sodelujejo tudi slovenski hotelirji. Koliko se jih je pridružilo pravni bitki, niso razkrili. Kot smo že poročali, se je več kot 10.000 evropskih hotelov združilo v tožbi proti platformi za rezervacijo nastanitev Booking....

#### Rank 3: RELEVANT

- Title: Škoda zaradi blokad avtoprevoznikov iz nečlanic EU-ja na Balkanu že večstomilijonska
- Decision: relevant
- Rationale: Haulier blockades/transport dispute; largely related.
- Category/date: gospodarstvo / 2026-01-28T14:33:49
- URL: https://www.rtvslo.si/gospodarstvo/skoda-zaradi-blokad-avtoprevoznikov-iz-neclanic-eu-ja-na-balkanu-ze-vecstomilijonska/771542
- FAISS rank/score: 3 / 0.8538
- Reranker score: n/a
- Keywords: Gospodarske posledice, Mejni prehodi, Finančna škoda, EU-ja, Blokade avtoprevoznikov
- Excerpt: Škoda zaradi blokad avtoprevoznikov iz nečlanic EU-ja na Balkanu že večstomilijonska Ključne besede: Gospodarske posledice, Mejni prehodi, Finančna škoda, EU-ja, Blokade avtoprevoznikov Avtoprevozniki iz štirih držav Zahodnega Balkana že tretji dan blokirajo terminale za tovorni promet na mejnih prehodih proti schengenskemu območju zaradi nezadovoljstva ob uvedbi novega sistema nadzora vstopa in izstopa (EES). Blokade terminalov za tovorni promet na mejnih prehodih izvajajo avtoprevozniki iz Srb...

#### Rank 4: NOT RELEVANT

- Title: Vozniki avtobusov opozarjajo na nevzdržne razmere. Takoj bi potrebovali dodatnih 860 voznikov.
- Decision: not_relevant
- Rationale: Bus drivers, not hauliers lawsuit.
- Category/date: gospodarstvo / 2024-09-11T13:35:08
- URL: https://www.rtvslo.si/gospodarstvo/vozniki-avtobusov-opozarjajo-na-nevzdrzne-razmere-takoj-bi-potrebovali-dodatnih-860-voznikov/720704
- FAISS rank/score: 4 / 0.8523
- Reranker score: n/a
- Keywords: Sindikat voznikov, Delovne razmere, Pomanjkanje kadrov, Vozniki avtobusov
- Excerpt: Vozniki avtobusov opozarjajo na nevzdržne razmere. Takoj bi potrebovali dodatnih 860 voznikov. Ključne besede: Sindikat voznikov, Delovne razmere, Pomanjkanje kadrov, Vozniki avtobusov Predstavniki sindikata voznikov avtobusov so opozorili na nevzdržno stanje v dejavnosti cestnega potniškega prometa. Menijo, da je tik pred tem, da se ustavi. Voznikov avtobusov je namreč zaradi preobremenjenosti in slabih delovnih razmer vse manj. Predsednik Sindikata voznikov avtobusov Slovenije Dušan Vidovič je...

#### Rank 5: NOT RELEVANT

- Title: Številni vozniki tožijo Renault zaradi težav, oglasili so se tudi slovenski lastniki
- Decision: not_relevant
- Rationale: Renault owners lawsuit, not hauliers.
- Category/date: zabava-in-slog / 2023-07-09T21:45:52
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/stevilni-vozniki-tozijo-renault-zaradi-tezav-oglasili-so-se-tudi-slovenski-lastniki/674591
- FAISS rank/score: 5 / 0.8513
- Reranker score: n/a
- Keywords: Renault, tožba, težave z motorjem, 1.2 TCe, težave, motor, avtomobil, 1,2-litrski, lastniki, Nissan, Dacia, vozniki, olje, pregrevanje, odpoklic, garancija, servis, odškodnina, sodišče, napaka, rešitev, kolektivna tožba
- Excerpt: Številni vozniki tožijo Renault zaradi težav, oglasili so se tudi slovenski lastniki Ključne besede: Renault, tožba, težave z motorjem, 1.2 TCe, težave, motor, avtomobil, 1,2-litrski, lastniki, Nissan, Dacia, vozniki, olje, pregrevanje, odpoklic, garancija, servis, odškodnina, sodišče, napaka, rešitev, kolektivna tožba Pred mesecem dni je skoraj 1800 francoskih lastnikov avtomobilov vložilo tožbo proti podjetju Renault zaradi težav z 1,2-litrskim motorjem, ki je bil med letoma 2012 in 2016 vgraj...


### 5. Vojna Zvezd v Sloveniji

Precision@5: 1/5 = 0.20

#### Rank 1: RELEVANT

- Title: Po svetu praznujejo dan Vojne zvezd
- Decision: relevant
- Rationale: Direct Star Wars result.
- Category/date: zabava-in-slog / 2023-05-04T17:09:00
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/po-svetu-praznujejo-dan-vojne-zvezd/667027
- FAISS rank/score: 1 / 0.8381
- Reranker score: n/a
- Keywords: Vojna zvezd, Star Wars, May the fourth be with you, franšiza, filmi, kultura, popularni, datum, praznovanje, Luka Skywalker, George Lucas, animirani, igralci, televizijske serije, igrače, videoigre, Lego, BioWare, Slovenija, otroci, liki, imena
- Excerpt: Po svetu praznujejo dan Vojne zvezd Ključne besede: Vojna zvezd, Star Wars, May the fourth be with you, franšiza, filmi, kultura, popularni, datum, praznovanje, Luka Skywalker, George Lucas, animirani, igralci, televizijske serije, igrače, videoigre, Lego, BioWare, Slovenija, otroci, liki, imena Ljubitelji ene največjih znanstvenofantastičnih franšiz na svetu že od leta 2011 četrtega maja praznujejo dan Vojne zvezd. Kultni filmi so vse od prvenca leta 1977 premikali meje žanra in se zasidrali gl...

#### Rank 2: NOT RELEVANT

- Title: Astronavti v slovenski jami, vesoljski Brad Pitt in najmasivnejša nevtronska zvezda
- Decision: not_relevant
- Rationale: Space/science result, not Star Wars.
- Category/date: znanost-in-tehnologija / 2019-09-21T18:55:56
- URL: https://www.rtvslo.si/znanost-in-tehnologija/astronavti-v-slovenski-jami-vesoljski-brad-pitt-in-najmasivnejsa-nevtronska-zvezda/500126
- FAISS rank/score: 2 / 0.8310
- Reranker score: n/a
- Keywords: Vesolje, Vesoljski tednik, Vesoljski tednik 2019, Vesoljski tednik september 2019, neutrona zvezda, delci, astronavti, Slovenija, jamarstvo, trening, življenje, voda, mikroplastika, znanost, spretnosti, varnost, vesoljski program, komunikacija, eksperimenti, skupinsko delo, problemi, izolacija
- Excerpt: Astronavti v slovenski jami, vesoljski Brad Pitt in najmasivnejša nevtronska zvezda Ključne besede: Vesolje, Vesoljski tednik, Vesoljski tednik 2019, Vesoljski tednik september 2019, neutrona zvezda, delci, astronavti, Slovenija, jamarstvo, trening, življenje, voda, mikroplastika, znanost, spretnosti, varnost, vesoljski program, komunikacija, eksperimenti, skupinsko delo, problemi, izolacija Sveže iz vesolja: odkrili so najmasivnejšo (znano) nevtronsko zvezdo, s 70-metrsko napravo so merili drug...

#### Rank 3: NOT RELEVANT

- Title: Slovenski vesoljski sektor se predstavlja v ZDA
- Decision: not_relevant
- Rationale: Slovenian space sector, not Star Wars.
- Category/date: slovenija / 2025-04-10T17:41:41
- URL: https://www.rtvslo.si/slovenija/preberite-tudi/slovenski-vesoljski-sektor-se-predstavlja-v-zda/742362
- FAISS rank/score: 3 / 0.8301
- Reranker score: n/a
- Keywords: Ameriški astronavt, Vesoljska industrija, Mednarodno sodelovanje, Space Symposium, Slovenski vesoljski sektor
- Excerpt: Slovenski vesoljski sektor se predstavlja v ZDA Ključne besede: Ameriški astronavt, Vesoljska industrija, Mednarodno sodelovanje, Space Symposium, Slovenski vesoljski sektor Slovenska vesoljska pisarna te dni v sodelovanju z Javno agencijo Spirit Slovenija, ministrstvom za obrambo in slovenskim veleposlaništvom v Washingtonu organizira obisk podjetij s področja vesoljske industrije v ZDA. Uspešno so se predstavila na srečanju Space Symposium v Colorado Springsu, obisk nadaljujejo v Denverju. Gre...

#### Rank 4: NOT RELEVANT

- Title: Roskozmos v vojni, fosfor v Enkeladu in slovenska vesoljska strategija
- Decision: not_relevant
- Rationale: Space/war/strategy false match, not Star Wars.
- Category/date: znanost-in-tehnologija / 2023-06-24T15:16:18
- URL: https://www.rtvslo.si/znanost-in-tehnologija/roskozmos-v-vojni-fosfor-v-enkeladu-in-slovenska-vesoljska-strategija/665675
- FAISS rank/score: 4 / 0.8284
- Reranker score: n/a
- Keywords: Vesolje, Vesoljski tednik, Raziskovanje vesolja, vesoljska tehnologija, raketa, izstrelitev, satelit, orbita, vesoljska agencija, vesoljski sektor, Evropska vesoljska agencija, SpaceX, falcon 9, tirnica, Cape Canaveral, Starlink, posnetek izstrelitve, United Launch Alliance, Delta IV Heavy, eksoplanet, teleskop James Webb, Amerika
- Excerpt: Roskozmos v vojni, fosfor v Enkeladu in slovenska vesoljska strategija Ključne besede: Vesolje, Vesoljski tednik, Raziskovanje vesolja, vesoljska tehnologija, raketa, izstrelitev, satelit, orbita, vesoljska agencija, vesoljski sektor, Evropska vesoljska agencija, SpaceX, falcon 9, tirnica, Cape Canaveral, Starlink, posnetek izstrelitve, United Launch Alliance, Delta IV Heavy, eksoplanet, teleskop James Webb, Amerika Ruska vesoljska korporacija sestavlja vojaško enoto za boj v Ukrajini, mogočna a...

#### Rank 5: NOT RELEVANT

- Title: Vesolje je tukaj ali Veliki slovenski pok: nova serija o slovenskih vesoljskih projektih
- Decision: not_relevant
- Rationale: Slovenian space projects, not Star Wars.
- Category/date: kultura / 2024-12-26T18:54:43
- URL: https://www.rtvslo.si/kultura/film-in-tv/vesolje-je-tukaj-ali-veliki-slovenski-pok-nova-serija-o-slovenskih-vesoljskih-projektih/731372
- FAISS rank/score: 5 / 0.8267
- Reranker score: n/a
- Keywords: Vesolje, Veliki slovenski pok, Esa
- Excerpt: Vesolje je tukaj ali Veliki slovenski pok: nova serija o slovenskih vesoljskih projektih Ključne besede: Vesolje, Veliki slovenski pok, Esa Mala Slovenija se lahko pohvali z dinamičnim vesoljskim sektorjem. Naša podjetja in znanstveniki so udeleženi pri najodmevnejših mednarodnih misijah. Predstavila jih bo nova serija Veliki slovenski pok. Je raziskovanje vesolja koristno? Kaj sploh ima Slovenija pri tem? In kakšno vlogo pri tem igra Evropska vesoljska agencija, katere polnopravni člani ravnoka...


### 6. Ogromni zastoji na Slovenskih cestah

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Zastoji precej preizkušali živce voznikov
- Decision: relevant
- Rationale: Direct traffic jams result.
- Category/date: slovenija / 2025-06-19T07:24:19
- URL: https://www.rtvslo.si/slovenija/za-pot-od-ljubljane-do-kopra-zaradi-zastojev-vozniki-potrebujejo-poltretjo-uro/749447
- FAISS rank/score: 1 / 0.8670
- Reranker score: n/a
- Keywords: Zastoji, Telovo, Avtoceste, Promet
- Excerpt: Zastoji precej preizkušali živce voznikov Ključne besede: Zastoji, Telovo, Avtoceste, Promet Zaradi katoliškega praznika telovo, ki je v Avstriji, večjem delu Nemčije in na Hrvaškem dela prost dan, na Darsu opozarjajo na povečan promet od severne proti južni meji. Zastoji so na več odsekih, gneča je tudi na ljubljanski obvoznici. Direkcija za avtoceste je že v tedenski napovedi obremenjenosti slovenskih avtocest opozorila, da bo promet po pričakovanjih v četrtek (torej, danes) zelo povečan zlast...

#### Rank 2: RELEVANT

- Title: Številni zastoji na cestah in avtocestah
- Decision: relevant
- Rationale: Direct traffic jams on roads/highways.
- Category/date: slovenija / 2025-06-05T09:22:05
- URL: https://www.rtvslo.si/slovenija/stevilni-zastoji-na-cestah-in-avtocestah/748004
- FAISS rank/score: 2 / 0.8669
- Reranker score: n/a
- Keywords: Reševalni pas, Prometno informacijski center, Zastoji, Gorenska avtocesta, Nesreča
- Excerpt: Številni zastoji na cestah in avtocestah Ključne besede: Reševalni pas, Prometno informacijski center, Zastoji, Gorenska avtocesta, Nesreča Na gorenjski avtocesti med Brnikom in Vodicami proti Ljubljani so posledice prometne nesreče odstranjene. Zastoji so na štajerski avtocesti med Dramljami in predorom Pletovarje proti Mariboru, zamuda je 10 - 15 minut inna primorski avtocesti med Nanosom in Gabrkom proti Kopru. Trenutno so zastoji tudi na cestah Medvode - Ljubljana, Dragonja - Šmarje in Lesce...

#### Rank 3: RELEVANT

- Title: Na avtocestah nastajajo zastoji, pot od Razdrtega do Ljubljane se podaljša za 45 minut
- Decision: relevant
- Rationale: Direct highway traffic jams.
- Category/date: slovenija / 2023-07-29T12:30:06
- URL: https://www.rtvslo.si/slovenija/na-avtocestah-nastajajo-zastoji-pot-od-razdrtega-do-ljubljane-se-podaljsa-za-45-minut/676502
- FAISS rank/score: 3 / 0.8632
- Reranker score: n/a
- Keywords: Potovalni čas, Gneča na cestah, Zastoji na avtocestah, promet, zastoji, avtocesta, hitra cesta, ceste, prometnoinformacijski center, zamuda, gneča, zapora, Jesenice, Avstrija, Postojna, Logatec, Vrhnika, Izola, Strunjan, Škofije, Koper, Karavanke, Štajerska
- Excerpt: Na avtocestah nastajajo zastoji, pot od Razdrtega do Ljubljane se podaljša za 45 minut Ključne besede: Potovalni čas, Gneča na cestah, Zastoji na avtocestah, promet, zastoji, avtocesta, hitra cesta, ceste, prometnoinformacijski center, zamuda, gneča, zapora, Jesenice, Avstrija, Postojna, Logatec, Vrhnika, Izola, Strunjan, Škofije, Koper, Karavanke, Štajerska Promet na slovenskih cestah je zgoščen. Zastoji tako nastajajo na primorski avtocesti v obe smeri in na gorenjski avtocesti v smeri Karavan...

#### Rank 4: RELEVANT

- Title: Pred Karavankami in Šentiljem dolgi zastoji
- Decision: relevant
- Rationale: Direct traffic jams result.
- Category/date: slovenija / 2024-08-17T07:57:05
- URL: https://www.rtvslo.si/slovenija/pred-karavankami-in-sentiljem-dolgi-zastoji/718223
- FAISS rank/score: 4 / 0.8621
- Reranker score: n/a
- Keywords: Reševalni pas, Varna vožnja, Preventivna akcija, Vročinski val, Prometna varnost
- Excerpt: Pred Karavankami in Šentiljem dolgi zastoji Ključne besede: Reševalni pas, Varna vožnja, Preventivna akcija, Vročinski val, Prometna varnost Na slovenskih cestah je tudi ta konec tedna zgoščen promet, gneča je tako v smeri proti morju kot proti notranjosti. Pred predorom Karavanke je kolona dolga 11 kilometrov, predor občasno zapirajo. Na primorski avtocesti je promet upočasnjen v smeri proti Primorski, pa tudi proti Ljubljani, in sicer na posameznih odsekih med Razdrtim in Brezovico. Zastoji so...

#### Rank 5: RELEVANT

- Title: Pred Karavankami in Šentiljem dolgi zastoji
- Decision: relevant
- Rationale: Duplicate direct traffic jams result.
- Category/date: slovenija / 2024-08-17T07:57:05
- URL: https://www.rtvslo.si/slovenija/pred-karavankami-11-kilometrski-zastoj-gneca-tudi-pred-prehodoma-sentilj-in-ljubelj/718223
- FAISS rank/score: 5 / 0.8621
- Reranker score: n/a
- Keywords: Reševalni pas, Varna vožnja, Preventivna akcija, Vročinski val, Prometna varnost
- Excerpt: Pred Karavankami in Šentiljem dolgi zastoji Ključne besede: Reševalni pas, Varna vožnja, Preventivna akcija, Vročinski val, Prometna varnost Na slovenskih cestah je tudi ta konec tedna zgoščen promet, gneča je tako v smeri proti morju kot proti notranjosti. Pred predorom Karavanke je kolona dolga 11 kilometrov, predor občasno zapirajo. Na primorski avtocesti je promet upočasnjen v smeri proti Primorski, pa tudi proti Ljubljani, in sicer na posameznih odsekih med Razdrtim in Brezovico. Zastoji so...


### 7. Višanje temperatur

Precision@5: 4/5 = 0.80

#### Rank 1: NOT RELEVANT

- Title: Povpraševanje po toplotnih kamerah strmo narašča
- Decision: not_relevant
- Rationale: Thermal camera demand, not rising temperatures.
- Category/date: znanost-in-tehnologija / 2020-03-25T14:01:05
- URL: https://www.rtvslo.si/znanost-in-tehnologija/povprasevanje-po-toplotnih-kamerah-strmo-narasca/518329
- FAISS rank/score: 1 / 0.8252
- Reranker score: n/a
- Keywords: Termalna kamera, Toplotna kamera, Infrardeča kamera, Termovizijska kamera, termovizijske kamere, merjenje temperature, infrardeče valovanje, pregrevanje, vzdrževanje, zdravstvo, imunski sistem, koronavirus, pandemija, dobavne poti, brezstičnost, industrija, gradbeništvo, elektroindustrija, gasilci, meteorologi, astronomi, bolezni, sars, prašičja gripa, umerjanje.
- Excerpt: Povpraševanje po toplotnih kamerah strmo narašča Ključne besede: Termalna kamera, Toplotna kamera, Infrardeča kamera, Termovizijska kamera, termovizijske kamere, merjenje temperature, infrardeče valovanje, pregrevanje, vzdrževanje, zdravstvo, imunski sistem, koronavirus, pandemija, dobavne poti, brezstičnost, industrija, gradbeništvo, elektroindustrija, gasilci, meteorologi, astronomi, bolezni, sars, prašičja gripa, umerjanje. Med širjenjem novega koronavirusa narašča tudi povpraševanje po termo...

#### Rank 2: RELEVANT

- Title: Ob dvigu temperature lahko pričakujemo več komarjev
- Decision: relevant
- Rationale: Effect of temperature rise.
- Category/date: slovenija / 2025-08-07T13:24:43
- URL: https://www.rtvslo.si/slovenija/ob-dvigu-temperature-lahko-pricakujemo-vec-komarjev/754077
- FAISS rank/score: 2 / 0.8248
- Reranker score: n/a
- Keywords: Repelenti, Preventivni ukrepi, Komarji
- Excerpt: Ob dvigu temperature lahko pričakujemo več komarjev Ključne besede: Repelenti, Preventivni ukrepi, Komarji Začetek poletja je bil sušen, zato je bilo komarjev manj. Zadnje deževje in višja temperatura bosta vplivala na njihovo številčnost. Odstranjevanje vode iz okolja in pravilno odlaganje odpadkov ter urejanje zelenih zmanjšujejo možnosti za razmnoževanje. Za razvoj komarjev sta ključni stoječa voda in zadostna toplota. Vodja kustodiata za nevretenčarje v Prirodoslovnem muzeju Slovenije Tea Kn...

#### Rank 3: RELEVANT

- Title: Sindikati: Ob vročinskem valu morajo delodajalci zmanjšati intenzivnost dela
- Decision: relevant
- Rationale: Heat wave/high temperatures.
- Category/date: okolje / 2022-06-25T10:45:29
- URL: https://www.rtvslo.si/okolje/sindikati-ob-vrocinskem-valu-morajo-delodajalci-zmanjsati-intenzivnost-dela/632188
- FAISS rank/score: 3 / 0.8208
- Reranker score: n/a
- Keywords: vreme, vročinski val, obremenitve, delo, temperatura, delovno okolje, sindikati, varnost, zdravje, produktivnost, delavci, kronične bolezni, vročina, gostinstvo, turizem, trgovina, gradbeništvo, komunala, pisarniški prostori, proizvodne hale, klimatska naprava, prezračevanje, zračenje
- Excerpt: Sindikati: Ob vročinskem valu morajo delodajalci zmanjšati intenzivnost dela Ključne besede: vreme, vročinski val, obremenitve, delo, temperatura, delovno okolje, sindikati, varnost, zdravje, produktivnost, delavci, kronične bolezni, vročina, gostinstvo, turizem, trgovina, gradbeništvo, komunala, pisarniški prostori, proizvodne hale, klimatska naprava, prezračevanje, zračenje Vremenoslovci napovedujejo, da bo prihodnji teden vse bolj vroče, s temperaturo tudi okoli 35 stopinj. Sindikati opozarja...

#### Rank 4: RELEVANT

- Title: Na Balkanu opozorila zaradi visokih temperatur. V BiH-u do 39 stopinj Celzija, v Srbiji do 40.
- Decision: relevant
- Rationale: Record/high temperatures.
- Category/date: okolje / 2025-07-21T11:37:08
- URL: https://www.rtvslo.si/okolje/na-balkanu-opozorila-zaradi-visokih-temperatur-v-bih-u-do-39-stopinj-celzija-v-srbiji-do-40/752529
- FAISS rank/score: 4 / 0.8183
- Reranker score: n/a
- Keywords: Vročinski val, Srbija, BiH, Hrvaška, Grčija
- Excerpt: Na Balkanu opozorila zaradi visokih temperatur. V BiH-u do 39 stopinj Celzija, v Srbiji do 40. Ključne besede: Vročinski val, Srbija, BiH, Hrvaška, Grčija Z Balkana poročajo o vremenskih opozorilih zaradi visokih temperatur. Za večji del BiH-a zaradi temperatur do 39 stopinj Celzija velja oranžni alarm. O novem vročinskem valu poročajo v Grčiji in Srbiji, kjer so razglasili rdeči alarm. Hidrometeorološki zavod Federacije BiH-a danes najvišje temperature – do 39 stopinj Celzija – pričakuje na jug...

#### Rank 5: RELEVANT

- Title: Na turnirjih ATP bodo uvedli pravilo o ekstremni vročini
- Decision: relevant
- Rationale: Extreme heat rule; high-temperature context.
- Category/date: sport / 2025-12-16T10:05:17
- URL: https://www.rtvslo.si/sport/tenis/na-turnirjih-atp-bodo-uvedli-pravilo-o-ekstremni-vrocini/767387
- FAISS rank/score: 5 / 0.8183
- Reranker score: n/a
- Keywords: ATP, tenis, vročina
- Excerpt: Na turnirjih ATP bodo uvedli pravilo o ekstremni vročini Ključne besede: ATP, tenis, vročina Vodilni predstavniki združenja profesionalnih igralcev tenisa ATP so napovedali uvedbo pravila o ekstremni vročini, ki bo začelo veljati leta 2026. V združenju ATP so se za uvedbo pravila odločili zaradi številnih kritik igralcev, povezanih z nevzdržnimi razmerami za igro na nekaterih turnirjih, poroča AFP. Pravilo že velja na ženski turneji WTA in na Odprtem prvenstvu v Avstraliji. "Ali želite, da igral...


### 8. Višanje cen nepremičnin v Sloveniji

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Cene stanovanjskih nepremičnin od leta 2022 zrasle za četrtino, v zadnjih 10 letih so se podvojile
- Decision: relevant
- Rationale: Direct real-estate price rise.
- Category/date: gospodarstvo / 2026-01-05T09:54:52
- URL: https://www.rtvslo.si/gospodarstvo/cene-stanovanjskih-nepremicnin-od-leta-2022-zrasle-za-cetrtino-v-zadnjih-10-letih-so-se-podvojile/769090
- FAISS rank/score: 1 / 0.8753
- Reranker score: n/a
- Keywords: nepremičnine, trg, cene, stanovanja
- Excerpt: Cene stanovanjskih nepremičnin od leta 2022 zrasle za četrtino, v zadnjih 10 letih so se podvojile Ključne besede: nepremičnine, trg, cene, stanovanja Cene stanovanj v Ljubljani dosegajo tudi do 8000 evrov na kvadratni meter, nepremičnine pa se še naprej dražijo. Ob tem se je lani nadaljevalo kopičenje praznih stanovanj, težava pa ostaja dolgotrajno pridobivanje gradbenih dovoljenj. Sredi lanskega leta je srednja vrednost novih stanovanjskih nepremičnin v Sloveniji prvič presegla 3000 evrov na k...

#### Rank 2: RELEVANT

- Title: Gurs: V Sloveniji lani prodanih manj hiš in stanovanj. Cene zrasle za devet oz. deset odstotkov.
- Decision: relevant
- Rationale: Direct Slovenian real-estate price rise.
- Category/date: gospodarstvo / 2025-04-15T06:31:30
- URL: https://www.rtvslo.si/gospodarstvo/gurs-v-sloveniji-lani-prodanih-manj-his-in-stanovanj-cene-zrasle-za-devet-oz-deset-odstotkov/742731
- FAISS rank/score: 2 / 0.8742
- Reranker score: n/a
- Keywords: Cene stanovanj, Nepremičninski trg, Gurs
- Excerpt: Gurs: V Sloveniji lani prodanih manj hiš in stanovanj. Cene zrasle za devet oz. deset odstotkov. Ključne besede: Cene stanovanj, Nepremičninski trg, Gurs Po podatkih Gursa je lani precej upadla prodaja vseh vrst nepremičnin. Na drugi strani pa so se denimo v Ljubljani cene stanovanj zvišale za kar 500 evrov/m2. "Povpraševanje še vedno močno presega ponudbo," pravi Boštjan Udovič iz GZS-ja. Geodetska uprava (Gurs) je na začetku aprila objavila poročilo o slovenskem nepremičninskem trgu za leto 20...

#### Rank 3: RELEVANT

- Title: Lani so se stanovanjske nepremičnine podražile najmanj v treh letih
- Decision: relevant
- Rationale: Direct residential real-estate price rise.
- Category/date: gospodarstvo / 2024-03-22T11:24:42
- URL: https://www.rtvslo.si/gospodarstvo/lani-so-se-stanovanjske-nepremicnine-podrazile-najmanj-v-treh-letih/702480
- FAISS rank/score: 3 / 0.8704
- Reranker score: n/a
- Keywords: Prodaja nepremičnin, Nove družinske hiše, Rabljena stanovanja, Rast cen, Cene stanovanjskih nepremičnin, nepremičnine, cene, stanovanja, rast, prodaja, trg, primerjava, Slovenija, Ljubljana, hiše, evro, četrtletje, podražitev, trend, novogradnje, statistika, Milijon, družinske hiše, Maribor
- Excerpt: Lani so se stanovanjske nepremičnine podražile najmanj v treh letih Ključne besede: Prodaja nepremičnin, Nove družinske hiše, Rabljena stanovanja, Rast cen, Cene stanovanjskih nepremičnin, nepremičnine, cene, stanovanja, rast, prodaja, trg, primerjava, Slovenija, Ljubljana, hiše, evro, četrtletje, podražitev, trend, novogradnje, statistika, Milijon, družinske hiše, Maribor Cene stanovanjskih nepremičnin so bile lani za 6,8 odstotka višje kot predlani, kar je najmanjša podražitev v zadnjih treh l...

#### Rank 4: RELEVANT

- Title: Stanovanjske nepremičnine se še dražijo
- Decision: relevant
- Rationale: Direct real-estate getting more expensive.
- Category/date: gospodarstvo / 2024-09-23T11:24:46
- URL: https://www.rtvslo.si/gospodarstvo/stanovanjske-nepremicnine-se-se-drazijo/721887
- FAISS rank/score: 4 / 0.8703
- Reranker score: n/a
- Keywords: Prodajna vrednost, Rabljena stanovanja, Nova stanovanja, Podražitev, Stanovanjske nepremičnine
- Excerpt: Stanovanjske nepremičnine se še dražijo Ključne besede: Prodajna vrednost, Rabljena stanovanja, Nova stanovanja, Podražitev, Stanovanjske nepremičnine Stanovanjske nepremičnine so se v drugem četrtletju podražile za 2,2 odstotka, v medletni primerjavi pa za 6,7 odstotka. Število prodaj stanovanjskih nepremičnin je bilo za petino nižje od povprečja prejšnjega leta, kažejo podatki Sursa. Nove stanovanjske nepremičnine so se po pocenitvi v letošnjem prvem četrtletju (za 7,6 odstotka) znova podražil...

#### Rank 5: RELEVANT

- Title: Prodaja nepremičnin upada, cene pa še naprej rastejo
- Decision: relevant
- Rationale: Direct real-estate prices rising.
- Category/date: gospodarstvo / 2024-12-23T15:25:02
- URL: https://www.rtvslo.si/gospodarstvo/prodaja-nepremicnin-upada-cene-pa-se-naprej-rastejo/731459
- FAISS rank/score: 5 / 0.8694
- Reranker score: n/a
- Keywords: nepremičnine, prodaja, cene
- Excerpt: Prodaja nepremičnin upada, cene pa še naprej rastejo Ključne besede: nepremičnine, prodaja, cene Prodaja stanovanjskih nepremičnin v Sloveniji upada. V tretjem četrtletju je bilo prodanih celo najmanj rabljenih nepremičnin v zadnjih 14 letih. Cene nepremičnin medtem še naprej rastejo, najbolj prav za rabljena stanovanja in hiše. Po izračunih Statističnega urada RS (Surs) je bilo v tretjem četrtletju letošnjega leta skupno prodnih 1737 stanovanjskih nepremičnin. To je 16 odstotkov manj kot v četr...


### 9. Rogljič in Pogačar na tekmi

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Roglič po 11. mestu: "Utrujen sem, Pogačar je res neverjeten"
- Decision: relevant
- Rationale: Direct Roglic/Pogacar result.
- Category/date: sport / 2025-09-28T15:24:12
- URL: https://www.rtvslo.si/sport/kolesarstvo/svetovno-prvenstvo-v-kolesarstvu/roglic-po-11-mestu-utrujen-sem-pogacar-je-res-neverjeten/759029
- FAISS rank/score: 1 / 0.8488
- Reranker score: n/a
- Keywords: Tadej Pogačar, Domen Novak, Matej Mohorič, odmevi
- Excerpt: Roglič po 11. mestu: "Utrujen sem, Pogačar je res neverjeten" Ključne besede: Tadej Pogačar, Domen Novak, Matej Mohorič, odmevi Tadej Pogačar je postal šele osmi kolesar, ki je ubranil naslov svetovnega prvaka v cestni vožnji. Lanski uspeh v Zürichu je ponovil in nadgradil z uspehom v Kigaliju. Do zdaj je bil le Peter Sagan tisti, ki je slavil trikrat zapored. Vsi kolesarji, ki so ubranili naslov: 1929 − Georges Ronsse (Belgija) 1957 − Rik Van Steenbergen (Belgija) 1961 − Rik Van Looy (Belgija)...

#### Rank 2: RELEVANT

- Title: Selektor Murn: Nimamo česa skrivati. Cilj je vsaj medalja na cestni dirki.
- Decision: relevant
- Rationale: Slovenian cycling road-race medal context.
- Category/date: sport / 2024-09-18T14:10:18
- URL: https://www.rtvslo.si/sport/kolesarstvo/svetovno-prvenstvo-v-kolesarstvu/selektor-murn-nimamo-cesa-skrivati-cilj-je-vsaj-medalja-na-cestni-dirki/721400
- FAISS rank/score: 2 / 0.8473
- Reranker score: n/a
- Keywords: kolesarstvo, SP v kolesarstvu, Jaka Primožič, Tadej Pogačar, Primož Roglič
- Excerpt: Selektor Murn: Nimamo česa skrivati. Cilj je vsaj medalja na cestni dirki. Ključne besede: kolesarstvo, SP v kolesarstvu, Jaka Primožič, Tadej Pogačar, Primož Roglič Slovenija na 97. svetovno prvenstvo v cestnem kolesarstvu odhaja kot favorizirana ekipa za osrednji dogodek – cestno dirko moške elite. Primož Roglič in Tadej Pogačar bosta skušala poskrbeti za še eno redkih manjkajočih lovorik – mavrično majico. V nedeljo se začenja letošnje, že 97. svetovno prvenstvo v cestnem kolesarstvu, ki ga m...

#### Rank 3: RELEVANT

- Title: Roglič v Andori dobil prestižno dirko 'pokra asov'
- Decision: relevant
- Rationale: Roglic race result; largely related.
- Category/date: sport / 2025-10-19T15:52:32
- URL: https://www.rtvslo.si/sport/kolesarstvo/roglic-v-andori-dobil-prestizno-dirko-pokra-asov/761326
- FAISS rank/score: 3 / 0.8473
- Reranker score: n/a
- Keywords: Primož Roglič, Tadej Pogačar, Jonas Vingegaard, Isaac del Toro
- Excerpt: Roglič v Andori dobil prestižno dirko 'pokra asov' Ključne besede: Primož Roglič, Tadej Pogačar, Jonas Vingegaard, Isaac del Toro Primož Roglič je zmagovalec dvodelne revijalne preizkušnje v Andori. Zasavec je bil dopoldne najhitrejši v gorskem kronometru, na mestnem kriteriju pa je bil drugi, kar je bilo dovolj za skupno zmago. Med štirimi tekmovalci je nastopal tudi Tadej Pogačar. Preizkušnja z imenom Andorra Cycling Masters je združila štiri zvezdnike kolesarstva. Ob Primožu Rogliču in Tadeju...

#### Rank 4: RELEVANT

- Title: Na Emiliji in Lombardiji prvo in drugo letošnje soočenje Pogačarja in Rogliča
- Decision: relevant
- Rationale: Direct Pogacar/Roglic race result.
- Category/date: sport / 2023-09-18T20:40:51
- URL: https://www.rtvslo.si/sport/kolesarstvo/na-emiliji-in-lombardiji-prvo-in-drugo-letosnje-soocenje-pogacarja-in-roglica/681833
- FAISS rank/score: 4 / 0.8470
- Reranker score: n/a
- Keywords: kolesarstvo, Dirka po Lombardiji, Tadej Pogačar, Primož Roglič, Marc Hirschi, ekipa UAE, slovenski državni prvak, Joxean Matxin Fernandez, Dirka po Emiliji, Dirka tri doline Vareseja, Vuelta, San Luco, Bologna, Dirka po Franciji, 2024, tritedenske dirke, enodnevne dirke, Madrid, kraljevska etapa, Angliru, Remco Evenepoel
- Excerpt: Na Emiliji in Lombardiji prvo in drugo letošnje soočenje Pogačarja in Rogliča Ključne besede: kolesarstvo, Dirka po Lombardiji, Tadej Pogačar, Primož Roglič, Marc Hirschi, ekipa UAE, slovenski državni prvak, Joxean Matxin Fernandez, Dirka po Emiliji, Dirka tri doline Vareseja, Vuelta, San Luco, Bologna, Dirka po Franciji, 2024, tritedenske dirke, enodnevne dirke, Madrid, kraljevska etapa, Angliru, Remco Evenepoel Tadej Pogačar je ob Marcu Hirschiju iz ekipe UAE že na startni listi Dirke po Lomba...

#### Rank 5: RELEVANT

- Title: Za Rogliča bo nedeljska cestna dirka borba in izziv
- Decision: relevant
- Rationale: Roglic road-race result; largely related.
- Category/date: sport / 2025-09-26T18:37:10
- URL: https://www.rtvslo.si/sport/kolesarstvo/svetovno-prvenstvo-v-kolesarstvu/za-roglica-bo-nedeljska-cestna-dirka-borba-in-izziv/758911
- FAISS rank/score: 5 / 0.8470
- Reranker score: n/a
- Keywords: kolesarstvo, svetovno prvenstvo, Primož Roglič
- Excerpt: Za Rogliča bo nedeljska cestna dirka borba in izziv Ključne besede: kolesarstvo, svetovno prvenstvo, Primož Roglič Na prizorišče svetovnega prvenstva v kolesarstvu je pripotoval še zadnji član slovenske reprezentance, Primož Roglič, ki je v Kigaliju opravil trening in si ogledal progo nedeljske cestne dirke, na kateri bo Slovenija nastopila z devetimi tekmovalci. Roglič je ponoči v Kigali pripotoval iz Španije. Na Sierra Nevadi je opravil samostojne višinske priprave in poskušal najti formo, s k...


### 10. Donald Trump novi zakoni

Precision@5: 3/5 = 0.60

#### Rank 1: NOT RELEVANT

- Title: Trump jo je v primeru obtožbe ponarejanja dokumentov odnesel brez kazni
- Decision: not_relevant
- Rationale: Trump legal case, not new laws.
- Category/date: svet / 2025-01-10T16:35:21
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/trump-jo-je-v-primeru-obtozbe-ponarejanja-dokumentov-odnesel-brez-kazni/732988
- FAISS rank/score: 1 / 0.8445
- Reranker score: n/a
- Keywords: Trump, Donald Trump, Stormy Daniels
- Excerpt: Trump jo je v primeru obtožbe ponarejanja dokumentov odnesel brez kazni Ključne besede: Trump, Donald Trump, Stormy Daniels Sodišče v New Yorku je za novoizvoljenega predsednika ZDA Donalda Trumpa zaradi ponarejanja dokumentov v zvezi s plačilom pornoigralki Stormy Daniels za molk o spolnem odnosu izreklo t. i. brezpogojni odpust, kar pomeni, da jo je odnesel brez kazni. "To je bila zelo grozna izkušnja. Mislim, da je bil to ogromen poraz za New York in newyorški sodni sistem, " je še pred izrek...

#### Rank 2: RELEVANT

- Title: Trump uvaja nove omejitve potovanj v ZDA
- Decision: relevant
- Rationale: New Trump travel restriction policy.
- Category/date: svet / 2025-12-17T10:13:47
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/trump-uvaja-nove-omejitve-potovanj-v-zda/767507
- FAISS rank/score: 2 / 0.8421
- Reranker score: n/a
- Keywords: Izvršni ukaz, Prepoved vstopa, Sirija, Omejitve potovanj, Trump
- Excerpt: Trump uvaja nove omejitve potovanj v ZDA Ključne besede: Izvršni ukaz, Prepoved vstopa, Sirija, Omejitve potovanj, Trump Administracija ameriškega predsednika Donalda Trumpa je za 19 držav, med njimi tudi Palestinsko upravo, uvedla nove omejitve potovanj. S tem je podvojila število držav, za katere veljajo omejitve glede potovanj in izseljevanja v ZDA. Bela hiša je sporočila, da Trump z izvršnim ukazom "razširja in poostruje omejitve vstopa za državljane iz držav, ki imajo dokazano resne pomanjk...

#### Rank 3: NOT RELEVANT

- Title: Newyorški porotniki odločili, da je Donald Trump kriv ponarejanja poslovnih dokumentov
- Decision: not_relevant
- Rationale: Trump legal case, not new laws.
- Category/date: svet / 2024-05-30T18:52:05
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/newyorski-porotniki-odlocili-da-je-donald-trump-kriv-ponarejanja-poslovnih-dokumentov/710158
- FAISS rank/score: 3 / 0.8418
- Reranker score: n/a
- Keywords: ZDA, Donald Trump, Stormy Daniels, Sojenje
- Excerpt: Newyorški porotniki odločili, da je Donald Trump kriv ponarejanja poslovnih dokumentov Ključne besede: ZDA, Donald Trump, Stormy Daniels, Sojenje Newyorški porotniki v sodnem procesu proti nekdanjemu predsedniku ZDA Donaldu Trumpu so že drugi dan zasedanja sprejeli odločitev. Odločili so, da je kriv v vseh 34 točkah obtožnice. Sodnik mu bo kazen izrekel 11. julija. Porota je odločila, da je Donald Trump kriv ponarejanja poslovnih dokumentov v povezavi s plačilom 130.000 dolarjev pornografski igr...

#### Rank 4: RELEVANT

- Title: Trump z novim zakonom uvedel višje kazni za trgovino s fentanilom
- Decision: relevant
- Rationale: Direct new Trump law result.
- Category/date: svet / 2025-07-17T10:37:53
- URL: https://www.rtvslo.si/svet/preberite-tudi/trump-z-novim-zakonom-uvedel-visje-kazni-za-trgovino-s-fentanilom/752186
- FAISS rank/score: 4 / 0.8404
- Reranker score: n/a
- Keywords: Nezakonito, Trgovina, Višje kazni, Fentanil, Trump
- Excerpt: Trump z novim zakonom uvedel višje kazni za trgovino s fentanilom Ključne besede: Nezakonito, Trgovina, Višje kazni, Fentanil, Trump Ameriški predsednik Donald Trump je v sredo podpisal zakon, ki sintetično drogo fentanil uvršča med najhujša prepovedana mamila v ZDA. Ob podpisu zakona je dejal, da bodo s tem zadali velik udarec mamilarskim kartelom, saj so za trgovino s fentanilom zdaj predvidene višje kazni. Fentanil je sredstvo, ki ga ameriški zdravniki včasih predpisujejo za lajšanje hudih bo...

#### Rank 5: RELEVANT

- Title: Trump podpisal prvi ameriški zakon o kriptovalutah
- Decision: relevant
- Rationale: Direct Trump-signed crypto law.
- Category/date: svet / 2025-07-19T14:19:39
- URL: https://www.rtvslo.si/svet/preberite-tudi/trump-podpisal-prvi-ameriski-zakon-o-kriptovalutah/752400
- FAISS rank/score: 5 / 0.8401
- Reranker score: n/a
- Keywords: Industrija kriptovalut, Stabilni kovanci, Zakon Genius, Kriptovalute, Trump
- Excerpt: Trump podpisal prvi ameriški zakon o kriptovalutah Ključne besede: Industrija kriptovalut, Stabilni kovanci, Zakon Genius, Kriptovalute, Trump Ameriški predsednik Donald Trump je podpisal prvi zakon o kriptovalutah v ZDA. Zadeva t. i. stabilne kovance – vrsto kriptovalut, katerih vrednost je vezana na stabilen zunanji vir, kot so dolar, evro ali zlato. Namen zakona je okrepiti zaupanje v industrijo kriptovalut, ki je z donacijami Trumpu postala pomemben političen igralec v Washingtonu. Zakon z i...


### 11. Evropska Unija in zveza NATO

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Evropa med Trumpom in Putinom
- Decision: relevant
- Rationale: Europe/geopolitical security context.
- Category/date: svet / 2025-02-14T19:04:31
- URL: https://www.rtvslo.si/svet/evropa-med-trumpom-in-putinom/736536
- FAISS rank/score: 1 / 0.8467
- Reranker score: n/a
- Keywords: rusija, zda, ukrajina, donaldtrump, vladimirputin, evropa
- Excerpt: Evropa med Trumpom in Putinom Ključne besede: rusija, zda, ukrajina, donaldtrump, vladimirputin, evropa Mednarodni odnosi se pospešeno spreminjajo. Od sveta, utemeljenega na boleči lekciji druge svetovne vojne, prehajamo v novo obdobje. Zdi se, da v čas, ko velja zakon močnejšega. Evropa manevrira med silnicami Rusije, ZDA in Kitajske, spopada se s pritiski tehnoloških velikanov, države največkrat niso poenotene glede prioritet, prebivalstvo geopolitične pretrese občuti na kakovosti življenja, k...

#### Rank 2: RELEVANT

- Title: Dodik v Moskvi kritiziral "ameriškega vazala" EU in "kolonijo" BiH
- Decision: relevant
- Rationale: EU geopolitical context.
- Category/date: svet / 2023-05-24T14:50:00
- URL: https://www.rtvslo.si/svet/evropa/dodik-v-moskvi-kritiziral-ameriskega-vazala-eu-in-kolonijo-bih/669339
- FAISS rank/score: 2 / 0.8453
- Reranker score: n/a
- Keywords: Milorad Dodik, Republika Srbska, Rusija, obisk, varnostni forum, EU, BiH, vojna v Ukrajini, Moskva, zgodovina, mednarodno pravo, ruska invazija, hegemonizem, Zahod, Nato, Vzhod, evropska varnostna arhitektura, Evropska unija, ZDA, gospodarsko sodelovanje, Evropska komisija, evropska integracija
- Excerpt: Dodik v Moskvi kritiziral "ameriškega vazala" EU in "kolonijo" BiH Ključne besede: Milorad Dodik, Republika Srbska, Rusija, obisk, varnostni forum, EU, BiH, vojna v Ukrajini, Moskva, zgodovina, mednarodno pravo, ruska invazija, hegemonizem, Zahod, Nato, Vzhod, evropska varnostna arhitektura, Evropska unija, ZDA, gospodarsko sodelovanje, Evropska komisija, evropska integracija Predsednik Republike Srbske Milorad Dodik nadaljuje obisk Moskve, kjer se je udeležil varnostnega foruma in opozoril, da...

#### Rank 3: RELEVANT

- Title: Ursula von der Leyen se spogleduje z mestom generalne sekretarke Nata
- Decision: relevant
- Rationale: Direct NATO leadership result.
- Category/date: svet / 2023-04-01T18:03:00
- URL: https://www.rtvslo.si/svet/evropa/ursula-von-der-leyen-se-spogleduje-z-mestom-generalne-sekretarke-nata/663442
- FAISS rank/score: 3 / 0.8429
- Reranker score: n/a
- Keywords: Ursula von der Leyen, Nato, Jens Stoltenberg, generalna sekretarka Nata, Evropska komisija, Nemčija, The Sun, diplomatski vir, Severnoatlantsko zavezništvo, Berliner Zeitung, tiskovni predstavnik, mandat, Velika Britanija, veto, nemške oborožene sile, Welt am Sonntag, španski premier, Pedro Sanchez, britanski obrambni minister, Ben Wallace
- Excerpt: Ursula von der Leyen se spogleduje z mestom generalne sekretarke Nata Ključne besede: Ursula von der Leyen, Nato, Jens Stoltenberg, generalna sekretarka Nata, Evropska komisija, Nemčija, The Sun, diplomatski vir, Severnoatlantsko zavezništvo, Berliner Zeitung, tiskovni predstavnik, mandat, Velika Britanija, veto, nemške oborožene sile, Welt am Sonntag, španski premier, Pedro Sanchez, britanski obrambni minister, Ben Wallace Predsednica Evropske komisije Ursula von der Leyen naj bi kandidirala za...

#### Rank 4: RELEVANT

- Title: Rutte: Če mislite, da se lahko Evropa brani sama, kar sanjajte naprej
- Decision: relevant
- Rationale: Direct Europe/NATO defence result.
- Category/date: svet / 2026-01-26T18:46:29
- URL: https://www.rtvslo.si/svet/rutte-ce-mislite-da-se-lahko-evropa-brani-sama-kar-sanjajte-naprej/771341
- FAISS rank/score: 4 / 0.8428
- Reranker score: n/a
- Keywords: ZDA, Nato, Mark Rutte
- Excerpt: Rutte: Če mislite, da se lahko Evropa brani sama, kar sanjajte naprej Ključne besede: ZDA, Nato, Mark Rutte Evropa se ne more braniti brez ZDA, potrebujemo drug drugega, je ob zadnjih napetosti v čezatlantskih odnosih dejal generalni sekretar zveze Nato Mark Rutte. "Kar sanjajte naprej," je odvrnil tistim, ki menijo, da se lahko Evropa brani sama. " Če kdor koli tu misli, da se lahko Evropska unija ali Evropa kot celota brani brez ZDA, naj kar sanja naprej. Tega ne morete, tega ne moremo, potreb...

#### Rank 5: RELEVANT

- Title: Costa o širitvi EU-ja: To je prava geopolitična naložba
- Decision: relevant
- Rationale: Direct EU result.
- Category/date: slovenija / 2025-09-01T23:04:53
- URL: https://www.rtvslo.si/slovenija/costa-o-siritvi-eu-ja-to-je-prava-geopoliticna-nalozba/756327
- FAISS rank/score: 5 / 0.8424
- Reranker score: n/a
- Keywords: EU, Evropska unija, Antonio Costa
- Excerpt: Costa o širitvi EU-ja: To je prava geopolitična naložba Ključne besede: EU, Evropska unija, Antonio Costa Države kandidatke morajo za vstop v Evropsko unijo izpolniti vse pogoje in vsa merila, obenem pa je njihov vstop tudi v interesu EU-ja, poudarja predsednik Evropskega sveta Antonio Costa. S predsednikom Evropskega sveta Antoniem Costo se je ob robu Blejskega strateškega foruma pogovarjal novinar Igor E. Bergant, pogovor je bil objavljen v Odmevih. Kako je cilj, Evropo ohraniti kot najvarnejš...


### 12. Velika Britanija Brexit

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Brexit pričakovanj ni upravičil, britanska javnost pa ga skoraj ne omenja več
- Decision: relevant
- Rationale: Direct Brexit result.
- Category/date: svet / 2025-01-31T06:20:23
- URL: https://www.rtvslo.si/svet/evropa/brexit-pricakovanj-ni-upravicil-britanska-javnost-pa-ga-skoraj-ne-omenja-vec/735075
- FAISS rank/score: 1 / 0.8510
- Reranker score: n/a
- Keywords: Gospodarske posledice, Evropska unija, Združeno kraljestvo, Brexit, Jan Grobovšek
- Excerpt: Brexit pričakovanj ni upravičil, britanska javnost pa ga skoraj ne omenja več Ključne besede: Gospodarske posledice, Evropska unija, Združeno kraljestvo, Brexit, Jan Grobovšek Pred petimi leti je Združeno kraljestvo izstopilo iz Evropske unije. Ekonomist z univerze v Edinburgu Jan Grobovšek pravi, da je s tem država dobila "najslabše od obeh svetov" – postala je manjše gospodarstvo in ni ujela gospodarskih priložnosti. Združeno kraljestvo je 31. januarja 2020 po 47 letih članstva kot prva članic...

#### Rank 2: RELEVANT

- Title: Velika Britanija prva evropska država v transpacifiškem prostotrgovinskem partnerstvu
- Decision: relevant
- Rationale: Post-Brexit UK trade context.
- Category/date: gospodarstvo / 2023-03-31T14:52:00
- URL: https://www.rtvslo.si/gospodarstvo/velika-britanija-prva-evropska-drzava-v-transpacifiskem-prostotrgovinskem-partnerstvu/663314
- FAISS rank/score: 2 / 0.8382
- Reranker score: n/a
- Keywords: Velika Britanija, CPTPP, transpacifiško prostotrgovinsko partnerstvo, transpacifiško partnerstvo, brexit, prostotrgovinski dogovor, gospodarske koristi, Rishi Sunak, Evropska unija, trgovinski bloki, Obama, Donald Trump, Kitajska, Japonska, Avstralija, Kanada, Nova Zelandija, Mehika, Južna Koreja, Tajvan, pridružitev
- Excerpt: Velika Britanija prva evropska država v transpacifiškem prostotrgovinskem partnerstvu Ključne besede: Velika Britanija, CPTPP, transpacifiško prostotrgovinsko partnerstvo, transpacifiško partnerstvo, brexit, prostotrgovinski dogovor, gospodarske koristi, Rishi Sunak, Evropska unija, trgovinski bloki, Obama, Donald Trump, Kitajska, Japonska, Avstralija, Kanada, Nova Zelandija, Mehika, Južna Koreja, Tajvan, pridružitev Velika Britanija se bo po dveh letih pogajanj pridružila Celostnemu in napredne...

#### Rank 3: RELEVANT

- Title: Velika Britanija hoče preoblikovati severnoirski protokol
- Decision: relevant
- Rationale: Direct Brexit/Northern Ireland protocol result.
- Category/date: svet / 2021-07-21T18:44:51
- URL: https://www.rtvslo.si/svet/evropa/velika-britanija-hoce-preoblikovati-severnoirski-protokol/588379
- FAISS rank/score: 3 / 0.8314
- Reranker score: n/a
- Keywords: Brexit, Velika Britanija, Bruselj, Britanska vlada, Evropska unija, Severnoirski protokol, Irski otok, Brandon Lewis, Parlament, London, Blago, Združeno kraljestvo, Enotni trg, David Frost, Gospodarska škoda, Severna Irska, Protesti, Maroš Šefčovič, Evropska komisija, Izstopni sporazum, Odbor
- Excerpt: Velika Britanija hoče preoblikovati severnoirski protokol Ključne besede: Brexit, Velika Britanija, Bruselj, Britanska vlada, Evropska unija, Severnoirski protokol, Irski otok, Brandon Lewis, Parlament, London, Blago, Združeno kraljestvo, Enotni trg, David Frost, Gospodarska škoda, Severna Irska, Protesti, Maroš Šefčovič, Evropska komisija, Izstopni sporazum, Odbor Britanska vlada se želi z Evropsko unijo znova pogajati o severnoirskem protokolu in ga spremeniti. Pozvala je tudi k moratoriju za...

#### Rank 4: RELEVANT

- Title: Britanci bodo zaostrili izdajanje vizumov, da bi zmanjšali priseljevanje
- Decision: relevant
- Rationale: UK migration policy explicitly tied to Brexit.
- Category/date: svet / 2023-12-05T09:17:17
- URL: https://www.rtvslo.si/svet/evropa/britanci-bodo-zaostrili-izdajanje-vizumov-da-bi-zmanjsali-priseljevanje/690539
- FAISS rank/score: 4 / 0.8310
- Reranker score: n/a
- Keywords: Velika Britanija, migracije, priseljevanje, tuji delavci, zakonito priseljevanje, nezakonito priseljevanje, minimalna plača, vizumi, družinski člani, politika, Evropska unija, brexit, neto migracije, Indija, Nigerija, Kitajska, premier, nadzor, javni zdravstveni sistem, notranji minister
- Excerpt: Britanci bodo zaostrili izdajanje vizumov, da bi zmanjšali priseljevanje Ključne besede: Velika Britanija, migracije, priseljevanje, tuji delavci, zakonito priseljevanje, nezakonito priseljevanje, minimalna plača, vizumi, družinski člani, politika, Evropska unija, brexit, neto migracije, Indija, Nigerija, Kitajska, premier, nadzor, javni zdravstveni sistem, notranji minister Velika Britanija se bo zaradi množičnega priseljevanja poleg nezakonitih migracij lotila tudi prihodov priseljencev po zak...

#### Rank 5: RELEVANT

- Title: Brexit je postal težava za e-mobilnost
- Decision: relevant
- Rationale: Direct Brexit result.
- Category/date: zabava-in-slog / 2023-06-05T07:45:00
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/brexit-je-postal-tezava-za-e-mobilnost/670651
- FAISS rank/score: 5 / 0.8287
- Reranker score: n/a
- Keywords: Brexit, Stellantis, carina, električni avtomobili, Velika Britanija, dajatve na izvoz, avtomobilska industrija, Aston Martin Lagonda, Unite, Carlos Tavares, električna vozila, BMW, Kitajska, Opel/Vauxhall, Ellesmere Port, dostavna vozila, investicije, zaposlovanje, gospodarstvo, kriza, blagovne znamke
- Excerpt: Brexit je postal težava za e-mobilnost Ključne besede: Brexit, Stellantis, carina, električni avtomobili, Velika Britanija, dajatve na izvoz, avtomobilska industrija, Aston Martin Lagonda, Unite, Carlos Tavares, električna vozila, BMW, Kitajska, Opel/Vauxhall, Ellesmere Port, dostavna vozila, investicije, zaposlovanje, gospodarstvo, kriza, blagovne znamke Morebitne dajatve na izvoz električnih avtomobilov iz Velike Britanije vznemirjajo avtomobilske proizvajalce. Stellantis odkrito grozi z zaprt...


### 13. Vojna v Ukrajini in Zelenski

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Zelenski: Zdaj ni čas za govor o volitvah
- Decision: relevant
- Rationale: Direct Zelensky/Ukraine wartime result.
- Category/date: svet / 2023-11-07T07:09:51
- URL: https://www.rtvslo.si/svet/evropa/zelenski-zdaj-ni-cas-za-govor-o-volitvah/687287
- FAISS rank/score: 1 / 0.8725
- Reranker score: n/a
- Keywords: Zelenski, Ukrajina, volitve, Volodimir Zelenski, predsedniške volitve, vojno stanje, ruska agresija, parlamentarne volitve, Lindsey Graham, svobodne volitve, vojna, Dmitro Kuleba, podpora, zahodni zavezniki, vojska, razkol, statična faza, državne strukture.
- Excerpt: Zelenski: Zdaj ni čas za govor o volitvah Ključne besede: Zelenski, Ukrajina, volitve, Volodimir Zelenski, predsedniške volitve, vojno stanje, ruska agresija, parlamentarne volitve, Lindsey Graham, svobodne volitve, vojna, Dmitro Kuleba, podpora, zahodni zavezniki, vojska, razkol, statična faza, državne strukture. Ukrajinski predsednik Volodimir Zelenski je zavrnil možnost predsedniških volitev prihodnje leto. Kot je dejal, bi bilo to neodgovorno. "Mislim, da zdaj ni pravi čas za volitve." "Odlo...

#### Rank 2: RELEVANT

- Title: Zelenski: S Trumpom na čelu ZDA se bo vojna z Rusijo končala prej
- Decision: relevant
- Rationale: Direct Zelensky/war result.
- Category/date: svet / 2024-11-16T10:32:34
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-s-trumpom-na-celu-zda-se-bo-vojna-z-rusijo-koncala-prej/727644
- FAISS rank/score: 2 / 0.8722
- Reranker score: n/a
- Keywords: Ukrajina, Rusija, vojna
- Excerpt: Zelenski: S Trumpom na čelu ZDA se bo vojna z Rusijo končala prej Ključne besede: Ukrajina, Rusija, vojna Ukrajinski predsednik Volodimir Zelenski je dejal, da mora Ukrajina narediti vse, kar je v njeni moči in s pomočjo diplomacije prihodnje leto zagotoviti konec vojne z Rusijo, ki po njegovih besedah napreduje na bojišču. Zelenski je v sobotnem radijskem intervjuju priznal, da so razmere na bojišču na vzhodu Ukrajine težke, saj ruske sile napredujejo, medtem ko ruski predsednik Vladimir Putin...

#### Rank 3: RELEVANT

- Title: Zelenski: Putin si prizadeva, da Trumpu ne bi uspelo končati vojne
- Decision: relevant
- Rationale: Direct Zelensky/war result.
- Category/date: svet / 2024-11-29T11:01:53
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-putin-si-prizadeva-da-trumpu-ne-bi-uspelo-koncati-vojne/728988
- FAISS rank/score: 3 / 0.8699
- Reranker score: n/a
- Keywords: Ukrajina, Rusija, Volodimir Zelenski
- Excerpt: Zelenski: Putin si prizadeva, da Trumpu ne bi uspelo končati vojne Ključne besede: Ukrajina, Rusija, Volodimir Zelenski Ukrajinski predsednik Volodimir Zelenski v nedavnem stopnjevanju ruske agresije vidi poskus ruskega predsednika Vladimirja Putina, da spodkoplje domnevna predvidena prizadevanja prihodnjega ameriškega predsednika Donalda Trumpa za mir. Putin hoče "zaostriti razmere, tako da Trumpu ne bi uspelo, da ne bi mogel končati vojne", je v četrtek zvečer v nagovoru dejal Zelenski. "Putin...

#### Rank 4: RELEVANT

- Title: Zelenski v Beli hiši: Mislim, da lahko s pomočjo Trumpa končamo vojno v Ukrajini
- Decision: relevant
- Rationale: Direct Zelensky/Ukraine war result.
- Category/date: svet / 2025-10-17T07:35:30
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-v-beli-hisi-mislim-da-lahko-s-pomocjo-trumpa-koncamo-vojno-v-ukrajini/761078
- FAISS rank/score: 4 / 0.8683
- Reranker score: n/a
- Keywords: Rusija, Ukrajina, ZDA, tomahawk, Volodimir Zelenski, Donald Trump
- Excerpt: Zelenski v Beli hiši: Mislim, da lahko s pomočjo Trumpa končamo vojno v Ukrajini Ključne besede: Rusija, Ukrajina, ZDA, tomahawk, Volodimir Zelenski, Donald Trump Ukrajinski predsednik Volodimir Zelenski je ob obisku Bele hiše dejal, da lahko s pomočjo ameriškega predsednika Donalda Trumpa končajo vojno v Ukrajini. "Mislim, da lahko z vašo pomočjo končamo to vojno, " je dejal Zelenski na srečanju s Trumpom in mu čestital za dogovor o prekinitvi ognja v Gazi. Trump je srečanje začel z besedami, d...

#### Rank 5: RELEVANT

- Title: Zelenski v Beli hiši: Mislim, da lahko s pomočjo Trumpa končamo vojno v Ukrajini
- Decision: relevant
- Rationale: Duplicate direct Zelensky/Ukraine war result.
- Category/date: svet / 2025-10-17T07:35:30
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-tretjic-letos-prihaja-v-belo-hiso-na-mizi-vprasanje-dobave-ameriskih-raket-tomahawk/761078
- FAISS rank/score: 5 / 0.8683
- Reranker score: n/a
- Keywords: Rusija, Ukrajina, ZDA, tomahawk, Volodimir Zelenski, Donald Trump
- Excerpt: Zelenski v Beli hiši: Mislim, da lahko s pomočjo Trumpa končamo vojno v Ukrajini Ključne besede: Rusija, Ukrajina, ZDA, tomahawk, Volodimir Zelenski, Donald Trump Ukrajinski predsednik Volodimir Zelenski je ob obisku Bele hiše dejal, da lahko s pomočjo ameriškega predsednika Donalda Trumpa končajo vojno v Ukrajini. "Mislim, da lahko z vašo pomočjo končamo to vojno, " je dejal Zelenski na srečanju s Trumpom in mu čestital za dogovor o prekinitvi ognja v Gazi. Trump je srečanje začel z besedami, d...


### 14. Kitajska proti ZDA

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Ši Džinping sprejel ameriške senatorje: Odnosi med državama ključni za usodo človeštva
- Decision: relevant
- Rationale: Direct China-US relations result.
- Category/date: svet / 2023-10-09T13:35:55
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/si-dzinping-sprejel-ameriske-senatorje-odnosi-med-drzavama-kljucni-za-usodo-clovestva/684219
- FAISS rank/score: 1 / 0.8649
- Reranker score: n/a
- Keywords: Kitajska, ZDA, obisk, senatorji, Ši Džinping, predsednik, odnosi, delegacija, senat, Peking, gospodarstvo, konkurenca, podjetja, sodelovanje, demokracija, pravice, kemikalije, vojna, Rusija, Ukrajina, človekove pravice, kritika
- Excerpt: Ši Džinping sprejel ameriške senatorje: Odnosi med državama ključni za usodo človeštva Ključne besede: Kitajska, ZDA, obisk, senatorji, Ši Džinping, predsednik, odnosi, delegacija, senat, Peking, gospodarstvo, konkurenca, podjetja, sodelovanje, demokracija, pravice, kemikalije, vojna, Rusija, Ukrajina, človekove pravice, kritika Kitajski predsednik Ši Džinping je v Pekingu sprejel delegacijo pod vodstvom senatorja Chucka Schumerja in dejal, da bodo odnosi med Kitajsko in ZDA vplivali na usodo čl...

#### Rank 2: RELEVANT

- Title: ZDA bodo za Kitajsko uvedle 104-odstotne carine
- Decision: relevant
- Rationale: Direct US tariffs against China.
- Category/date: svet / 2025-04-08T07:23:25
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/zda-bodo-za-kitajsko-uvedle-104-odstotne-carine/742022
- FAISS rank/score: 2 / 0.8623
- Reranker score: n/a
- Keywords: ZDA, Carine, Kitajska
- Excerpt: ZDA bodo za Kitajsko uvedle 104-odstotne carine Ključne besede: ZDA, Carine, Kitajska ZDA bodo v sredo minuto čez polnoč po vzhodnem času uvedle 104-odstotne carine na uvoz blaga iz Kitajske, je sporočila Bela hiša, potem ko Peking ni odpravil povračilnih carin na ameriško blago do roka, ki ga je določil Trump, in sicer do torka opoldne. Zaradi zaostrovanja trgovinske vojne med ZDA in Kitajsko se je nafta pocenila za en dolar in se giblje na najnižji ravni v štirih letih. Strah pred recesijo, ki...

#### Rank 3: RELEVANT

- Title: Kitajska po napovedi novih ameriških carin zagrozila s protiukrepi
- Decision: relevant
- Rationale: Direct China response to US tariffs.
- Category/date: gospodarstvo / 2025-10-12T13:10:13
- URL: https://www.rtvslo.si/gospodarstvo/kitajska-po-napovedi-novih-ameriskih-carin-zagrozila-s-protiukrepi/760526
- FAISS rank/score: 3 / 0.8605
- Reranker score: n/a
- Keywords: ZDA, Kitajska, carine
- Excerpt: Kitajska po napovedi novih ameriških carin zagrozila s protiukrepi Ključne besede: ZDA, Kitajska, carine Potem ko je predsednik ZDA Donald Trump z novembrom napovedal nove carine na uvoz iz Kitajske, je ta zagrozila s protiukrepi. V Pekingu ob tem Washingtonu očitajo dvojna merila in mu očitajo zlorabe načela nacionalne varnosti. S kitajskega ministrstva za trgovino so sporočili, da ameriška administracija že dolgo pretirava z uporabo načela nacionalne varnosti in ga zlorablja za nadzor nad izvo...

#### Rank 4: RELEVANT

- Title: Peking sporoča, da ne bo sprejel "izsiljevalske narave" ZDA
- Decision: relevant
- Rationale: Direct China-US pressure/tension result.
- Category/date: svet / 2025-04-08T07:23:25
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/peking-sporoca-da-ne-bo-sprejel-izsiljevalske-narave-zda/742022
- FAISS rank/score: 4 / 0.8554
- Reranker score: n/a
- Keywords: ZDA, Carine, Kitajska
- Excerpt: Peking sporoča, da ne bo sprejel "izsiljevalske narave" ZDA Ključne besede: ZDA, Carine, Kitajska Potem ko so ZDA Kitajski zagrozile z dodatnimi, 50-odstotnimi carinami, če ta ne bo umaknila povračilnih carin na uvoz ameriškega blaga, je kitajsko ministrstvo za trgovino sporočilo, da ne bodo sprejeli "izsiljevalske narave" ZDA. Ministrstvo je dodalo, da se bodo proti carinam borili "do konca", poroča BBC. Grožnjo ameriškega predsednika Donalda Trumpa z dodatnimi 50-odstotnimi carinami na kitajsk...

#### Rank 5: RELEVANT

- Title: Biden podpisal izvršni ukaz proti izvozu napredne tehnologije na Kitajsko
- Decision: relevant
- Rationale: Direct US technology export limits to China.
- Category/date: svet / 2023-08-10T10:00:53
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/biden-podpisal-izvrsni-ukaz-proti-izvozu-napredne-tehnologije-na-kitajsko/677661
- FAISS rank/score: 5 / 0.8549
- Reranker score: n/a
- Keywords: ZDA, Kitajska, napredna tehnologija, Ameriški predsednik, Joe Biden, izvršni ukaz, tehnologija, računalniški čipi, mikroelektronika, kvantne informacijske tehnologije, umetna inteligenca, investicije, vojaški nameni, trgovinska politika, zavezniki, industrija, naložbe, gospodarstvo, trgovinska zbornica, ekonomija, globalno, tuje naložbe
- Excerpt: Biden podpisal izvršni ukaz proti izvozu napredne tehnologije na Kitajsko Ključne besede: ZDA, Kitajska, napredna tehnologija, Ameriški predsednik, Joe Biden, izvršni ukaz, tehnologija, računalniški čipi, mikroelektronika, kvantne informacijske tehnologije, umetna inteligenca, investicije, vojaški nameni, trgovinska politika, zavezniki, industrija, naložbe, gospodarstvo, trgovinska zbornica, ekonomija, globalno, tuje naložbe Ameriški predsednik Joe Biden je podpisal izvršni ukaz, ki blokira izvo...


### 15. Korupcija v slovenski politiki

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: Demokrati zahtevajo razpravo o sistemski korupciji
- Decision: relevant
- Rationale: Direct systemic corruption politics result.
- Category/date: slovenija / 2025-12-17T19:05:26
- URL: https://www.rtvslo.si/slovenija/demokrati-zahtevajo-razpravo-o-sistemski-korupciji/767596
- FAISS rank/score: 1 / 0.8554
- Reranker score: n/a
- Keywords: Zoran Janković, Robert Golob, Anže Logar, Demokrati, DZ
- Excerpt: Demokrati zahtevajo razpravo o sistemski korupciji Ključne besede: Zoran Janković, Robert Golob, Anže Logar, Demokrati, DZ Poslanci iz vrst Demokratov po razkritjih o sumih podkupovanja, ki bremenijo tudi ljubljanskega župana Zorana Jankovića, zahtevajo sejo komisije za nadzor javnih financ. Opozarjajo na razpad pravne države in premierju Robertu Golobu očitajo neukrepanje. "Ne gre le za posamezne nepravilnosti in protizakonita ravnanja, ampak gre za organiziran sistem, kjer so določeni uradniki...

#### Rank 2: RELEVANT

- Title: OECD v Sloveniji preveril boj proti podkupovanju javnih uslužbencev
- Decision: relevant
- Rationale: Corruption/bribery in Slovenia.
- Category/date: gospodarstvo / 2025-02-18T18:43:18
- URL: https://www.rtvslo.si/gospodarstvo/oecd-v-sloveniji-preveril-boj-proti-podkupovanju-javnih-usluzbencev/736993
- FAISS rank/score: 2 / 0.8536
- Reranker score: n/a
- Keywords: Korupcija, Priporočila, Slovenija, Podkupovanje, OECD
- Excerpt: OECD v Sloveniji preveril boj proti podkupovanju javnih uslužbencev Ključne besede: Korupcija, Priporočila, Slovenija, Podkupovanje, OECD Delegacija Organizacije za gospodarsko sodelovanje in razvoj (OECD) je te dni v Sloveniji preučevala implementacijo priporočil, vezanih na izvajanje Konvencije OECD-ja o boju proti podkupovanju tujih javnih uslužbencev v mednarodnem poslovanju. Delovna skupina OECD-ja za boj proti podkupovanju tujih javnih uslužbencev v mednarodnem poslovanju spremlja izvajanj...

#### Rank 3: NOT RELEVANT

- Title: Logar in Stevanović "prijateljsko spila kavo"
- Decision: not_relevant
- Rationale: Political meeting, not mainly corruption.
- Category/date: slovenija / 2026-03-25T16:43:46
- URL: https://www.rtvslo.si/slovenija/parlamentarne-volitve-2026/logar-in-stevanovic-prijateljsko-spila-kavo/259450
- FAISS rank/score: 3 / 0.8493
- Reranker score: n/a
- Keywords: Korupcija, Koalicija, Sestanek, Stevanović, Logar
- Excerpt: Logar in Stevanović "prijateljsko spila kavo" Ključne besede: Korupcija, Koalicija, Sestanek, Stevanović, Logar Prvak Demokratov Anže Logar in predsednik stranke Resni.ca Zoran Stevanović sta danes "prijateljsko spila kavo", kot je njuno srečanje pokomentiral Stevanović. Po njegovem mnenju z Logarjem nista ključna igralca za sestavo vlade. Logarja in Stevanovića so namreč danes (sreda) v fotografski objektiv ujeli na tedniku Reporter. " V ozadju ni nobene zarote," je ob tem dejal Stevanović, ki...

#### Rank 4: RELEVANT

- Title: Financiranje politike: Snežičevo omrežje in SDS
- Decision: relevant
- Rationale: Political financing/corruption context.
- Category/date: slovenija / 2023-11-30T19:20:42
- URL: https://www.rtvslo.si/slovenija/financiranje-politike-snezicevo-omrezje-in-sds/690105
- FAISS rank/score: 4 / 0.8488
- Reranker score: n/a
- Keywords: Tarča, Planet TV, Rok Snežič, preiskovalna komisija, kriminalna združba, politika, Nova24TV, financiranje medijev, politične stranke, Janša, Orbán, Madžarska, lastništvo medijev, preiskovalne ugotovitve, koruptivna dejanja, nepovezani poslanci, oddaja Tarča, financiranje političnih strank, medijski monopoli, financiranje iz tujine, financiranje projektov
- Excerpt: Financiranje politike: Snežičevo omrežje in SDS Ključne besede: Tarča, Planet TV, Rok Snežič, preiskovalna komisija, kriminalna združba, politika, Nova24TV, financiranje medijev, politične stranke, Janša, Orbán, Madžarska, lastništvo medijev, preiskovalne ugotovitve, koruptivna dejanja, nepovezani poslanci, oddaja Tarča, financiranje političnih strank, medijski monopoli, financiranje iz tujine, financiranje projektov Tarča je podrobno pregledala ugotovitve preiskovalne komisije, ki je policiji i...

#### Rank 5: RELEVANT

- Title: Koalicija in opozicija sta se obmetavali z obtožbami korupcije
- Decision: relevant
- Rationale: Direct Slovenian political corruption result.
- Category/date: slovenija / 2024-02-20T20:53:47
- URL: https://www.rtvslo.si/slovenija/koalicija-in-opozicija-sta-se-obmetavali-z-obtozbami-korupcije/698992
- FAISS rank/score: 5 / 0.8487
- Reranker score: n/a
- Keywords: Politika, Slovenska politika, korupcija, pravosodje, DZ, Odbor za pravosodje, Litijska, afere, opozicija, koalicija, nakup, stavba, Litijska cesta, živahna razprava, SDS, priporočila, seja, poslanec, očitki, milijonski nakup, lastništvo, integriteta, javne funkcije, obljube.
- Excerpt: Koalicija in opozicija sta se obmetavali z obtožbami korupcije Ključne besede: Politika, Slovenska politika, korupcija, pravosodje, DZ, Odbor za pravosodje, Litijska, afere, opozicija, koalicija, nakup, stavba, Litijska cesta, živahna razprava, SDS, priporočila, seja, poslanec, očitki, milijonski nakup, lastništvo, integriteta, javne funkcije, obljube. Na razpravi o stanju na področju korupcije je opozicija poudarila zlasti afere spornega nakupa stavbe na Litijski cesti, koalicija pa je izpostav...


### 16. Izstrelitev rakete v vesolje

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Raketo s prvima slovenskima satelitoma le izstrelili: "V vesolju smo!"
- Decision: relevant
- Rationale: Direct rocket/satellites launch.
- Category/date: znanost-in-tehnologija / 2020-09-03T06:47:51
- URL: https://www.rtvslo.si/znanost-in-tehnologija/raketo-s-prvima-slovenskima-satelitoma-le-izstrelili-v-vesolju-smo/535004
- FAISS rank/score: 1 / 0.8743
- Reranker score: n/a
- Keywords: satelit, izstrelitev, Vega, Nemo HD in Trisat, Francoska Gvajana, raketa, Nemo HD, Trisat, evropska znanost, Arianespace, vesoljski center, Kourou, vodja projekta, Centrer odličnosti Vesolje-SI, znanost, slovensko gospodarstvo, orbita, vesolje, mikrosatelit, nanosatelit, testiranje
- Excerpt: Raketo s prvima slovenskima satelitoma le izstrelili: "V vesolju smo!" Ključne besede: satelit, izstrelitev, Vega, Nemo HD in Trisat, Francoska Gvajana, raketa, Nemo HD, Trisat, evropska znanost, Arianespace, vesoljski center, Kourou, vodja projekta, Centrer odličnosti Vesolje-SI, znanost, slovensko gospodarstvo, orbita, vesolje, mikrosatelit, nanosatelit, testiranje Iz Francoske Gvajane so ponoči vendarle izstrelili raketo Vega, s katero sta v vesolje poletela tudi prva slovenska satelita Nemo...

#### Rank 2: RELEVANT

- Title: Izstrelitev slovenskih satelitov preložena vsaj do nedelje
- Decision: relevant
- Rationale: Direct launch delay for satellites/rocket.
- Category/date: znanost-in-tehnologija / 2020-06-18T07:45:01
- URL: https://www.rtvslo.si/znanost-in-tehnologija/izstrelitev-slovenskih-satelitov-prelozena-vsaj-do-nedelje/527470
- FAISS rank/score: 2 / 0.8711
- Reranker score: n/a
- Keywords: izstrelitev, Nemo HD, Trisat, Vesolje-SI, raketa, Vega, slovenski sateliti, Francoska Gvajana, Arianespace, vreme, preložitev, Kourou, Centra odličnosti Vesolje-SI, sateliti, neugodne vetrovne razmere, nanosatelit, testiranje, elektronika, Zemlja, opazovanje, interaktivno, prelet, senzorji
- Excerpt: Izstrelitev slovenskih satelitov preložena vsaj do nedelje Ključne besede: izstrelitev, Nemo HD, Trisat, Vesolje-SI, raketa, Vega, slovenski sateliti, Francoska Gvajana, Arianespace, vreme, preložitev, Kourou, Centra odličnosti Vesolje-SI, sateliti, neugodne vetrovne razmere, nanosatelit, testiranje, elektronika, Zemlja, opazovanje, interaktivno, prelet, senzorji Izstrelitev rakete Vega s slovenskima satelitoma Nemo HD in Trisat z izstrelišča v Francoski Gvajani, ki je bila predvidena za petek z...

#### Rank 3: RELEVANT

- Title: Nasa uspešno izstrelila SpaceX-ovo raketo. Četverica bo v vesolju šest mesecev.
- Decision: relevant
- Rationale: Direct rocket launch to space.
- Category/date: znanost-in-tehnologija / 2023-03-02T12:24:00
- URL: https://www.rtvslo.si/znanost-in-tehnologija/nasa-uspesno-izstrelila-spacex-ovo-raketo-cetverica-bo-v-vesolju-sest-mesecev/659714
- FAISS rank/score: 3 / 0.8706
- Reranker score: n/a
- Keywords: SpaceX, Dragon Crew-6, misija, Nasa, Elon Musk, mednarodna vesoljska postaja, posadka, izstrelitev, težave, vesolje, astronavt, orbita, Združeni arabski emirati, ISS, predaja, Zemlja, kapsula, Rusija, Sojuz, puščanje, Kazahstan
- Excerpt: Nasa uspešno izstrelila SpaceX-ovo raketo. Četverica bo v vesolju šest mesecev. Ključne besede: SpaceX, Dragon Crew-6, misija, Nasa, Elon Musk, mednarodna vesoljska postaja, posadka, izstrelitev, težave, vesolje, astronavt, orbita, Združeni arabski emirati, ISS, predaja, Zemlja, kapsula, Rusija, Sojuz, puščanje, Kazahstan Iz Nasinega vesoljskega centra Kennedy na Floridi so uspešno izstrelili raketo ameriškega podjetja SpaceX, ki je v lasti milijarderja Elona Muska. V okviru misije Dragon Crew-6...

#### Rank 4: RELEVANT

- Title: Video: Tako je iz vesolja videti izstrelitev rakete
- Decision: relevant
- Rationale: Direct rocket launch from space.
- Category/date: znanost-in-tehnologija / 2018-11-25T11:06:09
- URL: https://www.rtvslo.si/znanost-in-tehnologija/video-tako-je-iz-vesolja-videti-izstrelitev-rakete/472829
- FAISS rank/score: 4 / 0.8705
- Reranker score: n/a
- Keywords: ISS, Mednarodna vesoljska postaja, Alexander Gerst, Poleti s posadko, Progress, Sojuz, raketa, vesolje, izstrelitev, vesoljsko plovilo, zaloge, Evropska vesoljska agencija, Esa, astronavt, poveljnik, kozmodrom, orbite, gorivo, kisik, preizkus, nesreča, senzor, Rusija, posadke, kupola, fotoaparat, fotografiranje.
- Excerpt: Video: Tako je iz vesolja videti izstrelitev rakete Ključne besede: ISS, Mednarodna vesoljska postaja, Alexander Gerst, Poleti s posadko, Progress, Sojuz, raketa, vesolje, izstrelitev, vesoljsko plovilo, zaloge, Evropska vesoljska agencija, Esa, astronavt, poveljnik, kozmodrom, orbite, gorivo, kisik, preizkus, nesreča, senzor, Rusija, posadke, kupola, fotoaparat, fotografiranje. Astronavt Alexander Gerst je posnel izstrelitev rakete z drugačne perspektive, kot smo je vajeni. Ujel je plovilo MS-1...

#### Rank 5: RELEVANT

- Title: SpaceX bo v četrtek zvečer izstrelil mogočno raketo Starship
- Decision: relevant
- Rationale: Direct Starship rocket launch.
- Category/date: znanost-in-tehnologija / 2025-03-03T20:06:34
- URL: https://www.rtvslo.si/znanost-in-tehnologija/spacex-bo-v-cetrtek-zvecer-izstrelil-mogocno-raketo-starship/449493
- FAISS rank/score: 5 / 0.8686
- Reranker score: n/a
- Keywords: Tehnologija, Izstrelitev, Super Heavy, SpaceX, Starship
- Excerpt: SpaceX bo v četrtek zvečer izstrelil mogočno raketo Starship Ključne besede: Tehnologija, Izstrelitev, Super Heavy, SpaceX, Starship Ameriško podjetje SpaceX bo v četrtek opravilo osmi preizkusni polet rakete Starship. Znova bo poskusilo uloviti stopnjo Super Heavy. Starship je nadgrajen in precej večji, v vesolje pa bo oddal prototipe nove generacije satelitov Starlink. Enourno izstrelitveno okno se bo odprlo v noči s četrtka na petek ob 00.30 po našem času. Izstrelitev bo potekala z Boca Chice...


### 17. Delnice Tesle padajo

Precision@5: 3/5 = 0.60

#### Rank 1: NOT RELEVANT

- Title: Od eko Muska do heil Tesle v nekaj sekundah
- Decision: not_relevant
- Rationale: Tesla/Musk column, not mainly shares falling.
- Category/date: kolumne / 2025-03-16T07:24:30
- URL: https://www.rtvslo.si/kolumne/od-eko-muska-do-heil-tesle-v-nekaj-sekundah/739587
- FAISS rank/score: 1 / 0.8441
- Reranker score: n/a
- Keywords: Elon Musk, Tesla, Andrej Brglez
- Excerpt: Od eko Muska do heil Tesle v nekaj sekundah Ključne besede: Elon Musk, Tesla, Andrej Brglez Moralna teža avta je termin, ki je v avtomobilski industriji znan že dolgo, kompas vrednot, načel in pravil v svetu avtomobilov pa se ponastavlja in prilagaja siceršnjemu družbenemu utripu v času. Poglejmo, kako je prvi prodajalec avtomobilov na svetu in nosilec upanja za elektrifikacijo mobilnosti postal najslabši prodajalec v zgodovini in kaj to pomeni za Teslo. Kadarkoli kdo reče "saj smo že prej vedel...

#### Rank 2: RELEVANT

- Title: Tehnološko opustošenje stoletja: iz velikanov izpuhtelo 5,4 bilijona dolarjev
- Decision: relevant
- Rationale: Direct Tesla stock/share losses.
- Category/date: gospodarstvo / 2022-12-25T07:40:17
- URL: https://www.rtvslo.si/gospodarstvo/borzni-komentar/tehnolosko-opustosenje-stoletja-iz-velikanov-izpuhtelo-5-4-bilijona-dolarjev/652126
- FAISS rank/score: 2 / 0.8418
- Reranker score: n/a
- Keywords: MMC-jev borzni komentar, tehnološke delnice, ARK Innovation, Cathie Wood, Tesla, Primož Cencelj, finančni trgi, recesija, Teslina delnica, Fed, inflacija, vlagatelji, izgube, kriza, mladi vlagatelji, ETF-sklad, kapital, Invitae, Coinbase, Twilio, tečaj, rast, spremembe, trg
- Excerpt: Tehnološko opustošenje stoletja: iz velikanov izpuhtelo 5,4 bilijona dolarjev Ključne besede: MMC-jev borzni komentar, tehnološke delnice, ARK Innovation, Cathie Wood, Tesla, Primož Cencelj, finančni trgi, recesija, Teslina delnica, Fed, inflacija, vlagatelji, izgube, kriza, mladi vlagatelji, ETF-sklad, kapital, Invitae, Coinbase, Twilio, tečaj, rast, spremembe, trg Ker Fedov boj proti inflaciji večjih rezultatov še ni prinesel, gospodarstvo pa bo očitno pahnil v recesijo, se finančni trgi od le...

#### Rank 3: NOT RELEVANT

- Title: Teslina berlinska tovarna bo zaradi pomanjkanja delov dva tedna zaprta
- Decision: not_relevant
- Rationale: Factory shutdown, not shares falling.
- Category/date: gospodarstvo / 2024-01-12T16:29:36
- URL: https://www.rtvslo.si/gospodarstvo/teslina-berlinska-tovarna-bo-zaradi-pomanjkanja-delov-dva-tedna-zaprta/694626
- FAISS rank/score: 3 / 0.8401
- Reranker score: n/a
- Keywords: Nemčija, Tesla, hutijevci, proizvodnja, motnje, dobavne verige, Rdeče morje, prekinitev, Berlin, tovarna, Jemen, solidarnost, Gaza, napadi, ladje, svobodna plovnost, vojska, cilji, predsednik ZDA, letalske operacije, zaposleni
- Excerpt: Teslina berlinska tovarna bo zaradi pomanjkanja delov dva tedna zaprta Ključne besede: Nemčija, Tesla, hutijevci, proizvodnja, motnje, dobavne verige, Rdeče morje, prekinitev, Berlin, tovarna, Jemen, solidarnost, Gaza, napadi, ladje, svobodna plovnost, vojska, cilji, predsednik ZDA, letalske operacije, zaposleni Ameriški proizvajalec električnih avtomobilov Tesla je zaradi motenj v dobavnih verigah po napadih hutijevskih upornikov v Rdečem morju napovedal dvotedensko prekinitev proizvodnje v svo...

#### Rank 4: RELEVANT

- Title: Tesli se upad dobave avtomobilov že finančno pozna
- Decision: relevant
- Rationale: Tesla financial decline and per-share result.
- Category/date: zabava-in-slog / 2025-01-31T08:08:29
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/tesli-se-upad-dobave-avtomobilov-ze-financno-pozna/735101
- FAISS rank/score: 4 / 0.8389
- Reranker score: n/a
- Keywords: Tesla, Tesla Y, Cybertuck
- Excerpt: Tesli se upad dobave avtomobilov že finančno pozna Ključne besede: Tesla, Tesla Y, Cybertuck Proizvajalec električnih avtomobilov je lani prvič v več kot desetletju zaznal upad dobave avtomobilov. Tesla je v zadnjem lanskem četrtletju vknjižil 25,7 milijarde dolarjev prihodkov, kar je dva odstotka manj kot leto prej. Prihodki ameriškega proizvajalca električnih avtomobilov so bili nižji od pričakovanj analitikov, ki so v povprečju računali, da bodo znašali 27,3 milijarde dolarjev, poroča nemška...

#### Rank 5: RELEVANT

- Title: Musk se zaradi padca prodaje Tesle umika iz vlade
- Decision: relevant
- Rationale: Tesla sales/profit fall result.
- Category/date: svet / 2025-04-23T09:44:00
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/musk-se-zaradi-padca-prodaje-tesle-umika-iz-vlade/743583
- FAISS rank/score: 5 / 0.8385
- Reranker score: n/a
- Keywords: Carine, Vlada, Musk, Prodaja, Tesla
- Excerpt: Musk se zaradi padca prodaje Tesle umika iz vlade Ključne besede: Carine, Vlada, Musk, Prodaja, Tesla Elon Musk je napovedal, da bo v prihodnje manj časa posvetil delu za urad za vladno učinkovitost (Doge), saj so dobički njegovega podjetja Tesla v prvem četrtletju padli za več kot dve tretjini. Glavni razlog za upad prodaje je prav njegovo delo v vladi. V torek je podjetje poročalo o 20-odstotnem padcu prihodkov od prodaje avtomobilov v prvem četrtletju leta 2025 v primerjavi z enakim obdobjem...


### 18. Nova verzija umetne inteligence

Precision@5: 3/5 = 0.60

#### Rank 1: RELEVANT

- Title: OpenAI predstavil najnovejši model umetne inteligence GPT-5 − pametnejši, hitrejši, uporabnejši
- Decision: relevant
- Rationale: Direct latest AI model/version result.
- Category/date: znanost-in-tehnologija / 2025-08-08T08:30:59
- URL: https://www.rtvslo.si/znanost-in-tehnologija/openai-predstavil-najnovejsi-model-umetne-inteligence-gpt-5-pametnejsi-hitrejsi-uporabnejsi/754133
- FAISS rank/score: 1 / 0.8351
- Reranker score: n/a
- Keywords: GPT-5, OpenAI, UI
- Excerpt: OpenAI predstavil najnovejši model umetne inteligence GPT-5 − pametnejši, hitrejši, uporabnejši Ključne besede: GPT-5, OpenAI, UI Podjetje OpenAI je predstavilo najnovejši in najnaprednejši model umetne inteligence velikega obsega GPT-5. GPT-5, ki je pametnejši, hitrejši in uporabnejši pri pisanju, programiranju in na drugih področjih, bo vsem na voljo brezplačno. OpenAI trdi, da je stopnja halucinacij GPT-5 nižja, kar pomeni, da si model manj pogosto izmišlja odgovore. V podjetju so pojasnili,...

#### Rank 2: RELEVANT

- Title: Apple bo svoje naprave nadgradil s ChatGPT-jem in glasovni pomočnici Siri dal nove funkcije
- Decision: relevant
- Rationale: New AI features/upgrade result.
- Category/date: znanost-in-tehnologija / 2024-06-11T09:23:51
- URL: https://www.rtvslo.si/znanost-in-tehnologija/apple-bo-svoje-naprave-nadgradil-s-chatgpt-jem-in-glasovni-pomocnici-siri-dal-nove-funkcije/711352
- FAISS rank/score: 2 / 0.8309
- Reranker score: n/a
- Keywords: Apple, OpenAI, ChatGPT, Tim Cook
- Excerpt: Apple bo svoje naprave nadgradil s ChatGPT-jem in glasovni pomočnici Siri dal nove funkcije Ključne besede: Apple, OpenAI, ChatGPT, Tim Cook Ameriško tehnološko podjetje Apple je predstavilo nove funkcije umetne inteligence za svoje naprave Apple Intelligence in partnerstvo s podjetjem OpenAI, ki bo še letos vključilo storitev ChatGPT v Applove naprave. Glavni izvršni direktor Appla Tim Cook je na sedežu tehnološkega velikana v kalifornijskem mestu Cupertino v Silicijevi dolini odprl letno konfe...

#### Rank 3: RELEVANT

- Title: Google predstavil nov program umetne inteligence Bard
- Decision: relevant
- Rationale: New AI program result.
- Category/date: znanost-in-tehnologija / 2023-02-07T11:00:00
- URL: https://www.rtvslo.si/znanost-in-tehnologija/google-predstavil-nov-program-umetne-inteligence-bard/657070
- FAISS rank/score: 3 / 0.8275
- Reranker score: n/a
- Keywords: Google, Bard, Umetna inteligenca, jezikovni model, intervju, Sundar Pichai, LaMDA, ChatGPT, OpenAI, Microsoft, investicija, partnerstvo, tehnološko podjetje, aplikacije za dialog, razvoj, napredki, zunanji vplivi, primerjava, inovacija, iskalnik
- Excerpt: Google predstavil nov program umetne inteligence Bard Ključne besede: Google, Bard, Umetna inteligenca, jezikovni model, intervju, Sundar Pichai, LaMDA, ChatGPT, OpenAI, Microsoft, investicija, partnerstvo, tehnološko podjetje, aplikacije za dialog, razvoj, napredki, zunanji vplivi, primerjava, inovacija, iskalnik Ameriški tehnološki velikan Google je uradno predstavil nov program umetne inteligence Bard. Kot poudarjajo v podjetju, gre za pomemben naslednji korak na področju umetne inteligence z...

#### Rank 4: NOT RELEVANT

- Title: Vlada potrdila strategijo za umetno inteligenco
- Decision: not_relevant
- Rationale: AI strategy, not a new version/model.
- Category/date: znanost-in-tehnologija / 2026-03-05T14:25:24
- URL: https://www.rtvslo.si/znanost-in-tehnologija/vlada-potrdila-strategijo-za-umetno-inteligenco/775445
- FAISS rank/score: 4 / 0.8268
- Reranker score: n/a
- Keywords: Slovenska kulturna identiteta, Akcijski načrt, Ksenija Klampfer, Strategija, Umetna inteligenca
- Excerpt: Vlada potrdila strategijo za umetno inteligenco Ključne besede: Slovenska kulturna identiteta, Akcijski načrt, Ksenija Klampfer, Strategija, Umetna inteligenca Vlada je sprejela nacionalno strategijo za umetno inteligenco za obdobje do leta 2030. Najpozneje v devetih mesecih bo pripravljen akcijski načrt, ki bo opredelil konkretne ukrepe, nosilce, časovnice, vire financiranja in kazalnike uspešnosti. Nacionalna strategija za umetno inteligenco 2030 opredeljuje vizijo razvoja uporabe umetne intel...

#### Rank 5: NOT RELEVANT

- Title: Umetna inteligenca se je že sposobna učiti brez človekove pomoči
- Decision: not_relevant
- Rationale: AI capability article, not a new version/model.
- Category/date: znanost-in-tehnologija / 2017-10-19T14:59:55
- URL: https://www.rtvslo.si/znanost-in-tehnologija/umetna-inteligenca-se-je-ze-sposobna-uciti-brez-clovekove-pomoci/435607
- FAISS rank/score: 5 / 0.8237
- Reranker score: n/a
- Keywords: umetna inteligenca, Go, programska oprema, Google, DeepMind, AlphaGo Zero, igra go, kitajska družabna igra, samoučenje, računalniška moč, podatki, neuronka mreža, algoritmi, profesionalci, razvoj, tehnologija, inovacija, napredek
- Excerpt: Umetna inteligenca se je že sposobna učiti brez človekove pomoči Ključne besede: umetna inteligenca, Go, programska oprema, Google, DeepMind, AlphaGo Zero, igra go, kitajska družabna igra, samoučenje, računalniška moč, podatki, neuronka mreža, algoritmi, profesionalci, razvoj, tehnologija, inovacija, napredek Medmrežni velikan Google razvija umetno inteligenco, ki se je sposobna učiti brez kakršnega koli človeškega posredovanja. Googlova raziskovalna skupina Google DeepMind je naredila velik kor...


### 19. Najbolj prodajan avtomobil

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: V Sloveniji lani prodanih 8,4 odstotka več avtomobilov – največ Volkswagnovih
- Decision: relevant
- Rationale: Direct best-selling car brands/models.
- Category/date: zabava-in-slog / 2025-01-08T13:22:41
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/v-sloveniji-lani-prodanih-8-4-odstotka-vec-avtomobilov-najvec-volkswagnovih/732724
- FAISS rank/score: 1 / 0.8618
- Reranker score: n/a
- Keywords: avtomobili, Slovenija, prodaja
- Excerpt: V Sloveniji lani prodanih 8,4 odstotka več avtomobilov – največ Volkswagnovih Ključne besede: avtomobili, Slovenija, prodaja V Sloveniji je bilo lani prvič registriranih 53.018 osebnih avtomobilov, kar je 8,4 odstotka več kot predlani. Med vsemi lani prodanimi osebnimi avtomobili je bilo električnih 9876 oziroma 27 odstotkov manj kot predlani. Največ osebnih avtomobilov je prodal Volkswagen (7924 oziroma skoraj 15-odstotni tržni delež), sledila sta Renault (5910 oziroma 11,2-odstotni delež) in Š...

#### Rank 2: RELEVANT

- Title: Po skromnejšem maju se prodaja vozil v Sloveniji krepi
- Decision: relevant
- Rationale: Vehicle sales with top brands/models.
- Category/date: zabava-in-slog / 2023-07-08T09:08:41
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/po-skromnejsem-maju-se-prodaja-vozil-v-sloveniji-krepi/674464
- FAISS rank/score: 2 / 0.8546
- Reranker score: n/a
- Keywords: Prodaja vozil, škoda octavia, Tesla, avtomobilski trg, registracija vozil, rast prodaje, Slovenija, osebna vozila, gospodarska vozila, znamke, modeli vozil, elektrificirana vozila, električna vozila, hibridna vozila, registracije vozil, junij, trendi prodaje, trg vozil, statistika registracij, priključni hibridi, blagi hibridi, Volkswagen, Renault, Toyota, Škoda, Ford, Opel, vozni park
- Excerpt: Po skromnejšem maju se prodaja vozil v Sloveniji krepi Ključne besede: Prodaja vozil, škoda octavia, Tesla, avtomobilski trg, registracija vozil, rast prodaje, Slovenija, osebna vozila, gospodarska vozila, znamke, modeli vozil, elektrificirana vozila, električna vozila, hibridna vozila, registracije vozil, junij, trendi prodaje, trg vozil, statistika registracij, priključni hibridi, blagi hibridi, Volkswagen, Renault, Toyota, Škoda, Ford, Opel, vozni park Medletna rast prodaje novih vozil na avt...

#### Rank 3: RELEVANT

- Title: Tesla model Y leta 2023 najbolje prodajano vozilo v Evropi
- Decision: relevant
- Rationale: Direct best-selling vehicle.
- Category/date: zabava-in-slog / 2024-01-21T12:31:47
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/tesla-model-y-leta-2023-najbolje-prodajano-vozilo-v-evropi/695612
- FAISS rank/score: 3 / 0.8537
- Reranker score: n/a
- Keywords: Tesla, Model Y, Prodaja vozil, električni avtomobil, Evropa, prodaja, Slovenija, leta 2023, registracije, cena, konkurenca, industrija, vozila, strokovnjaki, uspeh, popularnost, Dacia Sandero, Volkswagen T-Roc, Škoda Octavia
- Excerpt: Tesla model Y leta 2023 najbolje prodajano vozilo v Evropi Ključne besede: Tesla, Model Y, Prodaja vozil, električni avtomobil, Evropa, prodaja, Slovenija, leta 2023, registracije, cena, konkurenca, industrija, vozila, strokovnjaki, uspeh, popularnost, Dacia Sandero, Volkswagen T-Roc, Škoda Octavia Električni križanec tesla Y je prvi električni avtomobil, ki je do zdaj postal najbolje prodajano vozilo v Evropi v koledarskem letu. Tesla model Y je bil v Sloveniji sedmi najbolje prodajan model avt...

#### Rank 4: RELEVANT

- Title: Prodaja električnih avtomobilov lani strmo padla, najbolj priljubljena ostajata modela Tesla 3 in Y
- Decision: relevant
- Rationale: Popular/best-selling EV models context.
- Category/date: gospodarstvo / 2025-01-24T06:40:29
- URL: https://www.rtvslo.si/gospodarstvo/prodaja-elektricnih-avtomobilov-lani-strmo-padla-najbolj-priljubljena-ostajata-modela-tesla-3-in-y/733719
- FAISS rank/score: 4 / 0.8532
- Reranker score: n/a
- Keywords: Subvencije, Električni avtomobili, prodaja
- Excerpt: Prodaja električnih avtomobilov lani strmo padla, najbolj priljubljena ostajata modela Tesla 3 in Y Ključne besede: Subvencije, Električni avtomobili, prodaja Kljub državnim subvencijam v vrednosti nekaj tisoč evrov povsem električni avtomobili (še) niso prepričali slovenskih voznikov. V letu 2024 je njihova prodaja upadla skoraj za dve petini, njihov delež na cestah pa je manjši od državnih pričakovanj. Evropska unija, kljub dvomom o ustreznosti, še ni odstopila od ambicioznega načrta, da se bo...

#### Rank 5: NOT RELEVANT

- Title: Vsako drugo prodano vozilo je športni terenec
- Decision: not_relevant
- Rationale: SUV category sales, not a best-selling car/model.
- Category/date: zabava-in-slog / 2024-07-02T10:45:00
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/vsako-drugo-prodano-vozilo-je-sportni-terenec/713448
- FAISS rank/score: 5 / 0.8496
- Reranker score: n/a
- Keywords: Prodaja vozil, SUV, športni terenec
- Excerpt: Vsako drugo prodano vozilo je športni terenec Ključne besede: Prodaja vozil, SUV, športni terenec Športni terenci so lani predstavljali skoraj polovico vseh prodanih avtomobilov na svetu. Svetovna prodaja športnih terencev se je povečala za 16 odstotkov, na 37 milijonov vozil. Novi podatki analitskega podjetja JATO Dynamics so razkrili, da so športni terenci lani predstavljali skoraj polovico celotne svetovne prodaje avtomobilov, saj so se količine prodanih kombilimuzin, karavanov in limuzin zma...


### 20. Obisk tujega predsednika

Precision@5: 4/5 = 0.80

#### Rank 1: NOT RELEVANT

- Title: Še en kratki stik med predsednico države in predsednikom vlade?
- Decision: not_relevant
- Rationale: Domestic politics around invitation, not a foreign president visit.
- Category/date: slovenija / 2024-09-03T19:19:20
- URL: https://www.rtvslo.si/slovenija/se-en-kratki-stik-med-predsednico-drzave-in-predsednikom-vlade/719914
- FAISS rank/score: 1 / 0.8431
- Reranker score: n/a
- Keywords: Politika, Slovenska politika, Nataša Pirc Musar, Robert Golob
- Excerpt: Še en kratki stik med predsednico države in predsednikom vlade? Ključne besede: Politika, Slovenska politika, Nataša Pirc Musar, Robert Golob Ali na kritične besede predsednice države zaradi vladnega povabila nekdanje izraelske zunanje ministrice na Bled pomenijo neenotno zunanjo politiko ali le vnovičen kratki stik med predsednico države in predsednikom vlade? Potem ko je vladna Levica vabilo Izraelki Cipi Livni označila za cinizem, udeležence foruma na Bledu pa pričakali protestniki, jih je po...

#### Rank 2: RELEVANT

- Title: Urad predsednice: Vlada nima pristojnosti, da bi predsednici določala, koga lahko povabi
- Decision: relevant
- Rationale: Invitation for Chinese president visit to Slovenia.
- Category/date: slovenija / 2024-11-07T17:16:05
- URL: https://www.rtvslo.si/slovenija/urad-predsednice-vlada-nima-pristojnosti-da-bi-predsednici-dolocala-koga-lahko-povabi/726737
- FAISS rank/score: 2 / 0.8382
- Reranker score: n/a
- Keywords: Vabilo, Kitajska, Zunanja politika, Predsednica, Vlada
- Excerpt: Urad predsednice: Vlada nima pristojnosti, da bi predsednici določala, koga lahko povabi Ključne besede: Vabilo, Kitajska, Zunanja politika, Predsednica, Vlada Vabilo kitajskemu predsedniku Ši Džinpingu na obisk v Slovenijo je skladno s politiko vlade, predsednica pa zanj ni potrebovala soglasja vlade, so pojasnili v uradu predsednice republike Nataše Pirc Musar. Vabilo Šiju naj bi zmotilo kabinet premierja Roberta Goloba, na zunanjem ministrstvu pa so potrdili, da so vabilo posredovali naslovni...

#### Rank 3: RELEVANT

- Title: Poljski predsednik Duda v New Yorku obiskal Trumpa
- Decision: relevant
- Rationale: Foreign president visit result.
- Category/date: svet / 2024-04-18T10:45:47
- URL: https://www.rtvslo.si/svet/preberite-tudi/poljski-predsednik-duda-v-new-yorku-obiskal-trumpa/705442
- FAISS rank/score: 3 / 0.8338
- Reranker score: n/a
- Keywords: duda, trump, zda, poljska, Poljski predsednik, Donald Trump, Srečanje, Evropa, Manhattan, Premier, Druženje, Truth Social, Prijateljstvo, Konservativni, Liberalen, Ukrajina, Rusija, Joe Biden, Volitve, Nato, Madžarska, Viktor Orban, Britanija
- Excerpt: Poljski predsednik Duda v New Yorku obiskal Trumpa Ključne besede: duda, trump, zda, poljska, Poljski predsednik, Donald Trump, Srečanje, Evropa, Manhattan, Premier, Druženje, Truth Social, Prijateljstvo, Konservativni, Liberalen, Ukrajina, Rusija, Joe Biden, Volitve, Nato, Madžarska, Viktor Orban, Britanija Poljski predsednik Andrzej Duda je v sredo obiskal nekdanjega predsednika ZDA Donalda Trumpa v njegovi stolpnici na Manhattnu. Poljski premier Donald Tusk je pred srečanjem poudaril, da od p...

#### Rank 4: RELEVANT

- Title: Vučić se je poklonil Šiju: Nikjer ne boste naleteli na tako spoštovanje in ljubezen kot v Srbiji
- Decision: relevant
- Rationale: Foreign president visit result.
- Category/date: svet / 2024-05-08T08:43:56
- URL: https://www.rtvslo.si/svet/evropa/vucic-se-je-poklonil-siju-nikjer-ne-boste-naleteli-na-tako-spostovanje-in-ljubezen-kot-v-srbiji/707468
- FAISS rank/score: 4 / 0.8338
- Reranker score: n/a
- Keywords: Srbija, Kitajska, Ši Džinping, Aleksandar Vučić, kitajski, predsednik, obletnica, NATO, napad, veleposlaništvo, Beograd, prijateljstvo, delegacija, Instagram, palača Srbije, pogovori, zastave, spoštovanje, ljubezen, zgodovina, Tajvan
- Excerpt: Vučić se je poklonil Šiju: Nikjer ne boste naleteli na tako spoštovanje in ljubezen kot v Srbiji Ključne besede: Srbija, Kitajska, Ši Džinping, Aleksandar Vučić, kitajski, predsednik, obletnica, NATO, napad, veleposlaništvo, Beograd, prijateljstvo, delegacija, Instagram, palača Srbije, pogovori, zastave, spoštovanje, ljubezen, zgodovina, Tajvan Kitajski predsednik Ši Džinping je ob obletnici Natovega napada na kitajsko veleposlaništvo obiskal Beograd, kjer se mu je srbski predsednik Aleksandar V...

#### Rank 5: RELEVANT

- Title: Ši v Pirenejih končal obisk Francije. Macron ga je pozval, naj tesno sodeluje z Evropo.
- Decision: relevant
- Rationale: Foreign president visit result.
- Category/date: svet / 2024-05-07T20:24:42
- URL: https://www.rtvslo.si/svet/evropa/si-v-pirenejih-koncal-obisk-francije-macron-ga-je-pozval-naj-tesno-sodeluje-z-evropo/707445
- FAISS rank/score: 5 / 0.8327
- Reranker score: n/a
- Keywords: Ši Džinping, Francija, Srbija, Emmanuel Macron, politični obisk, trilateralno srečanje, Evropska unija, Kitajska, Ukrajina, trgovinski odnosi, dialog, sodelovanje, Natovo bombardiranje, Zvezna republika Jugoslavija, vojna, 25. obletnica, diplomatski odnosi, mednarodna politika, konflikt, mir
- Excerpt: Ši v Pirenejih končal obisk Francije. Macron ga je pozval, naj tesno sodeluje z Evropo. Ključne besede: Ši Džinping, Francija, Srbija, Emmanuel Macron, politični obisk, trilateralno srečanje, Evropska unija, Kitajska, Ukrajina, trgovinski odnosi, dialog, sodelovanje, Natovo bombardiranje, Zvezna republika Jugoslavija, vojna, 25. obletnica, diplomatski odnosi, mednarodna politika, konflikt, mir Kitajski voditelj Ši Džinping je v Pirenejih, kjer ga je v bližini prelaza Col du Tourmalet gostil fran...

