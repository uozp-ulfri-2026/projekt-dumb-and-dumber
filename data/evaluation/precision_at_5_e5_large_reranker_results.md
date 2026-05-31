# Precision@5 evaluation with reranker on - intfloat/multilingual-e5-large

Created: 2026-05-31T20:37:02
Relevance rule: largely related
Embedding model: `intfloat/multilingual-e5-large`
Reranker model: `cross-encoder/mmarco-mMiniLMv2-L12-H384-v1`
Retrieval: FAISS top 50 candidates, cross-encoder reranked, evaluated top 5
Raw output source: `data/evaluation/precision_at_5_e5_large_reranker_raw_outputs.json`

## Overall result

- Total relevant results: 88/100
- Precision@5: 0.88

## Per-prompt summary

| # | Prompt | Relevant@5 | Precision@5 |
|---:|---|---:|---:|
| 1 | Vpis v srednje šole | 5/5 | 1.00 |
| 2 | Zakoni glede generativne umetne inteligence | 5/5 | 1.00 |
| 3 | Cene kart na nogometnem svetovnem prvenstvu | 3/5 | 0.60 |
| 4 | Tožba slovenskih avtoprevoznikov | 2/5 | 0.40 |
| 5 | Vojna Zvezd v Sloveniji | 1/5 | 0.20 |
| 6 | Ogromni zastoji na Slovenskih cestah | 5/5 | 1.00 |
| 7 | Višanje temperatur | 5/5 | 1.00 |
| 8 | Višanje cen nepremičnin v Sloveniji | 5/5 | 1.00 |
| 9 | Rogljič in Pogačar na tekmi | 5/5 | 1.00 |
| 10 | Donald Trump novi zakoni | 4/5 | 0.80 |
| 11 | Evropska Unija in zveza NATO | 5/5 | 1.00 |
| 12 | Velika Britanija Brexit | 5/5 | 1.00 |
| 13 | Vojna v Ukrajini in Zelenski | 5/5 | 1.00 |
| 14 | Kitajska proti ZDA | 5/5 | 1.00 |
| 15 | Korupcija v slovenski politiki | 5/5 | 1.00 |
| 16 | Izstrelitev rakete v vesolje | 5/5 | 1.00 |
| 17 | Delnice Tesle padajo | 4/5 | 0.80 |
| 18 | Nova verzija umetne inteligence | 4/5 | 0.80 |
| 19 | Najbolj prodajan avtomobil | 5/5 | 1.00 |
| 20 | Obisk tujega predsednika | 5/5 | 1.00 |

## Detailed decisions

### 1. Vpis v srednje šole

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Vpis je omejen na 58 srednjih šolah, povečal se je vpis v srednje in nižje poklicne šole
- Decision: relevant
- Rationale: Direct secondary-school enrolment result.
- Category/date: slovenija / 2024-05-23T11:08:23
- URL: https://www.rtvslo.si/slovenija/vpis-je-omejen-na-58-srednjih-solah-povecal-se-je-vpis-v-srednje-in-nizje-poklicne-sole/709285
- FAISS rank/score: 2 / 0.8641
- Reranker score: 4.7520
- Keywords: Ministrstvo za vzgojo in izobraževanje, Gimnazijski programi, Poklicno izobraževanje, Srednje šole, Vpis
- Excerpt: Vpis je omejen na 58 srednjih šolah, povečal se je vpis v srednje in nižje poklicne šole Ključne besede: Ministrstvo za vzgojo in izobraževanje, Gimnazijski programi, Poklicno izobraževanje, Srednje šole, Vpis Prihodnje šolsko leto bo srednje šole obiskovalo 22.971 kandidatov, največ, 42,7 odstotka, se jih je vpisalo v srednje strokovne šole, sledijo gimnazije, srednje poklicne in nižje poklicne šole. Vpis bo omejen na 58 šolah, medtem ko je bil lani na 70. Vpis je omejen v 12 programih poklicne...

#### Rank 2: RELEVANT

- Title: Vpis v srednje šole: največ zanimanja za srednje strokovne šole
- Decision: relevant
- Rationale: Direct secondary-school enrolment result.
- Category/date: slovenija / 2023-04-25T17:29:00
- URL: https://www.rtvslo.si/slovenija/vpis-v-srednje-sole-najvec-zanimanja-za-srednje-strokovne-sole/666150
- FAISS rank/score: 4 / 0.8626
- Reranker score: 4.5939
- Keywords: vpis, šolsko leto, srednje šole, kandidati, mesta, prijavnica, izobraževalni programi, ministrstvo, poklicno izobraževanje, gimnazije, strokovno izobraževanje, razpisana mesta, podatki, statistika, sprejem, vpisni postopek, razporeditev, sposobnosti, prvi krog, programi, prosti poklice, želeni poklic, osnovno šolanje.
- Excerpt: Vpis v srednje šole: največ zanimanja za srednje strokovne šole Ključne besede: vpis, šolsko leto, srednje šole, kandidati, mesta, prijavnica, izobraževalni programi, ministrstvo, poklicno izobraževanje, gimnazije, strokovno izobraževanje, razpisana mesta, podatki, statistika, sprejem, vpisni postopek, razporeditev, sposobnosti, prvi krog, programi, prosti poklice, želeni poklic, osnovno šolanje. Za vpis novincev v srednje šole za prihodnje šolsko leto se je v roku na skupno 25.560 prvotno razpi...

#### Rank 3: RELEVANT

- Title: Vpisovanje v srednje šole: izteka se zadnji rok za prijavo za opravljanje preizkusa nadarjenosti
- Decision: relevant
- Rationale: Direct secondary-school application result.
- Category/date: slovenija / 2024-03-04T08:39:01
- URL: https://www.rtvslo.si/slovenija/vpisovanje-v-srednje-sole-izteka-se-zadnji-rok-za-prijavo-za-opravljanje-preizkusa-nadarjenosti/700309
- FAISS rank/score: 6 / 0.8623
- Reranker score: 3.1737
- Keywords: preizkus nadarjenosti, znanja in spretnosti, osnovna šola, prijava, skit scena, preizkus, nadarjenost, znanje, spretnosti, srednješolski programi, vpisni pogoji, športni oddelki, obvestilo, zdravniško potrdilo, preventivni pregled, športni pogoji, klasični jeziki, tuj jezik, gimnazija, obrazci, novinci, vpisna mesta, splošne gimnazije, strokovne gimnazije
- Excerpt: Vpisovanje v srednje šole: izteka se zadnji rok za prijavo za opravljanje preizkusa nadarjenosti Ključne besede: preizkus nadarjenosti, znanja in spretnosti, osnovna šola, prijava, skit scena, preizkus, nadarjenost, znanje, spretnosti, srednješolski programi, vpisni pogoji, športni oddelki, obvestilo, zdravniško potrdilo, preventivni pregled, športni pogoji, klasični jeziki, tuj jezik, gimnazija, obrazci, novinci, vpisna mesta, splošne gimnazije, strokovne gimnazije Izteka se rok za prijavo za o...

#### Rank 4: RELEVANT

- Title: Za bodoče dijake še vedno na voljo približno 2700 prostih mest, omejitev vpisa na 69 srednjih šolah
- Decision: relevant
- Rationale: Direct secondary-school places/enrolment result.
- Category/date: slovenija / 2025-06-02T10:40:25
- URL: https://www.rtvslo.si/slovenija/za-bodoce-dijake-se-vedno-na-voljo-priblizno-2700-prostih-mest-omejitev-vpisa-na-69-srednjih-solah/747655
- FAISS rank/score: 9 / 0.8596
- Reranker score: 3.1383
- Keywords: srednje šole, vpis, omejitev, dijaki, Študenti, Skit scena
- Excerpt: Za bodoče dijake še vedno na voljo približno 2700 prostih mest, omejitev vpisa na 69 srednjih šolah Ključne besede: srednje šole, vpis, omejitev, dijaki, Študenti, Skit scena Letos je moralo zaradi velikega interesa vpis omejiti 69 srednjih šol, kar je devet več kot lani. "Vendar velja posebej poudariti, da večina teh šol, ki bodo vpis omejile, nima posebnih presežkov prijavljenih," ob tem poudarjajo na ministrstvu. Na srednje šole se je do 6. maja, ko je bil zaključen rok za prenos prijav, za v...

#### Rank 5: RELEVANT

- Title: V srednje šole sprejetih 22.127 bodočih dijakov, na voljo je bilo 25.444 vpisnih mest
- Decision: relevant
- Rationale: Direct secondary-school enrolment result.
- Category/date: slovenija / 2023-07-03T08:56:03
- URL: https://www.rtvslo.si/slovenija/v-srednje-sole-sprejetih-22-127-bodocih-dijakov-na-voljo-je-bilo-25-444-vpisnih-mest/673860
- FAISS rank/score: 8 / 0.8603
- Reranker score: 2.6587
- Keywords: Srednje šole, dijaki, vpis, prosta mesta, ministrstvo, vzgoja, izobraževanje, srednješolski programi, prijavno-vpisni postopek, novinci, razpisana mesta, poklicno izobraževanje, gimnazije, omejitev vpisa, izbirni postopek, želeno šolo, drugi krog, mest, šole
- Excerpt: V srednje šole sprejetih 22.127 bodočih dijakov, na voljo je bilo 25.444 vpisnih mest Ključne besede: Srednje šole, dijaki, vpis, prosta mesta, ministrstvo, vzgoja, izobraževanje, srednješolski programi, prijavno-vpisni postopek, novinci, razpisana mesta, poklicno izobraževanje, gimnazije, omejitev vpisa, izbirni postopek, želeno šolo, drugi krog, mest, šole Ministrstvo za vzgojo in izobraževanje je objavilo število še prostih mest za vpis v 1. letnik posameznih srednješolskih programov. Kandida...


### 2. Zakoni glede generativne umetne inteligence

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: ZPS: Umetna inteligenca prinaša tudi negativne posledice – kršenje zasebnosti in osebne integritete
- Decision: relevant
- Rationale: AI regulation/rights/legal context.
- Category/date: gospodarstvo / 2023-06-20T13:58:03
- URL: https://www.rtvslo.si/gospodarstvo/zps-umetna-inteligenca-prinasa-tudi-negativne-posledice-krsenje-zasebnosti-in-osebne-integritete/672448
- FAISS rank/score: 5 / 0.8465
- Reranker score: 2.6032
- Keywords: Generativna umetna inteligenca, ZPS, Chat GPT, umetna inteligenca, potrošniki, tehnologija, aplikacija, pravice, zaupanje, varnost, kršenje zasebnosti, internet, digitalna politika, zakonodaja, Evropska unija, regulativa, ozaveščanje, opolnomočenje, lobiranje
- Excerpt: ZPS: Umetna inteligenca prinaša tudi negativne posledice – kršenje zasebnosti in osebne integritete Ključne besede: Generativna umetna inteligenca, ZPS, Chat GPT, umetna inteligenca, potrošniki, tehnologija, aplikacija, pravice, zaupanje, varnost, kršenje zasebnosti, internet, digitalna politika, zakonodaja, Evropska unija, regulativa, ozaveščanje, opolnomočenje, lobiranje V zadnjih mesecih je prišlo do bliskovite rasti ponudbe storitev, ki jih poganja generativna umetna inteligenca, ta pa ogrož...

#### Rank 2: RELEVANT

- Title: "Umetniška dela ustvarjajo izključno ljudje": poziv evropskega knjižnega sektorja za zaščito knjig
- Decision: relevant
- Rationale: Generative AI and copyright/legal protection.
- Category/date: kultura / 2025-04-23T17:02:00
- URL: https://www.rtvslo.si/kultura/knjige/umetniska-dela-ustvarjajo-izkljucno-ljudje-poziv-evropskega-knjiznega-sektorja-za-zascito-knjig/743658
- FAISS rank/score: 19 / 0.8383
- Reranker score: 2.0049
- Keywords: Evropski knjižni sektor, Generativna UI, Kulturni ekosistem, Avtorske pravice, Umetna inteligenca
- Excerpt: "Umetniška dela ustvarjajo izključno ljudje": poziv evropskega knjižnega sektorja za zaščito knjig Ključne besede: Evropski knjižni sektor, Generativna UI, Kulturni ekosistem, Avtorske pravice, Umetna inteligenca Ob vse večjem pojavu knjig, ki jih generira umetna inteligenca, evropski knjižni sektor poziva evropske politične odločevalce, da zaščitijo avtorska dela z jasnimi oznakami, finančno pa naj strojnega dela ne podpirajo z javnimi sredstvi. " Strojno izdelani proizvodi, ki z uporabo genera...

#### Rank 3: RELEVANT

- Title: Ob koncu kampanje UIzi prevedeno. UIzi zgrešeno: "UI naj v etični rabi podpira človečnost"
- Decision: relevant
- Rationale: AI ethics/transparency/copyright regulation.
- Category/date: kultura / 2025-11-03T17:49:11
- URL: https://www.rtvslo.si/kultura/jezik/ob-koncu-kampanje-uizi-prevedeno-uizi-zgreseno-ui-naj-v-eticni-rabi-podpira-clovecnost/762817
- FAISS rank/score: 43 / 0.8288
- Reranker score: 1.7153
- Keywords: Jezikovni poklici, Transparentnost, Etična raba, Avtorska pravica, Umetna inteligenca
- Excerpt: Ob koncu kampanje UIzi prevedeno. UIzi zgrešeno: "UI naj v etični rabi podpira človečnost" Ključne besede: Jezikovni poklici, Transparentnost, Etična raba, Avtorska pravica, Umetna inteligenca Organizatorji kampanje UIzi prevedeno. UIzi zgrešeno so ob njenem zaključku na javnost in odločevalce naslovili več zahtev, ki se dotikajo avtorskih pravic, transparentnosti glede rabe UI-ja ter ohranitve in razvoja jezikovnih poklicev. Glede avtorske pravice so zahteve podali v osmih točkah. Med drugim za...

#### Rank 4: RELEVANT

- Title: Vizualni umetniki pridobivajo v pravni bitki proti umetni inteligenci. Bo z glasbo drugače?
- Decision: relevant
- Rationale: Legal battle around AI training/copyright.
- Category/date: kultura / 2024-08-14T21:03:41
- URL: https://www.rtvslo.si/kultura/glasba/vizualni-umetniki-pridobivajo-v-pravni-bitki-proti-umetni-inteligenci-bo-z-glasbo-drugace/718051
- FAISS rank/score: 1 / 0.8586
- Reranker score: 0.6209
- Keywords: Poštena uporaba, Generativna orodja, Umetniška tožba, Avtorske pravice, Generirana umetnost
- Excerpt: Vizualni umetniki pridobivajo v pravni bitki proti umetni inteligenci. Bo z glasbo drugače? Ključne besede: Poštena uporaba, Generativna orodja, Umetniška tožba, Avtorske pravice, Generirana umetnost Pravno urejanje uporabe vizualnih ali glasbenih del za učenje umetne inteligence postaja vse bolj zapleteno, kar dokazujejo tudi zadnji sodni primeri v ZDA. V prihodnjih mesecih bo jasno, ali gre za pošteno uporabo ali kršitve avtorskih pravic. Na začetku letošnjega leta smo poročali o dolgem seznam...

#### Rank 5: RELEVANT

- Title: Vlada sprejela predlog, ki prinaša enotna pravila za razvoj in uporabo umetne inteligence v EU-ju
- Decision: relevant
- Rationale: Direct AI law/rules result.
- Category/date: slovenija / 2025-08-21T15:32:29
- URL: https://www.rtvslo.si/slovenija/vlada-sprejela-predlog-ki-prinasa-enotna-pravila-za-razvoj-in-uporabo-umetne-inteligence-v-eu-ju/755310
- FAISS rank/score: 20 / 0.8375
- Reranker score: 0.5668
- Keywords: UI, zakon, evropska uredba
- Excerpt: Vlada sprejela predlog, ki prinaša enotna pravila za razvoj in uporabo umetne inteligence v EU-ju Ključne besede: UI, zakon, evropska uredba Vlada je sprejela predlog zakona o izvajanju evropske uredbe o določitvi harmoniziranih pravil o umetni inteligenci oz. akta o umetni inteligenci. Predlog med drugim določa nadzorne organe in uvaja možnost imenovanja komisarja za etiko umetne inteligence. Akt o umetni inteligenci, katerega namen je izboljšati delovanje notranjega trga z uvedbo enotnih pravi...


### 3. Cene kart na nogometnem svetovnem prvenstvu

Precision@5: 3/5 = 0.60

#### Rank 1: RELEVANT

- Title: Tožba proti Fifi zaradi visokih cen vstopnic na SP 2026
- Decision: relevant
- Rationale: Direct World Cup ticket price lawsuit.
- Category/date: sport / 2026-03-24T11:22:40
- URL: https://www.rtvslo.si/sport/nogomet/tozba-proti-fifi-zaradi-visokih-cen-vstopnic-na-sp-2026/777332
- FAISS rank/score: 3 / 0.8608
- Reranker score: 1.3264
- Keywords: vstopnice, cene, svetovno prvenstvo, nogomet
- Excerpt: Tožba proti Fifi zaradi visokih cen vstopnic na SP 2026 Ključne besede: vstopnice, cene, svetovno prvenstvo, nogomet Združenje nogometnih navijačev Evrope (FSE) je pri Evropski komisiji vložilo tožbo proti Mednarodni nogometni zvezi (Fifa) zaradi previsokih cen vstopnic na letošnjem svetovnem prvenstvu, ki bo v ZDA, Kanadi in Mehiki. "Fifa ima monopol nad prodajo vstopnic za svetovno prvenstvo 2026 in to moč je izkoristila za vsiljevanje pogojev nogometnim privržencem, ki v konkurenčnem tržnem o...

