# Precision@5 evaluation without reranker

Created: 2026-05-31T20:26:07
Relevance rule: largely related
Embedding model: `rokn/slovlo-v1`
Reranker: disabled
Retrieval: direct FAISS top 5 results, no cross-encoder reranking
Full labeled JSON output: `data/evaluation/precision_at_5_no_reranker_decisions.json`
Raw FAISS-only output: `data/evaluation/precision_at_5_no_reranker_raw_outputs.json`

## Overall result

- Total relevant results: 77/100
- Micro precision@5: 0.77
- Macro precision@5: 0.77

## Per-prompt summary

| # | Prompt | Relevant@5 | Precision@5 |
|---:|---|---:|---:|
| 1 | Vpis v srednje šole | 5/5 | 1.00 |
| 2 | Zakoni glede generativne umetne inteligence | 4/5 | 0.80 |
| 3 | Cene kart na nogometnem svetovnem prvenstvu | 4/5 | 0.80 |
| 4 | Tožba slovenskih avtoprevoznikov | 0/5 | 0.00 |
| 5 | Vojna Zvezd v Sloveniji | 1/5 | 0.20 |
| 6 | Ogromni zastoji na Slovenskih cestah | 5/5 | 1.00 |
| 7 | Višanje temperatur | 5/5 | 1.00 |
| 8 | Višanje cen nepremičnin v Sloveniji | 4/5 | 0.80 |
| 9 | Rogljič in Pogačar na tekmi | 5/5 | 1.00 |
| 10 | Donald Trump novi zakoni | 5/5 | 1.00 |
| 11 | Evropska Unija in zveza NATO | 5/5 | 1.00 |
| 12 | Velika Britanija Brexit | 5/5 | 1.00 |
| 13 | Vojna v Ukrajini in Zelenski | 5/5 | 1.00 |
| 14 | Kitajska proti ZDA | 4/5 | 0.80 |
| 15 | Korupcija v slovenski politiki | 5/5 | 1.00 |
| 16 | Izstrelitev rakete v vesolje | 5/5 | 1.00 |
| 17 | Delnice Tesle padajo | 4/5 | 0.80 |
| 18 | Nova verzija umetne inteligence | 1/5 | 0.20 |
| 19 | Najbolj prodajan avtomobil | 5/5 | 1.00 |
| 20 | Obisk tujega predsednika | 0/5 | 0.00 |

## Detailed decisions

### 1. Vpis v srednje šole

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Vpisovanje v srednje šole: izteka se zadnji rok za prijavo za opravljanje preizkusa nadarjenosti
- Decision: relevant
- Rationale: Directly about application/enrolment procedures for secondary schools.
- Category/date: slovenija / 2024-03-04T08:39:01
- URL: https://www.rtvslo.si/slovenija/vpisovanje-v-srednje-sole-izteka-se-zadnji-rok-za-prijavo-za-opravljanje-preizkusa-nadarjenosti/700309
- FAISS rank/score: 1 / 0.8194
- Reranker score: n/a
- Keywords: preizkus nadarjenosti, znanja in spretnosti, osnovna šola, prijava, skit scena, preizkus, nadarjenost, znanje, spretnosti, srednješolski programi, vpisni pogoji, športni oddelki, obvestilo, zdravniško potrdilo, preventivni pregled, športni pogoji, klasični jeziki, tuj jezik, gimnazija, obrazci, novinci, vpisna mesta, splošne gimnazije, strokovne gimnazije
- Excerpt: Vpisovanje v srednje šole: izteka se zadnji rok za prijavo za opravljanje preizkusa nadarjenosti Ključne besede: preizkus nadarjenosti, znanja in spretnosti, osnovna šola, prijava, skit scena, preizkus, nadarjenost, znanje, spretnosti, srednješolski programi, vpisni pogoji, športni oddelki, obvestilo, zdravniško potrdilo, preventivni pregled, športni pogoji, klasični jeziki, tuj jezik, gimnazija, obrazci, novinci, vpisna mesta, splošne gimnazije, strokovne gimnazije Izteka se rok za prijavo za o...

#### Rank 2: RELEVANT

- Title: Zadnji dan za vpis na izbrano srednjo šolo
- Decision: relevant
- Rationale: Directly about enrolment in a selected secondary school.
- Category/date: slovenija / 2024-04-02T09:39:24
- URL: https://www.rtvslo.si/slovenija/zadnji-dan-za-vpis-na-izbrano-srednjo-solo/703604
- FAISS rank/score: 2 / 0.8158
- Reranker score: n/a
- Keywords: Regija, Prijavnica, Mest, Gimnazija, Izobraževanje, skit scena, vpis, srednješolski programi, Ministrstvo za vzgojo in izobraževanje, prijave, izobraževalni programi, prijavni rok, srednja šola, vpisovanje, izbirni postopek, osnovno šolstvo, osrednjeslovenska regija, šolsko leto, gimnazije, poklicno izobraževanje, regije, dijaki, dijakinje, mesta za vpis, razpisana mesta, 9. razred
- Excerpt: Zadnji dan za vpis na izbrano srednjo šolo Ključne besede: Regija, Prijavnica, Mest, Gimnazija, Izobraževanje, skit scena, vpis, srednješolski programi, Ministrstvo za vzgojo in izobraževanje, prijave, izobraževalni programi, prijavni rok, srednja šola, vpisovanje, izbirni postopek, osnovno šolstvo, osrednjeslovenska regija, šolsko leto, gimnazije, poklicno izobraževanje, regije, dijaki, dijakinje, mesta za vpis, razpisana mesta, 9. razred Danes se izteče rok za prijavo za vpis v srednješolske p...

#### Rank 3: RELEVANT

- Title: V srednje šole sprejetih 22.127 bodočih dijakov, na voljo je bilo 25.444 vpisnih mest
- Decision: relevant
- Rationale: Directly about accepted future secondary-school students and places.
- Category/date: slovenija / 2023-07-03T08:56:03
- URL: https://www.rtvslo.si/slovenija/v-srednje-sole-sprejetih-22-127-bodocih-dijakov-na-voljo-je-bilo-25-444-vpisnih-mest/673860
- FAISS rank/score: 3 / 0.8157
- Reranker score: n/a
- Keywords: Srednje šole, dijaki, vpis, prosta mesta, ministrstvo, vzgoja, izobraževanje, srednješolski programi, prijavno-vpisni postopek, novinci, razpisana mesta, poklicno izobraževanje, gimnazije, omejitev vpisa, izbirni postopek, želeno šolo, drugi krog, mest, šole
- Excerpt: V srednje šole sprejetih 22.127 bodočih dijakov, na voljo je bilo 25.444 vpisnih mest Ključne besede: Srednje šole, dijaki, vpis, prosta mesta, ministrstvo, vzgoja, izobraževanje, srednješolski programi, prijavno-vpisni postopek, novinci, razpisana mesta, poklicno izobraževanje, gimnazije, omejitev vpisa, izbirni postopek, želeno šolo, drugi krog, mest, šole Ministrstvo za vzgojo in izobraževanje je objavilo število še prostih mest za vpis v 1. letnik posameznih srednješolskih programov. Kandida...

#### Rank 4: RELEVANT

- Title: Zadnji dan za prijavo v srednje šole in dijaške domove
- Decision: relevant
- Rationale: Directly about applications to secondary schools and dormitories.
- Category/date: slovenija / 2025-04-02T09:43:41
- URL: https://www.rtvslo.si/slovenija/zadnji-dan-za-prijavo-v-srednje-sole-in-dijaske-domove/741401
- FAISS rank/score: 4 / 0.8140
- Reranker score: n/a
- Keywords: Izbirni postopek, Vpisna mesta, Dijaški domovi, Srednje šole, Prijave
- Excerpt: Zadnji dan za prijavo v srednje šole in dijaške domove Ključne besede: Izbirni postopek, Vpisna mesta, Dijaški domovi, Srednje šole, Prijave Izteka se rok za oddajo prijavnice za vpis novincev v srednje šole in dijaške domove za šolsko leto 2025/26. Letos jo je po novem mogoče oddati elektronsko. Stanje prijav po posameznih programih oz. šolah bo ministrstvo objavilo najpozneje do 8. aprila, do 6. maja pa bodo lahko nato učenci svojo prijavo prenesli v drug program. Osnovno šolo v letošnjem šols...

#### Rank 5: RELEVANT

- Title: Vpis je omejen na 58 srednjih šolah, povečal se je vpis v srednje in nižje poklicne šole
- Decision: relevant
- Rationale: Directly about enrolment limits and enrolment in secondary/vocational schools.
- Category/date: slovenija / 2024-05-23T11:08:23
- URL: https://www.rtvslo.si/slovenija/vpis-je-omejen-na-58-srednjih-solah-povecal-se-je-vpis-v-srednje-in-nizje-poklicne-sole/709285
- FAISS rank/score: 5 / 0.8123
- Reranker score: n/a
- Keywords: Ministrstvo za vzgojo in izobraževanje, Gimnazijski programi, Poklicno izobraževanje, Srednje šole, Vpis
- Excerpt: Vpis je omejen na 58 srednjih šolah, povečal se je vpis v srednje in nižje poklicne šole Ključne besede: Ministrstvo za vzgojo in izobraževanje, Gimnazijski programi, Poklicno izobraževanje, Srednje šole, Vpis Prihodnje šolsko leto bo srednje šole obiskovalo 22.971 kandidatov, največ, 42,7 odstotka, se jih je vpisalo v srednje strokovne šole, sledijo gimnazije, srednje poklicne in nižje poklicne šole. Vpis bo omejen na 58 šolah, medtem ko je bil lani na 70. Vpis je omejen v 12 programih poklicne...


### 2. Zakoni glede generativne umetne inteligence

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: Vlada sprejela predlog, ki prinaša enotna pravila za razvoj in uporabo umetne inteligence v EU-ju
- Decision: relevant
- Rationale: Directly about a proposed law and EU rules for artificial intelligence.
- Category/date: slovenija / 2025-08-21T15:32:29
- URL: https://www.rtvslo.si/slovenija/vlada-sprejela-predlog-ki-prinasa-enotna-pravila-za-razvoj-in-uporabo-umetne-inteligence-v-eu-ju/755310
- FAISS rank/score: 1 / 0.7996
- Reranker score: n/a
- Keywords: UI, zakon, evropska uredba
- Excerpt: Vlada sprejela predlog, ki prinaša enotna pravila za razvoj in uporabo umetne inteligence v EU-ju Ključne besede: UI, zakon, evropska uredba Vlada je sprejela predlog zakona o izvajanju evropske uredbe o določitvi harmoniziranih pravil o umetni inteligenci oz. akta o umetni inteligenci. Predlog med drugim določa nadzorne organe in uvaja možnost imenovanja komisarja za etiko umetne inteligence. Akt o umetni inteligenci, katerega namen je izboljšati delovanje notranjega trga z uvedbo enotnih pravi...

#### Rank 2: RELEVANT

- Title: Informacijski pooblaščenec poziva k spoštovanju pravil iz akta o umetni inteligenci
- Decision: relevant
- Rationale: Directly about rules from the AI Act.
- Category/date: slovenija / 2025-02-05T14:04:28
- URL: https://www.rtvslo.si/slovenija/preberite-tudi/informacijski-pooblascenec-poziva-k-spostovanju-pravil-iz-akta-o-umetni-inteligenci/735665
- FAISS rank/score: 2 / 0.7991
- Reranker score: n/a
- Keywords: Prepovedane prakse, Čustva posameznikov, Družbeno ocenjevanje, Umetna inteligenca, Informacijski pooblaščenec
- Excerpt: Informacijski pooblaščenec poziva k spoštovanju pravil iz akta o umetni inteligenci Ključne besede: Prepovedane prakse, Čustva posameznikov, Družbeno ocenjevanje, Umetna inteligenca, Informacijski pooblaščenec Informacijski pooblaščenec opozarja, da je od 2. februarja treba upoštevati prva pravila iz akta o umetni inteligenci, in sicer glede prepovedi uporabe določenih sistemov umetne inteligence. Med drugim so prepovedani sistemi za družbeno ocenjevanje ter sklepanje o čustvih posameznikov v šo...

#### Rank 3: RELEVANT

- Title: ZPS: Umetna inteligenca prinaša tudi negativne posledice – kršenje zasebnosti in osebne integritete
- Decision: relevant
- Rationale: About generative AI, consumer rights, legislation and regulation.
- Category/date: gospodarstvo / 2023-06-20T13:58:03
- URL: https://www.rtvslo.si/gospodarstvo/zps-umetna-inteligenca-prinasa-tudi-negativne-posledice-krsenje-zasebnosti-in-osebne-integritete/672448
- FAISS rank/score: 3 / 0.7911
- Reranker score: n/a
- Keywords: Generativna umetna inteligenca, ZPS, Chat GPT, umetna inteligenca, potrošniki, tehnologija, aplikacija, pravice, zaupanje, varnost, kršenje zasebnosti, internet, digitalna politika, zakonodaja, Evropska unija, regulativa, ozaveščanje, opolnomočenje, lobiranje
- Excerpt: ZPS: Umetna inteligenca prinaša tudi negativne posledice – kršenje zasebnosti in osebne integritete Ključne besede: Generativna umetna inteligenca, ZPS, Chat GPT, umetna inteligenca, potrošniki, tehnologija, aplikacija, pravice, zaupanje, varnost, kršenje zasebnosti, internet, digitalna politika, zakonodaja, Evropska unija, regulativa, ozaveščanje, opolnomočenje, lobiranje V zadnjih mesecih je prišlo do bliskovite rasti ponudbe storitev, ki jih poganja generativna umetna inteligenca, ta pa ogrož...

#### Rank 4: NOT RELEVANT

- Title: Razpis za nacionalno platformo za umetno inteligenco deli mnenja v stroki
- Decision: not_relevant
- Rationale: About a public tender/platform for generative AI, not mainly laws or regulation.
- Category/date: znanost-in-tehnologija / 2025-12-15T08:03:13
- URL: https://www.rtvslo.si/znanost-in-tehnologija/razpis-za-nacionalno-platformo-za-umetno-inteligenco-deli-mnenja-v-stroki/767256
- FAISS rank/score: 4 / 0.7899
- Reranker score: n/a
- Keywords: Licenciranje, Tehnološka suverenost, Razpis, ChatGPT, Generativna umetna inteligenca
- Excerpt: Razpis za nacionalno platformo za umetno inteligenco deli mnenja v stroki Ključne besede: Licenciranje, Tehnološka suverenost, Razpis, ChatGPT, Generativna umetna inteligenca Končalo se je razpisno zbiranje ponudb za nacionalno platformo umetne inteligence, s katero naj bi državljanom omogočili dostop do najzmogljivejših modelov umetne inteligence. Mnenja o upravičenosti takšne naložbe so različna. Danes marsikdo že uporablja orodja generativne umetne inteligence, kot je ChatGPT, predvsem brezpl...

#### Rank 5: RELEVANT

- Title: Ali umetna inteligenca loči sekstanje od spolnih zlorab?
- Decision: relevant
- Rationale: About EU regulation of AI and related digital/child-protection rules.
- Category/date: slovenija / 2023-09-28T06:15:45
- URL: https://www.rtvslo.si/slovenija/ali-umetna-inteligenca-loci-sekstanje-od-spolnih-zlorab/682895
- FAISS rank/score: 5 / 0.7869
- Reranker score: n/a
- Keywords: tehnologija, pravila, zakonodaja, uredba, skit scena, regulacija, Evropska unija, umetna inteligenca, varovanje podatkov, digitalni trg, digitalne storitve, nevladne organizacije, nadzor komunikacij, kibernetska varnost, otroci, mladi, digitalni prostor, človekove pravice, spolna zloraba, varnost, vključevanje
- Excerpt: Ali umetna inteligenca loči sekstanje od spolnih zlorab? Ključne besede: tehnologija, pravila, zakonodaja, uredba, skit scena, regulacija, Evropska unija, umetna inteligenca, varovanje podatkov, digitalni trg, digitalne storitve, nevladne organizacije, nadzor komunikacij, kibernetska varnost, otroci, mladi, digitalni prostor, človekove pravice, spolna zloraba, varnost, vključevanje Hiter razvoj novih tehnologij je obljubljal marsikaj, a smo se tako kot z vsako novo tehnologijo najprej precej moč...


### 3. Cene kart na nogometnem svetovnem prvenstvu

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: Tožba proti Fifi zaradi visokih cen vstopnic na SP 2026
- Decision: relevant
- Rationale: Directly about a lawsuit over high FIFA World Cup 2026 ticket prices.
- Category/date: sport / 2026-03-24T11:22:40
- URL: https://www.rtvslo.si/sport/nogomet/tozba-proti-fifi-zaradi-visokih-cen-vstopnic-na-sp-2026/777332
- FAISS rank/score: 1 / 0.7799
- Reranker score: n/a
- Keywords: vstopnice, cene, svetovno prvenstvo, nogomet
- Excerpt: Tožba proti Fifi zaradi visokih cen vstopnic na SP 2026 Ključne besede: vstopnice, cene, svetovno prvenstvo, nogomet Združenje nogometnih navijačev Evrope (FSE) je pri Evropski komisiji vložilo tožbo proti Mednarodni nogometni zvezi (Fifa) zaradi previsokih cen vstopnic na letošnjem svetovnem prvenstvu, ki bo v ZDA, Kanadi in Mehiki. "Fifa ima monopol nad prodajo vstopnic za svetovno prvenstvo 2026 in to moč je izkoristila za vsiljevanje pogojev nogometnim privržencem, ki v konkurenčnem tržnem o...

#### Rank 2: RELEVANT

- Title: Infantino zagovarja visoke cene vstopnic in pravi, da bodo ves denar vložili spet v nogomet
- Decision: relevant
- Rationale: Directly about high ticket prices for the football World Cup.
- Category/date: sport / 2025-12-30T08:47:57
- URL: https://www.rtvslo.si/sport/nogomet/infantino-zagovarja-visoke-cene-vstopnic-in-pravi-da-bodo-ves-denar-vlozili-spet-v-nogomet/768669
- FAISS rank/score: 2 / 0.7688
- Reranker score: n/a
- Keywords: Gianni Infantino, Fifa, SP, vstopnice
- Excerpt: Infantino zagovarja visoke cene vstopnic in pravi, da bodo ves denar vložili spet v nogomet Ključne besede: Gianni Infantino, Fifa, SP, vstopnice Predsednik Mednarodne nogometne zveze Fife Gianni Infantino zagovarja visoke cene vstopnic za prihajajoče svetovno prvenstvo. Infantino je dejal, da cene vstopnic zgolj odražajo trenutno povpraševanje po njih. Združenje nogometnih navijačev (FSA) je od začetka prodaje vstopnic za tekmovanje, ki bo med 11. junijem in 19. julijem prihodnje leto potekalo...

#### Rank 3: RELEVANT

- Title: Ogromno povpraševanje za nogometni spektakel leta
- Decision: relevant
- Rationale: Directly about FIFA ticket demand/sales for the football World Cup.
- Category/date: sport / 2026-01-15T16:54:35
- URL: https://www.rtvslo.si/sport/nogomet/svetovno-prvenstvo-v-nogometu/ogromno-povprasevanje-za-nogometni-spektakel-leta/770262
- FAISS rank/score: 3 / 0.7639
- Reranker score: n/a
- Keywords: Fifa, Navijači, Prodaja vstopnic, Nogometni dogodek
- Excerpt: Ogromno povpraševanje za nogometni spektakel leta Ključne besede: Fifa, Navijači, Prodaja vstopnic, Nogometni dogodek V zadnjem delu prodaje je mednarodna nogometna zveza (Fifa) prejela več kot pol milijarde zahtevkov za vstopnice za ogled tekem letošnjega svetovnega prvenstva, ki bo poleti potekalo v ZDA, Kanadi in Mehiki. Prodaja vstopnic se je začela 11. decembra in je trajala do 13. januarja. Prvič so bile naprodaj posamezne vstopnice za določene tekme. Navijači bodo o morebitnem uspehu v na...

#### Rank 4: NOT RELEVANT

- Title: Zasoljene cene vstopnic za slovenske tekme v Zagrebu
- Decision: not_relevant
- Rationale: About handball World Cup tickets, not football World Cup tickets.
- Category/date: sport / 2025-01-13T15:29:38
- URL: https://www.rtvslo.si/sport/rokomet/sp-v-rokometu-2025/zasoljene-cene-vstopnic-za-slovenske-tekme-v-zagrebu/733223
- FAISS rank/score: 4 / 0.7609
- Reranker score: n/a
- Keywords: Cene, Slovenija, Svetovno prvenstvo, Zagreb, Vstopnice
- Excerpt: Zasoljene cene vstopnic za slovenske tekme v Zagrebu Ključne besede: Cene, Slovenija, Svetovno prvenstvo, Zagreb, Vstopnice Slovenski rokometaši bodo skupinski del svetovnega prvenstva ter morebitna četrtfinale in polfinale odigrali v Zagrebu. Pričakuje se veliko slovenskih navijačev, a vstopnice nikakor niso poceni. Še več, zagrebška Arena bo imela v prvem delu najdražje vstopnice, dražje tudi od tistih na Danskem in Norveškem, ki sta soorganizatorici svetovnega prvenstva. Slovenija se bo v prv...

#### Rank 5: RELEVANT

- Title: Fifa začela prodajo vstopnic za SP 2026
- Decision: relevant
- Rationale: Directly about FIFA starting ticket sales for football World Cup 2026.
- Category/date: sport / 2025-09-10T15:48:43
- URL: https://www.rtvslo.si/sport/nogomet/fifa-zacela-prodajo-vstopnic-za-sp-2026/757188
- FAISS rank/score: 5 / 0.7542
- Reranker score: n/a
- Keywords: Nogomet, SP v nogometu, Vstopnice
- Excerpt: Fifa začela prodajo vstopnic za SP 2026 Ključne besede: Nogomet, SP v nogometu, Vstopnice Devet mesecev pred začetkom nogometnega svetovnega prvenstva 2026 v Mehiki, Kanadi in ZDA je Mednarodna nogometna zveza začela prodajo vstopnic. Danes popoldan se na spletni strani Fife začenja prva faza, šele naključni izbor pa bo pokazal, kdo bo prejel prve vstopnice za ogled skupaj kar 104 tekem SP-ja, poroča nemška tiskovna agencija DPA. Za prvo fazo nakupa vstopnic navijači za registracijo na spletni s...


### 4. Tožba slovenskih avtoprevoznikov

Precision@5: 0/5 = 0.00

#### Rank 1: NOT RELEVANT

- Title: Številni vozniki tožijo Renault zaradi težav, oglasili so se tudi slovenski lastniki
- Decision: not_relevant
- Rationale: About drivers/owners suing Renault, not Slovenian hauliers.
- Category/date: zabava-in-slog / 2023-07-09T21:45:52
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/stevilni-vozniki-tozijo-renault-zaradi-tezav-oglasili-so-se-tudi-slovenski-lastniki/674591
- FAISS rank/score: 1 / 0.7848
- Reranker score: n/a
- Keywords: Renault, tožba, težave z motorjem, 1.2 TCe, težave, motor, avtomobil, 1,2-litrski, lastniki, Nissan, Dacia, vozniki, olje, pregrevanje, odpoklic, garancija, servis, odškodnina, sodišče, napaka, rešitev, kolektivna tožba
- Excerpt: Številni vozniki tožijo Renault zaradi težav, oglasili so se tudi slovenski lastniki Ključne besede: Renault, tožba, težave z motorjem, 1.2 TCe, težave, motor, avtomobil, 1,2-litrski, lastniki, Nissan, Dacia, vozniki, olje, pregrevanje, odpoklic, garancija, servis, odškodnina, sodišče, napaka, rešitev, kolektivna tožba Pred mesecem dni je skoraj 1800 francoskih lastnikov avtomobilov vložilo tožbo proti podjetju Renault zaradi težav z 1,2-litrskim motorjem, ki je bil med letoma 2012 in 2016 vgraj...

#### Rank 2: NOT RELEVANT

- Title: Konvoj tovornih vozil za izredni prevoz vozil brez dovoljenj
- Decision: not_relevant
- Rationale: About an illegal oversized transport convoy, not a lawsuit by hauliers.
- Category/date: crna-kronika / 2024-05-28T17:01:56
- URL: https://www.rtvslo.si/crna-kronika/konvoj-tovornih-vozil-za-izredni-prevoz-vozil-brez-dovoljenj/709889
- FAISS rank/score: 2 / 0.7658
- Reranker score: n/a
- Keywords: Prekrškovni postopki, Energetski transformatorji, Brez dovoljenj, Izredni prevoz, Konvoj tovornih vozil
- Excerpt: Konvoj tovornih vozil za izredni prevoz vozil brez dovoljenj Ključne besede: Prekrškovni postopki, Energetski transformatorji, Brez dovoljenj, Izredni prevoz, Konvoj tovornih vozil Ljubljanski prometni policisti so prejšnji teden na gorenjski avtocesti ustavili konvoj tovornih vozil za izredni prevoz, ki je vozil brez predpisanih dovoljenj. Vozila so izločili iz prometa, voznikom in pravnim osebam pa izdali globe. Policisti postaje prometne policije Ljubljana so v noči na petek na gorenjski avto...

#### Rank 3: NOT RELEVANT

- Title: Število kršitev prepovedi prehitevanja za tovornjake na avtocestah se je povečalo za četrtino
- Decision: not_relevant
- Rationale: About truck overtaking violations, not a lawsuit by hauliers.
- Category/date: crna-kronika / 2023-06-10T11:31:00
- URL: https://www.rtvslo.si/crna-kronika/stevilo-krsitev-prepovedi-prehitevanja-za-tovornjake-na-avtocestah-se-je-povecalo-za-cetrtino/671352
- FAISS rank/score: 3 / 0.7633
- Reranker score: n/a
- Keywords: tovornjaki, prehitevanje, avtocesta, prekrški, Statistika, Policija, Tovorna vozila, Kršitve, Omejitev, Varnost, Promet, Pobuda, Ministrstvo, Nadzor, Ugotavljanje, Epidemija, Covid-19, Prilagoditev, Kadri, Postaje, Tovorni promet, Zgostitev
- Excerpt: Število kršitev prepovedi prehitevanja za tovornjake na avtocestah se je povečalo za četrtino Ključne besede: tovornjaki, prehitevanje, avtocesta, prekrški, Statistika, Policija, Tovorna vozila, Kršitve, Omejitev, Varnost, Promet, Pobuda, Ministrstvo, Nadzor, Ugotavljanje, Epidemija, Covid-19, Prilagoditev, Kadri, Postaje, Tovorni promet, Zgostitev Statistični podatki policije kažejo, da se število ugotovljenih kršitev prepovedi prehitevanja tovornih vozil na avtocesti povečuje. Do 18. maja jih...

#### Rank 4: NOT RELEVANT

- Title: AVP: Pri voznikih tovornjakov letos ugotovljenih 15,8 odstotka več prekrškov kot lani
- Decision: not_relevant
- Rationale: About truck-driver violations, not a lawsuit by hauliers.
- Category/date: slovenija / 2023-05-13T14:55:00
- URL: https://www.rtvslo.si/slovenija/avp-pri-voznikih-tovornjakov-letos-ugotovljenih-15-8-odstotka-vec-prekrskov-kot-lani/668042
- FAISS rank/score: 4 / 0.7616
- Reranker score: n/a
- Keywords: Preventivna akcija", tovornjaki, avtobusi, AVP, prekrški, vozniki, tovorna vozila, varnost, prometne nesreče, agencija, preventivne akcije, prometni predpisi, hitrost, mobilni telefoni, varnostni pas, prehitevanje, odgovornost, policija, evropske države, nacionalne akcije, utrujenost, Evropska komisija, prometna policija, cestni promet
- Excerpt: AVP: Pri voznikih tovornjakov letos ugotovljenih 15,8 odstotka več prekrškov kot lani Ključne besede: Preventivna akcija", tovornjaki, avtobusi, AVP, prekrški, vozniki, tovorna vozila, varnost, prometne nesreče, agencija, preventivne akcije, prometni predpisi, hitrost, mobilni telefoni, varnostni pas, prehitevanje, odgovornost, policija, evropske države, nacionalne akcije, utrujenost, Evropska komisija, prometna policija, cestni promet Pristojni opažajo vse več kršitev voznikov tovornih vozil, z...

#### Rank 5: NOT RELEVANT

- Title: Požigalci vozil, ki so povzročili za najmanj pol milijona evrov škode, obsojeni na zapor
- Decision: not_relevant
- Rationale: About vehicle arson convictions, not a lawsuit by hauliers.
- Category/date: crna-kronika / 2024-07-12T15:49:34
- URL: https://www.rtvslo.si/crna-kronika/pozigalci-vozil-ki-so-povzrocili-za-najmanj-pol-milijona-evrov-skode-obsojeni-na-zapor/714653
- FAISS rank/score: 5 / 0.7606
- Reranker score: n/a
- Keywords: Požigalec, Požigalci, Požigalci Maribor
- Excerpt: Požigalci vozil, ki so povzročili za najmanj pol milijona evrov škode, obsojeni na zapor Ključne besede: Požigalec, Požigalci, Požigalci Maribor Štirje mladeniči so bili zaradi požigov avtomobilov, tovornih vozil in avtobusa obsojeni na večletne zaporne kazni. Četverica je sklenila sporazum s tožilstvom, medtem ko petega obdolženega čaka sojenje. Eno vodilnih vlog pri požigih je imel Dario Vaupotič, ki je bil prisoten pri vseh več kot 20 primerih in je praviloma tudi poskrbel za vžige vozil na r...


### 5. Vojna Zvezd v Sloveniji

Precision@5: 1/5 = 0.20

#### Rank 1: NOT RELEVANT

- Title: Letalstvo Slovenske vojske se je preoblikovalo v brigado
- Decision: not_relevant
- Rationale: False match on Slovenian army/air defence, not Star Wars.
- Category/date: slovenija / 2024-05-09T17:24:23
- URL: https://www.rtvslo.si/slovenija/letalstvo-slovenske-vojske-se-je-preoblikovalo-v-brigado/707703
- FAISS rank/score: 1 / 0.7257
- Reranker score: n/a
- Keywords: vojska, letalstvo, brigada, vojašnica, slovesnost, brigade, vojaško letalstvo, zračna obramba, bataljon, minister, modernizacija, oprema, kadri, oborožene sile, Nato, poveljnik, sistem, usposabljanje, letalo, helikopter, evropski, obramba
- Excerpt: Letalstvo Slovenske vojske se je preoblikovalo v brigado Ključne besede: vojska, letalstvo, brigada, vojašnica, slovesnost, brigade, vojaško letalstvo, zračna obramba, bataljon, minister, modernizacija, oprema, kadri, oborožene sile, Nato, poveljnik, sistem, usposabljanje, letalo, helikopter, evropski, obramba V Vojašnici Jerneja Molana v Cerkljah ob Krki je potekala slovesnost ob ustanovitvi 15. brigade vojaškega letalstva in zračne obrambe ter 9. bataljona zračne obrambe. Minister Šarec je v n...

#### Rank 2: RELEVANT

- Title: Po svetu praznujejo dan Vojne zvezd
- Decision: relevant
- Rationale: Directly about Star Wars day and mentions Slovenia in the article metadata/text.
- Category/date: zabava-in-slog / 2023-05-04T17:09:00
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/po-svetu-praznujejo-dan-vojne-zvezd/667027
- FAISS rank/score: 2 / 0.7198
- Reranker score: n/a
- Keywords: Vojna zvezd, Star Wars, May the fourth be with you, franšiza, filmi, kultura, popularni, datum, praznovanje, Luka Skywalker, George Lucas, animirani, igralci, televizijske serije, igrače, videoigre, Lego, BioWare, Slovenija, otroci, liki, imena
- Excerpt: Po svetu praznujejo dan Vojne zvezd Ključne besede: Vojna zvezd, Star Wars, May the fourth be with you, franšiza, filmi, kultura, popularni, datum, praznovanje, Luka Skywalker, George Lucas, animirani, igralci, televizijske serije, igrače, videoigre, Lego, BioWare, Slovenija, otroci, liki, imena Ljubitelji ene največjih znanstvenofantastičnih franšiz na svetu že od leta 2011 četrtega maja praznujejo dan Vojne zvezd. Kultni filmi so vse od prvenca leta 1977 premikali meje žanra in se zasidrali gl...

#### Rank 3: NOT RELEVANT

- Title: Razstava in akademija ob 30-letnici Zveze veteranov vojne za Slovenijo
- Decision: not_relevant
- Rationale: False match on war veterans in Slovenia, not Star Wars.
- Category/date: slovenija / 2023-10-10T20:54:03
- URL: https://www.rtvslo.si/slovenija/preberite-tudi/razstava-in-akademija-ob-30-letnici-zveze-veteranov-vojne-za-slovenijo/684406
- FAISS rank/score: 3 / 0.7164
- Reranker score: n/a
- Keywords: Nataša Pirc Musar, Mitja Jankovič, 30-letnica delovanja, Zveza veteranov vojne za Slovenijo, Razstava, veterani, vojna za Slovenijo, slavnostna akademija, Ljubljana, Zveza veteranov, osamosvojitvena vojna, predsednica republike, pomembne funkcije, dialog, profesionalnost, mladi, spomin, generacije, teritorialna obramba, pravice, dedje, očetje, izobraževanje, skupščina.
- Excerpt: Razstava in akademija ob 30-letnici Zveze veteranov vojne za Slovenijo Ključne besede: Nataša Pirc Musar, Mitja Jankovič, 30-letnica delovanja, Zveza veteranov vojne za Slovenijo, Razstava, veterani, vojna za Slovenijo, slavnostna akademija, Ljubljana, Zveza veteranov, osamosvojitvena vojna, predsednica republike, pomembne funkcije, dialog, profesionalnost, mladi, spomin, generacije, teritorialna obramba, pravice, dedje, očetje, izobraževanje, skupščina. Zveza veteranov vojne za Slovenijo je ob...

#### Rank 4: NOT RELEVANT

- Title: Vlada sprejela letni načrt investicij v Slovenski vojski za leto 2025
- Decision: not_relevant
- Rationale: About Slovenian army investments, not Star Wars.
- Category/date: slovenija / 2025-11-26T15:56:55
- URL: https://www.rtvslo.si/slovenija/preberite-tudi/vlada-sprejela-letni-nacrt-investicij-v-slovenski-vojski-za-leto-2025/765345
- FAISS rank/score: 4 / 0.7129
- Reranker score: n/a
- Keywords: vlada, SV, investicije
- Excerpt: Vlada sprejela letni načrt investicij v Slovenski vojski za leto 2025 Ključne besede: vlada, SV, investicije Vlada je sprejela letni načrt investicij v Slovenski vojski za leto 2025. Obrambno ministrstvo letos izvaja projekte, namenjene izgradnji bataljonske bojne skupine in enote za specialno delovanje. Za investicije je načrtovanih več kot 34 milijonov evrov. Ministrstvo za obrambo bo letos uresničilo tudi prevzete finančne obveznosti za zračno obrambo in artilerijo. Cilj investiranja v zračno...