#### Rank 2: RELEVANT

- Title: Infantino zagovarja visoke cene vstopnic in pravi, da bodo ves denar vložili spet v nogomet
- Decision: relevant
- Rationale: Direct World Cup ticket price result.
- Category/date: sport / 2025-12-30T08:47:57
- URL: https://www.rtvslo.si/sport/nogomet/infantino-zagovarja-visoke-cene-vstopnic-in-pravi-da-bodo-ves-denar-vlozili-spet-v-nogomet/768669
- FAISS rank/score: 2 / 0.8611
- Reranker score: 0.9561
- Keywords: Gianni Infantino, Fifa, SP, vstopnice
- Excerpt: Infantino zagovarja visoke cene vstopnic in pravi, da bodo ves denar vložili spet v nogomet Ključne besede: Gianni Infantino, Fifa, SP, vstopnice Predsednik Mednarodne nogometne zveze Fife Gianni Infantino zagovarja visoke cene vstopnic za prihajajoče svetovno prvenstvo. Infantino je dejal, da cene vstopnic zgolj odražajo trenutno povpraševanje po njih. Združenje nogometnih navijačev (FSA) je od začetka prodaje vstopnic za tekmovanje, ki bo med 11. junijem in 19. julijem prihodnje leto potekalo...

#### Rank 3: NOT RELEVANT

- Title: Šeško zatresel mrežo nemočnega Kölna, Kane poskrbel za šov ob vrnitvi Neuerja
- Decision: not_relevant
- Rationale: Football match article, not World Cup ticket prices.
- Category/date: sport / 2023-10-28T18:29:20
- URL: https://www.rtvslo.si/sport/nogomet/nemsko-nogometno-prvenstvo/sesko-zatresel-mrezo-nemocnega-koelna-kane-poskrbel-za-sov-ob-vrnitvi-neuerja/686496
- FAISS rank/score: 37 / 0.8249
- Reranker score: 0.2751
- Keywords: Harry Kane, Manuel Neuer, Benjamin Šeško, Oliver Baumann, rdeči kartoni, hat-trick, Bayern, Allianz Arena, Darmstadt, Bundesliga, Nemčija, Katar, svetovno prvenstvo, zlom noge, okrevanje, Sven Ulreich, Joshua Kimmich, derbi, Dortmund, Konrad Laimer, Klaus Gjasula, Matej Maglica, videosodnik, Blancosljed, gol.
- Excerpt: Šeško zatresel mrežo nemočnega Kölna, Kane poskrbel za šov ob vrnitvi Neuerja Ključne besede: Harry Kane, Manuel Neuer, Benjamin Šeško, Oliver Baumann, rdeči kartoni, hat-trick, Bayern, Allianz Arena, Darmstadt, Bundesliga, Nemčija, Katar, svetovno prvenstvo, zlom noge, okrevanje, Sven Ulreich, Joshua Kimmich, derbi, Dortmund, Konrad Laimer, Klaus Gjasula, Matej Maglica, videosodnik, Blancosljed, gol. Trije rdeči kartoni v prvem polčasu, osem golov v drugem polčasu, hat-trick Harryja Kana z mojs...

#### Rank 4: RELEVANT

- Title: Ogromno povpraševanje za nogometni spektakel leta
- Decision: relevant
- Rationale: World Cup ticket demand/sales result.
- Category/date: sport / 2026-01-15T16:54:35
- URL: https://www.rtvslo.si/sport/nogomet/svetovno-prvenstvo-v-nogometu/ogromno-povprasevanje-za-nogometni-spektakel-leta/770262
- FAISS rank/score: 1 / 0.8636
- Reranker score: -0.0895
- Keywords: Fifa, Navijači, Prodaja vstopnic, Nogometni dogodek
- Excerpt: Ogromno povpraševanje za nogometni spektakel leta Ključne besede: Fifa, Navijači, Prodaja vstopnic, Nogometni dogodek V zadnjem delu prodaje je mednarodna nogometna zveza (Fifa) prejela več kot pol milijarde zahtevkov za vstopnice za ogled tekem letošnjega svetovnega prvenstva, ki bo poleti potekalo v ZDA, Kanadi in Mehiki. Prodaja vstopnic se je začela 11. decembra in je trajala do 13. januarja. Prvič so bile naprodaj posamezne vstopnice za določene tekme. Navijači bodo o morebitnem uspehu v na...

#### Rank 5: NOT RELEVANT

- Title: Zanimanje navijačev ogromno, zanesljivo bo "padel" Amsterdam 2000
- Decision: not_relevant
- Rationale: Euro football tickets, not World Cup ticket prices.
- Category/date: sport / 2024-02-12T18:34:36
- URL: https://www.rtvslo.si/sport/nogomet/evropsko-prvenstvo-v-nogometu/zanimanje-navijacev-ogromno-zanesljivo-bo-padel-amsterdam-2000/698108
- FAISS rank/score: 22 / 0.8324
- Reranker score: -0.6191
- Keywords: nogomet, evropsko prvenstvo 2024, nakup vstopnic, NZS, Martin Koželj, evropsko prvenstvo, vstopnice, prodaja, žreb, nakup, UEFA, preprodaja, splet, stadion, aplikacija, tekmovanje, tekme, ekipa, reprezentanca, spolzak teren, QR-koda, generalni sekretar
- Excerpt: Zanimanje navijačev ogromno, zanesljivo bo "padel" Amsterdam 2000 Ključne besede: nogomet, evropsko prvenstvo 2024, nakup vstopnic, NZS, Martin Koželj, evropsko prvenstvo, vstopnice, prodaja, žreb, nakup, UEFA, preprodaja, splet, stadion, aplikacija, tekmovanje, tekme, ekipa, reprezentanca, spolzak teren, QR-koda, generalni sekretar "Če bo kdo kupil vstopnico za EP prek drugih kanalov, bo na spolzkem terenu. Nekdo ti namreč lahko proda karto, a ne sprosti QR-kode 3 ure pred tekmo," opozarja gene...


### 4. Tožba slovenskih avtoprevoznikov

Precision@5: 2/5 = 0.40

#### Rank 1: NOT RELEVANT

- Title: Slovenski avtomobilski dobavitelji iščejo rešitev na Kitajskem
- Decision: not_relevant
- Rationale: Automotive suppliers, not hauliers/lawsuit.
- Category/date: gospodarstvo / 2024-10-08T16:18:51
- URL: https://www.rtvslo.si/gospodarstvo/slovenski-avtomobilski-dobavitelji-iscejo-resitev-na-kitajskem/646032
- FAISS rank/score: 45 / 0.8381
- Reranker score: 2.6029
- Keywords: Slovensko gospodarstvo, Avtomobilska industrija, Slovenska avtomobilska industrija, Matjaž Han, Slovenija-Kitajska, Dnevov dobaviteljev avtomobilske industrije
- Excerpt: Slovenski avtomobilski dobavitelji iščejo rešitev na Kitajskem Ključne besede: Slovensko gospodarstvo, Avtomobilska industrija, Slovenska avtomobilska industrija, Matjaž Han, Slovenija-Kitajska, Dnevov dobaviteljev avtomobilske industrije Slovenski avtomobilski dobavitelji v spremenjenih geopolitičnih razmerah vse bolj iščejo priložnosti na hitro rastočem kitajskem trgu. Te dni se v Ljubljani predstavljajo kitajskim proizvajalcem avtomobilov. Minister za gospodarstvo, turizem in šport Matjaž Han...

#### Rank 2: RELEVANT

- Title: Avtoprevozniki na zboru državi postavili zahteve, sicer lahko sledi zaprtje najpomembnejših cest
- Decision: relevant
- Rationale: Slovenian hauliers and demands; largely related.
- Category/date: gospodarstvo / 2025-10-18T15:03:41
- URL: https://www.rtvslo.si/gospodarstvo/avtoprevozniki-na-zboru-drzavi-postavili-zahteve-sicer-lahko-sledi-zaprtje-najpomembnejsih-cest/761263
- FAISS rank/score: 1 / 0.8628
- Reranker score: 2.2023
- Keywords: Digitalizacija, Kadrovska kriza, Zeleni prehod, Zaprtje cest, Avtoprevozniki
- Excerpt: Avtoprevozniki na zboru državi postavili zahteve, sicer lahko sledi zaprtje najpomembnejših cest Ključne besede: Digitalizacija, Kadrovska kriza, Zeleni prehod, Zaprtje cest, Avtoprevozniki Avtoprevozniki so na zboru v Celju na vlado naslovili zahteve, za katere pričakujejo, da jih izpolni do decembra oz. do marca 2026. V nasprotnem bodo decembra pripravili protest, za marec pa so napovedali zaprtje pomembnih cest v Sloveniji. Zbor sta organizirala sekcija za promet pri Obrtno-podjetniški zborni...

#### Rank 3: NOT RELEVANT

- Title: Avtoserviserji prijavili Zavarovalnico Triglav zaradi sumov zlorabe prevladujočega položaja na trgu
- Decision: not_relevant
- Rationale: Car repair shops/insurer, not hauliers.
- Category/date: gospodarstvo / 2025-05-12T13:48:49
- URL: https://www.rtvslo.si/gospodarstvo/avtoserviserji-prijavili-zavarovalnico-triglav-zaradi-sumov-zlorabe-prevladujocega-polozaja-na-trgu/745438
- FAISS rank/score: 8 / 0.8473
- Reranker score: 1.9528
- Keywords: AVK prijava, Urna postavka, Prevladojoči položaj, Avtoserviserji, Zavarovalnica Triglav
- Excerpt: Avtoserviserji prijavili Zavarovalnico Triglav zaradi sumov zlorabe prevladujočega položaja na trgu Ključne besede: AVK prijava, Urna postavka, Prevladojoči položaj, Avtoserviserji, Zavarovalnica Triglav Avtoserviserji, v Slovenskem društvu avtostroke (SDA), so Javni agenciji RS za varstvo konkurence (AVK) prijavili Zavarovalnico Triglav zaradi sumov zlorabe prevladujočega položaja na trgu. Trdijo, da so urne postavke nevzdržne in ne pokrijejo dela. Kot je danes v izjavi za medije pred sedežem A...

#### Rank 4: NOT RELEVANT

- Title: Avtoserviserji prijavili Zavarovalnico Triglav zaradi sumov zlorabe prevladujočega položaja na trgu
- Decision: not_relevant
- Rationale: Duplicate car repair shops/insurer result.
- Category/date: gospodarstvo / 2025-05-12T13:48:49
- URL: https://www.rtvslo.si/gospodarstvo/avtoserviserji-prijavili-zavarovalnico-triglav-zaradi-sumov-zlorabe-prevladojocega-polozaja-na-trgu/745438
- FAISS rank/score: 9 / 0.8473
- Reranker score: 1.9528
- Keywords: AVK prijava, Urna postavka, Prevladojoči položaj, Avtoserviserji, Zavarovalnica Triglav
- Excerpt: Avtoserviserji prijavili Zavarovalnico Triglav zaradi sumov zlorabe prevladujočega položaja na trgu Ključne besede: AVK prijava, Urna postavka, Prevladojoči položaj, Avtoserviserji, Zavarovalnica Triglav Avtoserviserji, v Slovenskem društvu avtostroke (SDA), so Javni agenciji RS za varstvo konkurence (AVK) prijavili Zavarovalnico Triglav zaradi sumov zlorabe prevladujočega položaja na trgu. Trdijo, da so urne postavke nevzdržne in ne pokrijejo dela. Kot je danes v izjavi za medije pred sedežem A...

#### Rank 5: RELEVANT

- Title: Avtoprevozniki zaradi kolapsa prometa čez Fernetiče grozijo tudi z zaprtjem avtocestnega križa
- Decision: relevant
- Rationale: Hauliers and traffic disruption; largely related.
- Category/date: gospodarstvo / 2025-08-26T13:18:22
- URL: https://www.rtvslo.si/gospodarstvo/avtoprevozniki-zaradi-kolapsa-prometa-cez-fernetice-grozijo-tudi-z-zaprtjem-avtocestnega-kriza/755699
- FAISS rank/score: 13 / 0.8460
- Reranker score: 1.9473
- Keywords: Primorska avtocesta, Prometni kolaps, Avtoprevozniki
- Excerpt: Avtoprevozniki zaradi kolapsa prometa čez Fernetiče grozijo tudi z zaprtjem avtocestnega križa Ključne besede: Primorska avtocesta, Prometni kolaps, Avtoprevozniki Avtoprevozniki zaradi posledic zaprtja vipavske hitre ceste proti Vrtojbi opozarjajo na neprevoznost na avtocesti A1 in pozivajo k takojšnjemu ukrepanju. Pred Fernetiči nastajajo kolone tovornjakov, ki segajo tudi na primorsko avtocesto. Avtoprevozniki so se danes zbrali na Razdrtem in pozvali odgovorne k takojšnjim ukrepom. Razmišlja...


### 5. Vojna Zvezd v Sloveniji

Precision@5: 1/5 = 0.20

#### Rank 1: NOT RELEVANT

- Title: Na čelu Zveze veteranov vojne za Slovenijo ostaja Ladislav Lipič
- Decision: not_relevant
- Rationale: False match on war veterans.
- Category/date: slovenija / 2024-04-06T19:27:44
- URL: https://www.rtvslo.si/slovenija/preberite-tudi/na-celu-zveze-veteranov-vojne-za-slovenijo-ostaja-ladislav-lipic/704146
- FAISS rank/score: 26 / 0.8176
- Reranker score: 2.8366
- Keywords: Mandatno obdobje, Ladislav Lipič, Zveza veteranov, Veterani, vojna, Slovenija, zveza, mandat, volitve, zbor, obrambni minister, Marjan Šarec, vrednote, domoljubje, pogum, Laško, epidemija, covid-19, poplave, izzivi, 30-letnica, teritorialna obramba, slavnostni govor, general Rudolf Maister, žrtve, politična opcija, društvo, ministrstvo, vojaški poklic, mladi, čast, zvestoba, poštenost, poročila, načrti, organe, volitve.
- Excerpt: Na čelu Zveze veteranov vojne za Slovenijo ostaja Ladislav Lipič Ključne besede: Mandatno obdobje, Ladislav Lipič, Zveza veteranov, Veterani, vojna, Slovenija, zveza, mandat, volitve, zbor, obrambni minister, Marjan Šarec, vrednote, domoljubje, pogum, Laško, epidemija, covid-19, poplave, izzivi, 30-letnica, teritorialna obramba, slavnostni govor, general Rudolf Maister, žrtve, politična opcija, društvo, ministrstvo, vojaški poklic, mladi, čast, zvestoba, poštenost, poročila, načrti, organe, voli...

#### Rank 2: RELEVANT

- Title: Po svetu praznujejo dan Vojne zvezd
- Decision: relevant
- Rationale: Direct Star Wars result.
- Category/date: zabava-in-slog / 2023-05-04T17:09:00
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/po-svetu-praznujejo-dan-vojne-zvezd/667027
- FAISS rank/score: 1 / 0.8381
- Reranker score: 1.3160
- Keywords: Vojna zvezd, Star Wars, May the fourth be with you, franšiza, filmi, kultura, popularni, datum, praznovanje, Luka Skywalker, George Lucas, animirani, igralci, televizijske serije, igrače, videoigre, Lego, BioWare, Slovenija, otroci, liki, imena
- Excerpt: Po svetu praznujejo dan Vojne zvezd Ključne besede: Vojna zvezd, Star Wars, May the fourth be with you, franšiza, filmi, kultura, popularni, datum, praznovanje, Luka Skywalker, George Lucas, animirani, igralci, televizijske serije, igrače, videoigre, Lego, BioWare, Slovenija, otroci, liki, imena Ljubitelji ene največjih znanstvenofantastičnih franšiz na svetu že od leta 2011 četrtega maja praznujejo dan Vojne zvezd. Kultni filmi so vse od prvenca leta 1977 premikali meje žanra in se zasidrali gl...

#### Rank 3: NOT RELEVANT

- Title: WSJ: V Sloveniji prijeta ruska vohuna v igri za izmenjavo zapornikov med ZDA in Rusijo?
- Decision: not_relevant
- Rationale: Russian spies/prisoner exchange, not Star Wars.
- Category/date: slovenija / 2024-06-17T19:27:41
- URL: https://www.rtvslo.si/slovenija/wsj-v-sloveniji-prijeta-ruska-vohuna-v-igri-za-izmenjavo-zapornikov-med-zda-in-rusijo/712098
- FAISS rank/score: 38 / 0.8157
- Reranker score: 1.2041
- Keywords: Obveščevalna služba SVR, Slovenija, Wall Street Journal, Izmenjava zapornikov, Ruska vohuna
- Excerpt: WSJ: V Sloveniji prijeta ruska vohuna v igri za izmenjavo zapornikov med ZDA in Rusijo? Ključne besede: Obveščevalna služba SVR, Slovenija, Wall Street Journal, Izmenjava zapornikov, Ruska vohuna Domnevnima ruskima vohunoma, ki so ju decembra 2022 prijeli v Sloveniji, bodo po tajnem sojenju v prihodnjih tednih izrekli sodbo zaradi vohunjenja. Po morebitni obsodbi bi lahko bila v igri za izmenjavo zapornikov med ZDA in Rusijo. Ameriški novinar Wall Street Journala (WSJ) Evan Gershkovich je zaradi...