#### Rank 5: NOT RELEVANT

- Title: Modernizacija slovenske vojske: Pet ponudb za osemkolesnike in nov sistem zračne obrambe
- Decision: not_relevant
- Rationale: About Slovenian army modernization, not Star Wars.
- Category/date: slovenija / 2023-07-12T07:18:29
- URL: https://www.rtvslo.si/slovenija/modernizacija-slovenske-vojske-pet-ponudb-za-osemkolesnike-in-nov-sistem-zracne-obrambe/674791
- FAISS rank/score: 5 / 0.7100
- Reranker score: n/a
- Keywords: slovenska vojska, Nato, Marjan Šarec, Globus, vojska, obramba, Natu, zaveze, modernizacija, bremena, podpolkovnik, vojak, tajno, brigada, motorizirana četa, logistična četa, vojaška policija, obljube, organizacija, zmogljivost, vojaška vozila, vojaška oprema, oborožene sile
- Excerpt: Modernizacija slovenske vojske: Pet ponudb za osemkolesnike in nov sistem zračne obrambe Ključne besede: slovenska vojska, Nato, Marjan Šarec, Globus, vojska, obramba, Natu, zaveze, modernizacija, bremena, podpolkovnik, vojak, tajno, brigada, motorizirana četa, logistična četa, vojaška policija, obljube, organizacija, zmogljivost, vojaška vozila, vojaška oprema, oborožene sile Minister za obrambo Marjan Šarec je tik pred odhodom na vrh zveze Nato v Vilno poudaril, da mora Slovenija izpolniti zav...


### 6. Ogromni zastoji na Slovenskih cestah

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Na avtocestah nastajajo zastoji, pot od Razdrtega do Ljubljane se podaljša za 45 minut
- Decision: relevant
- Rationale: Directly about highway traffic jams and delays.
- Category/date: slovenija / 2023-07-29T12:30:06
- URL: https://www.rtvslo.si/slovenija/na-avtocestah-nastajajo-zastoji-pot-od-razdrtega-do-ljubljane-se-podaljsa-za-45-minut/676502
- FAISS rank/score: 1 / 0.8296
- Reranker score: n/a
- Keywords: Potovalni čas, Gneča na cestah, Zastoji na avtocestah, promet, zastoji, avtocesta, hitra cesta, ceste, prometnoinformacijski center, zamuda, gneča, zapora, Jesenice, Avstrija, Postojna, Logatec, Vrhnika, Izola, Strunjan, Škofije, Koper, Karavanke, Štajerska
- Excerpt: Na avtocestah nastajajo zastoji, pot od Razdrtega do Ljubljane se podaljša za 45 minut Ključne besede: Potovalni čas, Gneča na cestah, Zastoji na avtocestah, promet, zastoji, avtocesta, hitra cesta, ceste, prometnoinformacijski center, zamuda, gneča, zapora, Jesenice, Avstrija, Postojna, Logatec, Vrhnika, Izola, Strunjan, Škofije, Koper, Karavanke, Štajerska Promet na slovenskih cestah je zgoščen. Zastoji tako nastajajo na primorski avtocesti v obe smeri in na gorenjski avtocesti v smeri Karavan...

#### Rank 2: RELEVANT

- Title: Na nekaterih cestah zaradi del, nesreč in prireditev gneča in zastoji
- Decision: relevant
- Rationale: Directly about road congestion and traffic jams.
- Category/date: slovenija / 2025-06-15T11:39:30
- URL: https://www.rtvslo.si/slovenija/na-nekaterih-cestah-zaradi-del-nesrec-in-prireditev-gneca-in-zastoji/749055
- FAISS rank/score: 2 / 0.8205
- Reranker score: n/a
- Keywords: Prometnoinformacijski center, Maraton Franja, Prometna nesreča, Štajerska avtocesta, Zastoji
- Excerpt: Na nekaterih cestah zaradi del, nesreč in prireditev gneča in zastoji Ključne besede: Prometnoinformacijski center, Maraton Franja, Prometna nesreča, Štajerska avtocesta, Zastoji Na cestah je ponekod na območju turističnih krajev gostejši promet, zastoji pa nastajajo tudi zaradi del na cestah, nesreč in prireditev. Trenutno zastoji nastajajo v obe smeri na cestah Sečovlje–Izola in Dragonja–Koper pri Orešju. Na hitri cesti Koper–Škofije je zaprt prehitevalni pas pri uvozu Koper center proti Ljubl...

#### Rank 3: RELEVANT

- Title: Številni zastoji na cestah in avtocestah
- Decision: relevant
- Rationale: Directly about many jams on roads and highways.
- Category/date: slovenija / 2025-06-05T09:22:05
- URL: https://www.rtvslo.si/slovenija/stevilni-zastoji-na-cestah-in-avtocestah/748004
- FAISS rank/score: 3 / 0.8201
- Reranker score: n/a
- Keywords: Reševalni pas, Prometno informacijski center, Zastoji, Gorenska avtocesta, Nesreča
- Excerpt: Številni zastoji na cestah in avtocestah Ključne besede: Reševalni pas, Prometno informacijski center, Zastoji, Gorenska avtocesta, Nesreča Na gorenjski avtocesti med Brnikom in Vodicami proti Ljubljani so posledice prometne nesreče odstranjene. Zastoji so na štajerski avtocesti med Dramljami in predorom Pletovarje proti Mariboru, zamuda je 10 - 15 minut inna primorski avtocesti med Nanosom in Gabrkom proti Kopru. Trenutno so zastoji tudi na cestah Medvode - Ljubljana, Dragonja - Šmarje in Lesce...

#### Rank 4: RELEVANT

- Title: Zastoji na primorski, štajerski in gorenjski avtocesti
- Decision: relevant
- Rationale: Directly about jams on Slovenian highways.
- Category/date: slovenija / 2023-05-27T13:21:00
- URL: https://www.rtvslo.si/slovenija/zastoji-na-primorski-stajerski-in-gorenjski-avtocesti/669708
- FAISS rank/score: 4 / 0.8195
- Reranker score: n/a
- Keywords: zastoji, avtocesta, promet, štajerska avtocesta, Trojane, Maribor, zastoj, Šentilj, razcep Dragučova, Fram, Slovenska Bistrica, Ljubljana, prometnoinformacijski center, avstrijska stran, predor Karavanke, Gorenjska avtocesta, Jesenice, Primorska avtocesta, razcep Nanos, Koper, prometna nesreča, Brezovica, Vrhnika
- Excerpt: Zastoji na primorski, štajerski in gorenjski avtocesti Ključne besede: zastoji, avtocesta, promet, štajerska avtocesta, Trojane, Maribor, zastoj, Šentilj, razcep Dragučova, Fram, Slovenska Bistrica, Ljubljana, prometnoinformacijski center, avstrijska stran, predor Karavanke, Gorenjska avtocesta, Jesenice, Primorska avtocesta, razcep Nanos, Koper, prometna nesreča, Brezovica, Vrhnika Na štajerski avtocesti je v predoru Trojane proti Mariboru zaprt vozni pas, zastoj nastaja tudi iz smeri Šentilja...

#### Rank 5: RELEVANT

- Title: V več državah dela prost dan, na avtocestah so bili zastoji
- Decision: relevant
- Rationale: Directly about highway jams.
- Category/date: slovenija / 2023-06-08T08:19:00
- URL: https://www.rtvslo.si/slovenija/v-vec-drzavah-dela-prost-dan-na-avtocestah-so-bili-zastoji/671058
- FAISS rank/score: 5 / 0.8144
- Reranker score: n/a
- Keywords: Promet, prazniki, gneča, katoliški praznik, rešnje telo, kri, telovo, Avstrija, Nemčija, Hrvaška, prost dan, počitnice, tujina, policija, zastoji, avtocesta, prometni center, Slovenija, Italija, obvoznica, delovna zapora, Maribor, Ljubljana, Koper, zastoj, Brda, Brezovica, Kopru
- Excerpt: V več državah dela prost dan, na avtocestah so bili zastoji Ključne besede: Promet, prazniki, gneča, katoliški praznik, rešnje telo, kri, telovo, Avstrija, Nemčija, Hrvaška, prost dan, počitnice, tujina, policija, zastoji, avtocesta, prometni center, Slovenija, Italija, obvoznica, delovna zapora, Maribor, Ljubljana, Koper, zastoj, Brda, Brezovica, Kopru Ob katoliškem prazniku svetega rešnjega telesa in krvi, imenovanem tudi telovo, ki je v več državah, med drugim v Avstriji, večjem delu Nemčije...


### 7. Višanje temperatur

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Temperature v Evropi blizu 40 stopinj; v Sevilli bodo poimenovali vročinske valove
- Decision: relevant
- Rationale: About high temperatures and heat waves in Europe.
- Category/date: okolje / 2022-06-27T17:26:47
- URL: https://www.rtvslo.si/okolje/temperature-v-evropi-blizu-40-stopinj-v-sevilli-bodo-poimenovali-vrocinske-valove/632404
- FAISS rank/score: 1 / 0.7762
- Reranker score: n/a
- Keywords: Evropa, vročina, vročinski val, temperature, rekordi, voda, pomanjkanje, suša, Italija, Španija, klimatsko hlajenje, električna energija, projekti, Sevilja, vročinski valovi, varnost, požarna varnost, ukrepi, podnebne spremembe.
- Excerpt: Temperature v Evropi blizu 40 stopinj; v Sevilli bodo poimenovali vročinske valove Ključne besede: Evropa, vročina, vročinski val, temperature, rekordi, voda, pomanjkanje, suša, Italija, Španija, klimatsko hlajenje, električna energija, projekti, Sevilja, vročinski valovi, varnost, požarna varnost, ukrepi, podnebne spremembe. Po Evropi prevladujejo visoke temperature in iz številnih delov poročajo o vročinskih rekordih, medtem ko oblasti zaradi pomanjkanja omejujejo porabo vode. Visoke temperatu...

#### Rank 2: RELEVANT

- Title: Povprečna temperatura se bo v petih letih verjetno zvišala za več kot 1,5 stopinje Celzija
- Decision: relevant
- Rationale: Directly about average temperature rising above 1.5 C.
- Category/date: okolje / 2023-05-17T18:02:00
- URL: https://www.rtvslo.si/okolje/povprecna-temperatura-se-bo-v-petih-letih-verjetno-zvisala-za-vec-kot-1-5-stopinje-celzija/668521
- FAISS rank/score: 2 / 0.7700
- Reranker score: n/a
- Keywords: Temperatura, Segrevanje, Svetovna meteorološka organizacija, WMO, Povprečna temperatura, Globalno segrevanje, Podnebne spremembe, El Niño, Amazonija, Deževni gozd, Savana, Padavine, Evropa, Aljaska, Sibirija, Sahel, Podnebni znanstveniki, Preventivni ukrepi, Ogrevanje, Poročilo, Zdravje, Okolje
- Excerpt: Povprečna temperatura se bo v petih letih verjetno zvišala za več kot 1,5 stopinje Celzija Ključne besede: Temperatura, Segrevanje, Svetovna meteorološka organizacija, WMO, Povprečna temperatura, Globalno segrevanje, Podnebne spremembe, El Niño, Amazonija, Deževni gozd, Savana, Padavine, Evropa, Aljaska, Sibirija, Sahel, Podnebni znanstveniki, Preventivni ukrepi, Ogrevanje, Poročilo, Zdravje, Okolje Svetovna povprečna letna temperatura se bo v prihodnjih petih letih verjetno prvič dvignila za ve...

#### Rank 3: RELEVANT

- Title: Že 50-odstotna verjetnost, da se bo temperatura do leta 2026 dvignila za več kot 1,5 stopinje
- Decision: relevant
- Rationale: Directly about rising temperature probability.
- Category/date: okolje / 2022-05-10T13:35:04
- URL: https://www.rtvslo.si/okolje/ze-50-odstotna-verjetnost-da-se-bo-temperatura-do-leta-2026-dvignila-za-vec-kot-1-5-stopinje/626850
- FAISS rank/score: 3 / 0.7651
- Reranker score: n/a
- Keywords: segrevanje ozračja, temperatura, okolje, podnebne spremembe, vročinski valovi, toplogredni plini, pariški sporazum, podnebna konferenca, vpliv podnebnih sprememb, arktična regija
- Excerpt: Že 50-odstotna verjetnost, da se bo temperatura do leta 2026 dvignila za več kot 1,5 stopinje Ključne besede: segrevanje ozračja, temperatura, okolje, podnebne spremembe, vročinski valovi, toplogredni plini, pariški sporazum, podnebna konferenca, vpliv podnebnih sprememb, arktična regija Obstaja že 50-odstotna verjetnost, da bo svet do leta 2026 presegel ključno mejo pri segrevanju ozračja, to je 1,5 stopinje Celzija. Vremenoslovci so tudi prepričani, da bomo v prihodnjih petih letih doživeli na...

#### Rank 4: RELEVANT

- Title: Prvi vročinski val. Arso svari tudi pred močnim vetrom.
- Decision: relevant
- Rationale: About a heat wave and high temperatures.
- Category/date: okolje / 2024-06-19T07:20:40
- URL: https://www.rtvslo.si/okolje/prvi-vrocinski-val-arso-svari-tudi-pred-mocnim-vetrom/712253
- FAISS rank/score: 4 / 0.7643
- Reranker score: n/a
- Keywords: Visoke temperature, Močan veter, Vročinski val
- Excerpt: Prvi vročinski val. Arso svari tudi pred močnim vetrom. Ključne besede: Visoke temperature, Močan veter, Vročinski val Slovenijo bo prvič letos zajel vročinski val, temperature se bodo povzpele nad 30 stopinj Celzija. NIJZ svetuje ljudem naj zmanjšajo izpostavljenost vročini in se umaknejo v senco, omejijo fizične aktivnosti in uživajo lahko hrano v manjših obrokih. Na Nacionalnem inštitutu za javno zdravje (NIJZ) so zapisali, da lahko težave preprečimo tako, da zmanjšamo obremenitev telesa s to...

#### Rank 5: RELEVANT

- Title: Sindikati: Ob vročinskem valu morajo delodajalci zmanjšati intenzivnost dela
- Decision: relevant
- Rationale: About work conditions during a heat wave/high temperatures.
- Category/date: okolje / 2022-06-25T10:45:29
- URL: https://www.rtvslo.si/okolje/sindikati-ob-vrocinskem-valu-morajo-delodajalci-zmanjsati-intenzivnost-dela/632188
- FAISS rank/score: 5 / 0.7641
- Reranker score: n/a
- Keywords: vreme, vročinski val, obremenitve, delo, temperatura, delovno okolje, sindikati, varnost, zdravje, produktivnost, delavci, kronične bolezni, vročina, gostinstvo, turizem, trgovina, gradbeništvo, komunala, pisarniški prostori, proizvodne hale, klimatska naprava, prezračevanje, zračenje
- Excerpt: Sindikati: Ob vročinskem valu morajo delodajalci zmanjšati intenzivnost dela Ključne besede: vreme, vročinski val, obremenitve, delo, temperatura, delovno okolje, sindikati, varnost, zdravje, produktivnost, delavci, kronične bolezni, vročina, gostinstvo, turizem, trgovina, gradbeništvo, komunala, pisarniški prostori, proizvodne hale, klimatska naprava, prezračevanje, zračenje Vremenoslovci napovedujejo, da bo prihodnji teden vse bolj vroče, s temperaturo tudi okoli 35 stopinj. Sindikati opozarja...


### 8. Višanje cen nepremičnin v Sloveniji

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: Cene stanovanjskih nepremičnin od leta 2022 zrasle za četrtino, v zadnjih 10 letih so se podvojile
- Decision: relevant
- Rationale: Directly about residential real-estate prices increasing.
- Category/date: gospodarstvo / 2026-01-05T09:54:52
- URL: https://www.rtvslo.si/gospodarstvo/cene-stanovanjskih-nepremicnin-od-leta-2022-zrasle-za-cetrtino-v-zadnjih-10-letih-so-se-podvojile/769090
- FAISS rank/score: 1 / 0.8199
- Reranker score: n/a
- Keywords: nepremičnine, trg, cene, stanovanja
- Excerpt: Cene stanovanjskih nepremičnin od leta 2022 zrasle za četrtino, v zadnjih 10 letih so se podvojile Ključne besede: nepremičnine, trg, cene, stanovanja Cene stanovanj v Ljubljani dosegajo tudi do 8000 evrov na kvadratni meter, nepremičnine pa se še naprej dražijo. Ob tem se je lani nadaljevalo kopičenje praznih stanovanj, težava pa ostaja dolgotrajno pridobivanje gradbenih dovoljenj. Sredi lanskega leta je srednja vrednost novih stanovanjskih nepremičnin v Sloveniji prvič presegla 3000 evrov na k...

#### Rank 2: RELEVANT

- Title: Lani rekordne cene nepremičnin, a nepremičninski trg se ohlaja
- Decision: relevant
- Rationale: Directly about record real-estate prices in Slovenia.
- Category/date: slovenija / 2023-03-31T17:33:00
- URL: https://www.rtvslo.si/slovenija/lani-rekordne-cene-nepremicnin-a-nepremicninski-trg-se-ohlaja/663341
- FAISS rank/score: 2 / 0.8176
- Reranker score: n/a
- Keywords: nepremičnine, stanovanja, hiše, prodaja, nepremičninski trg, cene, Gurs, rast, trg, Slovenija, rekord, zemljišča, Geodetska uprava RS, Ljubljana, Obala, alpsko turistično območje, Kranjska Gora, Bled, Bohinjsko jezero, cene kvadratnega metra, povprečje, Kranj, Medvode, Domžale, Kamnik, Grosuplje, Vrhnika, Logatec, Gorenjska, Novo mesto, nova Gorica, Vipavska dolina, Goriška brda, Bela krajina, Prekmurje.
- Excerpt: Lani rekordne cene nepremičnin, a nepremičninski trg se ohlaja Ključne besede: nepremičnine, stanovanja, hiše, prodaja, nepremičninski trg, cene, Gurs, rast, trg, Slovenija, rekord, zemljišča, Geodetska uprava RS, Ljubljana, Obala, alpsko turistično območje, Kranjska Gora, Bled, Bohinjsko jezero, cene kvadratnega metra, povprečje, Kranj, Medvode, Domžale, Kamnik, Grosuplje, Vrhnika, Logatec, Gorenjska, Novo mesto, nova Gorica, Vipavska dolina, Goriška brda, Bela krajina, Prekmurje. Cene stanovan...

#### Rank 3: RELEVANT

- Title: Prodaja nepremičnin upada, cene pa še naprej rastejo
- Decision: relevant
- Rationale: Directly about real-estate sales falling while prices rise.
- Category/date: gospodarstvo / 2024-12-23T15:25:02
- URL: https://www.rtvslo.si/gospodarstvo/prodaja-nepremicnin-upada-cene-pa-se-naprej-rastejo/731459
- FAISS rank/score: 3 / 0.8166
- Reranker score: n/a
- Keywords: nepremičnine, prodaja, cene
- Excerpt: Prodaja nepremičnin upada, cene pa še naprej rastejo Ključne besede: nepremičnine, prodaja, cene Prodaja stanovanjskih nepremičnin v Sloveniji upada. V tretjem četrtletju je bilo prodanih celo najmanj rabljenih nepremičnin v zadnjih 14 letih. Cene nepremičnin medtem še naprej rastejo, najbolj prav za rabljena stanovanja in hiše. Po izračunih Statističnega urada RS (Surs) je bilo v tretjem četrtletju letošnjega leta skupno prodnih 1737 stanovanjskih nepremičnin. To je 16 odstotkov manj kot v četr...

#### Rank 4: RELEVANT

- Title: Stanovanjske nepremičnine se še dražijo
- Decision: relevant
- Rationale: Directly about residential real estate getting more expensive.
- Category/date: gospodarstvo / 2024-09-23T11:24:46
- URL: https://www.rtvslo.si/gospodarstvo/stanovanjske-nepremicnine-se-se-drazijo/721887
- FAISS rank/score: 4 / 0.8133
- Reranker score: n/a
- Keywords: Prodajna vrednost, Rabljena stanovanja, Nova stanovanja, Podražitev, Stanovanjske nepremičnine
- Excerpt: Stanovanjske nepremičnine se še dražijo Ključne besede: Prodajna vrednost, Rabljena stanovanja, Nova stanovanja, Podražitev, Stanovanjske nepremičnine Stanovanjske nepremičnine so se v drugem četrtletju podražile za 2,2 odstotka, v medletni primerjavi pa za 6,7 odstotka. Število prodaj stanovanjskih nepremičnin je bilo za petino nižje od povprečja prejšnjega leta, kažejo podatki Sursa. Nove stanovanjske nepremičnine so se po pocenitvi v letošnjem prvem četrtletju (za 7,6 odstotka) znova podražil...

#### Rank 5: NOT RELEVANT

- Title: Velik naval ljudi na najnovejše ocene vrednosti nepremičnin
- Decision: not_relevant
- Rationale: About property valuation updates, not mainly rising market prices.
- Category/date: slovenija / 2024-10-11T16:30:14
- URL: https://www.rtvslo.si/slovenija/velik-naval-ljudi-na-najnovejse-ocene-vrednosti-nepremicnin/724015
- FAISS rank/score: 5 / 0.8108
- Reranker score: n/a
- Keywords: Modeli, Geodetska uprava, E-Prostor, Vrednotenje, Nepremičnine
- Excerpt: Velik naval ljudi na najnovejše ocene vrednosti nepremičnin Ključne besede: Modeli, Geodetska uprava, E-Prostor, Vrednotenje, Nepremičnine Portal geodetske uprave Prostor je od včeraj, ko so objavili poskusni izračun posplošenih vrednosti nepremičnin, na robu zmogljivosti, saj so našteli kar 300.000 vpogledov v desetih minutah. Geodetska uprava želi na portalu lastnike seznaniti, kakšno vrednost so pripisali njihovi nepremičnini, hkrati pa tudi, kakšne modele so uporabljali. Ocenili so približno...


### 9. Rogljič in Pogačar na tekmi

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Na Emiliji in Lombardiji prvo in drugo letošnje soočenje Pogačarja in Rogliča
- Decision: relevant
- Rationale: Directly about Roglic and Pogacar facing each other in races.
- Category/date: sport / 2023-09-18T20:40:51
- URL: https://www.rtvslo.si/sport/kolesarstvo/na-emiliji-in-lombardiji-prvo-in-drugo-letosnje-soocenje-pogacarja-in-roglica/681833
- FAISS rank/score: 1 / 0.7881
- Reranker score: n/a
- Keywords: kolesarstvo, Dirka po Lombardiji, Tadej Pogačar, Primož Roglič, Marc Hirschi, ekipa UAE, slovenski državni prvak, Joxean Matxin Fernandez, Dirka po Emiliji, Dirka tri doline Vareseja, Vuelta, San Luco, Bologna, Dirka po Franciji, 2024, tritedenske dirke, enodnevne dirke, Madrid, kraljevska etapa, Angliru, Remco Evenepoel
- Excerpt: Na Emiliji in Lombardiji prvo in drugo letošnje soočenje Pogačarja in Rogliča Ključne besede: kolesarstvo, Dirka po Lombardiji, Tadej Pogačar, Primož Roglič, Marc Hirschi, ekipa UAE, slovenski državni prvak, Joxean Matxin Fernandez, Dirka po Emiliji, Dirka tri doline Vareseja, Vuelta, San Luco, Bologna, Dirka po Franciji, 2024, tritedenske dirke, enodnevne dirke, Madrid, kraljevska etapa, Angliru, Remco Evenepoel Tadej Pogačar je ob Marcu Hirschiju iz ekipe UAE že na startni listi Dirke po Lomba...

#### Rank 2: RELEVANT

- Title: Pogačar se bo v soboto prvič predstavil v mavrični majici
- Decision: relevant
- Rationale: About Pogacar racing; related to the cycling/race prompt.
- Category/date: sport / 2024-10-04T08:00:52
- URL: https://www.rtvslo.si/sport/kolesarstvo/pogacar-se-bo-v-soboto-prvic-predstavil-v-mavricni-majici/723155
- FAISS rank/score: 2 / 0.7809
- Reranker score: n/a
- Keywords: Tadej Pogačar, Primož Roglič, Remco Evenepoel
- Excerpt: Pogačar se bo v soboto prvič predstavil v mavrični majici Ključne besede: Tadej Pogačar, Primož Roglič, Remco Evenepoel Svetovni prvak Tadej Pogačar bo v mavrični majici prvič kolesaril v soboto na dirki Giro dell'Emilia v Italiji, kjer bosta tekmovala tudi Primož Roglič in Remco Evenepoel. 107. izvedba italijanske klasike, ki sicer ni del svetovne serije, bo za kolesarje priprava za zadnjo veliko dirko sezone – Dirko po Lombardiji. Zadnja izmed petih"klasik" bo na sporedu v soboto, 12. oktobra....

#### Rank 3: RELEVANT

- Title: Pogačar bo v Glasgowu nastopil na cestni dirki in kronometru
- Decision: relevant
- Rationale: About Pogacar competing in races; related to the cycling/race prompt.
- Category/date: sport / 2023-07-31T12:59:00
- URL: https://www.rtvslo.si/sport/kolesarstvo/svetovno-prvenstvo-v-kolesarstvu/pogacar-bo-v-glasgowu-nastopil-na-cestni-dirki-in-kronometru/676660
- FAISS rank/score: 3 / 0.7769
- Reranker score: n/a
- Keywords: SP v kolesarstvu, Tadej Pogačar, Luka Mezgec, svetovno prvenstvo, Glasgow, cestna dirka, vožnja na čas, kolesarstvo, slovenska reprezentanca, TV SLO 2, MMC, kronometer, Škotska, kategorija do 23 let, ženska cestna dirka, moški konkurenca, olimpijski kros, BMX, parakolesarji, H3, prenosi, gorsko kolesarstvo
- Excerpt: Pogačar bo v Glasgowu nastopil na cestni dirki in kronometru Ključne besede: SP v kolesarstvu, Tadej Pogačar, Luka Mezgec, svetovno prvenstvo, Glasgow, cestna dirka, vožnja na čas, kolesarstvo, slovenska reprezentanca, TV SLO 2, MMC, kronometer, Škotska, kategorija do 23 let, ženska cestna dirka, moški konkurenca, olimpijski kros, BMX, parakolesarji, H3, prenosi, gorsko kolesarstvo Prvi kolesar sveta Tadej Pogačar je potrdil nastop za slovensko reprezentanco na bližnjem svetovnem prvenstvu v Gla...

#### Rank 4: RELEVANT

- Title: Izjemni Pogačar znova pometel s konkurenco, na kronometru odličen tudi Roglič
- Decision: relevant
- Rationale: Directly about Pogacar and Roglic in a race result.
- Category/date: sport / 2025-07-18T08:02:59
- URL: https://www.rtvslo.si/sport/kolesarstvo/dirka-po-franciji/izjemni-pogacar-znova-pometel-s-konkurenco-na-kronometru-odlicen-tudi-roglic/752257
- FAISS rank/score: 4 / 0.7759
- Reranker score: n/a
- Keywords: Kolesarstvo, Dirka po Franciji, Tour, 13. etapa, Kronometer, Tadej Pogačar, Jonas Vingegaard, Remco Evenepoel, Primož Roglič
- Excerpt: Izjemni Pogačar znova pometel s konkurenco, na kronometru odličen tudi Roglič Ključne besede: Kolesarstvo, Dirka po Franciji, Tour, 13. etapa, Kronometer, Tadej Pogačar, Jonas Vingegaard, Remco Evenepoel, Primož Roglič Tadej Pogačar je na 112. Dirki po Franciji dobil drugo etapo zapored in še povišal svojo prednost v skupnem seštevku. Najboljši kolesar na svetu je bil najhitrejši na gorskem kronometru, s tretjim mestom pa se je izkazal tudi Primož Roglič. Nova veličastna predstava kapetana ekipe...

#### Rank 5: RELEVANT

- Title: Pogačar prvič po lanskem aprilu izgubil točke, Roglič skočil na 4. mesto
- Decision: relevant
- Rationale: Directly about Pogacar and Roglic in a race/ranking context.
- Category/date: sport / 2025-04-01T17:17:08
- URL: https://www.rtvslo.si/sport/kolesarstvo/pogacar-prvic-po-lanskem-aprilu-izgubil-tocke-roglic-skocil-na-4-mesto/741345
- FAISS rank/score: 5 / 0.7735
- Reranker score: n/a
- Keywords: kolesarstvo, UCI-lestvica, Tadej Pogačar, Primož Roglič
- Excerpt: Pogačar prvič po lanskem aprilu izgubil točke, Roglič skočil na 4. mesto Ključne besede: kolesarstvo, UCI-lestvica, Tadej Pogačar, Primož Roglič Dirka po Kataloniji je prinesla Primožu Rogliču napredovanje za tri mesta na skupno 4. mesto najnovejše lestvice Mednarodne kolesarske zveze, kjer že 185. teden vodi Tadej Pogačar, ki pa je prvič po lanskem aprilu izgubil nekaj točk. Na tekoči 52-tedenski lestvici so namreč svetovnemu prvaku črtali točke za lanske etapne uspehe in skupno zmago na Dirki...


### 10. Donald Trump novi zakoni

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Trump najprej uvedel nove 10-odstotne carine, nato jih je dvignil na 15 odstotkov
- Decision: relevant
- Rationale: About Trump introducing new tariffs/policy.
- Category/date: svet / 2026-02-21T09:59:57
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/trump-najprej-uvedel-nove-10-odstotne-carine-nato-jih-je-dvignil-na-15-odstotkov/774153
- FAISS rank/score: 1 / 0.8066
- Reranker score: n/a
- Keywords: Zakon o trgovini, Uvoz, Vrhovno sodišče, Carine, Trump
- Excerpt: Trump najprej uvedel nove 10-odstotne carine, nato jih je dvignil na 15 odstotkov Ključne besede: Zakon o trgovini, Uvoz, Vrhovno sodišče, Carine, Trump Ameriški predsednik Donald Trump je v petek ostro kritiziral sodnike vrhovnega sodišča, ki so razveljavili njegove t. i. vzajemne carine. Takoj je podpisal izvršni ukaz in uvedel nove splošne 10-odstotne carine, nato pa jih je povišal na 15 odstotkov. V odzivu na odločitev vrhovnega sodišča je Donald Trump napovedal, da bo nemudoma podpisal ukaz...

#### Rank 2: RELEVANT

- Title: Trump z novim zakonom uvedel višje kazni za trgovino s fentanilom
- Decision: relevant
- Rationale: Directly about Trump and a new law.
- Category/date: svet / 2025-07-17T10:37:53
- URL: https://www.rtvslo.si/svet/preberite-tudi/trump-z-novim-zakonom-uvedel-visje-kazni-za-trgovino-s-fentanilom/752186
- FAISS rank/score: 2 / 0.8051
- Reranker score: n/a
- Keywords: Nezakonito, Trgovina, Višje kazni, Fentanil, Trump
- Excerpt: Trump z novim zakonom uvedel višje kazni za trgovino s fentanilom Ključne besede: Nezakonito, Trgovina, Višje kazni, Fentanil, Trump Ameriški predsednik Donald Trump je v sredo podpisal zakon, ki sintetično drogo fentanil uvršča med najhujša prepovedana mamila v ZDA. Ob podpisu zakona je dejal, da bodo s tem zadali velik udarec mamilarskim kartelom, saj so za trgovino s fentanilom zdaj predvidene višje kazni. Fentanil je sredstvo, ki ga ameriški zdravniki včasih predpisujejo za lajšanje hudih bo...

#### Rank 3: RELEVANT

- Title: S Trumpovim podpisom končana delna blokada ameriške vlade
- Decision: relevant
- Rationale: About Trump signing a government-funding measure.
- Category/date: svet / 2026-02-04T07:05:07
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/s-trumpovim-podpisom-koncana-delna-blokada-ameriske-vlade/772270
- FAISS rank/score: 3 / 0.8029
- Reranker score: n/a
- Keywords: ZDA, Donald Trump, financiranje vlade
- Excerpt: S Trumpovim podpisom končana delna blokada ameriške vlade Ključne besede: ZDA, Donald Trump, financiranje vlade Ameriški predsednik Donald Trump je podpisal zakone o nadaljevanju financiranja agencij svoje vlade, potem ko jih je nekaj ur prej tesno z 217 proti 214 glasovom potrdil predstavniški dom kongresa, s čimer se je po štirih dneh končala delna blokada vlade. Že lani je bilo potrjenih šest zakonov o proračunski porabi za razna ministrstva, tokrat jih je bilo prav tako do konca proračunskeg...

#### Rank 4: RELEVANT

- Title: Trump podpisal prvi ameriški zakon o kriptovalutah
- Decision: relevant
- Rationale: Directly about Trump signing a new cryptocurrency law.
- Category/date: svet / 2025-07-19T14:19:39
- URL: https://www.rtvslo.si/svet/preberite-tudi/trump-podpisal-prvi-ameriski-zakon-o-kriptovalutah/752400
- FAISS rank/score: 4 / 0.7979
- Reranker score: n/a
- Keywords: Industrija kriptovalut, Stabilni kovanci, Zakon Genius, Kriptovalute, Trump
- Excerpt: Trump podpisal prvi ameriški zakon o kriptovalutah Ključne besede: Industrija kriptovalut, Stabilni kovanci, Zakon Genius, Kriptovalute, Trump Ameriški predsednik Donald Trump je podpisal prvi zakon o kriptovalutah v ZDA. Zadeva t. i. stabilne kovance – vrsto kriptovalut, katerih vrednost je vezana na stabilen zunanji vir, kot so dolar, evro ali zlato. Namen zakona je okrepiti zaupanje v industrijo kriptovalut, ki je z donacijami Trumpu postala pomemben političen igralec v Washingtonu. Zakon z i...

#### Rank 5: RELEVANT