#### Rank 4: NOT RELEVANT

- Title: Slovenska vojska že več kot 20 let izvaja naloge doma in v tujini
- Decision: not_relevant
- Rationale: Slovenian army, not Star Wars.
- Category/date: slovenija / 2025-01-13T19:51:47
- URL: https://www.rtvslo.si/slovenija/slovenska-vojska-ze-vec-kot-20-let-izvaja-naloge-doma-in-v-tujini/733247
- FAISS rank/score: 47 / 0.8151
- Reranker score: 0.8168
- Keywords: SV, Slovenska vojska, Poveljstvo sil Slovenske vojske
- Excerpt: Slovenska vojska že več kot 20 let izvaja naloge doma in v tujini Ključne besede: SV, Slovenska vojska, Poveljstvo sil Slovenske vojske Slovenska vojska že več kot 20 let tako doma kot v tujini dokazuje, da je pripravljena obvladovati situacije in izvajati naloge znotraj zavezništva, in tako bo tudi v prihodnje, sporoča poveljnik sil brigadir Boštjan Močnik. Danes (ponedeljek) praznujemo dan Poveljstva sil Slovenske vojske, ki je bilo ustanovljeno pred 21 leti, takrat kot odziv na konec obvezneg...

#### Rank 5: NOT RELEVANT

- Title: Astronavti v slovenski jami, vesoljski Brad Pitt in najmasivnejša nevtronska zvezda
- Decision: not_relevant
- Rationale: Space/science result, not Star Wars.
- Category/date: znanost-in-tehnologija / 2019-09-21T18:55:56
- URL: https://www.rtvslo.si/znanost-in-tehnologija/astronavti-v-slovenski-jami-vesoljski-brad-pitt-in-najmasivnejsa-nevtronska-zvezda/500126
- FAISS rank/score: 2 / 0.8310
- Reranker score: 0.5671
- Keywords: Vesolje, Vesoljski tednik, Vesoljski tednik 2019, Vesoljski tednik september 2019, neutrona zvezda, delci, astronavti, Slovenija, jamarstvo, trening, življenje, voda, mikroplastika, znanost, spretnosti, varnost, vesoljski program, komunikacija, eksperimenti, skupinsko delo, problemi, izolacija
- Excerpt: Astronavti v slovenski jami, vesoljski Brad Pitt in najmasivnejša nevtronska zvezda Ključne besede: Vesolje, Vesoljski tednik, Vesoljski tednik 2019, Vesoljski tednik september 2019, neutrona zvezda, delci, astronavti, Slovenija, jamarstvo, trening, življenje, voda, mikroplastika, znanost, spretnosti, varnost, vesoljski program, komunikacija, eksperimenti, skupinsko delo, problemi, izolacija Sveže iz vesolja: odkrili so najmasivnejšo (znano) nevtronsko zvezdo, s 70-metrsko napravo so merili drug...


### 6. Ogromni zastoji na Slovenskih cestah

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Ob številnih tujih turistih na slovenskih cestah ves dan pričakovana gneča in zastoji
- Decision: relevant
- Rationale: Direct traffic jams on Slovenian roads.
- Category/date: slovenija / 2023-05-18T10:36:00
- URL: https://www.rtvslo.si/slovenija/ob-stevilnih-tujih-turistih-na-slovenskih-cestah-ves-dan-pricakovana-gneca-in-zastoji/668570
- FAISS rank/score: 9 / 0.8549
- Reranker score: 3.3571
- Keywords: promet, zastoji, Dars, cesta, zastoj, avtocesta, turist, praznik, dela prost dan, gneča, prometno-informacijski center, prometna informacija, mestno središče, obvoznica, Ljubljana, štajerska avtocesta, število kolone, gorenjska avtocesta, primorska avtocesta, vzdrževanje ceste
- Excerpt: Ob številnih tujih turistih na slovenskih cestah ves dan pričakovana gneča in zastoji Ključne besede: promet, zastoji, Dars, cesta, zastoj, avtocesta, turist, praznik, dela prost dan, gneča, prometno-informacijski center, prometna informacija, mestno središče, obvoznica, Ljubljana, štajerska avtocesta, število kolone, gorenjska avtocesta, primorska avtocesta, vzdrževanje ceste Na slovenskih cestah je močno zgoščen promet, na številnih avtocestnih odsekih so tudi zastoji. Veliko je predvsem turis...

#### Rank 2: RELEVANT

- Title: AMZS: Na pot le spočiti in pripravljeni. Ceste bodo letos še bolj obremenjene.
- Decision: relevant
- Rationale: Congested Slovenian roads.
- Category/date: slovenija / 2024-06-22T07:35:13
- URL: https://www.rtvslo.si/slovenija/amzs-na-pot-le-spociti-in-pripravljeni-ceste-bodo-letos-se-bolj-obremenjene/712638
- FAISS rank/score: 36 / 0.8445
- Reranker score: 2.3447
- Keywords: Nadzor na meji, Reševalni pas, Prometni zastoji, Potovanje, AMZS
- Excerpt: AMZS: Na pot le spočiti in pripravljeni. Ceste bodo letos še bolj obremenjene. Ključne besede: Nadzor na meji, Reševalni pas, Prometni zastoji, Potovanje, AMZS Do konca poletja lahko pričakujemo občutno povečan promet na cestah proti Hrvaški, predvsem ob petkih in sobotah, ter v obratni smeri ob sobotah in nedeljah. AMZS voznike opozarja, naj se na pot ustrezno pripravijo ter prej preverijo stanje na cestah. Avto-moto zveza Slovenije (AMZS) voznike poziva, da se na pot odpravijo spočiti in le s...

#### Rank 3: RELEVANT

- Title: V več državah dela prost dan, na avtocestah so bili zastoji
- Decision: relevant
- Rationale: Highway traffic jams.
- Category/date: slovenija / 2023-06-08T08:19:00
- URL: https://www.rtvslo.si/slovenija/v-vec-drzavah-dela-prost-dan-na-avtocestah-so-bili-zastoji/671058
- FAISS rank/score: 21 / 0.8499
- Reranker score: 1.8447
- Keywords: Promet, prazniki, gneča, katoliški praznik, rešnje telo, kri, telovo, Avstrija, Nemčija, Hrvaška, prost dan, počitnice, tujina, policija, zastoji, avtocesta, prometni center, Slovenija, Italija, obvoznica, delovna zapora, Maribor, Ljubljana, Koper, zastoj, Brda, Brezovica, Kopru
- Excerpt: V več državah dela prost dan, na avtocestah so bili zastoji Ključne besede: Promet, prazniki, gneča, katoliški praznik, rešnje telo, kri, telovo, Avstrija, Nemčija, Hrvaška, prost dan, počitnice, tujina, policija, zastoji, avtocesta, prometni center, Slovenija, Italija, obvoznica, delovna zapora, Maribor, Ljubljana, Koper, zastoj, Brda, Brezovica, Kopru Ob katoliškem prazniku svetega rešnjega telesa in krvi, imenovanem tudi telovo, ki je v več državah, med drugim v Avstriji, večjem delu Nemčije...

#### Rank 4: RELEVANT

- Title: Zastoji precej preizkušali živce voznikov
- Decision: relevant
- Rationale: Traffic jams result.
- Category/date: slovenija / 2025-06-19T07:24:19
- URL: https://www.rtvslo.si/slovenija/zastoji-precej-preizkusali-zivce-voznikov/749447
- FAISS rank/score: 27 / 0.8482
- Reranker score: 1.5828
- Keywords: Zastoji, Telovo, Avtoceste, Promet
- Excerpt: Zastoji precej preizkušali živce voznikov Ključne besede: Zastoji, Telovo, Avtoceste, Promet Zaradi katoliškega praznika telovo, ki je v Avstriji, večjem delu Nemčije in na Hrvaškem dela prost dan, je na slovenskih cestah nastal povečan promet. Zastoji so bili na več odsekih, gneča je bila tudi na ljubljanski obvoznici. Promet je bil pričakovano gost s številnimi zastoji, predvsem na avtocestah. Poglavitni razlog je bil praznik telovo, ki je v več evropskih državah dela prost dan. Stanje se je z...

#### Rank 5: RELEVANT

- Title: Bratušek: Čudežnih rešitev za trenutno stanje na slovenskih avtocestah ne more biti
- Decision: relevant
- Rationale: Slovenian highway congestion result.
- Category/date: slovenija / 2024-08-27T08:45:56
- URL: https://www.rtvslo.si/slovenija/bratusek-cudeznih-resitev-za-trenutno-stanje-na-slovenskih-avtocestah-ne-more-biti/719127
- FAISS rank/score: 19 / 0.8508
- Reranker score: 1.3037
- Keywords: promet, zastoji, Alenka Bratušek, Matej Ogrin, Marcel Štefančič, oddaja Marcel
- Excerpt: Bratušek: Čudežnih rešitev za trenutno stanje na slovenskih avtocestah ne more biti Ključne besede: promet, zastoji, Alenka Bratušek, Matej Ogrin, Marcel Štefančič, oddaja Marcel "Mislim, da ni realnih možnosti, da bo v naslednjih petih letih bolje," glede stanja na slovenskih avtocestah priznava ministrica Alenka Bratušek. Da hitrih rešitev za zastoje ni, poudarja tudi Matej Ogrin. "Na to se bomo morali navaditi," je dejal. Na slovenskih cestah je vse več osebnih in tovornih vozil, gneča in pro...


### 7. Višanje temperatur

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: "Ob nadaljnjem dviganju temperature bodo neurja še bistveno močnejša"
- Decision: relevant
- Rationale: Rising temperature/climate effect.
- Category/date: okolje / 2023-07-26T08:14:24
- URL: https://www.rtvslo.si/okolje/vreme-in-podnebje/ob-nadaljnjem-dviganju-temperature-bodo-neurja-se-bistveno-mocnejsa/676161
- FAISS rank/score: 47 / 0.8104
- Reranker score: -0.4744
- Keywords: neurja, klimatologija, podnebne spremembe, vremensko dogajanje, zračne mase, segrevanje ozračja, globalno segrevanje, temperature, klimatolog, padavine, suša, veter, toča, poplave, vodni viri, politika prilagajanja, turizem, kmetijstvo, zdravstvo, potrošniki, podnebni modeli
- Excerpt: "Ob nadaljnjem dviganju temperature bodo neurja še bistveno močnejša" Ključne besede: neurja, klimatologija, podnebne spremembe, vremensko dogajanje, zračne mase, segrevanje ozračja, globalno segrevanje, temperature, klimatolog, padavine, suša, veter, toča, poplave, vodni viri, politika prilagajanja, turizem, kmetijstvo, zdravstvo, potrošniki, podnebni modeli Ekstremno vremensko dogajanje, ki smo mu priča v zadnjih dneh, je posledica stika dveh zračnih mas nad našim ozemljem, zelo tople nad Sred...

#### Rank 2: RELEVANT

- Title: Namesto hlajenja ukrepi za preprečevanje pregrevanja mest
- Decision: relevant
- Rationale: Overheating cities/high temperature context.
- Category/date: slovenija / 2023-06-29T11:15:54
- URL: https://www.rtvslo.si/slovenija/ob-osmih/namesto-hlajenja-ukrepi-za-preprecevanje-pregrevanja-mest/673475
- FAISS rank/score: 16 / 0.8145
- Reranker score: -0.5247
- Keywords: Toplotni otoki, Mesta, Podnebne spremembe, temperatura, hlajenje, topel, junij, vroči dnevi, meteorološke statistike, podnebni vzorec, toplotni otok, klima, pregrevanje, mestno jedro, zeleni klini, urbana oaza, ranljivi prebivalci, vročinski valovi, segrevanje, svetovno prebivalstvo, vodne površine
- Excerpt: Namesto hlajenja ukrepi za preprečevanje pregrevanja mest Ključne besede: Toplotni otoki, Mesta, Podnebne spremembe, temperatura, hlajenje, topel, junij, vroči dnevi, meteorološke statistike, podnebni vzorec, toplotni otok, klima, pregrevanje, mestno jedro, zeleni klini, urbana oaza, ranljivi prebivalci, vročinski valovi, segrevanje, svetovno prebivalstvo, vodne površine V mestih se povečujeta tako temperatura kot število vročih dni; več kot za ogrevanje pozimi porabimo energije za hlajenje pole...

#### Rank 3: RELEVANT

- Title: Ob dvigu temperature lahko pričakujemo več komarjev
- Decision: relevant
- Rationale: Effects of rising temperature.
- Category/date: slovenija / 2025-08-07T13:24:43
- URL: https://www.rtvslo.si/slovenija/ob-dvigu-temperature-lahko-pricakujemo-vec-komarjev/754077
- FAISS rank/score: 2 / 0.8248
- Reranker score: -0.6272
- Keywords: Repelenti, Preventivni ukrepi, Komarji
- Excerpt: Ob dvigu temperature lahko pričakujemo več komarjev Ključne besede: Repelenti, Preventivni ukrepi, Komarji Začetek poletja je bil sušen, zato je bilo komarjev manj. Zadnje deževje in višja temperatura bosta vplivala na njihovo številčnost. Odstranjevanje vode iz okolja in pravilno odlaganje odpadkov ter urejanje zelenih zmanjšujejo možnosti za razmnoževanje. Za razvoj komarjev sta ključni stoječa voda in zadostna toplota. Vodja kustodiata za nevretenčarje v Prirodoslovnem muzeju Slovenije Tea Kn...

#### Rank 4: RELEVANT

- Title: Z višanjem temperatur se "facekiniji" prodajajo kot vroče žemljice
- Decision: relevant
- Rationale: Explicit rising temperatures result.
- Category/date: zabava-in-slog / 2023-07-21T12:05:56
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/z-visanjem-temperatur-se-facekiniji-prodajajo-kot-vroce-zemljice/675739
- FAISS rank/score: 43 / 0.8109
- Reranker score: -0.6364
- Keywords: vročina, Kitajska, sonce, facekini, zaščita pred soncem, pokrivala, vročinski rekordi, UV-žarki, bela polt, kozmetični izdelki, sončne bolezni, turizem, Peking, maska za obraz, prodaja, prodajalna, pandemija, zaščitna sredstva, ventilatorji, klasična lepota, pokrivala za obraz, koža
- Excerpt: Z višanjem temperatur se "facekiniji" prodajajo kot vroče žemljice Ključne besede: vročina, Kitajska, sonce, facekini, zaščita pred soncem, pokrivala, vročinski rekordi, UV-žarki, bela polt, kozmetični izdelki, sončne bolezni, turizem, Peking, maska za obraz, prodaja, prodajalna, pandemija, zaščitna sredstva, ventilatorji, klasična lepota, pokrivala za obraz, koža Ob podiranju vročinskih rekordov se vse več ljudi na Kitajskem odloči za nakup posebnega pokrivala, imenovanega "facekini". Z njim pr...

#### Rank 5: RELEVANT

- Title: Temperature do 37 stopinj Celzija, osvežitev v soboto
- Decision: relevant
- Rationale: High-temperature/weather result.
- Category/date: okolje / 2022-08-05T07:51:19
- URL: https://www.rtvslo.si/okolje/temperature-do-37-stopinj-celzija-osvezitev-v-soboto/636337
- FAISS rank/score: 50 / 0.8102
- Reranker score: -1.1821
- Keywords: vročina, vročinski val, vreme, temperatura, stopinje Celzija, Agencija RS za okolje, zrak, mraz, planote, hladna fronta, nevihte, veter, burja, padavine, suša, deževje
- Excerpt: Temperature do 37 stopinj Celzija, osvežitev v soboto Ključne besede: vročina, vročinski val, vreme, temperatura, stopinje Celzija, Agencija RS za okolje, zrak, mraz, planote, hladna fronta, nevihte, veter, burja, padavine, suša, deževje Pričakovati je vrhunec tretjega letošnjega vročinskega vala, temperature naj bi se povzpele do 37 stopinj Celzija. Največja toplotna obremenitev bo popoldne, in sicer na Primorskem in po nižinah v notranjosti Slovenije. Kot je za Radio Slovenija povedal dežurni...