- Title: Trump prepovedal vstop v ZDA državljanom 12 držav
- Decision: relevant
- Rationale: About a Trump entry-ban policy.
- Category/date: svet / 2025-06-05T06:55:12
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/trump-prepovedal-vstop-v-zda-drzavljanom-12-drzav/747985
- FAISS rank/score: 5 / 0.7963
- Reranker score: n/a
- Keywords: ZDA, Donald Trump, vizum
- Excerpt: Trump prepovedal vstop v ZDA državljanom 12 držav Ključne besede: ZDA, Donald Trump, vizum Ameriški predsednik Donald Trump je državljanom 12 držav, med njimi Afganistana, Haitija in Irana, prepovedal vstop v ZDA, ker naj bi predstavljali grožnjo nacionalni varnosti. Še za sedem držav pa je uvedel delno prepoved. Prepoved vstopa v ZDA bo veljala za državljane Afganistana, Mjanmara, Čada, Konga, Ekvatorialne Gvineje, Eritreje, Haitija, Irana, Libije, Somalije, Sudana in Jemna. Trump je uvedel tud...


### 11. Evropska Unija in zveza NATO

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Rutte: Če mislite, da se lahko Evropa brani sama, kar sanjajte naprej
- Decision: relevant
- Rationale: Directly about Europe and NATO defence.
- Category/date: svet / 2026-01-26T18:46:29
- URL: https://www.rtvslo.si/svet/rutte-ce-mislite-da-se-lahko-evropa-brani-sama-kar-sanjajte-naprej/771341
- FAISS rank/score: 1 / 0.7736
- Reranker score: n/a
- Keywords: ZDA, Nato, Mark Rutte
- Excerpt: Rutte: Če mislite, da se lahko Evropa brani sama, kar sanjajte naprej Ključne besede: ZDA, Nato, Mark Rutte Evropa se ne more braniti brez ZDA, potrebujemo drug drugega, je ob zadnjih napetosti v čezatlantskih odnosih dejal generalni sekretar zveze Nato Mark Rutte. "Kar sanjajte naprej," je odvrnil tistim, ki menijo, da se lahko Evropa brani sama. " Če kdor koli tu misli, da se lahko Evropska unija ali Evropa kot celota brani brez ZDA, naj kar sanja naprej. Tega ne morete, tega ne moremo, potreb...

#### Rank 2: RELEVANT

- Title: Francoski minister Barrot: Evropejci lahko in morajo prevzeti odgovornost za svojo varnost
- Decision: relevant
- Rationale: About European security/defence, related to EU-NATO context.
- Category/date: svet / 2026-01-27T19:42:38
- URL: https://www.rtvslo.si/svet/evropa/francoski-minister-barrot-evropejci-lahko-in-morajo-prevzeti-odgovornost-za-svojo-varnost/771458
- FAISS rank/score: 2 / 0.7655
- Reranker score: n/a
- Keywords: Neodvisnost, Nato, ZDA, Varnost, Evropa
- Excerpt: Francoski minister Barrot: Evropejci lahko in morajo prevzeti odgovornost za svojo varnost Ključne besede: Neodvisnost, Nato, ZDA, Varnost, Evropa Evropa lahko prevzame in mora prevzeti odgovornost za svojo varnost, je v odzivu na izjave generalnega sekretarja zveze Nato Marka Rutteja, da se Evropa ne more braniti brez ZDA, dejal francoski zunanji minister Jean-Noel Barrot. "Ne, dragi Mark Rutte. Evropejci lahko prevzamejo in morajo prevzeti odgovornost za svojo varnost. Celo ZDA se strinjajo s...

#### Rank 3: RELEVANT

- Title: Stoltenbergu za eno leto podaljšan mandat. Generalni sekretar Nata ostaja do oktobra 2024.
- Decision: relevant
- Rationale: Directly about NATO leadership.
- Category/date: svet / 2023-07-04T11:56:22
- URL: https://www.rtvslo.si/svet/evropa/stoltenbergu-za-eno-leto-podaljsan-mandat-generalni-sekretar-nata-ostaja-do-oktobra-2024/674010
- FAISS rank/score: 3 / 0.7626
- Reranker score: n/a
- Keywords: Jens Stoltenberg, Nato, Generalni sekretar, Mandat, Zavezništvo, Evropa, Severna Amerika, Varovanje, Ruska agresija, Ukrajina, Države članice, Litva, Naslednik, Danska, Združeno kraljestvo, Evropska unija, Španija, Volitve, Predsedniške volitve, ZDA
- Excerpt: Stoltenbergu za eno leto podaljšan mandat. Generalni sekretar Nata ostaja do oktobra 2024. Ključne besede: Jens Stoltenberg, Nato, Generalni sekretar, Mandat, Zavezništvo, Evropa, Severna Amerika, Varovanje, Ruska agresija, Ukrajina, Države članice, Litva, Naslednik, Danska, Združeno kraljestvo, Evropska unija, Španija, Volitve, Predsedniške volitve, ZDA Jens Stoltenberg bo na čelu Nata ostal do oktobra prihodnje leto. Kot je sporočil le nekaj dni pred vrhom Nata v Vilni, so mu članice zavezništ...

#### Rank 4: RELEVANT

- Title: Stoltenberg odhaja z mesta generalnega sekretarja Nata
- Decision: relevant
- Rationale: Directly about NATO leadership.
- Category/date: svet / 2024-10-01T07:51:59
- URL: https://www.rtvslo.si/svet/evropa/stoltenberg-odhaja-z-mesta-generalnega-sekretarja-nata/722769
- FAISS rank/score: 4 / 0.7618
- Reranker score: n/a
- Keywords: Nato, Jens Stoltenberg, Mark Rutte
- Excerpt: Stoltenberg odhaja z mesta generalnega sekretarja Nata Ključne besede: Nato, Jens Stoltenberg, Mark Rutte Nekdanji norveški premier Jens Stoltenberg po desetih letih končuje svoje delo generalnega sekretarja zveze Nato. To mesto prevzema nekdanji nizozemski premier Mark Rutte. V času Stoltenbergovega vodenja je zavezništvo doživelo vrsto sprememb in znova postalo najmočnejši porok varnosti in stabilnosti na evropski celini. Ni veliko organizacij, ki bi bile razglašene za odvečne in možgansko mrt...

#### Rank 5: RELEVANT

- Title: Sedmerica držav ob 20. obletnici vstopa v Nato objavila skupni zapis v podporo zavezništvu
- Decision: relevant
- Rationale: Directly about countries supporting NATO alliance membership.
- Category/date: svet / 2024-03-30T08:52:36
- URL: https://www.rtvslo.si/svet/preberite-tudi/sedmerica-drzav-ob-20-obletnici-vstopa-v-nato-objavila-skupni-zapis-v-podporo-zaveznistvu/703389
- FAISS rank/score: 5 / 0.7618
- Reranker score: n/a
- Keywords: Evro-atlantska varnost, Zavezništvo, Obletnica vstopa, Nato, zunanji ministri, zveza Nato, varnost, širitev, nadaljnja širitev, obletnica, Ukrajina, vojna, mir, stabilnost, odprtost vrat, članstvo, zaveza, obramba, proslava, 75. obletnica, Washington, julijski vrh, evroatlantska varnost, evropa
- Excerpt: Sedmerica držav ob 20. obletnici vstopa v Nato objavila skupni zapis v podporo zavezništvu Ključne besede: Evro-atlantska varnost, Zavezništvo, Obletnica vstopa, Nato, zunanji ministri, zveza Nato, varnost, širitev, nadaljnja širitev, obletnica, Ukrajina, vojna, mir, stabilnost, odprtost vrat, članstvo, zaveza, obramba, proslava, 75. obletnica, Washington, julijski vrh, evroatlantska varnost, evropa Zunanji ministri in ministrice Slovenije, Bolgarije, Estonije, Latvije, Litve, Romunije in Slovaš...


### 12. Velika Britanija Brexit

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Brexit pričakovanj ni upravičil, britanska javnost pa ga skoraj ne omenja več
- Decision: relevant
- Rationale: Directly about Brexit and UK public/economic expectations.
- Category/date: svet / 2025-01-31T06:20:23
- URL: https://www.rtvslo.si/svet/evropa/brexit-pricakovanj-ni-upravicil-britanska-javnost-pa-ga-skoraj-ne-omenja-vec/735075
- FAISS rank/score: 1 / 0.8255
- Reranker score: n/a
- Keywords: Gospodarske posledice, Evropska unija, Združeno kraljestvo, Brexit, Jan Grobovšek
- Excerpt: Brexit pričakovanj ni upravičil, britanska javnost pa ga skoraj ne omenja več Ključne besede: Gospodarske posledice, Evropska unija, Združeno kraljestvo, Brexit, Jan Grobovšek Pred petimi leti je Združeno kraljestvo izstopilo iz Evropske unije. Ekonomist z univerze v Edinburgu Jan Grobovšek pravi, da je s tem država dobila "najslabše od obeh svetov" – postala je manjše gospodarstvo in ni ujela gospodarskih priložnosti. Združeno kraljestvo je 31. januarja 2020 po 47 letih članstva kot prva članic...

#### Rank 2: RELEVANT

- Title: Velika Britanija prva evropska država v transpacifiškem prostotrgovinskem partnerstvu
- Decision: relevant
- Rationale: About UK trade strategy in a post-Brexit context.
- Category/date: gospodarstvo / 2023-03-31T14:52:00
- URL: https://www.rtvslo.si/gospodarstvo/velika-britanija-prva-evropska-drzava-v-transpacifiskem-prostotrgovinskem-partnerstvu/663314
- FAISS rank/score: 2 / 0.7919
- Reranker score: n/a
- Keywords: Velika Britanija, CPTPP, transpacifiško prostotrgovinsko partnerstvo, transpacifiško partnerstvo, brexit, prostotrgovinski dogovor, gospodarske koristi, Rishi Sunak, Evropska unija, trgovinski bloki, Obama, Donald Trump, Kitajska, Japonska, Avstralija, Kanada, Nova Zelandija, Mehika, Južna Koreja, Tajvan, pridružitev
- Excerpt: Velika Britanija prva evropska država v transpacifiškem prostotrgovinskem partnerstvu Ključne besede: Velika Britanija, CPTPP, transpacifiško prostotrgovinsko partnerstvo, transpacifiško partnerstvo, brexit, prostotrgovinski dogovor, gospodarske koristi, Rishi Sunak, Evropska unija, trgovinski bloki, Obama, Donald Trump, Kitajska, Japonska, Avstralija, Kanada, Nova Zelandija, Mehika, Južna Koreja, Tajvan, pridružitev Velika Britanija se bo po dveh letih pogajanj pridružila Celostnemu in napredne...

#### Rank 3: RELEVANT

- Title: Britanci bodo zaostrili izdajanje vizumov, da bi zmanjšali priseljevanje
- Decision: relevant
- Rationale: About UK migration policy and explicitly links it to Brexit.
- Category/date: svet / 2023-12-05T09:17:17
- URL: https://www.rtvslo.si/svet/evropa/britanci-bodo-zaostrili-izdajanje-vizumov-da-bi-zmanjsali-priseljevanje/690539
- FAISS rank/score: 3 / 0.7727
- Reranker score: n/a
- Keywords: Velika Britanija, migracije, priseljevanje, tuji delavci, zakonito priseljevanje, nezakonito priseljevanje, minimalna plača, vizumi, družinski člani, politika, Evropska unija, brexit, neto migracije, Indija, Nigerija, Kitajska, premier, nadzor, javni zdravstveni sistem, notranji minister
- Excerpt: Britanci bodo zaostrili izdajanje vizumov, da bi zmanjšali priseljevanje Ključne besede: Velika Britanija, migracije, priseljevanje, tuji delavci, zakonito priseljevanje, nezakonito priseljevanje, minimalna plača, vizumi, družinski člani, politika, Evropska unija, brexit, neto migracije, Indija, Nigerija, Kitajska, premier, nadzor, javni zdravstveni sistem, notranji minister Velika Britanija se bo zaradi množičnega priseljevanja poleg nezakonitih migracij lotila tudi prihodov priseljencev po zak...

#### Rank 4: RELEVANT

- Title: Lažje trgovanje med Veliko Britanijo ter Norveško, Islandijo in Lihtenštajnom
- Decision: relevant
- Rationale: About UK trade after leaving the EU.
- Category/date: svet / 2021-06-04T18:05:04
- URL: https://www.rtvslo.si/svet/evropa/lazje-trgovanje-med-veliko-britanijo-ter-norvesko-islandijo-in-lihtenstajnom/582981
- FAISS rank/score: 4 / 0.7682
- Reranker score: n/a
- Keywords: Velika Britanija, prostotrgovinski sporazum, Norveška, Islandija, Lihtenštajn, izstop, Evropska unija, trgovina, gospodarstvo, carine, izvoz, uvoz, podjetja, ribištvo, pogajanja, carinske kvote, carinske olajšave, Londonski dogovor, tržni dostop, prehranski proizvodi.
- Excerpt: Lažje trgovanje med Veliko Britanijo ter Norveško, Islandijo in Lihtenštajnom Ključne besede: Velika Britanija, prostotrgovinski sporazum, Norveška, Islandija, Lihtenštajn, izstop, Evropska unija, trgovina, gospodarstvo, carine, izvoz, uvoz, podjetja, ribištvo, pogajanja, carinske kvote, carinske olajšave, Londonski dogovor, tržni dostop, prehranski proizvodi. Velika Britanija je po izstopu Združenega kraljestva iz Evropske unije dosegla dogovor o prostotrgovinskem sporazumu z Norveško, Islandij...

#### Rank 5: RELEVANT

- Title: Brexit je postal težava za e-mobilnost
- Decision: relevant
- Rationale: Directly about Brexit effects on e-mobility/automotive trade.
- Category/date: zabava-in-slog / 2023-06-05T07:45:00
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/brexit-je-postal-tezava-za-e-mobilnost/670651
- FAISS rank/score: 5 / 0.7621
- Reranker score: n/a
- Keywords: Brexit, Stellantis, carina, električni avtomobili, Velika Britanija, dajatve na izvoz, avtomobilska industrija, Aston Martin Lagonda, Unite, Carlos Tavares, električna vozila, BMW, Kitajska, Opel/Vauxhall, Ellesmere Port, dostavna vozila, investicije, zaposlovanje, gospodarstvo, kriza, blagovne znamke
- Excerpt: Brexit je postal težava za e-mobilnost Ključne besede: Brexit, Stellantis, carina, električni avtomobili, Velika Britanija, dajatve na izvoz, avtomobilska industrija, Aston Martin Lagonda, Unite, Carlos Tavares, električna vozila, BMW, Kitajska, Opel/Vauxhall, Ellesmere Port, dostavna vozila, investicije, zaposlovanje, gospodarstvo, kriza, blagovne znamke Morebitne dajatve na izvoz električnih avtomobilov iz Velike Britanije vznemirjajo avtomobilske proizvajalce. Stellantis odkrito grozi z zaprt...


### 13. Vojna v Ukrajini in Zelenski

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Zelenski: V vojni umrlo 31.000 ukrajinskih vojakov. Moskva poroča o napredku ruskih sil.
- Decision: relevant
- Rationale: Directly about Zelensky and casualties in the Ukraine war.
- Category/date: svet / 2024-02-25T12:39:38
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-v-vojni-umrlo-31-000-ukrajinskih-vojakov-moskva-poroca-o-napredku-ruskih-sil/699466
- FAISS rank/score: 1 / 0.8163
- Reranker score: n/a
- Keywords: Ukrajina, Rusija, Avdijivka, Doneck, Volodimir Zelenski, vojna, žrtve, pomoč Zahoda, Putin, Vladimir Putin, žrtve vojne, civilisti, dejstva, podpora, vojaška pomoč, ofenziva, protiofenziva, Kremlj, informacije, strategija, končanje vojne, zmaga, poraz.
- Excerpt: Zelenski: V vojni umrlo 31.000 ukrajinskih vojakov. Moskva poroča o napredku ruskih sil. Ključne besede: Ukrajina, Rusija, Avdijivka, Doneck, Volodimir Zelenski, vojna, žrtve, pomoč Zahoda, Putin, Vladimir Putin, žrtve vojne, civilisti, dejstva, podpora, vojaška pomoč, ofenziva, protiofenziva, Kremlj, informacije, strategija, končanje vojne, zmaga, poraz. Ukrajinski predsednik Volodimir Zelenski je sporočil, da je bilo v dveh letih vojne ubitih 31.000 ukrajinskih vojakov. Medtem pa so ruske sile...

#### Rank 2: RELEVANT

- Title: Zelenski: Ukrajini bi lahko zaradi vojne na Bližnjem vzhodu začelo primanjkovati streliva in raket
- Decision: relevant
- Rationale: Directly about Zelensky, Ukraine war and weapons shortages.
- Category/date: svet / 2026-03-18T10:20:59
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-ukrajini-bi-lahko-zaradi-vojne-na-bliznjem-vzhodu-zacelo-primanjkovati-streliva-in-raket/776705
- FAISS rank/score: 2 / 0.8075
- Reranker score: n/a
- Keywords: Volodimir Zelenski, Ukrajina, Združeno kraljestvo, Iran
- Excerpt: Zelenski: Ukrajini bi lahko zaradi vojne na Bližnjem vzhodu začelo primanjkovati streliva in raket Ključne besede: Volodimir Zelenski, Ukrajina, Združeno kraljestvo, Iran Ukrajinski predsednik Volodimir Zelenski je ob obisku v Londonu v torek opozoril, da bi se Ukrajina zaradi vojne na Bližnjem vzhodu, ki jo je sprožila ukrajinska zaveznica ZDA, lahko kmalu spoprijela s pomanjkanjem streliva in raket. Zelenski je v pogovoru za BBC v torek poudaril, da ima "zelo slab občutek" glede vpliva konflik...