### 8. Višanje cen nepremičnin v Sloveniji

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Cene stanovanj so se lani zvišale za 8,5 odstotka
- Decision: relevant
- Rationale: Direct real-estate price rise.
- Category/date: gospodarstvo / 2025-03-24T11:15:44
- URL: https://www.rtvslo.si/gospodarstvo/cene-stanovanj-so-se-lani-zvisale-za-8-5-odstotka/740422
- FAISS rank/score: 9 / 0.8640
- Reranker score: 6.7813
- Keywords: Nove družinske hiše, Rabljena stanovanja, Prodaja nepremičnin, Zvišanje cen, Cene stanovanj
- Excerpt: Cene stanovanj so se lani zvišale za 8,5 odstotka Ključne besede: Nove družinske hiše, Rabljena stanovanja, Prodaja nepremičnin, Zvišanje cen, Cene stanovanj Cene stanovanjskih nepremičnin v Sloveniji so se lani zvišale deseto leto zapored, tokrat za 8,5 odstotka. Skupaj je bilo prodanih za približno 1,3 milijarde evrov stanovanjskih nepremičnin, kar je 14,7 odstotka manj kot leto prej. Lani se je zmanjšalo tudi število transakcij s stanovanjskimi nepremičninami. Potem ko je leta 2023 novega las...

#### Rank 2: RELEVANT

- Title: Gurs: V Sloveniji lani prodanih manj hiš in stanovanj. Cene zrasle za devet oz. deset odstotkov.
- Decision: relevant
- Rationale: Direct Slovenian housing price rise.
- Category/date: gospodarstvo / 2025-04-15T06:31:30
- URL: https://www.rtvslo.si/gospodarstvo/gurs-v-sloveniji-lani-prodanih-manj-his-in-stanovanj-cene-zrasle-za-devet-oz-deset-odstotkov/742731
- FAISS rank/score: 2 / 0.8742
- Reranker score: 6.7633
- Keywords: Cene stanovanj, Nepremičninski trg, Gurs
- Excerpt: Gurs: V Sloveniji lani prodanih manj hiš in stanovanj. Cene zrasle za devet oz. deset odstotkov. Ključne besede: Cene stanovanj, Nepremičninski trg, Gurs Po podatkih Gursa je lani precej upadla prodaja vseh vrst nepremičnin. Na drugi strani pa so se denimo v Ljubljani cene stanovanj zvišale za kar 500 evrov/m2. "Povpraševanje še vedno močno presega ponudbo," pravi Boštjan Udovič iz GZS-ja. Geodetska uprava (Gurs) je na začetku aprila objavila poročilo o slovenskem nepremičninskem trgu za leto 20...

#### Rank 3: RELEVANT

- Title: Prodaja nepremičnin upada, cene pa še naprej rastejo
- Decision: relevant
- Rationale: Direct real-estate prices rising.
- Category/date: gospodarstvo / 2024-12-23T15:25:02
- URL: https://www.rtvslo.si/gospodarstvo/prodaja-nepremicnin-upada-cene-pa-se-naprej-rastejo/731459
- FAISS rank/score: 5 / 0.8694
- Reranker score: 5.3918
- Keywords: nepremičnine, prodaja, cene
- Excerpt: Prodaja nepremičnin upada, cene pa še naprej rastejo Ključne besede: nepremičnine, prodaja, cene Prodaja stanovanjskih nepremičnin v Sloveniji upada. V tretjem četrtletju je bilo prodanih celo najmanj rabljenih nepremičnin v zadnjih 14 letih. Cene nepremičnin medtem še naprej rastejo, najbolj prav za rabljena stanovanja in hiše. Po izračunih Statističnega urada RS (Surs) je bilo v tretjem četrtletju letošnjega leta skupno prodnih 1737 stanovanjskih nepremičnin. To je 16 odstotkov manj kot v četr...

#### Rank 4: RELEVANT

- Title: Lani rekordne cene nepremičnin, a nepremičninski trg se ohlaja
- Decision: relevant
- Rationale: Direct real-estate price result.
- Category/date: slovenija / 2023-03-31T17:33:00
- URL: https://www.rtvslo.si/slovenija/lani-rekordne-cene-nepremicnin-a-nepremicninski-trg-se-ohlaja/663341
- FAISS rank/score: 7 / 0.8675
- Reranker score: 5.2698
- Keywords: nepremičnine, stanovanja, hiše, prodaja, nepremičninski trg, cene, Gurs, rast, trg, Slovenija, rekord, zemljišča, Geodetska uprava RS, Ljubljana, Obala, alpsko turistično območje, Kranjska Gora, Bled, Bohinjsko jezero, cene kvadratnega metra, povprečje, Kranj, Medvode, Domžale, Kamnik, Grosuplje, Vrhnika, Logatec, Gorenjska, Novo mesto, nova Gorica, Vipavska dolina, Goriška brda, Bela krajina, Prekmurje.
- Excerpt: Lani rekordne cene nepremičnin, a nepremičninski trg se ohlaja Ključne besede: nepremičnine, stanovanja, hiše, prodaja, nepremičninski trg, cene, Gurs, rast, trg, Slovenija, rekord, zemljišča, Geodetska uprava RS, Ljubljana, Obala, alpsko turistično območje, Kranjska Gora, Bled, Bohinjsko jezero, cene kvadratnega metra, povprečje, Kranj, Medvode, Domžale, Kamnik, Grosuplje, Vrhnika, Logatec, Gorenjska, Novo mesto, nova Gorica, Vipavska dolina, Goriška brda, Bela krajina, Prekmurje. Cene stanovan...

#### Rank 5: RELEVANT

- Title: Lani cene stanovanjskih hiš zrasle za devet odstotkov, cene stanovanj za deset odstotkov
- Decision: relevant
- Rationale: Housing/rental crisis related to rising housing costs.
- Category/date: gospodarstvo / 2025-04-01T18:17:30
- URL: https://www.rtvslo.si/gospodarstvo/lani-cene-stanovanjskih-his-zrasle-za-devet-odstotkov-cene-stanovanj-za-deset-odstotkov/741359
- FAISS rank/score: 19 / 0.8571
- Reranker score: 3.7431
- Keywords: Prodaja zemljišč, Srednja cena, Nepremičninski trg, Rast cen, Cene stanovanj
- Excerpt: Lani cene stanovanjskih hiš zrasle za devet odstotkov, cene stanovanj za deset odstotkov Ključne besede: Prodaja zemljišč, Srednja cena, Nepremičninski trg, Rast cen, Cene stanovanj Lani je na slovenskem nepremičninskem trgu tretje leto zaporedoma upadalo število kupoprodaj nepremičnin, medtem ko so cene še naprej rasle. GURS zmanjšanje pripisuje vladnim napovedim glede obdavčitve premoženja. Rast cen stanovanjskih nepremičnin in zemljišč za njihovo gradnjo lani po navedbah Geodetske uprave RS s...


### 9. Rogljič in Pogačar na tekmi

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Pogačar se bo v soboto prvič predstavil v mavrični majici
- Decision: relevant
- Rationale: Pogacar/race result.
- Category/date: sport / 2024-10-04T08:00:52
- URL: https://www.rtvslo.si/sport/kolesarstvo/pogacar-se-bo-v-soboto-prvic-predstavil-v-mavricni-majici/723155
- FAISS rank/score: 6 / 0.8463
- Reranker score: 6.4199
- Keywords: Tadej Pogačar, Primož Roglič, Remco Evenepoel
- Excerpt: Pogačar se bo v soboto prvič predstavil v mavrični majici Ključne besede: Tadej Pogačar, Primož Roglič, Remco Evenepoel Svetovni prvak Tadej Pogačar bo v mavrični majici prvič kolesaril v soboto na dirki Giro dell'Emilia v Italiji, kjer bosta tekmovala tudi Primož Roglič in Remco Evenepoel. 107. izvedba italijanske klasike, ki sicer ni del svetovne serije, bo za kolesarje priprava za zadnjo veliko dirko sezone – Dirko po Lombardiji. Zadnja izmed petih"klasik" bo na sporedu v soboto, 12. oktobra....

#### Rank 2: RELEVANT

- Title: Na Emiliji in Lombardiji prvo in drugo letošnje soočenje Pogačarja in Rogliča
- Decision: relevant
- Rationale: Direct Pogacar and Roglic race result.
- Category/date: sport / 2023-09-18T20:40:51
- URL: https://www.rtvslo.si/sport/kolesarstvo/na-emiliji-in-lombardiji-prvo-in-drugo-letosnje-soocenje-pogacarja-in-roglica/681833
- FAISS rank/score: 4 / 0.8470
- Reranker score: 6.3328
- Keywords: kolesarstvo, Dirka po Lombardiji, Tadej Pogačar, Primož Roglič, Marc Hirschi, ekipa UAE, slovenski državni prvak, Joxean Matxin Fernandez, Dirka po Emiliji, Dirka tri doline Vareseja, Vuelta, San Luco, Bologna, Dirka po Franciji, 2024, tritedenske dirke, enodnevne dirke, Madrid, kraljevska etapa, Angliru, Remco Evenepoel
- Excerpt: Na Emiliji in Lombardiji prvo in drugo letošnje soočenje Pogačarja in Rogliča Ključne besede: kolesarstvo, Dirka po Lombardiji, Tadej Pogačar, Primož Roglič, Marc Hirschi, ekipa UAE, slovenski državni prvak, Joxean Matxin Fernandez, Dirka po Emiliji, Dirka tri doline Vareseja, Vuelta, San Luco, Bologna, Dirka po Franciji, 2024, tritedenske dirke, enodnevne dirke, Madrid, kraljevska etapa, Angliru, Remco Evenepoel Tadej Pogačar je ob Marcu Hirschiju iz ekipe UAE že na startni listi Dirke po Lomba...

#### Rank 3: RELEVANT

- Title: Roglič v Andori dobil prestižno dirko 'pokra asov'
- Decision: relevant
- Rationale: Roglic race result; largely related.
- Category/date: sport / 2025-10-19T15:52:32
- URL: https://www.rtvslo.si/sport/kolesarstvo/roglic-v-andori-dobil-prestizno-dirko-pokra-asov/761326
- FAISS rank/score: 3 / 0.8473
- Reranker score: 4.9803
- Keywords: Primož Roglič, Tadej Pogačar, Jonas Vingegaard, Isaac del Toro
- Excerpt: Roglič v Andori dobil prestižno dirko 'pokra asov' Ključne besede: Primož Roglič, Tadej Pogačar, Jonas Vingegaard, Isaac del Toro Primož Roglič je zmagovalec dvodelne revijalne preizkušnje v Andori. Zasavec je bil dopoldne najhitrejši v gorskem kronometru, na mestnem kriteriju pa je bil drugi, kar je bilo dovolj za skupno zmago. Med štirimi tekmovalci je nastopal tudi Tadej Pogačar. Preizkušnja z imenom Andorra Cycling Masters je združila štiri zvezdnike kolesarstva. Ob Primožu Rogliču in Tadeju...

#### Rank 4: RELEVANT

- Title: Pogačar: Imamo več orožij. Če bomo dirkali pametno, imamo res močne karte.
- Decision: relevant
- Rationale: Pogacar cycling/race result.
- Category/date: sport / 2024-09-26T20:20:44
- URL: https://www.rtvslo.si/sport/kolesarstvo/svetovno-prvenstvo-v-kolesarstvu/pogacar-imamo-vec-orozij-ce-bomo-dirkali-pametno-imamo-res-mocne-karte/722330
- FAISS rank/score: 8 / 0.8446
- Reranker score: 4.9343
- Keywords: Tadej Pogačar, Primož Roglič, Uroš Murn
- Excerpt: Pogačar: Imamo več orožij. Če bomo dirkali pametno, imamo res močne karte. Ključne besede: Tadej Pogačar, Primož Roglič, Uroš Murn "Trasa je zelo zahtevna. Ni mi stoodstotno pisana na kožo, mi je pa veliko bolj kot lani," je povedal prvi favorit cestne dirke na svetovnem prvenstvu v kolesarstvu Tadej Pogačar. V Zürichu je slovenska kolesarska reprezentanca že v polni sestavi. Zadnji se je kolegom pridružil Luka Mezgec, glavna aduta Tadej Pogačar in Primož Roglič, ki sta letos skupaj osvojila vse...

#### Rank 5: RELEVANT