#### Rank 3: RELEVANT

- Title: Zelenski: Zdaj ni čas za govor o volitvah
- Decision: relevant
- Rationale: About Zelensky and elections in wartime Ukraine.
- Category/date: svet / 2023-11-07T07:09:51
- URL: https://www.rtvslo.si/svet/evropa/zelenski-zdaj-ni-cas-za-govor-o-volitvah/687287
- FAISS rank/score: 3 / 0.8055
- Reranker score: n/a
- Keywords: Zelenski, Ukrajina, volitve, Volodimir Zelenski, predsedniške volitve, vojno stanje, ruska agresija, parlamentarne volitve, Lindsey Graham, svobodne volitve, vojna, Dmitro Kuleba, podpora, zahodni zavezniki, vojska, razkol, statična faza, državne strukture.
- Excerpt: Zelenski: Zdaj ni čas za govor o volitvah Ključne besede: Zelenski, Ukrajina, volitve, Volodimir Zelenski, predsedniške volitve, vojno stanje, ruska agresija, parlamentarne volitve, Lindsey Graham, svobodne volitve, vojna, Dmitro Kuleba, podpora, zahodni zavezniki, vojska, razkol, statična faza, državne strukture. Ukrajinski predsednik Volodimir Zelenski je zavrnil možnost predsedniških volitev prihodnje leto. Kot je dejal, bi bilo to neodgovorno. "Mislim, da zdaj ni pravi čas za volitve." "Odlo...

#### Rank 4: RELEVANT

- Title: Zelenski zamenjal vojaški vrh in napovedal spremembo bojne taktike
- Decision: relevant
- Rationale: Directly about Zelensky changing military leadership/tactics.
- Category/date: svet / 2024-02-08T17:46:08
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-zamenjal-vojaski-vrh-in-napovedal-spremembo-bojne-taktike/697712
- FAISS rank/score: 4 / 0.8035
- Reranker score: n/a
- Keywords: Zelenski, Zalužni, Ukrajina, ukrajinski, predsednik, vojska, vrh, poveljnik, zamenjava, ekipa, obrambni minister, sprememba, spor, Rusija, invazija, ofenziva, pogovor, taktika, strategija, naloge, zmaga, vodstvo
- Excerpt: Zelenski zamenjal vojaški vrh in napovedal spremembo bojne taktike Ključne besede: Zelenski, Zalužni, Ukrajina, ukrajinski, predsednik, vojska, vrh, poveljnik, zamenjava, ekipa, obrambni minister, sprememba, spor, Rusija, invazija, ofenziva, pogovor, taktika, strategija, naloge, zmaga, vodstvo Ukrajinski predsednik Volodimir Zelenski je napovedal, da je čas za menjave v vrhu ukrajinske vojske, in za novega vrhovnega poveljnika imenoval poveljnika kopenskih sil Oleksandra Sirskega. Predtem se je...

#### Rank 5: RELEVANT

- Title: Zelenski: Če ZDA ne bodo pomagale, bo Ukrajina izgubila vojno
- Decision: relevant
- Rationale: Directly about Zelensky and Ukraine potentially losing the war.
- Category/date: svet / 2024-04-08T07:04:33
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-ce-zda-ne-bodo-pomagale-bo-ukrajina-izgubila-vojno/704234
- FAISS rank/score: 5 / 0.8030
- Reranker score: n/a
- Keywords: Ukrajina, Rusija, Jedrska elektrarna, Volodimir Zelenski, ZDA, Pomoč, vojna, kongres, vojaška pomoč, predsednik, varnost, konflikt, orožje, zračna obramba, napad, žrtve, mednarodna pomoč, propagiranje, napetosti, ruske sile, lokalne oblasti
- Excerpt: Zelenski: Če ZDA ne bodo pomagale, bo Ukrajina izgubila vojno Ključne besede: Ukrajina, Rusija, Jedrska elektrarna, Volodimir Zelenski, ZDA, Pomoč, vojna, kongres, vojaška pomoč, predsednik, varnost, konflikt, orožje, zračna obramba, napad, žrtve, mednarodna pomoč, propagiranje, napetosti, ruske sile, lokalne oblasti Če ameriški kongres ne odobri vojaške pomoči Ukrajini, bo ta izgubila vojno, je v nedeljo opozoril ukrajinski predsednik Volodimir Zelenski. Medtem IAEA poroča o večjem incidentu v...


### 14. Kitajska proti ZDA

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: Kitajska na področju umetne inteligence prehiteva ZDA
- Decision: relevant
- Rationale: Directly compares China and the US in AI.
- Category/date: znanost-in-tehnologija / 2019-03-19T08:39:25
- URL: https://www.rtvslo.si/znanost-in-tehnologija/kitajska-na-podrocju-umetne-inteligence-prehiteva-zda/483019
- FAISS rank/score: 1 / 0.7872
- Reranker score: n/a
- Keywords: AI, UI, Umetna inteligenca, Kitajska, Allen Institute for Artificial Intelligence, ZDA, raziskava, inštitut, tehnologija, avtonomna vozila, navidezna resničnost, 5G, naložbe, Peking, priseljevanje, strategija, Donald Trump, administracija, inovacije, nacionalna strategija, analitiki, Washington, raziskovalec
- Excerpt: Kitajska na področju umetne inteligence prehiteva ZDA Ključne besede: AI, UI, Umetna inteligenca, Kitajska, Allen Institute for Artificial Intelligence, ZDA, raziskava, inštitut, tehnologija, avtonomna vozila, navidezna resničnost, 5G, naložbe, Peking, priseljevanje, strategija, Donald Trump, administracija, inovacije, nacionalna strategija, analitiki, Washington, raziskovalec Kitajska je na dobri poti, da na področju umetne inteligence prehiti ZDA, kaže analiza, ki jo je v sredo objavil amerišk...

#### Rank 2: RELEVANT

- Title: Kitajski obrambni minister: Spopad Kitajske in ZDA bi bil neznosna katastrofa za svet
- Decision: relevant
- Rationale: Directly about a possible China-US conflict.
- Category/date: svet / 2023-06-04T09:05:31
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/kitajski-obrambni-minister-spopad-kitajske-in-zda-bi-bil-neznosna-katastrofa-za-svet/670585
- FAISS rank/score: 2 / 0.7837
- Reranker score: n/a
- Keywords: Kitajska, ZDA, Li Šangfu, konflikt, dialog, sodelovanje, varnost, vojska, politika, mednarodni odnosi, Sovjetska zveza, sankcije, orožje, Tajvan, Singapur, Azija, vrh, geopolitika, hladna vojna, hegemonija, diplomatski odnosi
- Excerpt: Kitajski obrambni minister: Spopad Kitajske in ZDA bi bil neznosna katastrofa za svet Ključne besede: Kitajska, ZDA, Li Šangfu, konflikt, dialog, sodelovanje, varnost, vojska, politika, mednarodni odnosi, Sovjetska zveza, sankcije, orožje, Tajvan, Singapur, Azija, vrh, geopolitika, hladna vojna, hegemonija, diplomatski odnosi Kitajski obrambni minister Li Šangfu je v nedeljo dejal, da bi bil spopad z ZDA "neznosna katastrofa" za svet, in da si njegova država želi dialog namesto spopada. Li, ki j...

#### Rank 3: RELEVANT

- Title: Kitajska po napovedi novih ameriških carin zagrozila s protiukrepi
- Decision: relevant
- Rationale: Directly about China responding to US tariffs.
- Category/date: gospodarstvo / 2025-10-12T13:10:13
- URL: https://www.rtvslo.si/gospodarstvo/kitajska-po-napovedi-novih-ameriskih-carin-zagrozila-s-protiukrepi/760526
- FAISS rank/score: 3 / 0.7742
- Reranker score: n/a
- Keywords: ZDA, Kitajska, carine
- Excerpt: Kitajska po napovedi novih ameriških carin zagrozila s protiukrepi Ključne besede: ZDA, Kitajska, carine Potem ko je predsednik ZDA Donald Trump z novembrom napovedal nove carine na uvoz iz Kitajske, je ta zagrozila s protiukrepi. V Pekingu ob tem Washingtonu očitajo dvojna merila in mu očitajo zlorabe načela nacionalne varnosti. S kitajskega ministrstva za trgovino so sporočili, da ameriška administracija že dolgo pretirava z uporabo načela nacionalne varnosti in ga zlorablja za nadzor nad izvo...

#### Rank 4: RELEVANT

- Title: Peking sporoča, da ne bo sprejel "izsiljevalske narave" ZDA
- Decision: relevant
- Rationale: Directly about China opposing US pressure.
- Category/date: svet / 2025-04-08T07:23:25
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/peking-sporoca-da-ne-bo-sprejel-izsiljevalske-narave-zda/742022
- FAISS rank/score: 4 / 0.7734
- Reranker score: n/a
- Keywords: ZDA, Carine, Kitajska
- Excerpt: Peking sporoča, da ne bo sprejel "izsiljevalske narave" ZDA Ključne besede: ZDA, Carine, Kitajska Potem ko so ZDA Kitajski zagrozile z dodatnimi, 50-odstotnimi carinami, če ta ne bo umaknila povračilnih carin na uvoz ameriškega blaga, je kitajsko ministrstvo za trgovino sporočilo, da ne bodo sprejeli "izsiljevalske narave" ZDA. Ministrstvo je dodalo, da se bodo proti carinam borili "do konca", poroča BBC. Grožnjo ameriškega predsednika Donalda Trumpa z dodatnimi 50-odstotnimi carinami na kitajsk...

#### Rank 5: NOT RELEVANT

- Title: V kitajski konzulat v ZDA trčil avtomobil, voznika ubila policija
- Decision: not_relevant
- Rationale: About a crash at a Chinese consulate in the US, not mainly China vs US relations.
- Category/date: svet / 2023-10-10T08:40:30
- URL: https://www.rtvslo.si/svet/preberite-tudi/v-kitajski-konzulat-v-zda-trcil-avtomobil-voznika-ubila-policija/684300
- FAISS rank/score: 5 / 0.7720
- Reranker score: n/a
- Keywords: konzulat, voznik, streljanje, Kitajski konzulat, San Francisco, ZDA, avtomobil, trčenje, policija, poškodbe, bolnišnica, preddverje, incident, videoposnetek, obsodba, varnost, preiskava, napad, tarča, azijsko-pacifiške države, vrh, predsednik Ši Džinping
- Excerpt: V kitajski konzulat v ZDA trčil avtomobil, voznika ubila policija Ključne besede: konzulat, voznik, streljanje, Kitajski konzulat, San Francisco, ZDA, avtomobil, trčenje, policija, poškodbe, bolnišnica, preddverje, incident, videoposnetek, obsodba, varnost, preiskava, napad, tarča, azijsko-pacifiške države, vrh, predsednik Ši Džinping V poslopje kitajskega konzulata v San Franciscu na zahodni obali ZDA je v ponedeljek trčil avtomobil. Policisti so streljali na voznika, ki je pozneje v bolnišnici...


### 15. Korupcija v slovenski politiki

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Slovenija na indeksu zaznave korupcije dosegla najslabši rezultat do zdaj
- Decision: relevant
- Rationale: Directly about Slovenia and corruption perception.
- Category/date: gospodarstvo / 2023-01-31T08:40:12
- URL: https://www.rtvslo.si/gospodarstvo/slovenija-na-indeksu-zaznave-korupcije-dosegla-najslabsi-rezultat-do-zdaj/656262
- FAISS rank/score: 1 / 0.7574
- Reranker score: n/a
- Keywords: CPI, Transparency International, indeks zaznave korupcije, korupcija, indeks zaznane korupcije, evropsko povprečje, države Zahodne Evrope, EU, boj proti korupciji, lestvica, točke, Danska, Finska, Nova Zelandija, Južni Sudan, Sirija, Somalija, Madžarska, Hrvaška, Avstrija, povprečje, OECD
- Excerpt: Slovenija na indeksu zaznave korupcije dosegla najslabši rezultat do zdaj Ključne besede: CPI, Transparency International, indeks zaznave korupcije, korupcija, indeks zaznane korupcije, evropsko povprečje, države Zahodne Evrope, EU, boj proti korupciji, lestvica, točke, Danska, Finska, Nova Zelandija, Južni Sudan, Sirija, Somalija, Madžarska, Hrvaška, Avstrija, povprečje, OECD Po zadnjih podatkih indeksa zaznane korupcije se stanje v Sloveniji slabša. S 56 točkami je v 10 letih nazadovala za pet...

#### Rank 2: RELEVANT

- Title: Demokrati zahtevajo razpravo o sistemski korupciji
- Decision: relevant
- Rationale: About Slovenian political debate on systemic corruption.
- Category/date: slovenija / 2025-12-17T19:05:26
- URL: https://www.rtvslo.si/slovenija/demokrati-zahtevajo-razpravo-o-sistemski-korupciji/767596
- FAISS rank/score: 2 / 0.7548
- Reranker score: n/a
- Keywords: Zoran Janković, Robert Golob, Anže Logar, Demokrati, DZ
- Excerpt: Demokrati zahtevajo razpravo o sistemski korupciji Ključne besede: Zoran Janković, Robert Golob, Anže Logar, Demokrati, DZ Poslanci iz vrst Demokratov po razkritjih o sumih podkupovanja, ki bremenijo tudi ljubljanskega župana Zorana Jankovića, zahtevajo sejo komisije za nadzor javnih financ. Opozarjajo na razpad pravne države in premierju Robertu Golobu očitajo neukrepanje. "Ne gre le za posamezne nepravilnosti in protizakonita ravnanja, ampak gre za organiziran sistem, kjer so določeni uradniki...

#### Rank 3: RELEVANT

- Title: Neža Grasselli: Korupciji lahko rečemo "ne" na volitvah
- Decision: relevant
- Rationale: About corruption and elections/politics in Slovenia.
- Category/date: slovenija / 2024-12-12T08:35:44
- URL: https://www.rtvslo.si/slovenija/ob-osmih/neza-grasselli-korupciji-lahko-recemo-ne-na-volitvah/730332
- FAISS rank/score: 3 / 0.7525
- Reranker score: n/a
- Keywords: korupcija, KPK, javna naročila, politične stranke
- Excerpt: Neža Grasselli: Korupciji lahko rečemo "ne" na volitvah Ključne besede: korupcija, KPK, javna naročila, politične stranke Slovenija ima težave s korupcijo. Kot pravi predsednica upravnega odbora Transparency International Slovenija Neža Grasselli, država sicer dela nekakšne premike, ampak na področju boja proti korupciji ni preboja. Na indeksu zaznave korupcije, ki ga vsako leto objavi Transparency International (TI), smo na lanski meritvi s 56 točkami od možnih sto izenačili zdajšnji najslabši...

#### Rank 4: RELEVANT

- Title: Kakšni so postopki državnih organov zoper politike?
- Decision: relevant
- Rationale: About state procedures against politicians; related to corruption/political accountability.
- Category/date: slovenija / 2025-10-09T19:20:55
- URL: https://www.rtvslo.si/slovenija/kaksni-so-postopki-drzavnih-organov-zoper-politike/760286
- FAISS rank/score: 4 / 0.7516
- Reranker score: n/a
- Keywords: Neodvisne institucije, Pravna država, Diskreditacija, Korupcija, Postopki državnih organov
- Excerpt: Kakšni so postopki državnih organov zoper politike? Ključne besede: Neodvisne institucije, Pravna država, Diskreditacija, Korupcija, Postopki državnih organov Zakaj politiki besede o spoštovanju pravne države in neodvisnih institucij prelomijo v hipu, ko se znajdejo v postopkih pred organi pregona? Kakšen vtis puščajo preiskave, ki se začnejo pol leta pred volitvami in zakaj do pravnomočnosti mine več let? "Spoštovani predsednik Vlade, dogodki preteklih dni, tednov in mesecev so dosegli točko, k...

#### Rank 5: RELEVANT

- Title: KPK: V Sloveniji manjka ustrezno prevzemanje odgovornosti najvišjih predstavnikov oblasti
- Decision: relevant
- Rationale: About KPK and accountability of top Slovenian officials.
- Category/date: slovenija / 2026-02-10T10:23:44
- URL: https://www.rtvslo.si/slovenija/kpk-v-sloveniji-manjka-ustrezno-prevzemanje-odgovornosti-najvisjih-predstavnikov-oblasti/772947
- FAISS rank/score: 5 / 0.7515
- Reranker score: n/a
- Keywords: korupcija, CPI, Slovenija
- Excerpt: KPK: V Sloveniji manjka ustrezno prevzemanje odgovornosti najvišjih predstavnikov oblasti Ključne besede: korupcija, CPI, Slovenija Slovenija je v Indeksu zaznave korupcije za leto 2025 dosegla 58 od 100 točk in se uvrstila na 41. mesto med 182 državami. Slovenija je v primerjavi z lani padla za pet mest. Premier Golob: "Morda smo bili uspavani z odličnimi rezultati v letu 2024" Po lanskem skoku navzgor, ko je Slovenija na lestvici zaznave korupcije za leto 2024 dosegla 60 točk, je letos indeks...