- Title: Slovenci po medaljo tako na cestni dirki kot na kronometru
- Decision: relevant
- Rationale: Slovenian cycling race/medal context.
- Category/date: sport / 2024-09-13T18:25:25
- URL: https://www.rtvslo.si/sport/kolesarstvo/svetovno-prvenstvo-v-kolesarstvu/slovenci-po-medaljo-tako-na-cestni-dirki-kot-na-kronometru/720972
- FAISS rank/score: 7 / 0.8447
- Reranker score: 4.8395
- Keywords: kolesarstvo, svetovno prvenstvo, Uroš Murn, Tadej Pogačar, Primož Roglič
- Excerpt: Slovenci po medaljo tako na cestni dirki kot na kronometru Ključne besede: kolesarstvo, svetovno prvenstvo, Uroš Murn, Tadej Pogačar, Primož Roglič Slovenija bo na svetovnem prvenstvu v kolesarstvu nastopila z najmočnejšo ekipo. "Na cestni dirki bodo nastopili vsi fantje, ki nastopajo v ekipah svetovne serije, Primož Roglič pa bo nastopil na cestni dirki in kronometru," je potrdil selektor Uroš Murn. Ob Pogačarju in Rogliču so se selektorjevemu pozivu za nastop na SP-ju v Švici (od 21. do 29. se...


### 10. Donald Trump novi zakoni

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: Trump najprej uvedel nove 10-odstotne carine, nato jih je dvignil na 15 odstotkov
- Decision: relevant
- Rationale: Trump tariff/policy result.
- Category/date: svet / 2026-02-21T09:59:57
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/trump-najprej-uvedel-nove-10-odstotne-carine-nato-jih-je-dvignil-na-15-odstotkov/774153
- FAISS rank/score: 12 / 0.8375
- Reranker score: 3.8402
- Keywords: Zakon o trgovini, Uvoz, Vrhovno sodišče, Carine, Trump
- Excerpt: Trump najprej uvedel nove 10-odstotne carine, nato jih je dvignil na 15 odstotkov Ključne besede: Zakon o trgovini, Uvoz, Vrhovno sodišče, Carine, Trump Ameriški predsednik Donald Trump je v petek ostro kritiziral sodnike vrhovnega sodišča, ki so razveljavili njegove t. i. vzajemne carine. Takoj je podpisal izvršni ukaz in uvedel nove splošne 10-odstotne carine, nato pa jih je povišal na 15 odstotkov. V odzivu na odločitev vrhovnega sodišča je Donald Trump napovedal, da bo nemudoma podpisal ukaz...

#### Rank 2: RELEVANT

- Title: Trump z novim zakonom uvedel višje kazni za trgovino s fentanilom
- Decision: relevant
- Rationale: Direct new Trump law result.
- Category/date: svet / 2025-07-17T10:37:53
- URL: https://www.rtvslo.si/svet/preberite-tudi/trump-z-novim-zakonom-uvedel-visje-kazni-za-trgovino-s-fentanilom/752186
- FAISS rank/score: 4 / 0.8404
- Reranker score: 3.8147
- Keywords: Nezakonito, Trgovina, Višje kazni, Fentanil, Trump
- Excerpt: Trump z novim zakonom uvedel višje kazni za trgovino s fentanilom Ključne besede: Nezakonito, Trgovina, Višje kazni, Fentanil, Trump Ameriški predsednik Donald Trump je v sredo podpisal zakon, ki sintetično drogo fentanil uvršča med najhujša prepovedana mamila v ZDA. Ob podpisu zakona je dejal, da bodo s tem zadali velik udarec mamilarskim kartelom, saj so za trgovino s fentanilom zdaj predvidene višje kazni. Fentanil je sredstvo, ki ga ameriški zdravniki včasih predpisujejo za lajšanje hudih bo...

#### Rank 3: NOT RELEVANT

- Title: Izvolitev Trumpa bi utegnila zamajati avtomobilsko industrijo
- Decision: not_relevant
- Rationale: Trump election effect on auto industry, not new laws.
- Category/date: zabava-in-slog / 2024-01-24T08:25:48
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/izvolitev-trumpa-bi-utegnila-zamajati-avtomobilsko-industrijo/695914
- FAISS rank/score: 13 / 0.8362
- Reranker score: 2.2184
- Keywords: Donald Trump, ameriške volitve, avtomobilska industrija, Nissan, General Motors, ZDA, električna vozila, zeleni prehod, zakon IRA, nizkoogljično gospodarstvo, subvencije, zelena energija, baterije, naložbe, gigatovarne, bidenomika, finančni direktor, izvršni direktor, notranje zgorevanje, deset odstotkov, Bidnova administracija
- Excerpt: Izvolitev Trumpa bi utegnila zamajati avtomobilsko industrijo Ključne besede: Donald Trump, ameriške volitve, avtomobilska industrija, Nissan, General Motors, ZDA, električna vozila, zeleni prehod, zakon IRA, nizkoogljično gospodarstvo, subvencije, zelena energija, baterije, naložbe, gigatovarne, bidenomika, finančni direktor, izvršni direktor, notranje zgorevanje, deset odstotkov, Bidnova administracija Nissan in GM svarita, da bi izvolitev Donalda Trumpa za novega predsednika ZDA škodovala pro...

#### Rank 4: RELEVANT

- Title: Začele so veljati nove ameriške carine, ki bodo sprva 10-odstotne. Veljale bodo 150 dni.
- Decision: relevant
- Rationale: New US tariff policy result.
- Category/date: gospodarstvo / 2026-02-24T10:37:01
- URL: https://www.rtvslo.si/gospodarstvo/zacele-so-veljati-nove-ameriske-carine-ki-bodo-sprva-10-odstotne-veljale-bodo-150-dni/774404
- FAISS rank/score: 10 / 0.8390
- Reranker score: 2.2000
- Keywords: ZDA, Donald Trump, Carine
- Excerpt: Začele so veljati nove ameriške carine, ki bodo sprva 10-odstotne. Veljale bodo 150 dni. Ključne besede: ZDA, Donald Trump, Carine Z današnjim dnem so začele veljati nove ameriške carine, ki jih je v petek v odzivu na razveljavitev lani uvedenih carin napovedal predsednik ZDA Donald Trump. Carine bodo sprva 10-, in ne 15-odstotne, kot je v soboto napovedal Trump. Ameriško vrhovno sodišče je v petek s šestimi glasovi proti trem razveljavilo carine, ki jih je Trump aprila lani uvedel na podlagi za...

#### Rank 5: RELEVANT

- Title: S Trumpovim podpisom končana delna blokada ameriške vlade
- Decision: relevant
- Rationale: Trump-signed government measure.
- Category/date: svet / 2026-02-04T07:05:07
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/s-trumpovim-podpisom-koncana-delna-blokada-ameriske-vlade/772270
- FAISS rank/score: 49 / 0.8285
- Reranker score: 2.0911
- Keywords: ZDA, Donald Trump, financiranje vlade
- Excerpt: S Trumpovim podpisom končana delna blokada ameriške vlade Ključne besede: ZDA, Donald Trump, financiranje vlade Ameriški predsednik Donald Trump je podpisal zakone o nadaljevanju financiranja agencij svoje vlade, potem ko jih je nekaj ur prej tesno z 217 proti 214 glasovom potrdil predstavniški dom kongresa, s čimer se je po štirih dneh končala delna blokada vlade. Že lani je bilo potrjenih šest zakonov o proračunski porabi za razna ministrstva, tokrat jih je bilo prav tako do konca proračunskeg...


### 11. Evropska Unija in zveza NATO

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Golob ob 30-letnici Sove pozval k samozavestni zadržanosti, budnosti in nenehni pripravljenosti
- Decision: relevant
- Rationale: EU/NATO/security architecture context.
- Category/date: slovenija / 2023-06-13T18:25:17
- URL: https://www.rtvslo.si/slovenija/golob-ob-30-letnici-sove-pozval-k-samozavestni-zadrzanosti-budnosti-in-nenehni-pripravljenosti/671692
- FAISS rank/score: 23 / 0.8376
- Reranker score: 1.7714
- Keywords: Sova, 30 let, Robert Golob, Evropa, prihodnost, vrednote, obveščevalna agencija, varnost, Jugoslavija, Evropska unija, NATO, Partnerstvo za mir, varnostna arhitektura, pariška listina, Rusija, Ukrajina, konflikt, begunska kriza, nacionalna varnost, suverenost, življenjski slog, tujina, partnerstvo, promet z občutljivim blagom, migracijski tokovi, informacijska varnost, protiobveščevalna dejavnost.
- Excerpt: Golob ob 30-letnici Sove pozval k samozavestni zadržanosti, budnosti in nenehni pripravljenosti Ključne besede: Sova, 30 let, Robert Golob, Evropa, prihodnost, vrednote, obveščevalna agencija, varnost, Jugoslavija, Evropska unija, NATO, Partnerstvo za mir, varnostna arhitektura, pariška listina, Rusija, Ukrajina, konflikt, begunska kriza, nacionalna varnost, suverenost, življenjski slog, tujina, partnerstvo, promet z občutljivim blagom, migracijski tokovi, informacijska varnost, protiobveščevaln...

#### Rank 2: RELEVANT

- Title: Erik Kopač: Za obrambo nismo sposobni porabiti niti dveh odstotkov BDP-ja
- Decision: relevant
- Rationale: NATO defence spending context.
- Category/date: slovenija / 2025-01-24T12:18:40
- URL: https://www.rtvslo.si/slovenija/ob-osmih/erik-kopac-za-obrambo-nismo-sposobni-porabiti-niti-dveh-odstotkov-bdp-ja/734420
- FAISS rank/score: 41 / 0.8358
- Reranker score: 1.7146
- Keywords: Vojaška industrija, Nato, Obrambni izdatki, Erik Kopač
- Excerpt: Erik Kopač: Za obrambo nismo sposobni porabiti niti dveh odstotkov BDP-ja Ključne besede: Vojaška industrija, Nato, Obrambni izdatki, Erik Kopač Pozivi za konkretno povečanje obrambnih izdatkov se kar vrstijo. Kolikšno povečanje je upravičeno, koliko pa ga napihuje vojaška industrija? Kaj si lahko privošči Slovenija? Po zamenjavi oblasti v Washingtonu se z vseh strani vrstijo pozivi k drastičnemu povečanju obrambnih izdatkov v evropskih članicah zveze Nato. Ameriški predsednik Donald Trump govor...

#### Rank 3: RELEVANT

- Title: Rutte: Nato je danes močnejši kot kdaj koli prej
- Decision: relevant
- Rationale: Direct NATO result.
- Category/date: svet / 2026-03-26T17:52:49
- URL: https://www.rtvslo.si/svet/evropa/rutte-nato-je-danes-mocnejsi-kot-kdaj-koli-prej/777638
- FAISS rank/score: 18 / 0.8392
- Reranker score: 1.0388
- Keywords: BDP, Povečanje, Mark Rutte, Obrambni izdatki, Nato
- Excerpt: Rutte: Nato je danes močnejši kot kdaj koli prej Ključne besede: BDP, Povečanje, Mark Rutte, Obrambni izdatki, Nato Evropske članice zveze Nato in Kanada so lani proračunske izdatke za obrambo v primerjavi z letom 2024 povečale za 20 odstotkov, je ob predstavitvi letnega poročila za 2025 sporočil generalni sekretar zavezništva Mark Rutte. "Številke v poročilu govorijo same zase. Naredili smo bistven napredek na področju obrambnih naložb in Nato je danes močnejši kot kdaj koli prej. Leta 2025 so...

#### Rank 4: RELEVANT

- Title: Rutte: Če mislite, da se lahko Evropa brani sama, kar sanjajte naprej
- Decision: relevant
- Rationale: Direct Europe/NATO defence result.
- Category/date: svet / 2026-01-26T18:46:29
- URL: https://www.rtvslo.si/svet/rutte-ce-mislite-da-se-lahko-evropa-brani-sama-kar-sanjajte-naprej/771341
- FAISS rank/score: 4 / 0.8428
- Reranker score: 1.0117
- Keywords: ZDA, Nato, Mark Rutte
- Excerpt: Rutte: Če mislite, da se lahko Evropa brani sama, kar sanjajte naprej Ključne besede: ZDA, Nato, Mark Rutte Evropa se ne more braniti brez ZDA, potrebujemo drug drugega, je ob zadnjih napetosti v čezatlantskih odnosih dejal generalni sekretar zveze Nato Mark Rutte. "Kar sanjajte naprej," je odvrnil tistim, ki menijo, da se lahko Evropa brani sama. " Če kdor koli tu misli, da se lahko Evropska unija ali Evropa kot celota brani brez ZDA, naj kar sanja naprej. Tega ne morete, tega ne moremo, potreb...

#### Rank 5: RELEVANT

- Title: Poročilo Nata: Kanada in evropske članice v lanskem letu občutno povečale izdatke za obrambo
- Decision: relevant
- Rationale: Direct NATO/european members result.
- Category/date: gospodarstvo / 2025-04-27T16:31:02
- URL: https://www.rtvslo.si/gospodarstvo/porocilo-nata-kanada-in-evropske-clanice-v-lanskem-letu-obcutno-povecale-izdatke-za-obrambo/744053
- FAISS rank/score: 13 / 0.8407
- Reranker score: 0.8555
- Keywords: Vojaška analiza, BDP cilj, NATO zavezništvo, Obrambni izdatki, Ruska agresija
- Excerpt: Poročilo Nata: Kanada in evropske članice v lanskem letu občutno povečale izdatke za obrambo Ključne besede: Vojaška analiza, BDP cilj, NATO zavezništvo, Obrambni izdatki, Ruska agresija Nato je dva meseca pred srečanjem voditeljev objavil poročilo generalnega sekretarja, ki med drugim prikazuje tudi porabo obrambnih izdatkov članic. Kanada in evropske članice so v letu 2024 občutno povečale izdatke za obrambo. Slovenija ostaja pri repu. Ruska agresija na Ukrajino je številne članice zveze NATO,...


### 12. Velika Britanija Brexit

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Velika Britanija prva evropska država v transpacifiškem prostotrgovinskem partnerstvu
- Decision: relevant
- Rationale: Post-Brexit UK trade context.
- Category/date: gospodarstvo / 2023-03-31T14:52:00
- URL: https://www.rtvslo.si/gospodarstvo/velika-britanija-prva-evropska-drzava-v-transpacifiskem-prostotrgovinskem-partnerstvu/663314
- FAISS rank/score: 2 / 0.8382
- Reranker score: 2.5412
- Keywords: Velika Britanija, CPTPP, transpacifiško prostotrgovinsko partnerstvo, transpacifiško partnerstvo, brexit, prostotrgovinski dogovor, gospodarske koristi, Rishi Sunak, Evropska unija, trgovinski bloki, Obama, Donald Trump, Kitajska, Japonska, Avstralija, Kanada, Nova Zelandija, Mehika, Južna Koreja, Tajvan, pridružitev
- Excerpt: Velika Britanija prva evropska država v transpacifiškem prostotrgovinskem partnerstvu Ključne besede: Velika Britanija, CPTPP, transpacifiško prostotrgovinsko partnerstvo, transpacifiško partnerstvo, brexit, prostotrgovinski dogovor, gospodarske koristi, Rishi Sunak, Evropska unija, trgovinski bloki, Obama, Donald Trump, Kitajska, Japonska, Avstralija, Kanada, Nova Zelandija, Mehika, Južna Koreja, Tajvan, pridružitev Velika Britanija se bo po dveh letih pogajanj pridružila Celostnemu in napredne...

#### Rank 2: RELEVANT

- Title: Britanci bodo zaostrili izdajanje vizumov, da bi zmanjšali priseljevanje
- Decision: relevant
- Rationale: UK migration policy explicitly tied to Brexit.
- Category/date: svet / 2023-12-05T09:17:17
- URL: https://www.rtvslo.si/svet/evropa/britanci-bodo-zaostrili-izdajanje-vizumov-da-bi-zmanjsali-priseljevanje/690539
- FAISS rank/score: 4 / 0.8310
- Reranker score: 2.0683
- Keywords: Velika Britanija, migracije, priseljevanje, tuji delavci, zakonito priseljevanje, nezakonito priseljevanje, minimalna plača, vizumi, družinski člani, politika, Evropska unija, brexit, neto migracije, Indija, Nigerija, Kitajska, premier, nadzor, javni zdravstveni sistem, notranji minister
- Excerpt: Britanci bodo zaostrili izdajanje vizumov, da bi zmanjšali priseljevanje Ključne besede: Velika Britanija, migracije, priseljevanje, tuji delavci, zakonito priseljevanje, nezakonito priseljevanje, minimalna plača, vizumi, družinski člani, politika, Evropska unija, brexit, neto migracije, Indija, Nigerija, Kitajska, premier, nadzor, javni zdravstveni sistem, notranji minister Velika Britanija se bo zaradi množičnega priseljevanja poleg nezakonitih migracij lotila tudi prihodov priseljencev po zak...

#### Rank 3: RELEVANT

- Title: Brexit je postal težava za e-mobilnost
- Decision: relevant
- Rationale: Direct Brexit result.
- Category/date: zabava-in-slog / 2023-06-05T07:45:00
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/brexit-je-postal-tezava-za-e-mobilnost/670651
- FAISS rank/score: 5 / 0.8287
- Reranker score: 1.6728
- Keywords: Brexit, Stellantis, carina, električni avtomobili, Velika Britanija, dajatve na izvoz, avtomobilska industrija, Aston Martin Lagonda, Unite, Carlos Tavares, električna vozila, BMW, Kitajska, Opel/Vauxhall, Ellesmere Port, dostavna vozila, investicije, zaposlovanje, gospodarstvo, kriza, blagovne znamke
- Excerpt: Brexit je postal težava za e-mobilnost Ključne besede: Brexit, Stellantis, carina, električni avtomobili, Velika Britanija, dajatve na izvoz, avtomobilska industrija, Aston Martin Lagonda, Unite, Carlos Tavares, električna vozila, BMW, Kitajska, Opel/Vauxhall, Ellesmere Port, dostavna vozila, investicije, zaposlovanje, gospodarstvo, kriza, blagovne znamke Morebitne dajatve na izvoz električnih avtomobilov iz Velike Britanije vznemirjajo avtomobilske proizvajalce. Stellantis odkrito grozi z zaprt...

#### Rank 4: RELEVANT

- Title: Brexit pričakovanj ni upravičil, britanska javnost pa ga skoraj ne omenja več
- Decision: relevant
- Rationale: Direct Brexit result.
- Category/date: svet / 2025-01-31T06:20:23
- URL: https://www.rtvslo.si/svet/evropa/brexit-pricakovanj-ni-upravicil-britanska-javnost-pa-ga-skoraj-ne-omenja-vec/735075
- FAISS rank/score: 1 / 0.8510
- Reranker score: 1.5294
- Keywords: Gospodarske posledice, Evropska unija, Združeno kraljestvo, Brexit, Jan Grobovšek
- Excerpt: Brexit pričakovanj ni upravičil, britanska javnost pa ga skoraj ne omenja več Ključne besede: Gospodarske posledice, Evropska unija, Združeno kraljestvo, Brexit, Jan Grobovšek Pred petimi leti je Združeno kraljestvo izstopilo iz Evropske unije. Ekonomist z univerze v Edinburgu Jan Grobovšek pravi, da je s tem država dobila "najslabše od obeh svetov" – postala je manjše gospodarstvo in ni ujela gospodarskih priložnosti. Združeno kraljestvo je 31. januarja 2020 po 47 letih članstva kot prva članic...

#### Rank 5: RELEVANT

- Title: Velika Britanija hoče preoblikovati severnoirski protokol
- Decision: relevant
- Rationale: Direct Brexit/Northern Ireland protocol result.
- Category/date: svet / 2021-07-21T18:44:51
- URL: https://www.rtvslo.si/svet/evropa/velika-britanija-hoce-preoblikovati-severnoirski-protokol/588379
- FAISS rank/score: 3 / 0.8314
- Reranker score: 1.3238
- Keywords: Brexit, Velika Britanija, Bruselj, Britanska vlada, Evropska unija, Severnoirski protokol, Irski otok, Brandon Lewis, Parlament, London, Blago, Združeno kraljestvo, Enotni trg, David Frost, Gospodarska škoda, Severna Irska, Protesti, Maroš Šefčovič, Evropska komisija, Izstopni sporazum, Odbor
- Excerpt: Velika Britanija hoče preoblikovati severnoirski protokol Ključne besede: Brexit, Velika Britanija, Bruselj, Britanska vlada, Evropska unija, Severnoirski protokol, Irski otok, Brandon Lewis, Parlament, London, Blago, Združeno kraljestvo, Enotni trg, David Frost, Gospodarska škoda, Severna Irska, Protesti, Maroš Šefčovič, Evropska komisija, Izstopni sporazum, Odbor Britanska vlada se želi z Evropsko unijo znova pogajati o severnoirskem protokolu in ga spremeniti. Pozvala je tudi k moratoriju za...


### 13. Vojna v Ukrajini in Zelenski

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Zelenski: V Rusijo prihaja vojna. Papež pozval k obnovitvi sporazuma o žitu.
- Decision: relevant
- Rationale: Direct Zelensky/Ukraine war result.
- Category/date: svet / 2023-07-30T09:43:53
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-v-rusijo-prihaja-vojna-papez-pozval-k-obnovitvi-sporazuma-o-zitu/676560
- FAISS rank/score: 40 / 0.8606
- Reranker score: 9.2562
- Keywords: vojna v Ukrajini, Vladimir Putin, pogajanja, Ukrajina, Rusija, napadi, vojna, letalniki, predsednik, obramba, teroristi, energetska infrastruktura, napad, uničenje, umrli, ranjeni, raketa, ruske sile, Sumi, Zaporožje, Ministrstvo, BBC
- Excerpt: Zelenski: V Rusijo prihaja vojna. Papež pozval k obnovitvi sporazuma o žitu. Ključne besede: vojna v Ukrajini, Vladimir Putin, pogajanja, Ukrajina, Rusija, napadi, vojna, letalniki, predsednik, obramba, teroristi, energetska infrastruktura, napad, uničenje, umrli, ranjeni, raketa, ruske sile, Sumi, Zaporožje, Ministrstvo, BBC V napadih po Ukrajini so bili ponoči ubiti najmanj trije ljudje, Rusija pa je nad Moskvo sestrelila ukrajinske letalnike. Ukrajinski predsednik Zelenski je dejal, da so nap...

#### Rank 2: RELEVANT

- Title: Zelenski: Moskva zavlačuje s srečanjem med predsednikoma Ukrajine in Rusije
- Decision: relevant
- Rationale: Direct Zelensky/Russia-Ukraine talks result.
- Category/date: svet / 2025-08-23T15:40:38
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-moskva-zavlacuje-s-srecanjem-med-predsednikoma-ukrajine-in-rusije/755482
- FAISS rank/score: 23 / 0.8638
- Reranker score: 8.7593
- Keywords: Ukrajina, Rusija, vojna
- Excerpt: Zelenski: Moskva zavlačuje s srečanjem med predsednikoma Ukrajine in Rusije Ključne besede: Ukrajina, Rusija, vojna Ukrajinski predsednik Volodimir Zelenski je prepričan, da bi morale države svetovnega juga spodbuditi Rusijo k sklenitvi miru v vojni v Ukrajini, vključno s pritiskom na Vladimirja Putina, da sede za pogajalsko mizo. "Potrdil sem svojo pripravljenost na kakršno koli obliko srečanja z ruskim voditeljem. Vendar vidimo, da Moskva znova poskuša vse skupaj še bolj zavleči," je Zelenski...

#### Rank 3: RELEVANT

- Title: Zelenski: Bližje smo miru in koncu vojne, kot si mislimo
- Decision: relevant
- Rationale: Direct Zelensky/war-peace result.
- Category/date: svet / 2024-09-24T08:53:42
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-blizje-smo-miru-in-koncu-vojne-kot-si-mislimo/721990
- FAISS rank/score: 9 / 0.8668
- Reranker score: 8.5168
- Keywords: Ukrajina, Rusija, vojna
- Excerpt: Zelenski: Bližje smo miru in koncu vojne, kot si mislimo Ključne besede: Ukrajina, Rusija, vojna "Mislim, da smo bližje miru, kot si mislimo. Blizu smo koncu vojne," je med obiskom v ZDA dejal ukrajinski predsednik Volodimir Zelenski, ki bo konec tedna Washingtonu predstavil svoj "načrt zmage". "Zdaj, ko se približuje konec leta, imamo resnično priložnost za okrepitev sodelovanja med Ukrajino in ZDA," je po srečanju z dvostrankarsko delegacijo ameriškega kongresa dejal Zelenski in izrazil prepri...

#### Rank 4: RELEVANT

- Title: Zelenski se je srečal z vojaki, ki se borijo v Kursku: Ukrajinci so lahko močnejši od sovražnika
- Decision: relevant
- Rationale: Direct Zelensky/Ukrainian soldiers result.
- Category/date: svet / 2024-10-04T09:53:55
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-se-je-srecal-z-vojaki-ki-se-borijo-v-kursku-ukrajinci-so-lahko-mocnejsi-od-sovraznika/723177
- FAISS rank/score: 38 / 0.8607
- Reranker score: 8.5141
- Keywords: Ukrajina, Rusija, vojna, Vugledar, Pokrovsk
- Excerpt: Zelenski se je srečal z vojaki, ki se borijo v Kursku: Ukrajinci so lahko močnejši od sovražnika Ključne besede: Ukrajina, Rusija, vojna, Vugledar, Pokrovsk Ukrajinski predsednik Volodimir Zelenski je sporočil, da je obiskal Sumsko oblast ob meji z Rusijo in se srečal z vojaki, ki sodelujejo v ofenzivi v ruski obmejni Kurski oblasti. Zelenski se je srečal z vojaki iz 82. zračno-jurišne brigade, ki se bori v Rusiji, in se seznanil s poročilom njenega poveljnika Dmitra Vološina, ki je govoril o op...

#### Rank 5: RELEVANT

- Title: Zelenski obiskal Pokrovsk in se zahvalil vsem za podporo Ukrajini
- Decision: relevant
- Rationale: Direct Zelensky/Ukraine support result.
- Category/date: svet / 2025-03-22T09:12:17
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-obiskal-pokrovsk-in-se-zahvalil-vsem-za-podporo-ukrajini/740260
- FAISS rank/score: 45 / 0.8599
- Reranker score: 8.4958
- Keywords: Ukrajina, Rusija, vojna
- Excerpt: Zelenski obiskal Pokrovsk in se zahvalil vsem za podporo Ukrajini Ključne besede: Ukrajina, Rusija, vojna Ukrajinski predsednik Volodimir Zelenski je obiskal Doneško oblast na vzhodu države, kjer se je poklonil padlim ukrajinskim vojakom in se zahvalil za podporo vsem, ki Kijev podpirajo v vojni proti Rusiji. "Zahvaljujem se vsem našim branilcem. Čast vsem padlim junakom," je Zelenski zapisal na omrežju X poleg posnetkov srečanja z vojaki in obiska začasnih spomenikov na upravni meji oblasti. "Z...


### 14. Kitajska proti ZDA

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Kitajska po napovedi novih ameriških carin zagrozila s protiukrepi
- Decision: relevant
- Rationale: Direct China response to US tariffs.
- Category/date: gospodarstvo / 2025-10-12T13:10:13
- URL: https://www.rtvslo.si/gospodarstvo/kitajska-po-napovedi-novih-ameriskih-carin-zagrozila-s-protiukrepi/760526
- FAISS rank/score: 3 / 0.8605
- Reranker score: 5.8505
- Keywords: ZDA, Kitajska, carine
- Excerpt: Kitajska po napovedi novih ameriških carin zagrozila s protiukrepi Ključne besede: ZDA, Kitajska, carine Potem ko je predsednik ZDA Donald Trump z novembrom napovedal nove carine na uvoz iz Kitajske, je ta zagrozila s protiukrepi. V Pekingu ob tem Washingtonu očitajo dvojna merila in mu očitajo zlorabe načela nacionalne varnosti. S kitajskega ministrstva za trgovino so sporočili, da ameriška administracija že dolgo pretirava z uporabo načela nacionalne varnosti in ga zlorablja za nadzor nad izvo...

#### Rank 2: RELEVANT

- Title: Kitajska na področju umetne inteligence prehiteva ZDA
- Decision: relevant
- Rationale: China vs US in AI.
- Category/date: znanost-in-tehnologija / 2019-03-19T08:39:25
- URL: https://www.rtvslo.si/znanost-in-tehnologija/kitajska-na-podrocju-umetne-inteligence-prehiteva-zda/483019
- FAISS rank/score: 18 / 0.8516
- Reranker score: 3.1589
- Keywords: AI, UI, Umetna inteligenca, Kitajska, Allen Institute for Artificial Intelligence, ZDA, raziskava, inštitut, tehnologija, avtonomna vozila, navidezna resničnost, 5G, naložbe, Peking, priseljevanje, strategija, Donald Trump, administracija, inovacije, nacionalna strategija, analitiki, Washington, raziskovalec
- Excerpt: Kitajska na področju umetne inteligence prehiteva ZDA Ključne besede: AI, UI, Umetna inteligenca, Kitajska, Allen Institute for Artificial Intelligence, ZDA, raziskava, inštitut, tehnologija, avtonomna vozila, navidezna resničnost, 5G, naložbe, Peking, priseljevanje, strategija, Donald Trump, administracija, inovacije, nacionalna strategija, analitiki, Washington, raziskovalec Kitajska je na dobri poti, da na področju umetne inteligence prehiti ZDA, kaže analiza, ki jo je v sredo objavil amerišk...

#### Rank 3: RELEVANT

- Title: Kitajski obrambni minister: Spopad Kitajske in ZDA bi bil neznosna katastrofa za svet
- Decision: relevant
- Rationale: Direct China-US conflict result.
- Category/date: svet / 2023-06-04T09:05:31
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/kitajski-obrambni-minister-spopad-kitajske-in-zda-bi-bil-neznosna-katastrofa-za-svet/670585
- FAISS rank/score: 13 / 0.8523
- Reranker score: 2.9728
- Keywords: Kitajska, ZDA, Li Šangfu, konflikt, dialog, sodelovanje, varnost, vojska, politika, mednarodni odnosi, Sovjetska zveza, sankcije, orožje, Tajvan, Singapur, Azija, vrh, geopolitika, hladna vojna, hegemonija, diplomatski odnosi
- Excerpt: Kitajski obrambni minister: Spopad Kitajske in ZDA bi bil neznosna katastrofa za svet Ključne besede: Kitajska, ZDA, Li Šangfu, konflikt, dialog, sodelovanje, varnost, vojska, politika, mednarodni odnosi, Sovjetska zveza, sankcije, orožje, Tajvan, Singapur, Azija, vrh, geopolitika, hladna vojna, hegemonija, diplomatski odnosi Kitajski obrambni minister Li Šangfu je v nedeljo dejal, da bi bil spopad z ZDA "neznosna katastrofa" za svet, in da si njegova država želi dialog namesto spopada. Li, ki j...

#### Rank 4: RELEVANT

- Title: ZDA in Kitajska naj bi dosegle okvirni dogovor, ki bi preložil uvedbo ameriških carin
- Decision: relevant
- Rationale: Direct US-China tariff talks result.
- Category/date: svet / 2025-10-26T14:29:41
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/zda-in-kitajska-naj-bi-dosegle-okvirni-dogovor-ki-bi-prelozil-uvedbo-ameriskih-carin/762061
- FAISS rank/score: 9 / 0.8528
- Reranker score: 2.9495
- Keywords: Malezija, Donald Trump, Ši Džinping, Kitajska, Carine, Asean
- Excerpt: ZDA in Kitajska naj bi dosegle okvirni dogovor, ki bi preložil uvedbo ameriških carin Ključne besede: Malezija, Donald Trump, Ši Džinping, Kitajska, Carine, Asean Ameriški uradniki so sporočili, da so s Kitajsko dosegli okvirni trgovinski dogovor, o katerem bosta prihodnji teden odločala predsednika Donald Trump in Ši Džinping. Dogovor bi pomenil preložitev uvedbe dodatnih ameriških carin na kitajsko blago. Ameriški finančni minister Scott Bessent je dejal, da so pogovori ob robu vrha Združenja...

#### Rank 5: RELEVANT

- Title: Trump pohvalil odnos med ZDA in Kitajsko po dogovoru o znižanju carin za 90 dni
- Decision: relevant
- Rationale: Direct US-China relations result.
- Category/date: gospodarstvo / 2025-05-12T09:56:38
- URL: https://www.rtvslo.si/gospodarstvo/trump-pohvalil-odnos-med-zda-in-kitajsko-po-dogovoru-o-znizanju-carin-za-90-dni/745396
- FAISS rank/score: 39 / 0.8467
- Reranker score: 2.8012
- Keywords: Kitajska, ZDA, Carine
- Excerpt: Trump pohvalil odnos med ZDA in Kitajsko po dogovoru o znižanju carin za 90 dni Ključne besede: Kitajska, ZDA, Carine Kitajska in ZDA so po pogovorih v Ženevi dosegli dogovor v trgovinski vojni, s čimer bo za obdobje 90 dni odpravljena večina carin in protiukrepov. Tako bosta obe državi vzajemne carine znižali za 115 odstotnih točk. V skladu z dogovorom med največjima svetovnima gospodarstvoma se bodo ameriške carine na uvoz iz Kitajske znižale s 145 na 30 odstotkov, kitajske carine na uvoz iz Z...


### 15. Korupcija v slovenski politiki

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Koalicija in opozicija sta se obmetavali z obtožbami korupcije
- Decision: relevant
- Rationale: Direct Slovenian political corruption accusations.
- Category/date: slovenija / 2024-02-20T20:53:47
- URL: https://www.rtvslo.si/slovenija/koalicija-in-opozicija-sta-se-obmetavali-z-obtozbami-korupcije/698992
- FAISS rank/score: 5 / 0.8487
- Reranker score: 2.9226
- Keywords: Politika, Slovenska politika, korupcija, pravosodje, DZ, Odbor za pravosodje, Litijska, afere, opozicija, koalicija, nakup, stavba, Litijska cesta, živahna razprava, SDS, priporočila, seja, poslanec, očitki, milijonski nakup, lastništvo, integriteta, javne funkcije, obljube.
- Excerpt: Koalicija in opozicija sta se obmetavali z obtožbami korupcije Ključne besede: Politika, Slovenska politika, korupcija, pravosodje, DZ, Odbor za pravosodje, Litijska, afere, opozicija, koalicija, nakup, stavba, Litijska cesta, živahna razprava, SDS, priporočila, seja, poslanec, očitki, milijonski nakup, lastništvo, integriteta, javne funkcije, obljube. Na razpravi o stanju na področju korupcije je opozicija poudarila zlasti afere spornega nakupa stavbe na Litijski cesti, koalicija pa je izpostav...

#### Rank 2: RELEVANT

- Title: OECD v Sloveniji preveril boj proti podkupovanju javnih uslužbencev
- Decision: relevant
- Rationale: Corruption/bribery in Slovenia.
- Category/date: gospodarstvo / 2025-02-18T18:43:18
- URL: https://www.rtvslo.si/gospodarstvo/oecd-v-sloveniji-preveril-boj-proti-podkupovanju-javnih-usluzbencev/736993
- FAISS rank/score: 2 / 0.8536
- Reranker score: 2.8897
- Keywords: Korupcija, Priporočila, Slovenija, Podkupovanje, OECD
- Excerpt: OECD v Sloveniji preveril boj proti podkupovanju javnih uslužbencev Ključne besede: Korupcija, Priporočila, Slovenija, Podkupovanje, OECD Delegacija Organizacije za gospodarsko sodelovanje in razvoj (OECD) je te dni v Sloveniji preučevala implementacijo priporočil, vezanih na izvajanje Konvencije OECD-ja o boju proti podkupovanju tujih javnih uslužbencev v mednarodnem poslovanju. Delovna skupina OECD-ja za boj proti podkupovanju tujih javnih uslužbencev v mednarodnem poslovanju spremlja izvajanj...

#### Rank 3: RELEVANT

- Title: KPK: V Sloveniji manjka ustrezno prevzemanje odgovornosti najvišjih predstavnikov oblasti
- Decision: relevant
- Rationale: Slovenian public-official accountability/corruption context.
- Category/date: slovenija / 2026-02-10T10:23:44
- URL: https://www.rtvslo.si/slovenija/kpk-v-sloveniji-manjka-ustrezno-prevzemanje-odgovornosti-najvisjih-predstavnikov-oblasti/772947
- FAISS rank/score: 25 / 0.8423
- Reranker score: 2.7702
- Keywords: korupcija, CPI, Slovenija
- Excerpt: KPK: V Sloveniji manjka ustrezno prevzemanje odgovornosti najvišjih predstavnikov oblasti Ključne besede: korupcija, CPI, Slovenija Slovenija je v Indeksu zaznave korupcije za leto 2025 dosegla 58 od 100 točk in se uvrstila na 41. mesto med 182 državami. Slovenija je v primerjavi z lani padla za pet mest. Premier Golob: "Morda smo bili uspavani z odličnimi rezultati v letu 2024" Po lanskem skoku navzgor, ko je Slovenija na lestvici zaznave korupcije za leto 2024 dosegla 60 točk, je letos indeks...

#### Rank 4: RELEVANT

- Title: Maruša Babnik: V Sloveniji smo preveč tolerantni do korupcije
- Decision: relevant
- Rationale: Direct corruption in Slovenia result.
- Category/date: slovenija / 2023-12-05T10:35:38
- URL: https://www.rtvslo.si/slovenija/ob-osmih/marusa-babnik-v-sloveniji-smo-prevec-tolerantni-do-korupcije/690549
- FAISS rank/score: 23 / 0.8431
- Reranker score: 2.1451
- Keywords: Korupcija, integriteta, KPK, Transparency International, Transparency International Slovenija, indeks zaznane korupcije, ničelna toleranca, finančne posledice, zaupanje v demokracijo, pravna država, ozaveščanje, preprečevanje korupcije, družba, institucije, primeri, Robert Golob, Komisija za preprečevanje korupcije, zgled.
- Excerpt: Maruša Babnik: V Sloveniji smo preveč tolerantni do korupcije Ključne besede: Korupcija, integriteta, KPK, Transparency International, Transparency International Slovenija, indeks zaznane korupcije, ničelna toleranca, finančne posledice, zaupanje v demokracijo, pravna država, ozaveščanje, preprečevanje korupcije, družba, institucije, primeri, Robert Golob, Komisija za preprečevanje korupcije, zgled. Za korupcijo je včasih veljalo samo podkupovanje, danes pa je to tudi kršitev integritete. A vsa...

#### Rank 5: RELEVANT

- Title: Seja komisije za nadzor javnih financ o korupciji prekinjena, padale tudi težke besede
- Decision: relevant
- Rationale: Direct corruption/public finance result.
- Category/date: slovenija / 2026-02-17T10:29:32
- URL: https://www.rtvslo.si/slovenija/seja-komisije-za-nadzor-javnih-financ-o-korupciji-prekinjena-padale-tudi-tezke-besede/773708
- FAISS rank/score: 13 / 0.8456
- Reranker score: 1.8615
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
- Reranker score: 6.0014
- Keywords: ISS, Mednarodna vesoljska postaja, Alexander Gerst, Poleti s posadko, Progress, Sojuz, raketa, vesolje, izstrelitev, vesoljsko plovilo, zaloge, Evropska vesoljska agencija, Esa, astronavt, poveljnik, kozmodrom, orbite, gorivo, kisik, preizkus, nesreča, senzor, Rusija, posadke, kupola, fotoaparat, fotografiranje.
- Excerpt: Video: Tako je iz vesolja videti izstrelitev rakete Ključne besede: ISS, Mednarodna vesoljska postaja, Alexander Gerst, Poleti s posadko, Progress, Sojuz, raketa, vesolje, izstrelitev, vesoljsko plovilo, zaloge, Evropska vesoljska agencija, Esa, astronavt, poveljnik, kozmodrom, orbite, gorivo, kisik, preizkus, nesreča, senzor, Rusija, posadke, kupola, fotoaparat, fotografiranje. Astronavt Alexander Gerst je posnel izstrelitev rakete z drugačne perspektive, kot smo je vajeni. Ujel je plovilo MS-1...

#### Rank 2: RELEVANT

- Title: Nasa uspešno izstrelila SpaceX-ovo raketo. Četverica bo v vesolju šest mesecev.
- Decision: relevant
- Rationale: Direct rocket launch to space.
- Category/date: znanost-in-tehnologija / 2023-03-02T12:24:00
- URL: https://www.rtvslo.si/znanost-in-tehnologija/nasa-uspesno-izstrelila-spacex-ovo-raketo-cetverica-bo-v-vesolju-sest-mesecev/659714
- FAISS rank/score: 3 / 0.8706
- Reranker score: 5.7290
- Keywords: SpaceX, Dragon Crew-6, misija, Nasa, Elon Musk, mednarodna vesoljska postaja, posadka, izstrelitev, težave, vesolje, astronavt, orbita, Združeni arabski emirati, ISS, predaja, Zemlja, kapsula, Rusija, Sojuz, puščanje, Kazahstan
- Excerpt: Nasa uspešno izstrelila SpaceX-ovo raketo. Četverica bo v vesolju šest mesecev. Ključne besede: SpaceX, Dragon Crew-6, misija, Nasa, Elon Musk, mednarodna vesoljska postaja, posadka, izstrelitev, težave, vesolje, astronavt, orbita, Združeni arabski emirati, ISS, predaja, Zemlja, kapsula, Rusija, Sojuz, puščanje, Kazahstan Iz Nasinega vesoljskega centra Kennedy na Floridi so uspešno izstrelili raketo ameriškega podjetja SpaceX, ki je v lasti milijarderja Elona Muska. V okviru misije Dragon Crew-6...

#### Rank 3: RELEVANT

- Title: Kitajska prvič izstrelila raketo v vesolje z morja
- Decision: relevant
- Rationale: Direct rocket launch to space.
- Category/date: znanost-in-tehnologija / 2019-06-05T14:56:54
- URL: https://www.rtvslo.si/znanost-in-tehnologija/kitajska-prvic-izstrelila-raketo-v-vesolje-z-morja/490292
- FAISS rank/score: 20 / 0.8593
- Reranker score: 5.6855
- Keywords: Kitajska, Kitajska vesolje, Kitajski vesoljski program, Izstrelitve, Izstrelitve 2019, Dolgi pohod 11, Dolgi pohod, raketa, vesolje, Nacionalna vesoljska administracija, izstrelitev, morje, satelit, znanstveni poskusi, komercialni, ladja, Rumeni morje, ekvator, hitrost, gorivo, konkurenčno, nosilna raketa, v orbito, novi generaciji, robotska sonda, vesoljska postaja
- Excerpt: Kitajska prvič izstrelila raketo v vesolje z morja Ključne besede: Kitajska, Kitajska vesolje, Kitajski vesoljski program, Izstrelitve, Izstrelitve 2019, Dolgi pohod 11, Dolgi pohod, raketa, vesolje, Nacionalna vesoljska administracija, izstrelitev, morje, satelit, znanstveni poskusi, komercialni, ladja, Rumeni morje, ekvator, hitrost, gorivo, konkurenčno, nosilna raketa, v orbito, novi generaciji, robotska sonda, vesoljska postaja Kitajska je prvič izstrelila raketo v vesolje z morja, je sporoč...

#### Rank 4: RELEVANT

- Title: Raketo s prvima slovenskima satelitoma le izstrelili: "V vesolju smo!"
- Decision: relevant
- Rationale: Direct rocket/satellites launch.
- Category/date: znanost-in-tehnologija / 2020-09-03T06:47:51
- URL: https://www.rtvslo.si/znanost-in-tehnologija/raketo-s-prvima-slovenskima-satelitoma-le-izstrelili-v-vesolju-smo/535004
- FAISS rank/score: 1 / 0.8743
- Reranker score: 5.5919
- Keywords: satelit, izstrelitev, Vega, Nemo HD in Trisat, Francoska Gvajana, raketa, Nemo HD, Trisat, evropska znanost, Arianespace, vesoljski center, Kourou, vodja projekta, Centrer odličnosti Vesolje-SI, znanost, slovensko gospodarstvo, orbita, vesolje, mikrosatelit, nanosatelit, testiranje
- Excerpt: Raketo s prvima slovenskima satelitoma le izstrelili: "V vesolju smo!" Ključne besede: satelit, izstrelitev, Vega, Nemo HD in Trisat, Francoska Gvajana, raketa, Nemo HD, Trisat, evropska znanost, Arianespace, vesoljski center, Kourou, vodja projekta, Centrer odličnosti Vesolje-SI, znanost, slovensko gospodarstvo, orbita, vesolje, mikrosatelit, nanosatelit, testiranje Iz Francoske Gvajane so ponoči vendarle izstrelili raketo Vega, s katero sta v vesolje poletela tudi prva slovenska satelita Nemo...

#### Rank 5: RELEVANT

- Title: SpaceX uspešno izstrelil ogromno raketo Starship, a tokrat brez ulova z mehanskimi rokami
- Decision: relevant
- Rationale: Direct Starship rocket launch.
- Category/date: znanost-in-tehnologija / 2024-11-19T23:03:23
- URL: https://www.rtvslo.si/znanost-in-tehnologija/spacex-uspesno-izstrelil-ogromno-raketo-starship-a-tokrat-brez-ulova-z-mehanskimi-rokami/728015
- FAISS rank/score: 45 / 0.8549
- Reranker score: 4.9065
- Keywords: SpaceX, Starship, Elon Musk, Donald Trump
- Excerpt: SpaceX uspešno izstrelil ogromno raketo Starship, a tokrat brez ulova z mehanskimi rokami Ključne besede: SpaceX, Starship, Elon Musk, Donald Trump Podjetje SpaceX Elona Muska je v torek iz Teksasa v vesolje izstrelilo svojo šesto testno raketo Starship. Ob ustanovitelju družbe Elonu Musku je bil prisoten tudi novoizvoljeni predsednik ZDA Donald Trump. Raketni sistem, namenjen pristanku astronavtov na Luni in prevozu posadk na Mars, je vzletel ob 23. uri po našem času (oz. ob 16. uri po krajevne...


### 17. Delnice Tesle padajo

Precision@5: 4/5 = 0.80

#### Rank 1: NOT RELEVANT

- Title: Vrnitev Tesle in vzpon indeksa S & P nad 5500 točk
- Decision: not_relevant
- Rationale: Tesla shares rising/recovering, opposite direction.
- Category/date: gospodarstvo / 2024-07-03T06:32:32
- URL: https://www.rtvslo.si/gospodarstvo/borzni-komentar/vrnitev-tesle-in-vzpon-indeksa-s-p-nad-5500-tock/713666
- FAISS rank/score: 14 / 0.8333
- Reranker score: 2.8397
- Keywords: MMC-jev borzni komentar, S & P 500, rekord, Tesline delnice
- Excerpt: Vrnitev Tesle in vzpon indeksa S & P nad 5500 točk Ključne besede: MMC-jev borzni komentar, S & P 500, rekord, Tesline delnice Wall Street je v drugo polletje vstopil optimistično, zadnje izjave Jeroma Powlla pa vlivajo upanje, da Fed dobiva boj z inflacijo. Indeksa S & P 500 in NASDAQ sta na novem rekordu, med posameznimi papirji pa je včeraj blestela Tesla. Tesline delnice so krenile za deset odstotkov navzgor (tudi nad 230 dolarjev), potem ko je proizvajalec električnih vozil sporočil, da je...

#### Rank 2: RELEVANT

- Title: Tesla izgublja primat na trgu e-vozil; prodajni pritisk pri bitcoinu popušča
- Decision: relevant
- Rationale: Tesla market/sales pressure context.
- Category/date: gospodarstvo / 2024-01-28T06:24:02
- URL: https://www.rtvslo.si/gospodarstvo/borzni-komentar/tesla-izgublja-primat-na-trgu-e-vozil-prodajni-pritisk-pri-bitcoinu-popusca/696349
- FAISS rank/score: 8 / 0.8369
- Reranker score: 2.5613
- Keywords: MMC-jev borzni komentar, Intel, Tesla, četrtletni poslovni rezultati, BYD, PCE-inflacija, ameriški BDP, bitcoin, ETF-sklad, Bitcoin Trust, delnice, New York, indeksi, dobiček, čipov, umetna inteligenca, Nvidija, podatkovni centri, Mobileye, samovozeča vozila, konkurenca, Kitajska, električna vozila, prodaja, rezultati, trgovanje, finance
- Excerpt: Tesla izgublja primat na trgu e-vozil; prodajni pritisk pri bitcoinu popušča Ključne besede: MMC-jev borzni komentar, Intel, Tesla, četrtletni poslovni rezultati, BYD, PCE-inflacija, ameriški BDP, bitcoin, ETF-sklad, Bitcoin Trust, delnice, New York, indeksi, dobiček, čipov, umetna inteligenca, Nvidija, podatkovni centri, Mobileye, samovozeča vozila, konkurenca, Kitajska, električna vozila, prodaja, rezultati, trgovanje, finance Čeprav sta Intel in Tesla s črnogledimi napovedmi malce pokvarila r...

#### Rank 3: RELEVANT

- Title: Tesla v prvem četrtletju s 13-odstotnim padcem prodaje avtomobilov
- Decision: relevant
- Rationale: Tesla sales falling result.
- Category/date: gospodarstvo / 2025-04-02T17:43:00
- URL: https://www.rtvslo.si/gospodarstvo/preberite-tudi/tesla-v-prvem-cetrtletju-s-13-odstotnim-padcem-prodaje-avtomobilov/741463
- FAISS rank/score: 12 / 0.8338
- Reranker score: 2.4292
- Keywords: Padec delnic, Bojkot, Elon Musk, Prodaja avtomobilov, Tesla
- Excerpt: Tesla v prvem četrtletju s 13-odstotnim padcem prodaje avtomobilov Ključne besede: Padec delnic, Bojkot, Elon Musk, Prodaja avtomobilov, Tesla Ameriški proizvajalec električnih avtomobilov Tesla je v prvem letošnjem četrtletju dobavil 336.681 avtomobilov, kar je 13 odstotkov manj kot leto prej, poroča francoska tiskovna agencija AFP. Manjša prodaja je posledica manjše proizvodnje zaradi posodabljanja tovarn in bojkota podjetja zaradi političnega delovanja direktorja Elona Muska. Število dobavlje...

#### Rank 4: RELEVANT

- Title: Musk po velikem padcu vrednosti Tesle obljublja, da bo podjetje najvrednejše na svetu
- Decision: relevant
- Rationale: Direct Tesla value drop result.
- Category/date: gospodarstvo / 2022-12-29T16:28:18
- URL: https://www.rtvslo.si/gospodarstvo/musk-po-velikem-padcu-vrednosti-tesle-obljublja-da-bo-podjetje-najvrednejse-na-svetu/652623
- FAISS rank/score: 10 / 0.8354
- Reranker score: 2.1845
- Keywords: Tesla, Elon Musk, Avtomobili, delnice, borzni trg, zaposleni, elektronsko pismo, dobave, popusti, analitiki, četrtletje, vrednost, povpraševanje, električni avtomobili, tehnološko podjetje, Twitter, proizvodnja, napoved, družbeno omrežje, direktor
- Excerpt: Musk po velikem padcu vrednosti Tesle obljublja, da bo podjetje najvrednejše na svetu Ključne besede: Tesla, Elon Musk, Avtomobili, delnice, borzni trg, zaposleni, elektronsko pismo, dobave, popusti, analitiki, četrtletje, vrednost, povpraševanje, električni avtomobili, tehnološko podjetje, Twitter, proizvodnja, napoved, družbeno omrežje, direktor Potem ko so delnice avtomobilskega podjetja Tesla letos izgubile 70 odstotkov, je lastnik Elon Musk zatrdil, da bo podjetje na dolgi rok najvrednejše...

#### Rank 5: RELEVANT

- Title: Tehnološke delnice vidno sestopile z vrhov, še bolj pa Teslin dobiček
- Decision: relevant
- Rationale: Tech stocks/Tesla profit falling result.
- Category/date: gospodarstvo / 2024-07-28T06:17:32
- URL: https://www.rtvslo.si/gospodarstvo/borzni-komentar/tehnoloske-delnice-vidno-sestopile-z-vrhov-se-bolj-pa-teslin-dobicek/716161
- FAISS rank/score: 9 / 0.8360
- Reranker score: 2.1118
- Keywords: MMC-jev borzni komentar, četrtletni poslovni rezultati, Tesla, Alphabet, Ford, Ryanair, Krka, dividenda
- Excerpt: Tehnološke delnice vidno sestopile z vrhov, še bolj pa Teslin dobiček Ključne besede: MMC-jev borzni komentar, četrtletni poslovni rezultati, Tesla, Alphabet, Ford, Ryanair, Krka, dividenda Po treh dneh resnih razprodaj so tehnološke delnice v New Yorku v petek le okrevale, delno tudi zaradi novih znakov, da se inflacija umirja in bi moral Fed s septembrom končno začeti zniževati obrestne mere, ki so že več kot leto dni na 23-letnem vrhu. Potem ko smo še v prvi polovici julija spremljali nove re...


### 18. Nova verzija umetne inteligence

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: Razvili umetno inteligenco, ki bo nadgradila izkušnjo športnih ljubiteljev
- Decision: relevant
- Rationale: New/developed AI system result.
- Category/date: zabava-in-slog / 2024-06-24T13:28:46
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/razvili-umetno-inteligenco-ki-bo-nadgradila-izkusnjo-sportnih-ljubiteljev/712824
- FAISS rank/score: 6 / 0.8234
- Reranker score: 3.8843
- Keywords: Generativna funkcija, Wimbledon, IBM, Športni podatki, Umetna inteligenca, skit scena
- Excerpt: Razvili umetno inteligenco, ki bo nadgradila izkušnjo športnih ljubiteljev Ključne besede: Generativna funkcija, Wimbledon, IBM, Športni podatki, Umetna inteligenca, skit scena Umetna inteligenca je dodobra vpeta v naš način življenja in je prisotna kot še nikoli doslej. Zdaj bo tehnologija vpeljana še v svet športa, natančneje tenisa, ki bo tako za tekmovalce kot navijače dodala novo dimenzijo. "Vi vidite tenis, mi vidimo podatke. Vi vidite golf, mi vidimo podatke," je za Euronews povedal Jonat...

#### Rank 2: RELEVANT

- Title: Google predstavil nov program umetne inteligence Bard
- Decision: relevant
- Rationale: New AI program result.
- Category/date: znanost-in-tehnologija / 2023-02-07T11:00:00
- URL: https://www.rtvslo.si/znanost-in-tehnologija/google-predstavil-nov-program-umetne-inteligence-bard/657070
- FAISS rank/score: 3 / 0.8275
- Reranker score: 3.5533
- Keywords: Google, Bard, Umetna inteligenca, jezikovni model, intervju, Sundar Pichai, LaMDA, ChatGPT, OpenAI, Microsoft, investicija, partnerstvo, tehnološko podjetje, aplikacije za dialog, razvoj, napredki, zunanji vplivi, primerjava, inovacija, iskalnik
- Excerpt: Google predstavil nov program umetne inteligence Bard Ključne besede: Google, Bard, Umetna inteligenca, jezikovni model, intervju, Sundar Pichai, LaMDA, ChatGPT, OpenAI, Microsoft, investicija, partnerstvo, tehnološko podjetje, aplikacije za dialog, razvoj, napredki, zunanji vplivi, primerjava, inovacija, iskalnik Ameriški tehnološki velikan Google je uradno predstavil nov program umetne inteligence Bard. Kot poudarjajo v podjetju, gre za pomemben naslednji korak na področju umetne inteligence z...

#### Rank 3: RELEVANT

- Title: Apple bo svoje naprave nadgradil s ChatGPT-jem in glasovni pomočnici Siri dal nove funkcije
- Decision: relevant
- Rationale: New AI features/upgrade result.
- Category/date: znanost-in-tehnologija / 2024-06-11T09:23:51
- URL: https://www.rtvslo.si/znanost-in-tehnologija/apple-bo-svoje-naprave-nadgradil-s-chatgpt-jem-in-glasovni-pomocnici-siri-dal-nove-funkcije/711352
- FAISS rank/score: 2 / 0.8309
- Reranker score: 2.5077
- Keywords: Apple, OpenAI, ChatGPT, Tim Cook
- Excerpt: Apple bo svoje naprave nadgradil s ChatGPT-jem in glasovni pomočnici Siri dal nove funkcije Ključne besede: Apple, OpenAI, ChatGPT, Tim Cook Ameriško tehnološko podjetje Apple je predstavilo nove funkcije umetne inteligence za svoje naprave Apple Intelligence in partnerstvo s podjetjem OpenAI, ki bo še letos vključilo storitev ChatGPT v Applove naprave. Glavni izvršni direktor Appla Tim Cook je na sedežu tehnološkega velikana v kalifornijskem mestu Cupertino v Silicijevi dolini odprl letno konfe...

#### Rank 4: RELEVANT

- Title: OpenAI predstavil najnovejši model umetne inteligence GPT-5 − pametnejši, hitrejši, uporabnejši
- Decision: relevant
- Rationale: Direct latest AI model result.
- Category/date: znanost-in-tehnologija / 2025-08-08T08:30:59
- URL: https://www.rtvslo.si/znanost-in-tehnologija/openai-predstavil-najnovejsi-model-umetne-inteligence-gpt-5-pametnejsi-hitrejsi-uporabnejsi/754133
- FAISS rank/score: 1 / 0.8351
- Reranker score: 2.3217
- Keywords: GPT-5, OpenAI, UI
- Excerpt: OpenAI predstavil najnovejši model umetne inteligence GPT-5 − pametnejši, hitrejši, uporabnejši Ključne besede: GPT-5, OpenAI, UI Podjetje OpenAI je predstavilo najnovejši in najnaprednejši model umetne inteligence velikega obsega GPT-5. GPT-5, ki je pametnejši, hitrejši in uporabnejši pri pisanju, programiranju in na drugih področjih, bo vsem na voljo brezplačno. OpenAI trdi, da je stopnja halucinacij GPT-5 nižja, kar pomeni, da si model manj pogosto izmišlja odgovore. V podjetju so pojasnili,...

#### Rank 5: NOT RELEVANT

- Title: Nov slovenski superračunalnik bo omogočil tovarno umetne inteligence
- Decision: not_relevant
- Rationale: AI infrastructure/supercomputer, not a new AI version/model.
- Category/date: slovenija / 2025-03-21T10:39:56
- URL: https://www.rtvslo.si/slovenija/ob-osmih/nov-slovenski-superracunalnik-bo-omogocil-tovarno-umetne-inteligence/740150
- FAISS rank/score: 34 / 0.8147
- Reranker score: 1.3183
- Keywords: umetna inteligenca, superračunalnik, Žiga Zebec, Maribor, Vega
- Excerpt: Nov slovenski superračunalnik bo omogočil tovarno umetne inteligence Ključne besede: umetna inteligenca, superračunalnik, Žiga Zebec, Maribor, Vega Z novim superračunalnikom Vega 2 bo Slovenija postala eno od ključnih središč umetne inteligence v Evropi, je v oddaji Ob osmih povedal raziskovalec na Inštitutu za informacijske znanosti Žiga Zebec. V Mariboru naj bi še letos začeli graditi visoko zmogljiv superračunalnik s tovarno umetne inteligence, enega od šestih takih v Evropi. S tem skuša Evro...


### 19. Najbolj prodajan avtomobil

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Tesla z dvema modeloma na lestvici najbolj prodajanih vozil na svetu
- Decision: relevant
- Rationale: Best-selling vehicles result.
- Category/date: zabava-in-slog / 2023-05-10T08:01:00
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/tesla-z-dvema-modeloma-na-lestvici-najbolj-prodajanih-vozil-na-svetu/667586
- FAISS rank/score: 25 / 0.8342
- Reranker score: 6.0795
- Keywords: Prodaja vozil, JATO Dynamics, Toyota RAV 4, Toyota, vozilo, prodaja, svet, avtomobili, modeli, Tesla, registracija, trg, razvoj, Severna Amerika, Evropa, Kitajska, padec, dobavna veriga, polprevodniki, motnje, Ukrajina, sankcije, Rusija, Volkswagen, Hyundai-Kia, Stellantis, General Motors, BYD, tržni delež, testiranje, Avtomobilnost.
- Excerpt: Tesla z dvema modeloma na lestvici najbolj prodajanih vozil na svetu Ključne besede: Prodaja vozil, JATO Dynamics, Toyota RAV 4, Toyota, vozilo, prodaja, svet, avtomobili, modeli, Tesla, registracija, trg, razvoj, Severna Amerika, Evropa, Kitajska, padec, dobavna veriga, polprevodniki, motnje, Ukrajina, sankcije, Rusija, Volkswagen, Hyundai-Kia, Stellantis, General Motors, BYD, tržni delež, testiranje, Avtomobilnost. Toyota je leta 2022 prodala največ vozil na svetu. Med desetimi najbolje prodaj...

#### Rank 2: RELEVANT

- Title: Dacia sandero premagala teslo Y
- Decision: relevant
- Rationale: Direct sales ranking result.
- Category/date: zabava-in-slog / 2024-03-23T07:37:23
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/dacia-sandero-premagala-teslo-y/702542
- FAISS rank/score: 9 / 0.8485
- Reranker score: 5.7634
- Keywords: Dacia sandero, Tesla model y, Volkswagen golf, Evropa, prodaja avtomobilov, Dataforce, sindikati, prodaja vozil, Teslina tovarna, Grünheide, Berlin, avtomobilska industrija, Peugeot 208, Citroen C3, kombilimuzina, električni avtomobili, avtomobilske tovarne, aktivisti, prodajne uspešnice, prodajne enote
- Excerpt: Dacia sandero premagala teslo Y Ključne besede: Dacia sandero, Tesla model y, Volkswagen golf, Evropa, prodaja avtomobilov, Dataforce, sindikati, prodaja vozil, Teslina tovarna, Grünheide, Berlin, avtomobilska industrija, Peugeot 208, Citroen C3, kombilimuzina, električni avtomobili, avtomobilske tovarne, aktivisti, prodajne uspešnice, prodajne enote Dacia Sandero je ponovno najbolje prodajani avto v Evropi. Premagala je teslo model Y, največjo uspešnico leta 2023. Dacia sandero je na dobri poti...

#### Rank 3: RELEVANT

- Title: Čeprav je prodaja vozil okrevala, je bilo leto 2023 eno najslabših v zadnjih 25 letih
- Decision: relevant
- Rationale: Vehicle sales ranking context.
- Category/date: zabava-in-slog / 2024-02-26T18:55:43
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/ceprav-je-prodaja-vozil-okrevala-je-bilo-leto-2023-eno-najslabsih-v-zadnjih-25-letih/699614
- FAISS rank/score: 16 / 0.8410
- Reranker score: 5.3133
- Keywords: Rabljeni avtomobili, Električna vozila, Volkswagen, AMZS, Prodaja vozil, avtomobili, prodaja električnih avtomobilov pa je v lanskem letu v primerjavi z letom 2022 narasla za 140 odstotkov. Na področju električnih vozil je najbolj prodajan model ostal Tesla Model 3, sledijo mu modeli Renault Zoe in Volkswagen ID.4. Kljub veliki rasti pa električni avtomobili še vedno predstavljajo manjši delež celotne prodaje vozil v Sloveniji. AMZS ocenjuje, da bo zanimanje za električna vozila še naprej raslo, predvsem zaradi okoljskih in davčnih spodbud vlade ter širše ponudbe električnih modelov na trgu.
- Excerpt: Čeprav je prodaja vozil okrevala, je bilo leto 2023 eno najslabših v zadnjih 25 letih Ključne besede: Rabljeni avtomobili, Električna vozila, Volkswagen, AMZS, Prodaja vozil, avtomobili, prodaja električnih avtomobilov pa je v lanskem letu v primerjavi z letom 2022 narasla za 140 odstotkov. Na področju električnih vozil je najbolj prodajan model ostal Tesla Model 3, sledijo mu modeli Renault Zoe in Volkswagen ID.4. Kljub veliki rasti pa električni avtomobili še vedno predstavljajo manjši delež c...

#### Rank 4: RELEVANT

- Title: V Sloveniji lani prodanih 8,4 odstotka več avtomobilov – največ Volkswagnovih
- Decision: relevant
- Rationale: Direct best-selling car/brand result.
- Category/date: zabava-in-slog / 2025-01-08T13:22:41
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/v-sloveniji-lani-prodanih-8-4-odstotka-vec-avtomobilov-najvec-volkswagnovih/732724
- FAISS rank/score: 1 / 0.8618
- Reranker score: 4.8218
- Keywords: avtomobili, Slovenija, prodaja
- Excerpt: V Sloveniji lani prodanih 8,4 odstotka več avtomobilov – največ Volkswagnovih Ključne besede: avtomobili, Slovenija, prodaja V Sloveniji je bilo lani prvič registriranih 53.018 osebnih avtomobilov, kar je 8,4 odstotka več kot predlani. Med vsemi lani prodanimi osebnimi avtomobili je bilo električnih 9876 oziroma 27 odstotkov manj kot predlani. Največ osebnih avtomobilov je prodal Volkswagen (7924 oziroma skoraj 15-odstotni tržni delež), sledila sta Renault (5910 oziroma 11,2-odstotni delež) in Š...

#### Rank 5: RELEVANT

- Title: Tesla model Y leta 2023 najbolje prodajano vozilo v Evropi
- Decision: relevant
- Rationale: Direct best-selling vehicle result.
- Category/date: zabava-in-slog / 2024-01-21T12:31:47
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/tesla-model-y-leta-2023-najbolje-prodajano-vozilo-v-evropi/695612
- FAISS rank/score: 3 / 0.8537
- Reranker score: 4.4125
- Keywords: Tesla, Model Y, Prodaja vozil, električni avtomobil, Evropa, prodaja, Slovenija, leta 2023, registracije, cena, konkurenca, industrija, vozila, strokovnjaki, uspeh, popularnost, Dacia Sandero, Volkswagen T-Roc, Škoda Octavia
- Excerpt: Tesla model Y leta 2023 najbolje prodajano vozilo v Evropi Ključne besede: Tesla, Model Y, Prodaja vozil, električni avtomobil, Evropa, prodaja, Slovenija, leta 2023, registracije, cena, konkurenca, industrija, vozila, strokovnjaki, uspeh, popularnost, Dacia Sandero, Volkswagen T-Roc, Škoda Octavia Električni križanec tesla Y je prvi električni avtomobil, ki je do zdaj postal najbolje prodajano vozilo v Evropi v koledarskem letu. Tesla model Y je bil v Sloveniji sedmi najbolje prodajan model avt...


### 20. Obisk tujega predsednika

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Zoran Milanović si je za prvo pot v tujino v drugem predsedniškem mandatu izbral Slovenijo
- Decision: relevant
- Rationale: Direct foreign president visit to Slovenia.
- Category/date: slovenija / 2025-02-19T13:19:48
- URL: https://www.rtvslo.si/slovenija/zoran-milanovic-si-je-za-prvo-pot-v-tujino-v-drugem-predsedniskem-mandatu-izbral-slovenijo/737062
- FAISS rank/score: 8 / 0.8313
- Reranker score: 3.9424
- Keywords: Uradni obisk, Slovenija, Zoran Milanović
- Excerpt: Zoran Milanović si je za prvo pot v tujino v drugem predsedniškem mandatu izbral Slovenijo Ključne besede: Uradni obisk, Slovenija, Zoran Milanović Hrvaški predsednik Zoran Milanović, ki je v torek v Zagrebu prisegel za drugi predsedniški petletni mandat, bo prihodnjo sredo na uradnem obisku v Sloveniji. Iz urada predsednice republike Nataše Pirc Musar so sporočili, da gre za prvo uradno pot Zorana Milanovića v tujino po nastopu drugega mandata predsednika republike. " Namen obiska je nadaljevan...

#### Rank 2: RELEVANT

- Title: Poljski predsednik Duda v New Yorku obiskal Trumpa
- Decision: relevant
- Rationale: Foreign president visit result.
- Category/date: svet / 2024-04-18T10:45:47
- URL: https://www.rtvslo.si/svet/preberite-tudi/poljski-predsednik-duda-v-new-yorku-obiskal-trumpa/705442
- FAISS rank/score: 3 / 0.8338
- Reranker score: 1.8172
- Keywords: duda, trump, zda, poljska, Poljski predsednik, Donald Trump, Srečanje, Evropa, Manhattan, Premier, Druženje, Truth Social, Prijateljstvo, Konservativni, Liberalen, Ukrajina, Rusija, Joe Biden, Volitve, Nato, Madžarska, Viktor Orban, Britanija
- Excerpt: Poljski predsednik Duda v New Yorku obiskal Trumpa Ključne besede: duda, trump, zda, poljska, Poljski predsednik, Donald Trump, Srečanje, Evropa, Manhattan, Premier, Druženje, Truth Social, Prijateljstvo, Konservativni, Liberalen, Ukrajina, Rusija, Joe Biden, Volitve, Nato, Madžarska, Viktor Orban, Britanija Poljski predsednik Andrzej Duda je v sredo obiskal nekdanjega predsednika ZDA Donalda Trumpa v njegovi stolpnici na Manhattnu. Poljski premier Donald Tusk je pred srečanjem poudaril, da od p...

#### Rank 3: RELEVANT

- Title: Urad predsednice: Vlada nima pristojnosti, da bi predsednici določala, koga lahko povabi
- Decision: relevant
- Rationale: Invitation for foreign president visit.
- Category/date: slovenija / 2024-11-07T17:16:05
- URL: https://www.rtvslo.si/slovenija/urad-predsednice-vlada-nima-pristojnosti-da-bi-predsednici-dolocala-koga-lahko-povabi/726737
- FAISS rank/score: 2 / 0.8382
- Reranker score: 1.5927
- Keywords: Vabilo, Kitajska, Zunanja politika, Predsednica, Vlada
- Excerpt: Urad predsednice: Vlada nima pristojnosti, da bi predsednici določala, koga lahko povabi Ključne besede: Vabilo, Kitajska, Zunanja politika, Predsednica, Vlada Vabilo kitajskemu predsedniku Ši Džinpingu na obisk v Slovenijo je skladno s politiko vlade, predsednica pa zanj ni potrebovala soglasja vlade, so pojasnili v uradu predsednice republike Nataše Pirc Musar. Vabilo Šiju naj bi zmotilo kabinet premierja Roberta Goloba, na zunanjem ministrstvu pa so potrdili, da so vabilo posredovali naslovni...

#### Rank 4: RELEVANT

- Title: Putin v Kirgiziji prvič na obisku v tujini po izdaji naloga ICC-ja
- Decision: relevant
- Rationale: Foreign visit by president.
- Category/date: svet / 2023-10-12T11:03:00
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/putin-v-kirgiziji-prvic-na-obisku-v-tujini-po-izdaji-naloga-icc-ja/684578
- FAISS rank/score: 24 / 0.8259
- Reranker score: 1.0552
- Keywords: Rusija, Kirgizistan, Vladimir Putin, ICC, Kirgizija, Mednarodno kazensko sodišče, Haag, Skupnost neodvisnih držav, SND, Aleksander Lukašenko, Sadir Žaparov, Zračna obramba, Ukrajina, Dekleta, Moskva, Marija Lvova-Belova, Pravice otrok, Aretekacija, Preventivni ukrepi, Brics, Južna Afrika
- Excerpt: Putin v Kirgiziji prvič na obisku v tujini po izdaji naloga ICC-ja Ključne besede: Rusija, Kirgizistan, Vladimir Putin, ICC, Kirgizija, Mednarodno kazensko sodišče, Haag, Skupnost neodvisnih držav, SND, Aleksander Lukašenko, Sadir Žaparov, Zračna obramba, Ukrajina, Dekleta, Moskva, Marija Lvova-Belova, Pravice otrok, Aretekacija, Preventivni ukrepi, Brics, Južna Afrika Ruski predsednik Vladimir Putin je prispel na obisk v Kirgizijo, kar je njegova prva pot v tujino, potem ko je Mednarodno kazens...

#### Rank 5: RELEVANT

- Title: Kitajski predsednik Ši začenja obisk v Evropi
- Decision: relevant
- Rationale: Foreign president visit to Europe.
- Category/date: svet / 2024-05-05T08:19:20
- URL: https://www.rtvslo.si/svet/evropa/kitajski-predsednik-si-zacenja-obisk-v-evropi/707152
- FAISS rank/score: 37 / 0.8240
- Reranker score: 0.6876
- Keywords: Trgovinski sporazum, Vojna v Ukrajini, Emmanuel Macron, Evropa, Xi Jinping, Kitajski predsednik, Ši Džinping, obisk, Francija, Srbija, Madžarska, Ursula von der Leyen, mednarodne krize, Ukrajina, Bližnji vzhod, trgovina, sodelovanje, globalni izzivi, revija Economist, Olaf Scholz, voditelji, Aleksandar Vučič, sporazum, prostotravni.
- Excerpt: Kitajski predsednik Ši začenja obisk v Evropi Ključne besede: Trgovinski sporazum, Vojna v Ukrajini, Emmanuel Macron, Evropa, Xi Jinping, Kitajski predsednik, Ši Džinping, obisk, Francija, Srbija, Madžarska, Ursula von der Leyen, mednarodne krize, Ukrajina, Bližnji vzhod, trgovina, sodelovanje, globalni izzivi, revija Economist, Olaf Scholz, voditelji, Aleksandar Vučič, sporazum, prostotravni. Kitajski predsednik Ši Džinping danes začenja šestdnevni uradni obisk v Evropi, v okviru katerega bo do...