### 16. Izstrelitev rakete v vesolje

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Video: Tako je iz vesolja videti izstrelitev rakete
- Decision: relevant
- Rationale: Directly about a rocket launch seen from space.
- Category/date: znanost-in-tehnologija / 2018-11-25T11:06:09
- URL: https://www.rtvslo.si/znanost-in-tehnologija/video-tako-je-iz-vesolja-videti-izstrelitev-rakete/472829
- FAISS rank/score: 1 / 0.8347
- Reranker score: n/a
- Keywords: ISS, Mednarodna vesoljska postaja, Alexander Gerst, Poleti s posadko, Progress, Sojuz, raketa, vesolje, izstrelitev, vesoljsko plovilo, zaloge, Evropska vesoljska agencija, Esa, astronavt, poveljnik, kozmodrom, orbite, gorivo, kisik, preizkus, nesreča, senzor, Rusija, posadke, kupola, fotoaparat, fotografiranje.
- Excerpt: Video: Tako je iz vesolja videti izstrelitev rakete Ključne besede: ISS, Mednarodna vesoljska postaja, Alexander Gerst, Poleti s posadko, Progress, Sojuz, raketa, vesolje, izstrelitev, vesoljsko plovilo, zaloge, Evropska vesoljska agencija, Esa, astronavt, poveljnik, kozmodrom, orbite, gorivo, kisik, preizkus, nesreča, senzor, Rusija, posadke, kupola, fotoaparat, fotografiranje. Astronavt Alexander Gerst je posnel izstrelitev rakete z drugačne perspektive, kot smo je vajeni. Ujel je plovilo MS-1...

#### Rank 2: RELEVANT

- Title: Raketo s prvima slovenskima satelitoma le izstrelili: "V vesolju smo!"
- Decision: relevant
- Rationale: Directly about a rocket launch carrying Slovenian satellites into space.
- Category/date: znanost-in-tehnologija / 2020-09-03T06:47:51
- URL: https://www.rtvslo.si/znanost-in-tehnologija/raketo-s-prvima-slovenskima-satelitoma-le-izstrelili-v-vesolju-smo/535004
- FAISS rank/score: 2 / 0.8105
- Reranker score: n/a
- Keywords: satelit, izstrelitev, Vega, Nemo HD in Trisat, Francoska Gvajana, raketa, Nemo HD, Trisat, evropska znanost, Arianespace, vesoljski center, Kourou, vodja projekta, Centrer odličnosti Vesolje-SI, znanost, slovensko gospodarstvo, orbita, vesolje, mikrosatelit, nanosatelit, testiranje
- Excerpt: Raketo s prvima slovenskima satelitoma le izstrelili: "V vesolju smo!" Ključne besede: satelit, izstrelitev, Vega, Nemo HD in Trisat, Francoska Gvajana, raketa, Nemo HD, Trisat, evropska znanost, Arianespace, vesoljski center, Kourou, vodja projekta, Centrer odličnosti Vesolje-SI, znanost, slovensko gospodarstvo, orbita, vesolje, mikrosatelit, nanosatelit, testiranje Iz Francoske Gvajane so ponoči vendarle izstrelili raketo Vega, s katero sta v vesolje poletela tudi prva slovenska satelita Nemo...

#### Rank 3: RELEVANT

- Title: Nasa uspešno izstrelila SpaceX-ovo raketo. Četverica bo v vesolju šest mesecev.
- Decision: relevant
- Rationale: Directly about a NASA/SpaceX rocket launch to space.
- Category/date: znanost-in-tehnologija / 2023-03-02T12:24:00
- URL: https://www.rtvslo.si/znanost-in-tehnologija/nasa-uspesno-izstrelila-spacex-ovo-raketo-cetverica-bo-v-vesolju-sest-mesecev/659714
- FAISS rank/score: 3 / 0.8073
- Reranker score: n/a
- Keywords: SpaceX, Dragon Crew-6, misija, Nasa, Elon Musk, mednarodna vesoljska postaja, posadka, izstrelitev, težave, vesolje, astronavt, orbita, Združeni arabski emirati, ISS, predaja, Zemlja, kapsula, Rusija, Sojuz, puščanje, Kazahstan
- Excerpt: Nasa uspešno izstrelila SpaceX-ovo raketo. Četverica bo v vesolju šest mesecev. Ključne besede: SpaceX, Dragon Crew-6, misija, Nasa, Elon Musk, mednarodna vesoljska postaja, posadka, izstrelitev, težave, vesolje, astronavt, orbita, Združeni arabski emirati, ISS, predaja, Zemlja, kapsula, Rusija, Sojuz, puščanje, Kazahstan Iz Nasinega vesoljskega centra Kennedy na Floridi so uspešno izstrelili raketo ameriškega podjetja SpaceX, ki je v lasti milijarderja Elona Muska. V okviru misije Dragon Crew-6...

#### Rank 4: RELEVANT

- Title: SpaceX bo v četrtek zvečer izstrelil mogočno raketo Starship
- Decision: relevant
- Rationale: Directly about a planned Starship rocket launch.
- Category/date: znanost-in-tehnologija / 2025-03-03T20:06:34
- URL: https://www.rtvslo.si/znanost-in-tehnologija/spacex-bo-v-cetrtek-zvecer-izstrelil-mogocno-raketo-starship/449493
- FAISS rank/score: 4 / 0.8055
- Reranker score: n/a
- Keywords: Tehnologija, Izstrelitev, Super Heavy, SpaceX, Starship
- Excerpt: SpaceX bo v četrtek zvečer izstrelil mogočno raketo Starship Ključne besede: Tehnologija, Izstrelitev, Super Heavy, SpaceX, Starship Ameriško podjetje SpaceX bo v četrtek opravilo osmi preizkusni polet rakete Starship. Znova bo poskusilo uloviti stopnjo Super Heavy. Starship je nadgrajen in precej večji, v vesolje pa bo oddal prototipe nove generacije satelitov Starlink. Enourno izstrelitveno okno se bo odprlo v noči s četrtka na petek ob 00.30 po našem času. Izstrelitev bo potekala z Boca Chice...

#### Rank 5: RELEVANT

- Title: Prva britanska izstrelitev vesoljske rakete se je končala z razočaranjem
- Decision: relevant
- Rationale: Directly about a space-rocket launch attempt.
- Category/date: znanost-in-tehnologija / 2023-01-09T15:17:00
- URL: https://www.rtvslo.si/znanost-in-tehnologija/prva-britanska-izstrelitev-vesoljske-rakete-se-je-koncala-z-razocaranjem/653702
- FAISS rank/score: 5 / 0.8042
- Reranker score: n/a
- Keywords: Cornwall, LauncherOne, Raketa, Velika Britanija, satelit, Orbita, Virgin Orbit, preizkus, napaka, vesolje, Richard Branson, motor, evropske vesoljske ambicije, Kozmično dekle, letalo Boeing 747, preureditev, misija Vega-V, Esina, Ukrajina, Ariane 6
- Excerpt: Prva britanska izstrelitev vesoljske rakete se je končala z razočaranjem Ključne besede: Cornwall, LauncherOne, Raketa, Velika Britanija, satelit, Orbita, Virgin Orbit, preizkus, napaka, vesolje, Richard Branson, motor, evropske vesoljske ambicije, Kozmično dekle, letalo Boeing 747, preureditev, misija Vega-V, Esina, Ukrajina, Ariane 6 Velika Britanija je davi s predelanega letala boeing 747 nad Atlantikom izstrelila svojo prvo raketo z devetimi sateliti, vendar LauncherOne zaradi napake ni dose...


### 17. Delnice Tesle padajo

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: Tehnološke delnice vidno sestopile z vrhov, še bolj pa Teslin dobiček
- Decision: relevant
- Rationale: Directly about technology shares falling and Tesla profit/stock context.
- Category/date: gospodarstvo / 2024-07-28T06:17:32
- URL: https://www.rtvslo.si/gospodarstvo/borzni-komentar/tehnoloske-delnice-vidno-sestopile-z-vrhov-se-bolj-pa-teslin-dobicek/716161
- FAISS rank/score: 1 / 0.8250
- Reranker score: n/a
- Keywords: MMC-jev borzni komentar, četrtletni poslovni rezultati, Tesla, Alphabet, Ford, Ryanair, Krka, dividenda
- Excerpt: Tehnološke delnice vidno sestopile z vrhov, še bolj pa Teslin dobiček Ključne besede: MMC-jev borzni komentar, četrtletni poslovni rezultati, Tesla, Alphabet, Ford, Ryanair, Krka, dividenda Po treh dneh resnih razprodaj so tehnološke delnice v New Yorku v petek le okrevale, delno tudi zaradi novih znakov, da se inflacija umirja in bi moral Fed s septembrom končno začeti zniževati obrestne mere, ki so že več kot leto dni na 23-letnem vrhu. Potem ko smo še v prvi polovici julija spremljali nove re...

#### Rank 2: NOT RELEVANT

- Title: Vrnitev Tesle in vzpon indeksa S & P nad 5500 točk
- Decision: not_relevant
- Rationale: About Tesla shares rising/recovering, the opposite of the prompt.
- Category/date: gospodarstvo / 2024-07-03T06:32:32
- URL: https://www.rtvslo.si/gospodarstvo/borzni-komentar/vrnitev-tesle-in-vzpon-indeksa-s-p-nad-5500-tock/713666
- FAISS rank/score: 2 / 0.8155
- Reranker score: n/a
- Keywords: MMC-jev borzni komentar, S & P 500, rekord, Tesline delnice
- Excerpt: Vrnitev Tesle in vzpon indeksa S & P nad 5500 točk Ključne besede: MMC-jev borzni komentar, S & P 500, rekord, Tesline delnice Wall Street je v drugo polletje vstopil optimistično, zadnje izjave Jeroma Powlla pa vlivajo upanje, da Fed dobiva boj z inflacijo. Indeksa S & P 500 in NASDAQ sta na novem rekordu, med posameznimi papirji pa je včeraj blestela Tesla. Tesline delnice so krenile za deset odstotkov navzgor (tudi nad 230 dolarjev), potem ko je proizvajalec električnih vozil sporočil, da je...

#### Rank 3: RELEVANT

- Title: Tesli se upad dobave avtomobilov že finančno pozna
- Decision: relevant
- Rationale: About Tesla financial decline after delivery drop.
- Category/date: zabava-in-slog / 2025-01-31T08:08:29
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/tesli-se-upad-dobave-avtomobilov-ze-financno-pozna/735101
- FAISS rank/score: 3 / 0.7987
- Reranker score: n/a
- Keywords: Tesla, Tesla Y, Cybertuck
- Excerpt: Tesli se upad dobave avtomobilov že finančno pozna Ključne besede: Tesla, Tesla Y, Cybertuck Proizvajalec električnih avtomobilov je lani prvič v več kot desetletju zaznal upad dobave avtomobilov. Tesla je v zadnjem lanskem četrtletju vknjižil 25,7 milijarde dolarjev prihodkov, kar je dva odstotka manj kot leto prej. Prihodki ameriškega proizvajalca električnih avtomobilov so bili nižji od pričakovanj analitikov, ki so v povprečju računali, da bodo znašali 27,3 milijarde dolarjev, poroča nemška...

#### Rank 4: RELEVANT

- Title: Tesla v prvem četrtletju s 13-odstotnim padcem prodaje avtomobilov
- Decision: relevant
- Rationale: Directly about Tesla sales falling and includes stock-drop context.
- Category/date: gospodarstvo / 2025-04-02T17:43:00
- URL: https://www.rtvslo.si/gospodarstvo/preberite-tudi/tesla-v-prvem-cetrtletju-s-13-odstotnim-padcem-prodaje-avtomobilov/741463
- FAISS rank/score: 4 / 0.7939
- Reranker score: n/a
- Keywords: Padec delnic, Bojkot, Elon Musk, Prodaja avtomobilov, Tesla
- Excerpt: Tesla v prvem četrtletju s 13-odstotnim padcem prodaje avtomobilov Ključne besede: Padec delnic, Bojkot, Elon Musk, Prodaja avtomobilov, Tesla Ameriški proizvajalec električnih avtomobilov Tesla je v prvem letošnjem četrtletju dobavil 336.681 avtomobilov, kar je 13 odstotkov manj kot leto prej, poroča francoska tiskovna agencija AFP. Manjša prodaja je posledica manjše proizvodnje zaradi posodabljanja tovarn in bojkota podjetja zaradi političnega delovanja direktorja Elona Muska. Število dobavlje...

#### Rank 5: RELEVANT

- Title: Veličastnih 7: v enem tednu izpuhtelo za skoraj bilijon papirnatega premoženja
- Decision: relevant
- Rationale: About major stock value losses among tech giants including Tesla.
- Category/date: gospodarstvo / 2024-04-21T06:06:20
- URL: https://www.rtvslo.si/gospodarstvo/borzni-komentar/velicastnih-7-v-enem-tednu-izpuhtelo-za-skoraj-bilijon-papirnatega-premozenja/705659
- FAISS rank/score: 5 / 0.7934
- Reranker score: n/a
- Keywords: MMC-jev borzni komentar, Nvidia, padec delnic, DZU, vzajemni skladi, bitcoin, halving, geopolitična situacija, delniški indeksi, padec vrednosti delnic, tehnološki velikani, Nvidija, Microsoft, Apple, Alphabet, Amazon, Meta, Tesla, tržna kapitalizacija, prodaja vozil, Tesla in stečaj, četrtletne objave, analitiki, dobiček, S & P-jev indeks
- Excerpt: Veličastnih 7: v enem tednu izpuhtelo za skoraj bilijon papirnatega premoženja Ključne besede: MMC-jev borzni komentar, Nvidia, padec delnic, DZU, vzajemni skladi, bitcoin, halving, geopolitična situacija, delniški indeksi, padec vrednosti delnic, tehnološki velikani, Nvidija, Microsoft, Apple, Alphabet, Amazon, Meta, Tesla, tržna kapitalizacija, prodaja vozil, Tesla in stečaj, četrtletne objave, analitiki, dobiček, S & P-jev indeks Geopolitična zaostrovanja so nekoliko oklestila vrednosti delni...


### 18. Nova verzija umetne inteligence

Precision@5: 1/5 = 0.20

#### Rank 1: NOT RELEVANT

- Title: Z umetno inteligenco brali možgansko aktivnost
- Decision: not_relevant
- Rationale: About an AI research application, not a new AI version/model.
- Category/date: znanost-in-tehnologija / 2017-08-23T13:05:58
- URL: https://www.rtvslo.si/znanost-in-tehnologija/z-umetno-inteligenco-brali-mozgansko-aktivnost/430694
- FAISS rank/score: 1 / 0.8220
- Reranker score: n/a
- Keywords: umetna inteligenca, UI, AI, simulacija nevronskih mrež, umetne nevronske mreže, encefalografija, možgani, Tonio Ball, Robin Tibor Schirrmeister, globoko učenje, možganska aktivnost, nevronske mreže, razvoj, algoritem, gibanje, trirazsežnostna telesa, raziskava, model, naravni signali, fonetični zvoki, plasti, nelinarna funkcija, vzorci obnašanja.
- Excerpt: Z umetno inteligenco brali možgansko aktivnost Ključne besede: umetna inteligenca, UI, AI, simulacija nevronskih mrež, umetne nevronske mreže, encefalografija, možgani, Tonio Ball, Robin Tibor Schirrmeister, globoko učenje, možganska aktivnost, nevronske mreže, razvoj, algoritem, gibanje, trirazsežnostna telesa, raziskava, model, naravni signali, fonetični zvoki, plasti, nelinarna funkcija, vzorci obnašanja. Nemški znanstveniki so ustvarili umetno inteligenco, ki se je sama naučila, kako razvozl...

#### Rank 2: NOT RELEVANT

- Title: Umetna inteligenca se že odloča namesto nas
- Decision: not_relevant
- Rationale: General article about AI decisions, not a new version/model.
- Category/date: znanost-in-tehnologija / 2018-06-28T07:47:02
- URL: https://www.rtvslo.si/znanost-in-tehnologija/umetna-inteligenca-se-ze-odloca-namesto-nas/459213
- FAISS rank/score: 2 / 0.8184
- Reranker score: n/a
- Keywords: Umetna inteligenca, Algoritem, Podatki, Futuristika, Kibervarnost, Tehnološka utopija, Digitalizacija, Tehnologija, IT varnost, digitalni velikani, moč, države, dodana vrednost, količina podatkov, uporaba podatkov, vzorci, ravnanja posameznikov, odmevne zgodbe, Snowden, Cambridge Analytica, manipulacije, prevzem oblasti, algoritmi, splet, življenjski partner, borza, zločin, odločitve, svet, rešitve, korporacije, zbiranje podatkov.
- Excerpt: Umetna inteligenca se že odloča namesto nas Ključne besede: Umetna inteligenca, Algoritem, Podatki, Futuristika, Kibervarnost, Tehnološka utopija, Digitalizacija, Tehnologija, IT varnost, digitalni velikani, moč, države, dodana vrednost, količina podatkov, uporaba podatkov, vzorci, ravnanja posameznikov, odmevne zgodbe, Snowden, Cambridge Analytica, manipulacije, prevzem oblasti, algoritmi, splet, življenjski partner, borza, zločin, odločitve, svet, rešitve, korporacije, zbiranje podatkov. Podat...

#### Rank 3: RELEVANT

- Title: Google predstavil nov program umetne inteligence Bard
- Decision: relevant
- Rationale: Directly about Google presenting a new AI program, Bard.
- Category/date: znanost-in-tehnologija / 2023-02-07T11:00:00
- URL: https://www.rtvslo.si/znanost-in-tehnologija/google-predstavil-nov-program-umetne-inteligence-bard/657070
- FAISS rank/score: 3 / 0.8147
- Reranker score: n/a
- Keywords: Google, Bard, Umetna inteligenca, jezikovni model, intervju, Sundar Pichai, LaMDA, ChatGPT, OpenAI, Microsoft, investicija, partnerstvo, tehnološko podjetje, aplikacije za dialog, razvoj, napredki, zunanji vplivi, primerjava, inovacija, iskalnik
- Excerpt: Google predstavil nov program umetne inteligence Bard Ključne besede: Google, Bard, Umetna inteligenca, jezikovni model, intervju, Sundar Pichai, LaMDA, ChatGPT, OpenAI, Microsoft, investicija, partnerstvo, tehnološko podjetje, aplikacije za dialog, razvoj, napredki, zunanji vplivi, primerjava, inovacija, iskalnik Ameriški tehnološki velikan Google je uradno predstavil nov program umetne inteligence Bard. Kot poudarjajo v podjetju, gre za pomemben naslednji korak na področju umetne inteligence z...

#### Rank 4: NOT RELEVANT

- Title: Umetna inteligenca spreminja svet
- Decision: not_relevant
- Rationale: General article about AI changing the world, not a new version/model.
- Category/date: znanost-in-tehnologija / 2018-01-02T06:38:17
- URL: https://www.rtvslo.si/znanost-in-tehnologija/umetna-inteligenca-spreminja-svet/441933
- FAISS rank/score: 4 / 0.8132
- Reranker score: n/a
- Keywords: umetna inteligenca, tehnologija, digitalni svet, matematika, strojno učenje, digitalizacija, podatkovna analiza, tehnološki napredek, razvoj tehnologije, programiranje, računalništvo, aplikacije, informacijska tehnologija, inovacije, algoritmi, podatkovno rudarjenje, avtomatizacija, zmogljivi računalniki, digitalni podatki
- Excerpt: Umetna inteligenca spreminja svet Ključne besede: umetna inteligenca, tehnologija, digitalni svet, matematika, strojno učenje, digitalizacija, podatkovna analiza, tehnološki napredek, razvoj tehnologije, programiranje, računalništvo, aplikacije, informacijska tehnologija, inovacije, algoritmi, podatkovno rudarjenje, avtomatizacija, zmogljivi računalniki, digitalni podatki Vsake toliko se pojavijo nove tehnologije – na primer tisk, parni stroj ali motor z notranjim zgorevanjem –, ki zmorejo v tem...

#### Rank 5: NOT RELEVANT

- Title: “Umetna inteligenca bo kot elektrika”
- Decision: not_relevant
- Rationale: General/future-looking article about AI, not a new version/model.
- Category/date: znanost-in-tehnologija / 2019-06-10T12:24:48
- URL: https://www.rtvslo.si/znanost-in-tehnologija/umetna-inteligenca-bo-kot-elektrika/491471
- FAISS rank/score: 5 / 0.8055
- Reranker score: n/a
- Keywords: Umetna inteligenca, znanost, frekvencax, prihodnost, etične dileme, tehnologija, regulacija, uporaba, družbene okoliščine, politične odločitve, znanstvenofantastične meje, digitalna etika, podatkovna etika, zlorabe, odgovornost, razvoj, tehnološke zmogljivosti, inovacije, zabrinutost, navdušenje
- Excerpt: “Umetna inteligenca bo kot elektrika” Ključne besede: Umetna inteligenca, znanost, frekvencax, prihodnost, etične dileme, tehnologija, regulacija, uporaba, družbene okoliščine, politične odločitve, znanstvenofantastične meje, digitalna etika, podatkovna etika, zlorabe, odgovornost, razvoj, tehnološke zmogljivosti, inovacije, zabrinutost, navdušenje Po enem izmed scenarijev bi nas umetna inteligenca lahko nepovratno prehitela kot dirkalni avto. In vsak dan ponudila nekaj deset odkritij v rangu No...


### 19. Najbolj prodajan avtomobil

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: V Sloveniji lani prodanih 8,4 odstotka več avtomobilov – največ Volkswagnovih
- Decision: relevant
- Rationale: Directly about best-selling car brands/models in Slovenia.
- Category/date: zabava-in-slog / 2025-01-08T13:22:41
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/v-sloveniji-lani-prodanih-8-4-odstotka-vec-avtomobilov-najvec-volkswagnovih/732724
- FAISS rank/score: 1 / 0.8124
- Reranker score: n/a
- Keywords: avtomobili, Slovenija, prodaja
- Excerpt: V Sloveniji lani prodanih 8,4 odstotka več avtomobilov – največ Volkswagnovih Ključne besede: avtomobili, Slovenija, prodaja V Sloveniji je bilo lani prvič registriranih 53.018 osebnih avtomobilov, kar je 8,4 odstotka več kot predlani. Med vsemi lani prodanimi osebnimi avtomobili je bilo električnih 9876 oziroma 27 odstotkov manj kot predlani. Največ osebnih avtomobilov je prodal Volkswagen (7924 oziroma skoraj 15-odstotni tržni delež), sledila sta Renault (5910 oziroma 11,2-odstotni delež) in Š...

#### Rank 2: RELEVANT

- Title: Lani največ avtomobilov prodal Volkswagen, najbolj priljubljena škoda octavia
- Decision: relevant
- Rationale: Directly about the brand/model that sold the most cars.
- Category/date: gospodarstvo / 2024-01-15T15:52:19
- URL: https://www.rtvslo.si/gospodarstvo/lani-najvec-avtomobilov-prodal-volkswagen-najbolj-priljubljena-skoda-octavia/694894
- FAISS rank/score: 2 / 0.8053
- Reranker score: n/a
- Keywords: Tržni delež, Električni avtomobili, Škoda Octavia, Volkswagen, avtomobili, Slovenija, registracija, vozilo, gospodarsko, znamka, model, električni avtomobil, hibridni pogon, prodaja, Škoda, Renault, Ford, Toyota, Tesla, ID.4, enyaq, corolla
- Excerpt: Lani največ avtomobilov prodal Volkswagen, najbolj priljubljena škoda octavia Ključne besede: Tržni delež, Električni avtomobili, Škoda Octavia, Volkswagen, avtomobili, Slovenija, registracija, vozilo, gospodarsko, znamka, model, električni avtomobil, hibridni pogon, prodaja, Škoda, Renault, Ford, Toyota, Tesla, ID.4, enyaq, corolla V Sloveniji je bilo lani prvič registriranih 48.923 osebnih avtomobilov, kar je 5,6 odstotka več kot predlani. Število prvič registriranih lahkih gospodarskih vozil...

#### Rank 3: RELEVANT

- Title: Tesla z dvema modeloma na lestvici najbolj prodajanih vozil na svetu
- Decision: relevant
- Rationale: Directly about best-selling vehicles worldwide.
- Category/date: zabava-in-slog / 2023-05-10T08:01:00
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/tesla-z-dvema-modeloma-na-lestvici-najbolj-prodajanih-vozil-na-svetu/667586
- FAISS rank/score: 3 / 0.8006
- Reranker score: n/a
- Keywords: Prodaja vozil, JATO Dynamics, Toyota RAV 4, Toyota, vozilo, prodaja, svet, avtomobili, modeli, Tesla, registracija, trg, razvoj, Severna Amerika, Evropa, Kitajska, padec, dobavna veriga, polprevodniki, motnje, Ukrajina, sankcije, Rusija, Volkswagen, Hyundai-Kia, Stellantis, General Motors, BYD, tržni delež, testiranje, Avtomobilnost.
- Excerpt: Tesla z dvema modeloma na lestvici najbolj prodajanih vozil na svetu Ključne besede: Prodaja vozil, JATO Dynamics, Toyota RAV 4, Toyota, vozilo, prodaja, svet, avtomobili, modeli, Tesla, registracija, trg, razvoj, Severna Amerika, Evropa, Kitajska, padec, dobavna veriga, polprevodniki, motnje, Ukrajina, sankcije, Rusija, Volkswagen, Hyundai-Kia, Stellantis, General Motors, BYD, tržni delež, testiranje, Avtomobilnost. Toyota je leta 2022 prodala največ vozil na svetu. Med desetimi najbolje prodaj...

#### Rank 4: RELEVANT

- Title: Tesla model Y leta 2023 najbolje prodajano vozilo v Evropi
- Decision: relevant
- Rationale: Directly about Tesla Model Y as the best-selling vehicle in Europe.
- Category/date: zabava-in-slog / 2024-01-21T12:31:47
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/tesla-model-y-leta-2023-najbolje-prodajano-vozilo-v-evropi/695612
- FAISS rank/score: 4 / 0.8005
- Reranker score: n/a
- Keywords: Tesla, Model Y, Prodaja vozil, električni avtomobil, Evropa, prodaja, Slovenija, leta 2023, registracije, cena, konkurenca, industrija, vozila, strokovnjaki, uspeh, popularnost, Dacia Sandero, Volkswagen T-Roc, Škoda Octavia
- Excerpt: Tesla model Y leta 2023 najbolje prodajano vozilo v Evropi Ključne besede: Tesla, Model Y, Prodaja vozil, električni avtomobil, Evropa, prodaja, Slovenija, leta 2023, registracije, cena, konkurenca, industrija, vozila, strokovnjaki, uspeh, popularnost, Dacia Sandero, Volkswagen T-Roc, Škoda Octavia Električni križanec tesla Y je prvi električni avtomobil, ki je do zdaj postal najbolje prodajano vozilo v Evropi v koledarskem letu. Tesla model Y je bil v Sloveniji sedmi najbolje prodajan model avt...

#### Rank 5: RELEVANT

- Title: Po skromnejšem maju se prodaja vozil v Sloveniji krepi
- Decision: relevant
- Rationale: About vehicle sales with top brands/models; sufficiently related to best-selling cars.
- Category/date: zabava-in-slog / 2023-07-08T09:08:41
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/po-skromnejsem-maju-se-prodaja-vozil-v-sloveniji-krepi/674464
- FAISS rank/score: 5 / 0.7900
- Reranker score: n/a
- Keywords: Prodaja vozil, škoda octavia, Tesla, avtomobilski trg, registracija vozil, rast prodaje, Slovenija, osebna vozila, gospodarska vozila, znamke, modeli vozil, elektrificirana vozila, električna vozila, hibridna vozila, registracije vozil, junij, trendi prodaje, trg vozil, statistika registracij, priključni hibridi, blagi hibridi, Volkswagen, Renault, Toyota, Škoda, Ford, Opel, vozni park
- Excerpt: Po skromnejšem maju se prodaja vozil v Sloveniji krepi Ključne besede: Prodaja vozil, škoda octavia, Tesla, avtomobilski trg, registracija vozil, rast prodaje, Slovenija, osebna vozila, gospodarska vozila, znamke, modeli vozil, elektrificirana vozila, električna vozila, hibridna vozila, registracije vozil, junij, trendi prodaje, trg vozil, statistika registracij, priključni hibridi, blagi hibridi, Volkswagen, Renault, Toyota, Škoda, Ford, Opel, vozni park Medletna rast prodaje novih vozil na avt...


### 20. Obisk tujega predsednika

Precision@5: 0/5 = 0.00

#### Rank 1: NOT RELEVANT

- Title: Uradni portret Donalda Trumpa spominja na njegovo zaporniško fotografijo. Namerno?
- Decision: not_relevant
- Rationale: About Trump official portrait, not a foreign president visit.
- Category/date: zabava-in-slog / 2025-01-17T09:02:28
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/uradni-portret-donalda-trumpa-spominja-na-njegovo-zapornisko-fotografijo-namerno/733643
- FAISS rank/score: 1 / 0.7376
- Reranker score: n/a
- Keywords: portret, Donald Trump, JD Vance, inavguracija
- Excerpt: Uradni portret Donalda Trumpa spominja na njegovo zaporniško fotografijo. Namerno? Ključne besede: portret, Donald Trump, JD Vance, inavguracija Znana sta uradna portreta Donalda Trumpa in JD Vancea, ki bosta v ponedeljek uradno začela svoja mandata novega predsednika in podpredsednika ZDA. Trump in Vance, oba republikanca, sta se odločila za usklajen videz, saj sta oba izbrala modro obleko, belo srajco in modro kravato. Trump poleg tega na suknjiču nosi tudi majhno značko z ameriško zastavo. Dr...

#### Rank 2: NOT RELEVANT

- Title: Voznik, ki je trčil v ogrado Bele hiše, obtožen poskusa napada na predsednika ZDA
- Decision: not_relevant
- Rationale: About an attempted attack at the White House, not a presidential visit.
- Category/date: svet / 2023-05-24T09:59:00
- URL: https://www.rtvslo.si/svet/preberite-tudi/voznik-ki-je-trcil-v-ogrado-bele-hise-obtozen-poskusa-napada-na-predsednika-zda/669290
- FAISS rank/score: 2 / 0.7325
- Reranker score: n/a
- Keywords: ZDA, Bela hiša, voznik, Selitveni tovornjak, Napad, Predsednik ZDA, Uničevanje, Javna lastnina, Ameriški mediji, Obveščevalna služba, Missouri, Tožilstvo, Nacistični spominki, Betonska ograda, Evakuacija, Washington, Tajna služba, St. Louis, Umor, Genetski poskusi
- Excerpt: Voznik, ki je trčil v ogrado Bele hiše, obtožen poskusa napada na predsednika ZDA Ključne besede: ZDA, Bela hiša, voznik, Selitveni tovornjak, Napad, Predsednik ZDA, Uničevanje, Javna lastnina, Ameriški mediji, Obveščevalna služba, Missouri, Tožilstvo, Nacistični spominki, Betonska ograda, Evakuacija, Washington, Tajna služba, St. Louis, Umor, Genetski poskusi Voznik, ki je nedavno z najetim selitvenim tovornjakom večkrat trčil v varnostno ogrado Bele hiše, je obtožen napada na predsednika ZDA i...

#### Rank 3: NOT RELEVANT

- Title: Trump portret Obame zamenjal za svojega, Bela hiša kritiku: "Umiri se, bedak"
- Decision: not_relevant
- Rationale: About a portrait change in the White House, not a foreign president visit.
- Category/date: zabava-in-slog / 2025-04-13T08:03:20
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/trump-portret-obame-zamenjal-za-svojega-bela-hisa-kritiku-umiri-se-bedak/742593
- FAISS rank/score: 3 / 0.7297
- Reranker score: n/a
- Keywords: Bela hiša, Portret, Obama, Trump
- Excerpt: Trump portret Obame zamenjal za svojega, Bela hiša kritiku: "Umiri se, bedak" Ključne besede: Bela hiša, Portret, Obama, Trump Ameriški predsednik Donald Trump je v Beli hiši uradni portret nekdanjega predsednika Baracka Obame zamenjal s svojo lastno podobo. Namesto 44. predsednika ZDA preddverje Bele hiše zdaj krasi upodobitev Trumpa tik po poskusu atentata julija lani. Nova slika, ki zdaj visi v preddverju Državnega nadstropja Bele hiše, prikazuje trenutek, ko Donald Trump, prekrit s krvjo, dv...

#### Rank 4: NOT RELEVANT

- Title: Donald Trump – kako je nepredvidljivi nepremičninski mogotec pristal v Beli hiši
- Decision: not_relevant
- Rationale: Biographical/political profile of Trump, not a foreign presidential visit.
- Category/date: svet / 2024-08-16T08:30:09
- URL: https://www.rtvslo.si/svet/zda-2024/donald-trump-kako-je-nepredvidljivi-nepremicninski-mogotec-pristal-v-beli-hisi/718117
- FAISS rank/score: 4 / 0.7281
- Reranker score: n/a
- Keywords: Donald Trump, ZDA 2024, Trump
- Excerpt: Donald Trump – kako je nepredvidljivi nepremičninski mogotec pristal v Beli hiši Ključne besede: Donald Trump, ZDA 2024, Trump Donald Trump je imel kot predsednik nemalo pomanjkljivosti. A ker imajo ZDA kratek spomin in jih štiri leta vidno pešajočega Joeja Bidna niso ravno navdahnile, se obračajo nazaj k Trumpu. Vsaj so se, dokler je bil njegov protikandidat Biden. S precej bolj energično Kamalo Harris so karte zdaj premešane. A kakšna je bila pot 78-letnega Trumpa do položaja, ko se še v tretj...

#### Rank 5: NOT RELEVANT

- Title: Donald Trump – kako je nepredvidljivi nepremičninski mogotec končal v Beli hiši
- Decision: not_relevant
- Rationale: Duplicate biographical/political profile of Trump, not a foreign presidential visit.
- Category/date: svet / 2024-08-16T08:30:09
- URL: https://www.rtvslo.si/svet/zda-2024/donald-trump-kako-je-nepredvidljivi-nepremicninski-mogotec-koncal-v-beli-hisi/718117
- FAISS rank/score: 5 / 0.7253
- Reranker score: n/a
- Keywords: Donald Trump, ZDA 2024, Trump
- Excerpt: Donald Trump – kako je nepredvidljivi nepremičninski mogotec končal v Beli hiši Ključne besede: Donald Trump, ZDA 2024, Trump Donald Trump je imel kot predsednik nemalo pomanjkljivosti. A ker imajo ZDA kratek spomin in jih štiri leta vidno pešajočega Joeja Bidna niso ravno navdihnila, se obračajo nazaj k Trumpu. Oziroma so se, dokler je bil njegov protikandidat Biden. S precej bolj energično Kamalo Harris so karte zdaj premešane. A kakšna je bila pot 78-letnega Trumpa do položaja, ko se še tretj...

