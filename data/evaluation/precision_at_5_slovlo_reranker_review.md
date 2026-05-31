# Precision@5 evaluation with reranker on

Created: 2026-05-31T20:08:06
Relevance rule: largely related
Embedding model: `rokn/slovlo-v1`
Reranker model: `cross-encoder/mmarco-mMiniLMv2-L12-H384-v1`
Retrieval: FAISS top 50 candidates, reranked, evaluated top 5 results
Full labeled JSON output: `data/evaluation/precision_at_5_reranker_decisions.json`
Raw reranker output: `data/evaluation/precision_at_5_reranker_raw_outputs.json`

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
| 4 | Tožba slovenskih avtoprevoznikov | 1/5 | 0.20 |
| 5 | Vojna Zvezd v Sloveniji | 1/5 | 0.20 |
| 6 | Ogromni zastoji na Slovenskih cestah | 5/5 | 1.00 |
| 7 | Višanje temperatur | 5/5 | 1.00 |
| 8 | Višanje cen nepremičnin v Sloveniji | 5/5 | 1.00 |
| 9 | Rogljič in Pogačar na tekmi | 5/5 | 1.00 |
| 10 | Donald Trump novi zakoni | 5/5 | 1.00 |
| 11 | Evropska Unija in zveza NATO | 5/5 | 1.00 |
| 12 | Velika Britanija Brexit | 4/5 | 0.80 |
| 13 | Vojna v Ukrajini in Zelenski | 5/5 | 1.00 |
| 14 | Kitajska proti ZDA | 5/5 | 1.00 |
| 15 | Korupcija v slovenski politiki | 5/5 | 1.00 |
| 16 | Izstrelitev rakete v vesolje | 5/5 | 1.00 |
| 17 | Delnice Tesle padajo | 4/5 | 0.80 |
| 18 | Nova verzija umetne inteligence | 5/5 | 1.00 |
| 19 | Najbolj prodajan avtomobil | 5/5 | 1.00 |
| 20 | Obisk tujega predsednika | 3/5 | 0.60 |

## Detailed decisions

### 1. Vpis v srednje šole

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Vpis je omejen na 58 srednjih šolah, povečal se je vpis v srednje in nižje poklicne šole
- Decision: relevant
- Rationale: Directly about enrolment in secondary schools.
- Category/date: slovenija / 2024-05-23T11:08:23
- URL: https://www.rtvslo.si/slovenija/vpis-je-omejen-na-58-srednjih-solah-povecal-se-je-vpis-v-srednje-in-nizje-poklicne-sole/709285
- FAISS rank/score: 5 / 0.8123
- Reranker score: 4.7520
- Keywords: Ministrstvo za vzgojo in izobraževanje, Gimnazijski programi, Poklicno izobraževanje, Srednje šole, Vpis
- Excerpt: Vpis je omejen na 58 srednjih šolah, povečal se je vpis v srednje in nižje poklicne šole Ključne besede: Ministrstvo za vzgojo in izobraževanje, Gimnazijski programi, Poklicno izobraževanje, Srednje šole, Vpis Prihodnje šolsko leto bo srednje šole obiskovalo 22.971 kandidatov, največ, 42,7 odstotka, se jih je vpisalo v srednje strokovne šole, sledijo gimnazije, srednje poklicne in nižje poklicne šole. Vpis bo omejen na 58 šolah, medtem ko je bil lani na 70. Vpis je omejen v 12 programih poklicne...

#### Rank 2: RELEVANT

- Title: Vpis v srednje šole: največ zanimanja za srednje strokovne šole
- Decision: relevant
- Rationale: Directly about interest/enrolment in secondary schools.
- Category/date: slovenija / 2023-04-25T17:29:00
- URL: https://www.rtvslo.si/slovenija/vpis-v-srednje-sole-najvec-zanimanja-za-srednje-strokovne-sole/666150
- FAISS rank/score: 7 / 0.8068
- Reranker score: 4.5939
- Keywords: vpis, šolsko leto, srednje šole, kandidati, mesta, prijavnica, izobraževalni programi, ministrstvo, poklicno izobraževanje, gimnazije, strokovno izobraževanje, razpisana mesta, podatki, statistika, sprejem, vpisni postopek, razporeditev, sposobnosti, prvi krog, programi, prosti poklice, želeni poklic, osnovno šolanje.
- Excerpt: Vpis v srednje šole: največ zanimanja za srednje strokovne šole Ključne besede: vpis, šolsko leto, srednje šole, kandidati, mesta, prijavnica, izobraževalni programi, ministrstvo, poklicno izobraževanje, gimnazije, strokovno izobraževanje, razpisana mesta, podatki, statistika, sprejem, vpisni postopek, razporeditev, sposobnosti, prvi krog, programi, prosti poklice, želeni poklic, osnovno šolanje. Za vpis novincev v srednje šole za prihodnje šolsko leto se je v roku na skupno 25.560 prvotno razpi...

#### Rank 3: RELEVANT

- Title: Vpisovanje v srednje šole: izteka se zadnji rok za prijavo za opravljanje preizkusa nadarjenosti
- Decision: relevant
- Rationale: Directly about secondary school application/enrolment process.
- Category/date: slovenija / 2024-03-04T08:39:01
- URL: https://www.rtvslo.si/slovenija/vpisovanje-v-srednje-sole-izteka-se-zadnji-rok-za-prijavo-za-opravljanje-preizkusa-nadarjenosti/700309
- FAISS rank/score: 1 / 0.8194
- Reranker score: 3.1737
- Keywords: preizkus nadarjenosti, znanja in spretnosti, osnovna šola, prijava, skit scena, preizkus, nadarjenost, znanje, spretnosti, srednješolski programi, vpisni pogoji, športni oddelki, obvestilo, zdravniško potrdilo, preventivni pregled, športni pogoji, klasični jeziki, tuj jezik, gimnazija, obrazci, novinci, vpisna mesta, splošne gimnazije, strokovne gimnazije
- Excerpt: Vpisovanje v srednje šole: izteka se zadnji rok za prijavo za opravljanje preizkusa nadarjenosti Ključne besede: preizkus nadarjenosti, znanja in spretnosti, osnovna šola, prijava, skit scena, preizkus, nadarjenost, znanje, spretnosti, srednješolski programi, vpisni pogoji, športni oddelki, obvestilo, zdravniško potrdilo, preventivni pregled, športni pogoji, klasični jeziki, tuj jezik, gimnazija, obrazci, novinci, vpisna mesta, splošne gimnazije, strokovne gimnazije Izteka se rok za prijavo za o...

#### Rank 4: RELEVANT

- Title: Za bodoče dijake še vedno na voljo približno 2700 prostih mest, omejitev vpisa na 69 srednjih šolah
- Decision: relevant
- Rationale: Directly about available secondary school places and enrolment limits.
- Category/date: slovenija / 2025-06-02T10:40:25
- URL: https://www.rtvslo.si/slovenija/za-bodoce-dijake-se-vedno-na-voljo-priblizno-2700-prostih-mest-omejitev-vpisa-na-69-srednjih-solah/747655
- FAISS rank/score: 16 / 0.7647
- Reranker score: 3.1383
- Keywords: srednje šole, vpis, omejitev, dijaki, Študenti, Skit scena
- Excerpt: Za bodoče dijake še vedno na voljo približno 2700 prostih mest, omejitev vpisa na 69 srednjih šolah Ključne besede: srednje šole, vpis, omejitev, dijaki, Študenti, Skit scena Letos je moralo zaradi velikega interesa vpis omejiti 69 srednjih šol, kar je devet več kot lani. "Vendar velja posebej poudariti, da večina teh šol, ki bodo vpis omejile, nima posebnih presežkov prijavljenih," ob tem poudarjajo na ministrstvu. Na srednje šole se je do 6. maja, ko je bil zaključen rok za prenos prijav, za v...

#### Rank 5: RELEVANT

- Title: V srednje šole sprejetih 22.127 bodočih dijakov, na voljo je bilo 25.444 vpisnih mest
- Decision: relevant
- Rationale: Directly about accepted future secondary school students and places.
- Category/date: slovenija / 2023-07-03T08:56:03
- URL: https://www.rtvslo.si/slovenija/v-srednje-sole-sprejetih-22-127-bodocih-dijakov-na-voljo-je-bilo-25-444-vpisnih-mest/673860
- FAISS rank/score: 3 / 0.8157
- Reranker score: 2.6587
- Keywords: Srednje šole, dijaki, vpis, prosta mesta, ministrstvo, vzgoja, izobraževanje, srednješolski programi, prijavno-vpisni postopek, novinci, razpisana mesta, poklicno izobraževanje, gimnazije, omejitev vpisa, izbirni postopek, želeno šolo, drugi krog, mest, šole
- Excerpt: V srednje šole sprejetih 22.127 bodočih dijakov, na voljo je bilo 25.444 vpisnih mest Ključne besede: Srednje šole, dijaki, vpis, prosta mesta, ministrstvo, vzgoja, izobraževanje, srednješolski programi, prijavno-vpisni postopek, novinci, razpisana mesta, poklicno izobraževanje, gimnazije, omejitev vpisa, izbirni postopek, želeno šolo, drugi krog, mest, šole Ministrstvo za vzgojo in izobraževanje je objavilo število še prostih mest za vpis v 1. letnik posameznih srednješolskih programov. Kandida...


### 2. Zakoni glede generativne umetne inteligence

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: ZPS: Umetna inteligenca prinaša tudi negativne posledice – kršenje zasebnosti in osebne integritete
- Decision: relevant
- Rationale: About generative AI, consumer rights, regulation and legislation.
- Category/date: gospodarstvo / 2023-06-20T13:58:03
- URL: https://www.rtvslo.si/gospodarstvo/zps-umetna-inteligenca-prinasa-tudi-negativne-posledice-krsenje-zasebnosti-in-osebne-integritete/672448
- FAISS rank/score: 3 / 0.7911
- Reranker score: 2.6032
- Keywords: Generativna umetna inteligenca, ZPS, Chat GPT, umetna inteligenca, potrošniki, tehnologija, aplikacija, pravice, zaupanje, varnost, kršenje zasebnosti, internet, digitalna politika, zakonodaja, Evropska unija, regulativa, ozaveščanje, opolnomočenje, lobiranje
- Excerpt: ZPS: Umetna inteligenca prinaša tudi negativne posledice – kršenje zasebnosti in osebne integritete Ključne besede: Generativna umetna inteligenca, ZPS, Chat GPT, umetna inteligenca, potrošniki, tehnologija, aplikacija, pravice, zaupanje, varnost, kršenje zasebnosti, internet, digitalna politika, zakonodaja, Evropska unija, regulativa, ozaveščanje, opolnomočenje, lobiranje V zadnjih mesecih je prišlo do bliskovite rasti ponudbe storitev, ki jih poganja generativna umetna inteligenca, ta pa ogrož...

#### Rank 2: RELEVANT

- Title: "Umetniška dela ustvarjajo izključno ljudje": poziv evropskega knjižnega sektorja za zaščito knjig
- Decision: relevant
- Rationale: About generative AI and copyright/legal protection for books.
- Category/date: kultura / 2025-04-23T17:02:00
- URL: https://www.rtvslo.si/kultura/knjige/umetniska-dela-ustvarjajo-izkljucno-ljudje-poziv-evropskega-knjiznega-sektorja-za-zascito-knjig/743658
- FAISS rank/score: 12 / 0.7812
- Reranker score: 2.0049
- Keywords: Evropski knjižni sektor, Generativna UI, Kulturni ekosistem, Avtorske pravice, Umetna inteligenca
- Excerpt: "Umetniška dela ustvarjajo izključno ljudje": poziv evropskega knjižnega sektorja za zaščito knjig Ključne besede: Evropski knjižni sektor, Generativna UI, Kulturni ekosistem, Avtorske pravice, Umetna inteligenca Ob vse večjem pojavu knjig, ki jih generira umetna inteligenca, evropski knjižni sektor poziva evropske politične odločevalce, da zaščitijo avtorska dela z jasnimi oznakami, finančno pa naj strojnega dela ne podpirajo z javnimi sredstvi. " Strojno izdelani proizvodi, ki z uporabo genera...

#### Rank 3: RELEVANT

- Title: Ob koncu kampanje UIzi prevedeno. UIzi zgrešeno: "UI naj v etični rabi podpira človečnost"
- Decision: relevant
- Rationale: About AI use, transparency, copyright and legal regulation.
- Category/date: kultura / 2025-11-03T17:49:11
- URL: https://www.rtvslo.si/kultura/jezik/ob-koncu-kampanje-uizi-prevedeno-uizi-zgreseno-ui-naj-v-eticni-rabi-podpira-clovecnost/762817
- FAISS rank/score: 24 / 0.7644
- Reranker score: 1.7153
- Keywords: Jezikovni poklici, Transparentnost, Etična raba, Avtorska pravica, Umetna inteligenca
- Excerpt: Ob koncu kampanje UIzi prevedeno. UIzi zgrešeno: "UI naj v etični rabi podpira človečnost" Ključne besede: Jezikovni poklici, Transparentnost, Etična raba, Avtorska pravica, Umetna inteligenca Organizatorji kampanje UIzi prevedeno. UIzi zgrešeno so ob njenem zaključku na javnost in odločevalce naslovili več zahtev, ki se dotikajo avtorskih pravic, transparentnosti glede rabe UI-ja ter ohranitve in razvoja jezikovnih poklicev. Glede avtorske pravice so zahteve podali v osmih točkah. Med drugim za...

#### Rank 4: RELEVANT

- Title: Vizualni umetniki pridobivajo v pravni bitki proti umetni inteligenci. Bo z glasbo drugače?
- Decision: relevant
- Rationale: About legal disputes and copyright around generative AI.
- Category/date: kultura / 2024-08-14T21:03:41
- URL: https://www.rtvslo.si/kultura/glasba/vizualni-umetniki-pridobivajo-v-pravni-bitki-proti-umetni-inteligenci-bo-z-glasbo-drugace/718051
- FAISS rank/score: 27 / 0.7639
- Reranker score: 0.6209
- Keywords: Poštena uporaba, Generativna orodja, Umetniška tožba, Avtorske pravice, Generirana umetnost
- Excerpt: Vizualni umetniki pridobivajo v pravni bitki proti umetni inteligenci. Bo z glasbo drugače? Ključne besede: Poštena uporaba, Generativna orodja, Umetniška tožba, Avtorske pravice, Generirana umetnost Pravno urejanje uporabe vizualnih ali glasbenih del za učenje umetne inteligence postaja vse bolj zapleteno, kar dokazujejo tudi zadnji sodni primeri v ZDA. V prihodnjih mesecih bo jasno, ali gre za pošteno uporabo ali kršitve avtorskih pravic. Na začetku letošnjega leta smo poročali o dolgem seznam...

#### Rank 5: RELEVANT

- Title: Vlada sprejela predlog, ki prinaša enotna pravila za razvoj in uporabo umetne inteligence v EU-ju
- Decision: relevant
- Rationale: Directly about legal rules for AI in the EU.
- Category/date: slovenija / 2025-08-21T15:32:29
- URL: https://www.rtvslo.si/slovenija/vlada-sprejela-predlog-ki-prinasa-enotna-pravila-za-razvoj-in-uporabo-umetne-inteligence-v-eu-ju/755310
- FAISS rank/score: 1 / 0.7996
- Reranker score: 0.5668
- Keywords: UI, zakon, evropska uredba
- Excerpt: Vlada sprejela predlog, ki prinaša enotna pravila za razvoj in uporabo umetne inteligence v EU-ju Ključne besede: UI, zakon, evropska uredba Vlada je sprejela predlog zakona o izvajanju evropske uredbe o določitvi harmoniziranih pravil o umetni inteligenci oz. akta o umetni inteligenci. Predlog med drugim določa nadzorne organe in uvaja možnost imenovanja komisarja za etiko umetne inteligence. Akt o umetni inteligenci, katerega namen je izboljšati delovanje notranjega trga z uvedbo enotnih pravi...


### 3. Cene kart na nogometnem svetovnem prvenstvu

Precision@5: 3/5 = 0.60

#### Rank 1: RELEVANT

- Title: Tožba proti Fifi zaradi visokih cen vstopnic na SP 2026
- Decision: relevant
- Rationale: Directly about lawsuit against FIFA over high World Cup 2026 ticket prices.
- Category/date: sport / 2026-03-24T11:22:40
- URL: https://www.rtvslo.si/sport/nogomet/tozba-proti-fifi-zaradi-visokih-cen-vstopnic-na-sp-2026/777332
- FAISS rank/score: 1 / 0.7799
- Reranker score: 1.3264
- Keywords: vstopnice, cene, svetovno prvenstvo, nogomet
- Excerpt: Tožba proti Fifi zaradi visokih cen vstopnic na SP 2026 Ključne besede: vstopnice, cene, svetovno prvenstvo, nogomet Združenje nogometnih navijačev Evrope (FSE) je pri Evropski komisiji vložilo tožbo proti Mednarodni nogometni zvezi (Fifa) zaradi previsokih cen vstopnic na letošnjem svetovnem prvenstvu, ki bo v ZDA, Kanadi in Mehiki. "Fifa ima monopol nad prodajo vstopnic za svetovno prvenstvo 2026 in to moč je izkoristila za vsiljevanje pogojev nogometnim privržencem, ki v konkurenčnem tržnem o...

#### Rank 2: RELEVANT

- Title: Infantino zagovarja visoke cene vstopnic in pravi, da bodo ves denar vložili spet v nogomet
- Decision: relevant
- Rationale: Directly about high football ticket prices and FIFA/Infantino.
- Category/date: sport / 2025-12-30T08:47:57
- URL: https://www.rtvslo.si/sport/nogomet/infantino-zagovarja-visoke-cene-vstopnic-in-pravi-da-bodo-ves-denar-vlozili-spet-v-nogomet/768669
- FAISS rank/score: 2 / 0.7688
- Reranker score: 0.9561
- Keywords: Gianni Infantino, Fifa, SP, vstopnice
- Excerpt: Infantino zagovarja visoke cene vstopnic in pravi, da bodo ves denar vložili spet v nogomet Ključne besede: Gianni Infantino, Fifa, SP, vstopnice Predsednik Mednarodne nogometne zveze Fife Gianni Infantino zagovarja visoke cene vstopnic za prihajajoče svetovno prvenstvo. Infantino je dejal, da cene vstopnic zgolj odražajo trenutno povpraševanje po njih. Združenje nogometnih navijačev (FSA) je od začetka prodaje vstopnic za tekmovanje, ki bo med 11. junijem in 19. julijem prihodnje leto potekalo...

#### Rank 3: RELEVANT

- Title: Ogromno povpraševanje za nogometni spektakel leta
- Decision: relevant
- Rationale: About huge demand for a football spectacle and tickets/pricing context.
- Category/date: sport / 2026-01-15T16:54:35
- URL: https://www.rtvslo.si/sport/nogomet/svetovno-prvenstvo-v-nogometu/ogromno-povprasevanje-za-nogometni-spektakel-leta/770262
- FAISS rank/score: 3 / 0.7639
- Reranker score: -0.0895
- Keywords: Fifa, Navijači, Prodaja vstopnic, Nogometni dogodek
- Excerpt: Ogromno povpraševanje za nogometni spektakel leta Ključne besede: Fifa, Navijači, Prodaja vstopnic, Nogometni dogodek V zadnjem delu prodaje je mednarodna nogometna zveza (Fifa) prejela več kot pol milijarde zahtevkov za vstopnice za ogled tekem letošnjega svetovnega prvenstva, ki bo poleti potekalo v ZDA, Kanadi in Mehiki. Prodaja vstopnic se je začela 11. decembra in je trajala do 13. januarja. Prvič so bile naprodaj posamezne vstopnice za določene tekme. Navijači bodo o morebitnem uspehu v na...

#### Rank 4: NOT RELEVANT

- Title: Svetovni klubski prvak bo prejel več kot sto milijonov evrov
- Decision: not_relevant
- Rationale: About Club World Cup prize money, not ticket prices for the World Cup.
- Category/date: sport / 2025-06-10T09:51:35
- URL: https://www.rtvslo.si/sport/nogomet/svetovni-klubski-prvak-bo-prejel-vec-kot-sto-milijonov-evrov/748500
- FAISS rank/score: 11 / 0.7364
- Reranker score: -1.1068
- Keywords: nogomet, svetovno klubsko prvenstvo, Fifa
- Excerpt: Svetovni klubski prvak bo prejel več kot sto milijonov evrov Ključne besede: nogomet, svetovno klubsko prvenstvo, Fifa V ZDA se bo v noči na nedeljo začelo klubsko svetovno prvenstvo v nogometu. To je prenovljeni turnir z 32 ekipami. Denarni sklad bo znašal kar milijardo ameriških dolarjev oziroma 876 milijonov evrov. Od tega bo zmagovalcu pripadlo 109 milijonov evrov, so poudarili pri Mednarodni nogometni zvezi (Fifa). Turnir z 32 ekipami, ki bo potekal v ZDA do 13. julija, se že od trenutka, k...

#### Rank 5: NOT RELEVANT

- Title: Zeničan ponudil balkon, žar in pijačo za ogled spektakla v Zenici. Cena 500 evrov.
- Decision: not_relevant
- Rationale: About private viewing from a balcony, not World Cup ticket prices.
- Category/date: zabava-in-slog / 2026-03-30T13:04:33
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/zenican-ponudil-balkon-zar-in-pijaco-za-ogled-spektakla-v-zenici-cena-500-evrov/777924
- FAISS rank/score: 50 / 0.7130
- Reranker score: -1.2890
- Keywords: BiH, Italija, kvalifikacije, vstopnice, SP
- Excerpt: Zeničan ponudil balkon, žar in pijačo za ogled spektakla v Zenici. Cena 500 evrov. Ključne besede: BiH, Italija, kvalifikacije, vstopnice, SP Čeprav so vstopnice za odločilno tekmo za nastop na SP-ju v nogometu med Italijo in BiH-om ekspresno pošle, so za kanček upanja in smeh poskrbeli stanovalci okoliških blokov v Zenici, ki imajo pogled na nogometno zelenico. Med njimi izstopa Dino Mujanović, ki je z oglasom na Facebooku postal zvezda družbenih omrežij. Prebivalec Zenice je tam delil fotograf...


### 4. Tožba slovenskih avtoprevoznikov

Precision@5: 1/5 = 0.20

#### Rank 1: RELEVANT

- Title: Avtoprevozniki na zboru državi postavili zahteve, sicer lahko sledi zaprtje najpomembnejših cest
- Decision: relevant
- Rationale: About Slovenian hauliers/transporters and their demands, though not specifically a lawsuit.
- Category/date: gospodarstvo / 2025-10-18T15:03:41
- URL: https://www.rtvslo.si/gospodarstvo/avtoprevozniki-na-zboru-drzavi-postavili-zahteve-sicer-lahko-sledi-zaprtje-najpomembnejsih-cest/761263
- FAISS rank/score: 49 / 0.7320
- Reranker score: 2.2023
- Keywords: Digitalizacija, Kadrovska kriza, Zeleni prehod, Zaprtje cest, Avtoprevozniki
- Excerpt: Avtoprevozniki na zboru državi postavili zahteve, sicer lahko sledi zaprtje najpomembnejših cest Ključne besede: Digitalizacija, Kadrovska kriza, Zeleni prehod, Zaprtje cest, Avtoprevozniki Avtoprevozniki so na zboru v Celju na vlado naslovili zahteve, za katere pričakujejo, da jih izpolni do decembra oz. do marca 2026. V nasprotnem bodo decembra pripravili protest, za marec pa so napovedali zaprtje pomembnih cest v Sloveniji. Zbor sta organizirala sekcija za promet pri Obrtno-podjetniški zborni...

#### Rank 2: NOT RELEVANT

- Title: Avtoserviserji prijavili Zavarovalnico Triglav zaradi sumov zlorabe prevladujočega položaja na trgu
- Decision: not_relevant
- Rationale: About car repair shops and insurer Triglav, not Slovenian hauliers.
- Category/date: gospodarstvo / 2025-05-12T13:48:49
- URL: https://www.rtvslo.si/gospodarstvo/avtoserviserji-prijavili-zavarovalnico-triglav-zaradi-sumov-zlorabe-prevladujocega-polozaja-na-trgu/745438
- FAISS rank/score: 35 / 0.7350
- Reranker score: 1.9528
- Keywords: AVK prijava, Urna postavka, Prevladojoči položaj, Avtoserviserji, Zavarovalnica Triglav
- Excerpt: Avtoserviserji prijavili Zavarovalnico Triglav zaradi sumov zlorabe prevladujočega položaja na trgu Ključne besede: AVK prijava, Urna postavka, Prevladojoči položaj, Avtoserviserji, Zavarovalnica Triglav Avtoserviserji, v Slovenskem društvu avtostroke (SDA), so Javni agenciji RS za varstvo konkurence (AVK) prijavili Zavarovalnico Triglav zaradi sumov zlorabe prevladujočega položaja na trgu. Trdijo, da so urne postavke nevzdržne in ne pokrijejo dela. Kot je danes v izjavi za medije pred sedežem A...

#### Rank 3: NOT RELEVANT

- Title: Avtoserviserji prijavili Zavarovalnico Triglav zaradi sumov zlorabe prevladujočega položaja na trgu
- Decision: not_relevant
- Rationale: Duplicate about car repair shops and insurer Triglav, not Slovenian hauliers.
- Category/date: gospodarstvo / 2025-05-12T13:48:49
- URL: https://www.rtvslo.si/gospodarstvo/avtoserviserji-prijavili-zavarovalnico-triglav-zaradi-sumov-zlorabe-prevladojocega-polozaja-na-trgu/745438
- FAISS rank/score: 36 / 0.7350
- Reranker score: 1.9528
- Keywords: AVK prijava, Urna postavka, Prevladojoči položaj, Avtoserviserji, Zavarovalnica Triglav
- Excerpt: Avtoserviserji prijavili Zavarovalnico Triglav zaradi sumov zlorabe prevladujočega položaja na trgu Ključne besede: AVK prijava, Urna postavka, Prevladojoči položaj, Avtoserviserji, Zavarovalnica Triglav Avtoserviserji, v Slovenskem društvu avtostroke (SDA), so Javni agenciji RS za varstvo konkurence (AVK) prijavili Zavarovalnico Triglav zaradi sumov zlorabe prevladujočega položaja na trgu. Trdijo, da so urne postavke nevzdržne in ne pokrijejo dela. Kot je danes v izjavi za medije pred sedežem A...

#### Rank 4: NOT RELEVANT

- Title: Številni vozniki tožijo Renault zaradi težav, oglasili so se tudi slovenski lastniki
- Decision: not_relevant
- Rationale: About drivers/owners suing Renault, not Slovenian hauliers.
- Category/date: zabava-in-slog / 2023-07-09T21:45:52
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/stevilni-vozniki-tozijo-renault-zaradi-tezav-oglasili-so-se-tudi-slovenski-lastniki/674591
- FAISS rank/score: 1 / 0.7848
- Reranker score: 1.8911
- Keywords: Renault, tožba, težave z motorjem, 1.2 TCe, težave, motor, avtomobil, 1,2-litrski, lastniki, Nissan, Dacia, vozniki, olje, pregrevanje, odpoklic, garancija, servis, odškodnina, sodišče, napaka, rešitev, kolektivna tožba
- Excerpt: Številni vozniki tožijo Renault zaradi težav, oglasili so se tudi slovenski lastniki Ključne besede: Renault, tožba, težave z motorjem, 1.2 TCe, težave, motor, avtomobil, 1,2-litrski, lastniki, Nissan, Dacia, vozniki, olje, pregrevanje, odpoklic, garancija, servis, odškodnina, sodišče, napaka, rešitev, kolektivna tožba Pred mesecem dni je skoraj 1800 francoskih lastnikov avtomobilov vložilo tožbo proti podjetju Renault zaradi težav z 1,2-litrskim motorjem, ki je bil med letoma 2012 in 2016 vgraj...

#### Rank 5: NOT RELEVANT

- Title: ZPS: Lastniki vozil VW, ki so vložili tožbo zaradi prirejanja izpustov, bodo prejeli odškodnino
- Decision: not_relevant
- Rationale: About VW owners and emissions compensation, not Slovenian hauliers.
- Category/date: gospodarstvo / 2024-11-19T15:24:56
- URL: https://www.rtvslo.si/gospodarstvo/zps-lastniki-vozil-vw-ki-so-vlozili-tozbo-zaradi-prirejanja-izpustov-bodo-prejeli-odskodnino/727972
- FAISS rank/score: 18 / 0.7483
- Reranker score: 1.4229
- Keywords: ZPS, Poravnava, Odškodnina, Volkswagen
- Excerpt: ZPS: Lastniki vozil VW, ki so vložili tožbo zaradi prirejanja izpustov, bodo prejeli odškodnino Ključne besede: ZPS, Poravnava, Odškodnina, Volkswagen Volkswagen je pristal na poravnavo s slovenskimi potrošniki, ki so preko zveze potrošnikov vložili skupno tožbo proti Volkswagnu zaradi afere dieselgate, v kateri je VW priznal, da je v vozila namestil opremo za prirejanje izpustov. Zveza potrošnikov Slovenije (ZPS), ki je leta 2017 v kampanji PreVWara zbrala zainteresirane slovenske potrošnike, k...


### 5. Vojna Zvezd v Sloveniji

Precision@5: 1/5 = 0.20

#### Rank 1: NOT RELEVANT

- Title: Razstava in akademija ob 30-letnici Zveze veteranov vojne za Slovenijo
- Decision: not_relevant
- Rationale: False match on war/veterans/Slovenia, not Star Wars.
- Category/date: slovenija / 2023-10-10T20:54:03
- URL: https://www.rtvslo.si/slovenija/preberite-tudi/razstava-in-akademija-ob-30-letnici-zveze-veteranov-vojne-za-slovenijo/684406
- FAISS rank/score: 3 / 0.7164
- Reranker score: 3.2253
- Keywords: Nataša Pirc Musar, Mitja Jankovič, 30-letnica delovanja, Zveza veteranov vojne za Slovenijo, Razstava, veterani, vojna za Slovenijo, slavnostna akademija, Ljubljana, Zveza veteranov, osamosvojitvena vojna, predsednica republike, pomembne funkcije, dialog, profesionalnost, mladi, spomin, generacije, teritorialna obramba, pravice, dedje, očetje, izobraževanje, skupščina.
- Excerpt: Razstava in akademija ob 30-letnici Zveze veteranov vojne za Slovenijo Ključne besede: Nataša Pirc Musar, Mitja Jankovič, 30-letnica delovanja, Zveza veteranov vojne za Slovenijo, Razstava, veterani, vojna za Slovenijo, slavnostna akademija, Ljubljana, Zveza veteranov, osamosvojitvena vojna, predsednica republike, pomembne funkcije, dialog, profesionalnost, mladi, spomin, generacije, teritorialna obramba, pravice, dedje, očetje, izobraževanje, skupščina. Zveza veteranov vojne za Slovenijo je ob...

#### Rank 2: NOT RELEVANT

- Title: Na čelu Zveze veteranov vojne za Slovenijo ostaja Ladislav Lipič
- Decision: not_relevant
- Rationale: False match on war veterans, not Star Wars.
- Category/date: slovenija / 2024-04-06T19:27:44
- URL: https://www.rtvslo.si/slovenija/preberite-tudi/na-celu-zveze-veteranov-vojne-za-slovenijo-ostaja-ladislav-lipic/704146
- FAISS rank/score: 16 / 0.6992
- Reranker score: 2.8366
- Keywords: Mandatno obdobje, Ladislav Lipič, Zveza veteranov, Veterani, vojna, Slovenija, zveza, mandat, volitve, zbor, obrambni minister, Marjan Šarec, vrednote, domoljubje, pogum, Laško, epidemija, covid-19, poplave, izzivi, 30-letnica, teritorialna obramba, slavnostni govor, general Rudolf Maister, žrtve, politična opcija, društvo, ministrstvo, vojaški poklic, mladi, čast, zvestoba, poštenost, poročila, načrti, organe, volitve.
- Excerpt: Na čelu Zveze veteranov vojne za Slovenijo ostaja Ladislav Lipič Ključne besede: Mandatno obdobje, Ladislav Lipič, Zveza veteranov, Veterani, vojna, Slovenija, zveza, mandat, volitve, zbor, obrambni minister, Marjan Šarec, vrednote, domoljubje, pogum, Laško, epidemija, covid-19, poplave, izzivi, 30-letnica, teritorialna obramba, slavnostni govor, general Rudolf Maister, žrtve, politična opcija, društvo, ministrstvo, vojaški poklic, mladi, čast, zvestoba, poštenost, poročila, načrti, organe, voli...

#### Rank 3: NOT RELEVANT

- Title: SV se pripravlja na mednarodno vojaško vajo Jadranski udar. V njej bo sodelovalo 31 držav.
- Decision: not_relevant
- Rationale: About a military exercise, not Star Wars.
- Category/date: slovenija / 2025-06-10T13:38:47
- URL: https://www.rtvslo.si/slovenija/sv-se-pripravlja-na-mednarodno-vojasko-vajo-jadranski-udar-v-njej-bo-sodelovalo-31-drzav/748532
- FAISS rank/score: 35 / 0.6938
- Reranker score: 2.0423
- Keywords: Zračna podpora, Vojaško usposabljanje, 31 držav, Jadranski udar, Mednarodna vojaška vaja
- Excerpt: SV se pripravlja na mednarodno vojaško vajo Jadranski udar. V njej bo sodelovalo 31 držav. Ključne besede: Zračna podpora, Vojaško usposabljanje, 31 držav, Jadranski udar, Mednarodna vojaška vaja Slovenska vojska (SV) se pripravlja na 12. mednarodno vojaško vajo Jadranski udar 2025, ki bo v Sloveniji od 13. do 24. junija. Urili bodo kontrolorje združenega ognja. Sodelovalo bo okoli 100 pripadnikov z uporabo različnih vojaških vozil. Poveljnik 15. brigade vojaškega letalstva in zračne obrambe Jan...

#### Rank 4: NOT RELEVANT

- Title: "V zavezništvu ni ključno, koliko narediš, ampak ali narediš, kar si obljubil. Tega se nismo držali"
- Decision: not_relevant
- Rationale: About NATO/alliance obligations, not Star Wars.
- Category/date: slovenija / 2024-03-28T07:30:00
- URL: https://www.rtvslo.si/slovenija/v-zaveznistvu-ni-kljucno-koliko-naredis-ampak-ali-naredis-kar-si-obljubil-tega-se-nismo-drzali/702791
- FAISS rank/score: 32 / 0.6949
- Reranker score: 1.8389
- Keywords: Bojne skupine, Vojaška oprema, Obrambni proračun, Slovenija, Nato, članstvo, obrambni izdatki, vojaško zavezništvo, integracija, razvojna sprememba, bojne sposobnosti, varnostni položaj, Evropa, Ukrajina, načrti, zavezništvu, financiranje, nabava
- Excerpt: "V zavezništvu ni ključno, koliko narediš, ampak ali narediš, kar si obljubil. Tega se nismo držali" Ključne besede: Bojne skupine, Vojaška oprema, Obrambni proračun, Slovenija, Nato, članstvo, obrambni izdatki, vojaško zavezništvo, integracija, razvojna sprememba, bojne sposobnosti, varnostni položaj, Evropa, Ukrajina, načrti, zavezništvu, financiranje, nabava Slovenija je 29. marca 2004, skupaj z Bolgarijo, Estonijo, Latvijo, Litvo, Romunijo in Slovaško, postala polnopravna članica vojaškega z...

#### Rank 5: RELEVANT

- Title: Po svetu praznujejo dan Vojne zvezd
- Decision: relevant
- Rationale: About Star Wars day; related to Vojna zvezd even if not specifically Slovenia.
- Category/date: zabava-in-slog / 2023-05-04T17:09:00
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/po-svetu-praznujejo-dan-vojne-zvezd/667027
- FAISS rank/score: 2 / 0.7198
- Reranker score: 1.3160
- Keywords: Vojna zvezd, Star Wars, May the fourth be with you, franšiza, filmi, kultura, popularni, datum, praznovanje, Luka Skywalker, George Lucas, animirani, igralci, televizijske serije, igrače, videoigre, Lego, BioWare, Slovenija, otroci, liki, imena
- Excerpt: Po svetu praznujejo dan Vojne zvezd Ključne besede: Vojna zvezd, Star Wars, May the fourth be with you, franšiza, filmi, kultura, popularni, datum, praznovanje, Luka Skywalker, George Lucas, animirani, igralci, televizijske serije, igrače, videoigre, Lego, BioWare, Slovenija, otroci, liki, imena Ljubitelji ene največjih znanstvenofantastičnih franšiz na svetu že od leta 2011 četrtega maja praznujejo dan Vojne zvezd. Kultni filmi so vse od prvenca leta 1977 premikali meje žanra in se zasidrali gl...


### 6. Ogromni zastoji na Slovenskih cestah

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Ob številnih tujih turistih na slovenskih cestah ves dan pričakovana gneča in zastoji
- Decision: relevant
- Rationale: Directly about traffic jams on Slovenian roads.
- Category/date: slovenija / 2023-05-18T10:36:00
- URL: https://www.rtvslo.si/slovenija/ob-stevilnih-tujih-turistih-na-slovenskih-cestah-ves-dan-pricakovana-gneca-in-zastoji/668570
- FAISS rank/score: 6 / 0.8126
- Reranker score: 3.3571
- Keywords: promet, zastoji, Dars, cesta, zastoj, avtocesta, turist, praznik, dela prost dan, gneča, prometno-informacijski center, prometna informacija, mestno središče, obvoznica, Ljubljana, štajerska avtocesta, število kolone, gorenjska avtocesta, primorska avtocesta, vzdrževanje ceste
- Excerpt: Ob številnih tujih turistih na slovenskih cestah ves dan pričakovana gneča in zastoji Ključne besede: promet, zastoji, Dars, cesta, zastoj, avtocesta, turist, praznik, dela prost dan, gneča, prometno-informacijski center, prometna informacija, mestno središče, obvoznica, Ljubljana, štajerska avtocesta, število kolone, gorenjska avtocesta, primorska avtocesta, vzdrževanje ceste Na slovenskih cestah je močno zgoščen promet, na številnih avtocestnih odsekih so tudi zastoji. Veliko je predvsem turis...

#### Rank 2: RELEVANT

- Title: AMZS: Na pot le spočiti in pripravljeni. Ceste bodo letos še bolj obremenjene.
- Decision: relevant
- Rationale: About congested Slovenian roads.
- Category/date: slovenija / 2024-06-22T07:35:13
- URL: https://www.rtvslo.si/slovenija/amzs-na-pot-le-spociti-in-pripravljeni-ceste-bodo-letos-se-bolj-obremenjene/712638
- FAISS rank/score: 49 / 0.7561
- Reranker score: 2.3447
- Keywords: Nadzor na meji, Reševalni pas, Prometni zastoji, Potovanje, AMZS
- Excerpt: AMZS: Na pot le spočiti in pripravljeni. Ceste bodo letos še bolj obremenjene. Ključne besede: Nadzor na meji, Reševalni pas, Prometni zastoji, Potovanje, AMZS Do konca poletja lahko pričakujemo občutno povečan promet na cestah proti Hrvaški, predvsem ob petkih in sobotah, ter v obratni smeri ob sobotah in nedeljah. AMZS voznike opozarja, naj se na pot ustrezno pripravijo ter prej preverijo stanje na cestah. Avto-moto zveza Slovenije (AMZS) voznike poziva, da se na pot odpravijo spočiti in le s...

#### Rank 3: RELEVANT

- Title: Dars: Zastoje na avtocesti povzročili zdrsi tovornjakov, bilo jih je najmanj 30
- Decision: relevant
- Rationale: About traffic jams caused by trucks on roads/highways.
- Category/date: okolje / 2023-01-16T06:07:00
- URL: https://www.rtvslo.si/okolje/dars-zastoje-na-avtocesti-povzrocili-zdrsi-tovornjakov-bilo-jih-je-najmanj-30/654426
- FAISS rank/score: 45 / 0.7590
- Reranker score: 2.1564
- Keywords: Sneženje, Promet, Ceste, avtocesta, zastoj, tovorna vozila, zdrs, neustrezna oprema, plužna vozila, Dars, neodgovorni vozniki, zimska oprema, pluženje, preventiva, izločanje vozil, nesreče, zastoji, vzdrževanje, sol, natrijev klorid, kalcijev klorid.
- Excerpt: Dars: Zastoje na avtocesti povzročili zdrsi tovornjakov, bilo jih je najmanj 30 Ključne besede: Sneženje, Promet, Ceste, avtocesta, zastoj, tovorna vozila, zdrs, neustrezna oprema, plužna vozila, Dars, neodgovorni vozniki, zimska oprema, pluženje, preventiva, izločanje vozil, nesreče, zastoji, vzdrževanje, sol, natrijev klorid, kalcijev klorid. Zastoji na avtocestah so bili posledica najmanj 30 zdrsov tovornih vozil zaradi neustrezne opreme, ki so se zgodili med približno 4.30 in 6.00, pojasnjuj...

#### Rank 4: RELEVANT

- Title: V več državah dela prost dan, na avtocestah so bili zastoji
- Decision: relevant
- Rationale: About traffic jams on highways.
- Category/date: slovenija / 2023-06-08T08:19:00
- URL: https://www.rtvslo.si/slovenija/v-vec-drzavah-dela-prost-dan-na-avtocestah-so-bili-zastoji/671058
- FAISS rank/score: 5 / 0.8144
- Reranker score: 1.8447
- Keywords: Promet, prazniki, gneča, katoliški praznik, rešnje telo, kri, telovo, Avstrija, Nemčija, Hrvaška, prost dan, počitnice, tujina, policija, zastoji, avtocesta, prometni center, Slovenija, Italija, obvoznica, delovna zapora, Maribor, Ljubljana, Koper, zastoj, Brda, Brezovica, Kopru
- Excerpt: V več državah dela prost dan, na avtocestah so bili zastoji Ključne besede: Promet, prazniki, gneča, katoliški praznik, rešnje telo, kri, telovo, Avstrija, Nemčija, Hrvaška, prost dan, počitnice, tujina, policija, zastoji, avtocesta, prometni center, Slovenija, Italija, obvoznica, delovna zapora, Maribor, Ljubljana, Koper, zastoj, Brda, Brezovica, Kopru Ob katoliškem prazniku svetega rešnjega telesa in krvi, imenovanem tudi telovo, ki je v več državah, med drugim v Avstriji, večjem delu Nemčije...

#### Rank 5: RELEVANT

- Title: Primorska avtocesta zaradi zdrsov tovornih vozil le delno odprta, težave tudi drugod
- Decision: relevant
- Rationale: About highway disruptions and truck skids causing traffic problems.
- Category/date: okolje / 2026-01-06T07:28:00
- URL: https://www.rtvslo.si/okolje/vreme/primorska-avtocesta-zaradi-zdrsov-tovornih-vozil-le-delno-odprta-tezave-tudi-drugod/769193
- FAISS rank/score: 29 / 0.7722
- Reranker score: 1.7801
- Keywords: Padavine, Nizke temperature, Burja, Južna Slovenija, Sneg
- Excerpt: Primorska avtocesta zaradi zdrsov tovornih vozil le delno odprta, težave tudi drugod Ključne besede: Padavine, Nizke temperature, Burja, Južna Slovenija, Sneg Zaradi sneženja in nizkih temperatur se je na slovenskih cestah zgodilo več nesreč, ponekod so nastajali daljši zastoji. Primorska avtocesta je zaradi zdrsa več tovornih vozil le delno prevozna, tovorna vozila izločajo na vseh avtocestah. Zaradi zdrsov tovornih vozil promet poteka po enem pasu med Senožečami in Nanosom proti Ljubljani, moč...


### 7. Višanje temperatur

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Že 50-odstotna verjetnost, da se bo temperatura do leta 2026 dvignila za več kot 1,5 stopinje
- Decision: relevant
- Rationale: Directly about rising global temperature.
- Category/date: okolje / 2022-05-10T13:35:04
- URL: https://www.rtvslo.si/okolje/ze-50-odstotna-verjetnost-da-se-bo-temperatura-do-leta-2026-dvignila-za-vec-kot-1-5-stopinje/626850
- FAISS rank/score: 3 / 0.7651
- Reranker score: 0.3368
- Keywords: segrevanje ozračja, temperatura, okolje, podnebne spremembe, vročinski valovi, toplogredni plini, pariški sporazum, podnebna konferenca, vpliv podnebnih sprememb, arktična regija
- Excerpt: Že 50-odstotna verjetnost, da se bo temperatura do leta 2026 dvignila za več kot 1,5 stopinje Ključne besede: segrevanje ozračja, temperatura, okolje, podnebne spremembe, vročinski valovi, toplogredni plini, pariški sporazum, podnebna konferenca, vpliv podnebnih sprememb, arktična regija Obstaja že 50-odstotna verjetnost, da bo svet do leta 2026 presegel ključno mejo pri segrevanju ozračja, to je 1,5 stopinje Celzija. Vremenoslovci so tudi prepričani, da bomo v prihodnjih petih letih doživeli na...

#### Rank 2: RELEVANT

- Title: Z višanjem temperatur se "facekiniji" prodajajo kot vroče žemljice
- Decision: relevant
- Rationale: About effects of rising temperatures and heat records.
- Category/date: zabava-in-slog / 2023-07-21T12:05:56
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/z-visanjem-temperatur-se-facekiniji-prodajajo-kot-vroce-zemljice/675739
- FAISS rank/score: 15 / 0.7465
- Reranker score: -0.6364
- Keywords: vročina, Kitajska, sonce, facekini, zaščita pred soncem, pokrivala, vročinski rekordi, UV-žarki, bela polt, kozmetični izdelki, sončne bolezni, turizem, Peking, maska za obraz, prodaja, prodajalna, pandemija, zaščitna sredstva, ventilatorji, klasična lepota, pokrivala za obraz, koža
- Excerpt: Z višanjem temperatur se "facekiniji" prodajajo kot vroče žemljice Ključne besede: vročina, Kitajska, sonce, facekini, zaščita pred soncem, pokrivala, vročinski rekordi, UV-žarki, bela polt, kozmetični izdelki, sončne bolezni, turizem, Peking, maska za obraz, prodaja, prodajalna, pandemija, zaščitna sredstva, ventilatorji, klasična lepota, pokrivala za obraz, koža Ob podiranju vročinskih rekordov se vse več ljudi na Kitajskem odloči za nakup posebnega pokrivala, imenovanega "facekini". Z njim pr...

#### Rank 3: RELEVANT

- Title: Povprečna temperatura se bo v petih letih verjetno zvišala za več kot 1,5 stopinje Celzija
- Decision: relevant
- Rationale: Directly about average temperature likely rising above 1.5 C.
- Category/date: okolje / 2023-05-17T18:02:00
- URL: https://www.rtvslo.si/okolje/povprecna-temperatura-se-bo-v-petih-letih-verjetno-zvisala-za-vec-kot-1-5-stopinje-celzija/668521
- FAISS rank/score: 2 / 0.7700
- Reranker score: -1.0047
- Keywords: Temperatura, Segrevanje, Svetovna meteorološka organizacija, WMO, Povprečna temperatura, Globalno segrevanje, Podnebne spremembe, El Niño, Amazonija, Deževni gozd, Savana, Padavine, Evropa, Aljaska, Sibirija, Sahel, Podnebni znanstveniki, Preventivni ukrepi, Ogrevanje, Poročilo, Zdravje, Okolje
- Excerpt: Povprečna temperatura se bo v petih letih verjetno zvišala za več kot 1,5 stopinje Celzija Ključne besede: Temperatura, Segrevanje, Svetovna meteorološka organizacija, WMO, Povprečna temperatura, Globalno segrevanje, Podnebne spremembe, El Niño, Amazonija, Deževni gozd, Savana, Padavine, Evropa, Aljaska, Sibirija, Sahel, Podnebni znanstveniki, Preventivni ukrepi, Ogrevanje, Poročilo, Zdravje, Okolje Svetovna povprečna letna temperatura se bo v prihodnjih petih letih verjetno prvič dvignila za ve...

#### Rank 4: RELEVANT

- Title: KS 90: Tudi ob rekordnih dobičkih opažamo nedopustno varčevanje na račun zdravja delavcev
- Decision: relevant
- Rationale: About high/rising temperatures affecting workers.
- Category/date: gospodarstvo / 2024-06-18T12:15:12
- URL: https://www.rtvslo.si/gospodarstvo/ks-90-tudi-ob-rekordnih-dobickih-opazamo-nedopustno-varcevanje-na-racun-zdravja-delavcev/712162
- FAISS rank/score: 28 / 0.7441
- Reranker score: -1.0828
- Keywords: vročina, delavci, zdravje, KS90
- Excerpt: KS 90: Tudi ob rekordnih dobičkih opažamo nedopustno varčevanje na račun zdravja delavcev Ključne besede: vročina, delavci, zdravje, KS90 Konfederacija sindikatov 90 Slovenije delodajalce poziva, naj v vročih dneh za svoje delavce zagotovijo varno in zdravo delovno okolje. Kot opozarjajo, za postavljanje dobičkov pred zdravje zaposlenih "ne sme biti prav nobenega razumskega argumenta". V Konfederaciji sindikatov 90 Slovenje (KS 90) ob napovedanem vročinskem valu – temperature se bodo v prihodnih...

#### Rank 5: RELEVANT

- Title: Več kot 30 delovnih inšpektorjev preverja delovišča na prostem pri visoki temperaturi
- Decision: relevant
- Rationale: About work at high temperatures and inspection measures.
- Category/date: gospodarstvo / 2025-08-13T07:39:42
- URL: https://www.rtvslo.si/gospodarstvo/vec-kot-30-delovnih-inspektorjev-preverja-delovisca-na-prostem-pri-visoki-temperaturi/754535
- FAISS rank/score: 47 / 0.7395
- Reranker score: -1.2504
- Keywords: Varnost in zdravje, Gradbišča, Pravilnik za delo, Visoke temperature, Delovni inšpektorji
- Excerpt: Več kot 30 delovnih inšpektorjev preverja delovišča na prostem pri visoki temperaturi Ključne besede: Varnost in zdravje, Gradbišča, Pravilnik za delo, Visoke temperature, Delovni inšpektorji Delovni inšpektorji so v torek začeli izvajati usmerjene inšpekcijske nadzore glede dela na prostem pri visoki temperaturi. Julija je začel veljati nov pravilnik, ki prinaša jasna pravila glede ukrepov, ko temperatura preseže 30 stopinj Celzija. Ker je bil julij hladen in deževen, posebnih nadzorov sprva ni...


### 8. Višanje cen nepremičnin v Sloveniji

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Cene stanovanj so se lani zvišale za 8,5 odstotka
- Decision: relevant
- Rationale: Directly about rising apartment prices.
- Category/date: gospodarstvo / 2025-03-24T11:15:44
- URL: https://www.rtvslo.si/gospodarstvo/cene-stanovanj-so-se-lani-zvisale-za-8-5-odstotka/740422
- FAISS rank/score: 11 / 0.8010
- Reranker score: 6.7813
- Keywords: Nove družinske hiše, Rabljena stanovanja, Prodaja nepremičnin, Zvišanje cen, Cene stanovanj
- Excerpt: Cene stanovanj so se lani zvišale za 8,5 odstotka Ključne besede: Nove družinske hiše, Rabljena stanovanja, Prodaja nepremičnin, Zvišanje cen, Cene stanovanj Cene stanovanjskih nepremičnin v Sloveniji so se lani zvišale deseto leto zapored, tokrat za 8,5 odstotka. Skupaj je bilo prodanih za približno 1,3 milijarde evrov stanovanjskih nepremičnin, kar je 14,7 odstotka manj kot leto prej. Lani se je zmanjšalo tudi število transakcij s stanovanjskimi nepremičninami. Potem ko je leta 2023 novega las...

#### Rank 2: RELEVANT

- Title: Gurs: V Sloveniji lani prodanih manj hiš in stanovanj. Cene zrasle za devet oz. deset odstotkov.
- Decision: relevant
- Rationale: Directly about Slovenian house/apartment prices rising.
- Category/date: gospodarstvo / 2025-04-15T06:31:30
- URL: https://www.rtvslo.si/gospodarstvo/gurs-v-sloveniji-lani-prodanih-manj-his-in-stanovanj-cene-zrasle-za-devet-oz-deset-odstotkov/742731
- FAISS rank/score: 8 / 0.8081
- Reranker score: 6.7633
- Keywords: Cene stanovanj, Nepremičninski trg, Gurs
- Excerpt: Gurs: V Sloveniji lani prodanih manj hiš in stanovanj. Cene zrasle za devet oz. deset odstotkov. Ključne besede: Cene stanovanj, Nepremičninski trg, Gurs Po podatkih Gursa je lani precej upadla prodaja vseh vrst nepremičnin. Na drugi strani pa so se denimo v Ljubljani cene stanovanj zvišale za kar 500 evrov/m2. "Povpraševanje še vedno močno presega ponudbo," pravi Boštjan Udovič iz GZS-ja. Geodetska uprava (Gurs) je na začetku aprila objavila poročilo o slovenskem nepremičninskem trgu za leto 20...

#### Rank 3: RELEVANT

- Title: Prodaja nepremičnin upada, cene pa še naprej rastejo
- Decision: relevant
- Rationale: Directly about real estate sales falling while prices rise.
- Category/date: gospodarstvo / 2024-12-23T15:25:02
- URL: https://www.rtvslo.si/gospodarstvo/prodaja-nepremicnin-upada-cene-pa-se-naprej-rastejo/731459
- FAISS rank/score: 3 / 0.8166
- Reranker score: 5.3918
- Keywords: nepremičnine, prodaja, cene
- Excerpt: Prodaja nepremičnin upada, cene pa še naprej rastejo Ključne besede: nepremičnine, prodaja, cene Prodaja stanovanjskih nepremičnin v Sloveniji upada. V tretjem četrtletju je bilo prodanih celo najmanj rabljenih nepremičnin v zadnjih 14 letih. Cene nepremičnin medtem še naprej rastejo, najbolj prav za rabljena stanovanja in hiše. Po izračunih Statističnega urada RS (Surs) je bilo v tretjem četrtletju letošnjega leta skupno prodnih 1737 stanovanjskih nepremičnin. To je 16 odstotkov manj kot v četr...

#### Rank 4: RELEVANT

- Title: Lani rekordne cene nepremičnin, a nepremičninski trg se ohlaja
- Decision: relevant
- Rationale: Directly about record real estate prices in Slovenia.
- Category/date: slovenija / 2023-03-31T17:33:00
- URL: https://www.rtvslo.si/slovenija/lani-rekordne-cene-nepremicnin-a-nepremicninski-trg-se-ohlaja/663341
- FAISS rank/score: 2 / 0.8176
- Reranker score: 5.2698
- Keywords: nepremičnine, stanovanja, hiše, prodaja, nepremičninski trg, cene, Gurs, rast, trg, Slovenija, rekord, zemljišča, Geodetska uprava RS, Ljubljana, Obala, alpsko turistično območje, Kranjska Gora, Bled, Bohinjsko jezero, cene kvadratnega metra, povprečje, Kranj, Medvode, Domžale, Kamnik, Grosuplje, Vrhnika, Logatec, Gorenjska, Novo mesto, nova Gorica, Vipavska dolina, Goriška brda, Bela krajina, Prekmurje.
- Excerpt: Lani rekordne cene nepremičnin, a nepremičninski trg se ohlaja Ključne besede: nepremičnine, stanovanja, hiše, prodaja, nepremičninski trg, cene, Gurs, rast, trg, Slovenija, rekord, zemljišča, Geodetska uprava RS, Ljubljana, Obala, alpsko turistično območje, Kranjska Gora, Bled, Bohinjsko jezero, cene kvadratnega metra, povprečje, Kranj, Medvode, Domžale, Kamnik, Grosuplje, Vrhnika, Logatec, Gorenjska, Novo mesto, nova Gorica, Vipavska dolina, Goriška brda, Bela krajina, Prekmurje. Cene stanovan...

#### Rank 5: RELEVANT

- Title: Lani cene stanovanjskih hiš zrasle za devet odstotkov, cene stanovanj za deset odstotkov
- Decision: relevant
- Rationale: Directly about house and apartment prices rising.
- Category/date: gospodarstvo / 2025-04-01T18:17:30
- URL: https://www.rtvslo.si/gospodarstvo/lani-cene-stanovanjskih-his-zrasle-za-devet-odstotkov-cene-stanovanj-za-deset-odstotkov/741359
- FAISS rank/score: 10 / 0.8050
- Reranker score: 3.7431
- Keywords: Prodaja zemljišč, Srednja cena, Nepremičninski trg, Rast cen, Cene stanovanj
- Excerpt: Lani cene stanovanjskih hiš zrasle za devet odstotkov, cene stanovanj za deset odstotkov Ključne besede: Prodaja zemljišč, Srednja cena, Nepremičninski trg, Rast cen, Cene stanovanj Lani je na slovenskem nepremičninskem trgu tretje leto zaporedoma upadalo število kupoprodaj nepremičnin, medtem ko so cene še naprej rasle. GURS zmanjšanje pripisuje vladnim napovedim glede obdavčitve premoženja. Rast cen stanovanjskih nepremičnin in zemljišč za njihovo gradnjo lani po navedbah Geodetske uprave RS s...


### 9. Rogljič in Pogačar na tekmi

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Pogačar se bo v soboto prvič predstavil v mavrični majici
- Decision: relevant
- Rationale: About Pogacar appearing/racing; cycling context is related.
- Category/date: sport / 2024-10-04T08:00:52
- URL: https://www.rtvslo.si/sport/kolesarstvo/pogacar-se-bo-v-soboto-prvic-predstavil-v-mavricni-majici/723155
- FAISS rank/score: 2 / 0.7809
- Reranker score: 6.4199
- Keywords: Tadej Pogačar, Primož Roglič, Remco Evenepoel
- Excerpt: Pogačar se bo v soboto prvič predstavil v mavrični majici Ključne besede: Tadej Pogačar, Primož Roglič, Remco Evenepoel Svetovni prvak Tadej Pogačar bo v mavrični majici prvič kolesaril v soboto na dirki Giro dell'Emilia v Italiji, kjer bosta tekmovala tudi Primož Roglič in Remco Evenepoel. 107. izvedba italijanske klasike, ki sicer ni del svetovne serije, bo za kolesarje priprava za zadnjo veliko dirko sezone – Dirko po Lombardiji. Zadnja izmed petih"klasik" bo na sporedu v soboto, 12. oktobra....

#### Rank 2: RELEVANT

- Title: Na Emiliji in Lombardiji prvo in drugo letošnje soočenje Pogačarja in Rogliča
- Decision: relevant
- Rationale: Directly about Pogacar and Roglic competing/meeting.
- Category/date: sport / 2023-09-18T20:40:51
- URL: https://www.rtvslo.si/sport/kolesarstvo/na-emiliji-in-lombardiji-prvo-in-drugo-letosnje-soocenje-pogacarja-in-roglica/681833
- FAISS rank/score: 1 / 0.7881
- Reranker score: 6.3328
- Keywords: kolesarstvo, Dirka po Lombardiji, Tadej Pogačar, Primož Roglič, Marc Hirschi, ekipa UAE, slovenski državni prvak, Joxean Matxin Fernandez, Dirka po Emiliji, Dirka tri doline Vareseja, Vuelta, San Luco, Bologna, Dirka po Franciji, 2024, tritedenske dirke, enodnevne dirke, Madrid, kraljevska etapa, Angliru, Remco Evenepoel
- Excerpt: Na Emiliji in Lombardiji prvo in drugo letošnje soočenje Pogačarja in Rogliča Ključne besede: kolesarstvo, Dirka po Lombardiji, Tadej Pogačar, Primož Roglič, Marc Hirschi, ekipa UAE, slovenski državni prvak, Joxean Matxin Fernandez, Dirka po Emiliji, Dirka tri doline Vareseja, Vuelta, San Luco, Bologna, Dirka po Franciji, 2024, tritedenske dirke, enodnevne dirke, Madrid, kraljevska etapa, Angliru, Remco Evenepoel Tadej Pogačar je ob Marcu Hirschiju iz ekipe UAE že na startni listi Dirke po Lomba...

#### Rank 3: RELEVANT

- Title: Pogačar zanesljivo vodi, Roglič skočil na peto mesto
- Decision: relevant
- Rationale: Directly about Pogacar and Roglic in a race ranking.
- Category/date: sport / 2024-09-10T12:25:18
- URL: https://www.rtvslo.si/sport/kolesarstvo/pogacar-zanesljivo-vodi-roglic-skocil-na-peto-mesto/720571
- FAISS rank/score: 7 / 0.7684
- Reranker score: 5.5761
- Keywords: kolesarstvo, Tadej Pogačar, Primož Roglič
- Excerpt: Pogačar zanesljivo vodi, Roglič skočil na peto mesto Ključne besede: kolesarstvo, Tadej Pogačar, Primož Roglič Tadej Pogačar (UAE Emirates) je še naprej prepričljivo vodilni na lestvici Mednarodne kolesarske zveze UCI, na peto mesto pa se je prebil zmagovalec Dirke po Španiji Primož Roglič (Red Bull Bora Hansgrohe). 25-letni slovenski as je vodilni na lestvici nepretrgoma vse od 28. septembra 2021, od takrat pa je nanizal 153 tednov na vrhu. Skupaj jih ima v karieri že 163 in je tudi v tem pogle...

#### Rank 4: RELEVANT

- Title: Pogačar zanesljivo vodi, Roglič skočil na peto mesto
- Decision: relevant
- Rationale: Duplicate but still directly about Pogacar and Roglic in a race ranking.
- Category/date: sport / 2024-09-10T12:25:18
- URL: https://www.rtvslo.si/sport/kolesarstvo/pogacar-zanesljivo-vodi-roglic-po-zmagi-na-vuelti-skocil-na-peto-mesto/720571
- FAISS rank/score: 8 / 0.7684
- Reranker score: 5.5761
- Keywords: kolesarstvo, Tadej Pogačar, Primož Roglič
- Excerpt: Pogačar zanesljivo vodi, Roglič skočil na peto mesto Ključne besede: kolesarstvo, Tadej Pogačar, Primož Roglič Tadej Pogačar (UAE Emirates) je še naprej prepričljivo vodilni na lestvici Mednarodne kolesarske zveze UCI, na peto mesto pa se je prebil zmagovalec Dirke po Španiji Primož Roglič (Red Bull Bora Hansgrohe). 25-letni slovenski as je vodilni na lestvici nepretrgoma vse od 28. septembra 2021, od takrat pa je nanizal 153 tednov na vrhu. Skupaj jih ima v karieri že 163 in je tudi v tem pogle...

#### Rank 5: RELEVANT

- Title: Pogačar utrdil vodstvo, Roglič napredoval na 6. mesto
- Decision: relevant
- Rationale: Directly about Pogacar and Roglic in a race ranking.
- Category/date: sport / 2025-07-29T10:33:18
- URL: https://www.rtvslo.si/sport/kolesarstvo/pogacar-utrdil-vodstvo-roglic-napredoval-na-6-mesto/753192
- FAISS rank/score: 16 / 0.7641
- Reranker score: 5.0963
- Keywords: kolesarstvo, UCI-lestvica, Tadej Pogačar, Primož Roglič
- Excerpt: Pogačar utrdil vodstvo, Roglič napredoval na 6. mesto Ključne besede: kolesarstvo, UCI-lestvica, Tadej Pogačar, Primož Roglič 201 zaporedni teden že ni bilo menjave na vrhu UCI-lestvice. S četrto osvojitvijo Dirke po Franciji je Tadej Pogačar še utrdil vodstvo, saj ima zdaj pred drugouvrščenim Madsom Pedersenom skoraj sedem tisoč točk prednosti. Primož Roglič je zdaj 6. Na posodobljeni lestvici Mednarodne kolesarske zveze ima zdaj Tadej Pogačar 11.465 točk, njegov novi prvi zasledovalec pa je ko...


### 10. Donald Trump novi zakoni

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Trump najprej uvedel nove 10-odstotne carine, nato jih je dvignil na 15 odstotkov
- Decision: relevant
- Rationale: About Trump introducing new tariffs/policy.
- Category/date: svet / 2026-02-21T09:59:57
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/trump-najprej-uvedel-nove-10-odstotne-carine-nato-jih-je-dvignil-na-15-odstotkov/774153
- FAISS rank/score: 1 / 0.8066
- Reranker score: 3.8402
- Keywords: Zakon o trgovini, Uvoz, Vrhovno sodišče, Carine, Trump
- Excerpt: Trump najprej uvedel nove 10-odstotne carine, nato jih je dvignil na 15 odstotkov Ključne besede: Zakon o trgovini, Uvoz, Vrhovno sodišče, Carine, Trump Ameriški predsednik Donald Trump je v petek ostro kritiziral sodnike vrhovnega sodišča, ki so razveljavili njegove t. i. vzajemne carine. Takoj je podpisal izvršni ukaz in uvedel nove splošne 10-odstotne carine, nato pa jih je povišal na 15 odstotkov. V odzivu na odločitev vrhovnega sodišča je Donald Trump napovedal, da bo nemudoma podpisal ukaz...

#### Rank 2: RELEVANT

- Title: Trump z novim zakonom uvedel višje kazni za trgovino s fentanilom
- Decision: relevant
- Rationale: Directly about a new law signed/introduced by Trump.
- Category/date: svet / 2025-07-17T10:37:53
- URL: https://www.rtvslo.si/svet/preberite-tudi/trump-z-novim-zakonom-uvedel-visje-kazni-za-trgovino-s-fentanilom/752186
- FAISS rank/score: 2 / 0.8051
- Reranker score: 3.8147
- Keywords: Nezakonito, Trgovina, Višje kazni, Fentanil, Trump
- Excerpt: Trump z novim zakonom uvedel višje kazni za trgovino s fentanilom Ključne besede: Nezakonito, Trgovina, Višje kazni, Fentanil, Trump Ameriški predsednik Donald Trump je v sredo podpisal zakon, ki sintetično drogo fentanil uvršča med najhujša prepovedana mamila v ZDA. Ob podpisu zakona je dejal, da bodo s tem zadali velik udarec mamilarskim kartelom, saj so za trgovino s fentanilom zdaj predvidene višje kazni. Fentanil je sredstvo, ki ga ameriški zdravniki včasih predpisujejo za lajšanje hudih bo...

#### Rank 3: RELEVANT

- Title: Trump od sodišča zahteva odložitev zakona o prepovedi TikToka v ZDA
- Decision: relevant
- Rationale: About Trump and a law banning TikTok.
- Category/date: svet / 2024-12-28T09:22:40
- URL: https://www.rtvslo.si/svet/preberite-tudi/trump-od-sodisca-zahteva-odlozitev-zakona-o-prepovedi-tiktoka-v-zda/731796
- FAISS rank/score: 34 / 0.7760
- Reranker score: 2.5917
- Keywords: Vrhovno sodišče, Prepoved, TikTok, Trump
- Excerpt: Trump od sodišča zahteva odložitev zakona o prepovedi TikToka v ZDA Ključne besede: Vrhovno sodišče, Prepoved, TikTok, Trump Novoizvoljeni ameriški predsednik Donald Trump je v petek od ameriškega vrhovnega sodišča zahteval, naj odloži zakon o prepovedi poslovanja družbenega omrežja TikTok v ZDA, če ga kitajsko matično podjetje ByteDance ne bo prodalo. Trump meni, da bi lahko nadaljevanje pogajanj rešilo TikTok in hkrati obravnavalo vprašanja nacionalne varnosti. Trumpov odvetnik je v petek sodi...

#### Rank 4: RELEVANT

- Title: Začele so veljati nove ameriške carine, ki bodo sprva 10-odstotne. Veljale bodo 150 dni.
- Decision: relevant
- Rationale: About new US tariffs linked to Trump policy context.
- Category/date: gospodarstvo / 2026-02-24T10:37:01
- URL: https://www.rtvslo.si/gospodarstvo/zacele-so-veljati-nove-ameriske-carine-ki-bodo-sprva-10-odstotne-veljale-bodo-150-dni/774404
- FAISS rank/score: 11 / 0.7902
- Reranker score: 2.2000
- Keywords: ZDA, Donald Trump, Carine
- Excerpt: Začele so veljati nove ameriške carine, ki bodo sprva 10-odstotne. Veljale bodo 150 dni. Ključne besede: ZDA, Donald Trump, Carine Z današnjim dnem so začele veljati nove ameriške carine, ki jih je v petek v odzivu na razveljavitev lani uvedenih carin napovedal predsednik ZDA Donald Trump. Carine bodo sprva 10-, in ne 15-odstotne, kot je v soboto napovedal Trump. Ameriško vrhovno sodišče je v petek s šestimi glasovi proti trem razveljavilo carine, ki jih je Trump aprila lani uvedel na podlagi za...

#### Rank 5: RELEVANT

- Title: S Trumpovim podpisom končana delna blokada ameriške vlade
- Decision: relevant
- Rationale: About Trump signing a measure ending a government shutdown.
- Category/date: svet / 2026-02-04T07:05:07
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/s-trumpovim-podpisom-koncana-delna-blokada-ameriske-vlade/772270
- FAISS rank/score: 3 / 0.8029
- Reranker score: 2.0911
- Keywords: ZDA, Donald Trump, financiranje vlade
- Excerpt: S Trumpovim podpisom končana delna blokada ameriške vlade Ključne besede: ZDA, Donald Trump, financiranje vlade Ameriški predsednik Donald Trump je podpisal zakone o nadaljevanju financiranja agencij svoje vlade, potem ko jih je nekaj ur prej tesno z 217 proti 214 glasovom potrdil predstavniški dom kongresa, s čimer se je po štirih dneh končala delna blokada vlade. Že lani je bilo potrjenih šest zakonov o proračunski porabi za razna ministrstva, tokrat jih je bilo prav tako do konca proračunskeg...


### 11. Evropska Unija in zveza NATO

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Se bodo višji obrambni izdatki, ki jih načrtuje EU, porabljali po Natovih pravilih?
- Decision: relevant
- Rationale: Directly connects EU defence spending and NATO rules.
- Category/date: slovenija / 2025-03-20T06:11:03
- URL: https://www.rtvslo.si/slovenija/se-bodo-visji-obrambni-izdatki-ki-jih-nacrtuje-eu-porabljali-po-natovih-pravilih/739846
- FAISS rank/score: 43 / 0.7352
- Reranker score: 1.2649
- Keywords: Kolektivna obramba, Vojaška zmogljivost, Strateški zaveznik, Evropska unija, Obrambni izdatki
- Excerpt: Se bodo višji obrambni izdatki, ki jih načrtuje EU, porabljali po Natovih pravilih? Ključne besede: Kolektivna obramba, Vojaška zmogljivost, Strateški zaveznik, Evropska unija, Obrambni izdatki EU namerava z zaveznicami, kot so Norveška, Združeno kraljestvo in morda tudi Kanada, znotraj Nata vzpostaviti "evropski obrambni steber", meni obramboslovec Klemen Grošelj in poudarja, da bodo višji obrambni izdatki namenjeni predvsem oboroževanju. Evropska komisija v načrtu za okrepitev evropske varnost...

#### Rank 2: RELEVANT

- Title: Rutte: Nato je danes močnejši kot kdaj koli prej
- Decision: relevant
- Rationale: About NATO strength and alliance context.
- Category/date: svet / 2026-03-26T17:52:49
- URL: https://www.rtvslo.si/svet/evropa/rutte-nato-je-danes-mocnejsi-kot-kdaj-koli-prej/777638
- FAISS rank/score: 13 / 0.7530
- Reranker score: 1.0388
- Keywords: BDP, Povečanje, Mark Rutte, Obrambni izdatki, Nato
- Excerpt: Rutte: Nato je danes močnejši kot kdaj koli prej Ključne besede: BDP, Povečanje, Mark Rutte, Obrambni izdatki, Nato Evropske članice zveze Nato in Kanada so lani proračunske izdatke za obrambo v primerjavi z letom 2024 povečale za 20 odstotkov, je ob predstavitvi letnega poročila za 2025 sporočil generalni sekretar zavezništva Mark Rutte. "Številke v poročilu govorijo same zase. Naredili smo bistven napredek na področju obrambnih naložb in Nato je danes močnejši kot kdaj koli prej. Leta 2025 so...

#### Rank 3: RELEVANT

- Title: Rutte: Če mislite, da se lahko Evropa brani sama, kar sanjajte naprej
- Decision: relevant
- Rationale: Directly about Europe and NATO defence.
- Category/date: svet / 2026-01-26T18:46:29
- URL: https://www.rtvslo.si/svet/rutte-ce-mislite-da-se-lahko-evropa-brani-sama-kar-sanjajte-naprej/771341
- FAISS rank/score: 1 / 0.7736
- Reranker score: 1.0117
- Keywords: ZDA, Nato, Mark Rutte
- Excerpt: Rutte: Če mislite, da se lahko Evropa brani sama, kar sanjajte naprej Ključne besede: ZDA, Nato, Mark Rutte Evropa se ne more braniti brez ZDA, potrebujemo drug drugega, je ob zadnjih napetosti v čezatlantskih odnosih dejal generalni sekretar zveze Nato Mark Rutte. "Kar sanjajte naprej," je odvrnil tistim, ki menijo, da se lahko Evropa brani sama. " Če kdor koli tu misli, da se lahko Evropska unija ali Evropa kot celota brani brez ZDA, naj kar sanja naprej. Tega ne morete, tega ne moremo, potreb...

#### Rank 4: RELEVANT

- Title: Poročilo Nata: Kanada in evropske članice v lanskem letu občutno povečale izdatke za obrambo
- Decision: relevant
- Rationale: About NATO report and European/Canadian defence spending.
- Category/date: gospodarstvo / 2025-04-27T16:31:02
- URL: https://www.rtvslo.si/gospodarstvo/porocilo-nata-kanada-in-evropske-clanice-v-lanskem-letu-obcutno-povecale-izdatke-za-obrambo/744053
- FAISS rank/score: 11 / 0.7552
- Reranker score: 0.8555
- Keywords: Vojaška analiza, BDP cilj, NATO zavezništvo, Obrambni izdatki, Ruska agresija
- Excerpt: Poročilo Nata: Kanada in evropske članice v lanskem letu občutno povečale izdatke za obrambo Ključne besede: Vojaška analiza, BDP cilj, NATO zavezništvo, Obrambni izdatki, Ruska agresija Nato je dva meseca pred srečanjem voditeljev objavil poročilo generalnega sekretarja, ki med drugim prikazuje tudi porabo obrambnih izdatkov članic. Kanada in evropske članice so v letu 2024 občutno povečale izdatke za obrambo. Slovenija ostaja pri repu. Ruska agresija na Ukrajino je številne članice zveze NATO,...

#### Rank 5: RELEVANT

- Title: ZDA dve visoki poveljništvi v Natu predajajo Evropi
- Decision: relevant
- Rationale: About NATO command transfer to Europe.
- Category/date: svet / 2026-02-10T10:47:55
- URL: https://www.rtvslo.si/svet/s-in-j-amerika/zda-dve-visoki-poveljnistvi-v-natu-predajajo-evropi/772949
- FAISS rank/score: 20 / 0.7490
- Reranker score: 0.8080
- Keywords: ZDA, Reorganizacija, Evropa, Poveljništvo, NATO
- Excerpt: ZDA dve visoki poveljništvi v Natu predajajo Evropi Ključne besede: ZDA, Reorganizacija, Evropa, Poveljništvo, NATO ZDA bodo predale dva visoka poveljniška položaja v zvezi Nato, in sicer poveljstvi v Neaplju in Norfolku v ameriški zvezni državi Virginia, ki jih bosta zasedla poveljnika iz Italije in Velike Britanije. "Zaveznice so se strinjale z novo razporeditvijo visokih položajev v strukturi zavezništva, v kateri bodo imele evropske zaveznice (...) večjo vlogo pri vojaškem vodenju," je dejal...


### 12. Velika Britanija Brexit

Precision@5: 4/5 = 0.80

#### Rank 1: RELEVANT

- Title: Velika Britanija prva evropska država v transpacifiškem prostotrgovinskem partnerstvu
- Decision: relevant
- Rationale: About the UK joining a trade partnership in the post-Brexit trade context.
- Category/date: gospodarstvo / 2023-03-31T14:52:00
- URL: https://www.rtvslo.si/gospodarstvo/velika-britanija-prva-evropska-drzava-v-transpacifiskem-prostotrgovinskem-partnerstvu/663314
- FAISS rank/score: 2 / 0.7919
- Reranker score: 2.5412
- Keywords: Velika Britanija, CPTPP, transpacifiško prostotrgovinsko partnerstvo, transpacifiško partnerstvo, brexit, prostotrgovinski dogovor, gospodarske koristi, Rishi Sunak, Evropska unija, trgovinski bloki, Obama, Donald Trump, Kitajska, Japonska, Avstralija, Kanada, Nova Zelandija, Mehika, Južna Koreja, Tajvan, pridružitev
- Excerpt: Velika Britanija prva evropska država v transpacifiškem prostotrgovinskem partnerstvu Ključne besede: Velika Britanija, CPTPP, transpacifiško prostotrgovinsko partnerstvo, transpacifiško partnerstvo, brexit, prostotrgovinski dogovor, gospodarske koristi, Rishi Sunak, Evropska unija, trgovinski bloki, Obama, Donald Trump, Kitajska, Japonska, Avstralija, Kanada, Nova Zelandija, Mehika, Južna Koreja, Tajvan, pridružitev Velika Britanija se bo po dveh letih pogajanj pridružila Celostnemu in napredne...

#### Rank 2: NOT RELEVANT

- Title: Britanci bodo zaostrili izdajanje vizumov, da bi zmanjšali priseljevanje
- Decision: not_relevant
- Rationale: About UK visas/immigration, not substantially about Brexit.
- Category/date: svet / 2023-12-05T09:17:17
- URL: https://www.rtvslo.si/svet/evropa/britanci-bodo-zaostrili-izdajanje-vizumov-da-bi-zmanjsali-priseljevanje/690539
- FAISS rank/score: 3 / 0.7727
- Reranker score: 2.0683
- Keywords: Velika Britanija, migracije, priseljevanje, tuji delavci, zakonito priseljevanje, nezakonito priseljevanje, minimalna plača, vizumi, družinski člani, politika, Evropska unija, brexit, neto migracije, Indija, Nigerija, Kitajska, premier, nadzor, javni zdravstveni sistem, notranji minister
- Excerpt: Britanci bodo zaostrili izdajanje vizumov, da bi zmanjšali priseljevanje Ključne besede: Velika Britanija, migracije, priseljevanje, tuji delavci, zakonito priseljevanje, nezakonito priseljevanje, minimalna plača, vizumi, družinski člani, politika, Evropska unija, brexit, neto migracije, Indija, Nigerija, Kitajska, premier, nadzor, javni zdravstveni sistem, notranji minister Velika Britanija se bo zaradi množičnega priseljevanja poleg nezakonitih migracij lotila tudi prihodov priseljencev po zak...

#### Rank 3: RELEVANT

- Title: Brexit je postal težava za e-mobilnost
- Decision: relevant
- Rationale: Directly about Brexit and e-mobility.
- Category/date: zabava-in-slog / 2023-06-05T07:45:00
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/brexit-je-postal-tezava-za-e-mobilnost/670651
- FAISS rank/score: 5 / 0.7621
- Reranker score: 1.6728
- Keywords: Brexit, Stellantis, carina, električni avtomobili, Velika Britanija, dajatve na izvoz, avtomobilska industrija, Aston Martin Lagonda, Unite, Carlos Tavares, električna vozila, BMW, Kitajska, Opel/Vauxhall, Ellesmere Port, dostavna vozila, investicije, zaposlovanje, gospodarstvo, kriza, blagovne znamke
- Excerpt: Brexit je postal težava za e-mobilnost Ključne besede: Brexit, Stellantis, carina, električni avtomobili, Velika Britanija, dajatve na izvoz, avtomobilska industrija, Aston Martin Lagonda, Unite, Carlos Tavares, električna vozila, BMW, Kitajska, Opel/Vauxhall, Ellesmere Port, dostavna vozila, investicije, zaposlovanje, gospodarstvo, kriza, blagovne znamke Morebitne dajatve na izvoz električnih avtomobilov iz Velike Britanije vznemirjajo avtomobilske proizvajalce. Stellantis odkrito grozi z zaprt...

#### Rank 4: RELEVANT

- Title: Brexit pričakovanj ni upravičil, britanska javnost pa ga skoraj ne omenja več
- Decision: relevant
- Rationale: Directly about Brexit expectations and public opinion.
- Category/date: svet / 2025-01-31T06:20:23
- URL: https://www.rtvslo.si/svet/evropa/brexit-pricakovanj-ni-upravicil-britanska-javnost-pa-ga-skoraj-ne-omenja-vec/735075
- FAISS rank/score: 1 / 0.8255
- Reranker score: 1.5294
- Keywords: Gospodarske posledice, Evropska unija, Združeno kraljestvo, Brexit, Jan Grobovšek
- Excerpt: Brexit pričakovanj ni upravičil, britanska javnost pa ga skoraj ne omenja več Ključne besede: Gospodarske posledice, Evropska unija, Združeno kraljestvo, Brexit, Jan Grobovšek Pred petimi leti je Združeno kraljestvo izstopilo iz Evropske unije. Ekonomist z univerze v Edinburgu Jan Grobovšek pravi, da je s tem država dobila "najslabše od obeh svetov" – postala je manjše gospodarstvo in ni ujela gospodarskih priložnosti. Združeno kraljestvo je 31. januarja 2020 po 47 letih članstva kot prva članic...

#### Rank 5: RELEVANT

- Title: Velika Britanija hoče preoblikovati severnoirski protokol
- Decision: relevant
- Rationale: About the Northern Ireland protocol, a Brexit-related issue.
- Category/date: svet / 2021-07-21T18:44:51
- URL: https://www.rtvslo.si/svet/evropa/velika-britanija-hoce-preoblikovati-severnoirski-protokol/588379
- FAISS rank/score: 6 / 0.7606
- Reranker score: 1.3238
- Keywords: Brexit, Velika Britanija, Bruselj, Britanska vlada, Evropska unija, Severnoirski protokol, Irski otok, Brandon Lewis, Parlament, London, Blago, Združeno kraljestvo, Enotni trg, David Frost, Gospodarska škoda, Severna Irska, Protesti, Maroš Šefčovič, Evropska komisija, Izstopni sporazum, Odbor
- Excerpt: Velika Britanija hoče preoblikovati severnoirski protokol Ključne besede: Brexit, Velika Britanija, Bruselj, Britanska vlada, Evropska unija, Severnoirski protokol, Irski otok, Brandon Lewis, Parlament, London, Blago, Združeno kraljestvo, Enotni trg, David Frost, Gospodarska škoda, Severna Irska, Protesti, Maroš Šefčovič, Evropska komisija, Izstopni sporazum, Odbor Britanska vlada se želi z Evropsko unijo znova pogajati o severnoirskem protokolu in ga spremeniti. Pozvala je tudi k moratoriju za...


### 13. Vojna v Ukrajini in Zelenski

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Zelenski obiskal vojake na fronti v Donecku in jim podelil medalje
- Decision: relevant
- Rationale: Directly about Zelensky visiting soldiers on the Ukrainian front.
- Category/date: svet / 2023-06-26T13:32:11
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-obiskal-vojake-na-fronti-v-donecku-in-jim-podelil-medalje/673117
- FAISS rank/score: 27 / 0.7939
- Reranker score: 9.3015
- Keywords: Ukrajina, vojna, Volodimir Zelenski, protiofenziva, ukrajinski, predsednik, vojaki, fronta, Doneck, Rusija, ofenziva, sile, spopadi, medalje, vojska, preboj, Moskva, obrambni minister, minister, teritorialne, Siberija, Krim.
- Excerpt: Zelenski obiskal vojake na fronti v Donecku in jim podelil medalje Ključne besede: Ukrajina, vojna, Volodimir Zelenski, protiofenziva, ukrajinski, predsednik, vojaki, fronta, Doneck, Rusija, ofenziva, sile, spopadi, medalje, vojska, preboj, Moskva, obrambni minister, minister, teritorialne, Siberija, Krim. Ukrajinski predsednik Volodimir Zelenski je obiskal ukrajinske vojake na fronti v Donecku na vzhodu Ukrajine, ki je delno še vedno pod nadzorom ruskih sil. Ukrajinske sile pa naj bi med protio...

#### Rank 2: RELEVANT

- Title: Zelenski: V Rusijo prihaja vojna. Papež pozval k obnovitvi sporazuma o žitu.
- Decision: relevant
- Rationale: Directly about Zelensky and war with Russia/Ukraine.
- Category/date: svet / 2023-07-30T09:43:53
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-v-rusijo-prihaja-vojna-papez-pozval-k-obnovitvi-sporazuma-o-zitu/676560
- FAISS rank/score: 10 / 0.8015
- Reranker score: 9.2562
- Keywords: vojna v Ukrajini, Vladimir Putin, pogajanja, Ukrajina, Rusija, napadi, vojna, letalniki, predsednik, obramba, teroristi, energetska infrastruktura, napad, uničenje, umrli, ranjeni, raketa, ruske sile, Sumi, Zaporožje, Ministrstvo, BBC
- Excerpt: Zelenski: V Rusijo prihaja vojna. Papež pozval k obnovitvi sporazuma o žitu. Ključne besede: vojna v Ukrajini, Vladimir Putin, pogajanja, Ukrajina, Rusija, napadi, vojna, letalniki, predsednik, obramba, teroristi, energetska infrastruktura, napad, uničenje, umrli, ranjeni, raketa, ruske sile, Sumi, Zaporožje, Ministrstvo, BBC V napadih po Ukrajini so bili ponoči ubiti najmanj trije ljudje, Rusija pa je nad Moskvo sestrelila ukrajinske letalnike. Ukrajinski predsednik Zelenski je dejal, da so nap...

#### Rank 3: RELEVANT

- Title: Zelenski: Bližje smo miru in koncu vojne, kot si mislimo
- Decision: relevant
- Rationale: Directly about Zelensky, peace and end of the war.
- Category/date: svet / 2024-09-24T08:53:42
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-blizje-smo-miru-in-koncu-vojne-kot-si-mislimo/721990
- FAISS rank/score: 13 / 0.7993
- Reranker score: 8.5168
- Keywords: Ukrajina, Rusija, vojna
- Excerpt: Zelenski: Bližje smo miru in koncu vojne, kot si mislimo Ključne besede: Ukrajina, Rusija, vojna "Mislim, da smo bližje miru, kot si mislimo. Blizu smo koncu vojne," je med obiskom v ZDA dejal ukrajinski predsednik Volodimir Zelenski, ki bo konec tedna Washingtonu predstavil svoj "načrt zmage". "Zdaj, ko se približuje konec leta, imamo resnično priložnost za okrepitev sodelovanja med Ukrajino in ZDA," je po srečanju z dvostrankarsko delegacijo ameriškega kongresa dejal Zelenski in izrazil prepri...

#### Rank 4: RELEVANT

- Title: Zelenski se je srečal z vojaki, ki se borijo v Kursku: Ukrajinci so lahko močnejši od sovražnika
- Decision: relevant
- Rationale: Directly about Zelensky and Ukrainian soldiers fighting in Kursk.
- Category/date: svet / 2024-10-04T09:53:55
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-se-je-srecal-z-vojaki-ki-se-borijo-v-kursku-ukrajinci-so-lahko-mocnejsi-od-sovraznika/723177
- FAISS rank/score: 6 / 0.8026
- Reranker score: 8.5141
- Keywords: Ukrajina, Rusija, vojna, Vugledar, Pokrovsk
- Excerpt: Zelenski se je srečal z vojaki, ki se borijo v Kursku: Ukrajinci so lahko močnejši od sovražnika Ključne besede: Ukrajina, Rusija, vojna, Vugledar, Pokrovsk Ukrajinski predsednik Volodimir Zelenski je sporočil, da je obiskal Sumsko oblast ob meji z Rusijo in se srečal z vojaki, ki sodelujejo v ofenzivi v ruski obmejni Kurski oblasti. Zelenski se je srečal z vojaki iz 82. zračno-jurišne brigade, ki se bori v Rusiji, in se seznanil s poročilom njenega poveljnika Dmitra Vološina, ki je govoril o op...

#### Rank 5: RELEVANT

- Title: Zelenski napovedal vojaške okrepitve. Ukrajina napadla rusko naftno infrastrukturo.
- Decision: relevant
- Rationale: Directly about Zelensky, Ukrainian military reinforcements and attacks.
- Category/date: svet / 2025-08-15T16:59:38
- URL: https://www.rtvslo.si/svet/vojna-v-ukrajini/zelenski-napovedal-vojaske-okrepitve-ukrajina-napadla-rusko-naftno-infrastrukturo/754789
- FAISS rank/score: 18 / 0.7973
- Reranker score: 8.3200
- Keywords: Napad z droni, Ruske sile, Vzhod Ukrajine, Vojaške okrepitve, Zelenski
- Excerpt: Zelenski napovedal vojaške okrepitve. Ukrajina napadla rusko naftno infrastrukturo. Ključne besede: Napad z droni, Ruske sile, Vzhod Ukrajine, Vojaške okrepitve, Zelenski Ukrajinski predsednik Volodimir Zelenski je dejal, da bo ukrajinska vojska poslala dodatne okrepitve na vzhod države, kjer so ruske sile v preteklih dneh hitro napredovale proti mestu Dobropilja. "Danes je bila sprejeta odločitev, da se območje Dobropilje in druga območja v Doneški oblasti dodatno okrepijo," je Zelenski dejal n...


### 14. Kitajska proti ZDA

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Kitajska po napovedi novih ameriških carin zagrozila s protiukrepi
- Decision: relevant
- Rationale: Directly about China responding to new US tariffs.
- Category/date: gospodarstvo / 2025-10-12T13:10:13
- URL: https://www.rtvslo.si/gospodarstvo/kitajska-po-napovedi-novih-ameriskih-carin-zagrozila-s-protiukrepi/760526
- FAISS rank/score: 3 / 0.7742
- Reranker score: 5.8505
- Keywords: ZDA, Kitajska, carine
- Excerpt: Kitajska po napovedi novih ameriških carin zagrozila s protiukrepi Ključne besede: ZDA, Kitajska, carine Potem ko je predsednik ZDA Donald Trump z novembrom napovedal nove carine na uvoz iz Kitajske, je ta zagrozila s protiukrepi. V Pekingu ob tem Washingtonu očitajo dvojna merila in mu očitajo zlorabe načela nacionalne varnosti. S kitajskega ministrstva za trgovino so sporočili, da ameriška administracija že dolgo pretirava z uporabo načela nacionalne varnosti in ga zlorablja za nadzor nad izvo...

#### Rank 2: RELEVANT

- Title: Kitajska na področju umetne inteligence prehiteva ZDA
- Decision: relevant
- Rationale: Directly compares China and the US in AI.
- Category/date: znanost-in-tehnologija / 2019-03-19T08:39:25
- URL: https://www.rtvslo.si/znanost-in-tehnologija/kitajska-na-podrocju-umetne-inteligence-prehiteva-zda/483019
- FAISS rank/score: 1 / 0.7872
- Reranker score: 3.1589
- Keywords: AI, UI, Umetna inteligenca, Kitajska, Allen Institute for Artificial Intelligence, ZDA, raziskava, inštitut, tehnologija, avtonomna vozila, navidezna resničnost, 5G, naložbe, Peking, priseljevanje, strategija, Donald Trump, administracija, inovacije, nacionalna strategija, analitiki, Washington, raziskovalec
- Excerpt: Kitajska na področju umetne inteligence prehiteva ZDA Ključne besede: AI, UI, Umetna inteligenca, Kitajska, Allen Institute for Artificial Intelligence, ZDA, raziskava, inštitut, tehnologija, avtonomna vozila, navidezna resničnost, 5G, naložbe, Peking, priseljevanje, strategija, Donald Trump, administracija, inovacije, nacionalna strategija, analitiki, Washington, raziskovalec Kitajska je na dobri poti, da na področju umetne inteligence prehiti ZDA, kaže analiza, ki jo je v sredo objavil amerišk...

#### Rank 3: RELEVANT

- Title: Kitajski obrambni minister: Spopad Kitajske in ZDA bi bil neznosna katastrofa za svet
- Decision: relevant
- Rationale: Directly about potential China-US conflict.
- Category/date: svet / 2023-06-04T09:05:31
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/kitajski-obrambni-minister-spopad-kitajske-in-zda-bi-bil-neznosna-katastrofa-za-svet/670585
- FAISS rank/score: 2 / 0.7837
- Reranker score: 2.9728
- Keywords: Kitajska, ZDA, Li Šangfu, konflikt, dialog, sodelovanje, varnost, vojska, politika, mednarodni odnosi, Sovjetska zveza, sankcije, orožje, Tajvan, Singapur, Azija, vrh, geopolitika, hladna vojna, hegemonija, diplomatski odnosi
- Excerpt: Kitajski obrambni minister: Spopad Kitajske in ZDA bi bil neznosna katastrofa za svet Ključne besede: Kitajska, ZDA, Li Šangfu, konflikt, dialog, sodelovanje, varnost, vojska, politika, mednarodni odnosi, Sovjetska zveza, sankcije, orožje, Tajvan, Singapur, Azija, vrh, geopolitika, hladna vojna, hegemonija, diplomatski odnosi Kitajski obrambni minister Li Šangfu je v nedeljo dejal, da bi bil spopad z ZDA "neznosna katastrofa" za svet, in da si njegova država želi dialog namesto spopada. Li, ki j...

#### Rank 4: RELEVANT

- Title: ZDA in Kitajska naj bi dosegle okvirni dogovor, ki bi preložil uvedbo ameriških carin
- Decision: relevant
- Rationale: Directly about US-China tariff negotiations.
- Category/date: svet / 2025-10-26T14:29:41
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/zda-in-kitajska-naj-bi-dosegle-okvirni-dogovor-ki-bi-prelozil-uvedbo-ameriskih-carin/762061
- FAISS rank/score: 46 / 0.7446
- Reranker score: 2.9495
- Keywords: Malezija, Donald Trump, Ši Džinping, Kitajska, Carine, Asean
- Excerpt: ZDA in Kitajska naj bi dosegle okvirni dogovor, ki bi preložil uvedbo ameriških carin Ključne besede: Malezija, Donald Trump, Ši Džinping, Kitajska, Carine, Asean Ameriški uradniki so sporočili, da so s Kitajsko dosegli okvirni trgovinski dogovor, o katerem bosta prihodnji teden odločala predsednika Donald Trump in Ši Džinping. Dogovor bi pomenil preložitev uvedbe dodatnih ameriških carin na kitajsko blago. Ameriški finančni minister Scott Bessent je dejal, da so pogovori ob robu vrha Združenja...

#### Rank 5: RELEVANT

- Title: Trump pohvalil odnos med ZDA in Kitajsko po dogovoru o znižanju carin za 90 dni
- Decision: relevant
- Rationale: Directly about US-China relations after tariff agreement.
- Category/date: gospodarstvo / 2025-05-12T09:56:38
- URL: https://www.rtvslo.si/gospodarstvo/trump-pohvalil-odnos-med-zda-in-kitajsko-po-dogovoru-o-znizanju-carin-za-90-dni/745396
- FAISS rank/score: 35 / 0.7509
- Reranker score: 2.8012
- Keywords: Kitajska, ZDA, Carine
- Excerpt: Trump pohvalil odnos med ZDA in Kitajsko po dogovoru o znižanju carin za 90 dni Ključne besede: Kitajska, ZDA, Carine Kitajska in ZDA so po pogovorih v Ženevi dosegli dogovor v trgovinski vojni, s čimer bo za obdobje 90 dni odpravljena večina carin in protiukrepov. Tako bosta obe državi vzajemne carine znižali za 115 odstotnih točk. V skladu z dogovorom med največjima svetovnima gospodarstvoma se bodo ameriške carine na uvoz iz Kitajske znižale s 145 na 30 odstotkov, kitajske carine na uvoz iz Z...


### 15. Korupcija v slovenski politiki

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Koalicija in opozicija sta se obmetavali z obtožbami korupcije
- Decision: relevant
- Rationale: Directly about corruption accusations between Slovenian coalition and opposition.
- Category/date: slovenija / 2024-02-20T20:53:47
- URL: https://www.rtvslo.si/slovenija/koalicija-in-opozicija-sta-se-obmetavali-z-obtozbami-korupcije/698992
- FAISS rank/score: 37 / 0.7311
- Reranker score: 2.9226
- Keywords: Politika, Slovenska politika, korupcija, pravosodje, DZ, Odbor za pravosodje, Litijska, afere, opozicija, koalicija, nakup, stavba, Litijska cesta, živahna razprava, SDS, priporočila, seja, poslanec, očitki, milijonski nakup, lastništvo, integriteta, javne funkcije, obljube.
- Excerpt: Koalicija in opozicija sta se obmetavali z obtožbami korupcije Ključne besede: Politika, Slovenska politika, korupcija, pravosodje, DZ, Odbor za pravosodje, Litijska, afere, opozicija, koalicija, nakup, stavba, Litijska cesta, živahna razprava, SDS, priporočila, seja, poslanec, očitki, milijonski nakup, lastništvo, integriteta, javne funkcije, obljube. Na razpravi o stanju na področju korupcije je opozicija poudarila zlasti afere spornega nakupa stavbe na Litijski cesti, koalicija pa je izpostav...

#### Rank 2: RELEVANT

- Title: KPK: V Sloveniji manjka ustrezno prevzemanje odgovornosti najvišjih predstavnikov oblasti
- Decision: relevant
- Rationale: About responsibility/accountability of top Slovenian public officials.
- Category/date: slovenija / 2026-02-10T10:23:44
- URL: https://www.rtvslo.si/slovenija/kpk-v-sloveniji-manjka-ustrezno-prevzemanje-odgovornosti-najvisjih-predstavnikov-oblasti/772947
- FAISS rank/score: 5 / 0.7515
- Reranker score: 2.7702
- Keywords: korupcija, CPI, Slovenija
- Excerpt: KPK: V Sloveniji manjka ustrezno prevzemanje odgovornosti najvišjih predstavnikov oblasti Ključne besede: korupcija, CPI, Slovenija Slovenija je v Indeksu zaznave korupcije za leto 2025 dosegla 58 od 100 točk in se uvrstila na 41. mesto med 182 državami. Slovenija je v primerjavi z lani padla za pet mest. Premier Golob: "Morda smo bili uspavani z odličnimi rezultati v letu 2024" Po lanskem skoku navzgor, ko je Slovenija na lestvici zaznave korupcije za leto 2024 dosegla 60 točk, je letos indeks...

#### Rank 3: RELEVANT

- Title: Maruša Babnik: V Sloveniji smo preveč tolerantni do korupcije
- Decision: relevant
- Rationale: Directly about tolerance of corruption in Slovenia.
- Category/date: slovenija / 2023-12-05T10:35:38
- URL: https://www.rtvslo.si/slovenija/ob-osmih/marusa-babnik-v-sloveniji-smo-prevec-tolerantni-do-korupcije/690549
- FAISS rank/score: 13 / 0.7420
- Reranker score: 2.1451
- Keywords: Korupcija, integriteta, KPK, Transparency International, Transparency International Slovenija, indeks zaznane korupcije, ničelna toleranca, finančne posledice, zaupanje v demokracijo, pravna država, ozaveščanje, preprečevanje korupcije, družba, institucije, primeri, Robert Golob, Komisija za preprečevanje korupcije, zgled.
- Excerpt: Maruša Babnik: V Sloveniji smo preveč tolerantni do korupcije Ključne besede: Korupcija, integriteta, KPK, Transparency International, Transparency International Slovenija, indeks zaznane korupcije, ničelna toleranca, finančne posledice, zaupanje v demokracijo, pravna država, ozaveščanje, preprečevanje korupcije, družba, institucije, primeri, Robert Golob, Komisija za preprečevanje korupcije, zgled. Za korupcijo je včasih veljalo samo podkupovanje, danes pa je to tudi kršitev integritete. A vsa...

#### Rank 4: RELEVANT

- Title: Slovenija na indeksu zaznave korupcije dosegla najslabši rezultat do zdaj
- Decision: relevant
- Rationale: Directly about Slovenia on the corruption perception index.
- Category/date: gospodarstvo / 2023-01-31T08:40:12
- URL: https://www.rtvslo.si/gospodarstvo/slovenija-na-indeksu-zaznave-korupcije-dosegla-najslabsi-rezultat-do-zdaj/656262
- FAISS rank/score: 1 / 0.7574
- Reranker score: 2.0837
- Keywords: CPI, Transparency International, indeks zaznave korupcije, korupcija, indeks zaznane korupcije, evropsko povprečje, države Zahodne Evrope, EU, boj proti korupciji, lestvica, točke, Danska, Finska, Nova Zelandija, Južni Sudan, Sirija, Somalija, Madžarska, Hrvaška, Avstrija, povprečje, OECD
- Excerpt: Slovenija na indeksu zaznave korupcije dosegla najslabši rezultat do zdaj Ključne besede: CPI, Transparency International, indeks zaznave korupcije, korupcija, indeks zaznane korupcije, evropsko povprečje, države Zahodne Evrope, EU, boj proti korupciji, lestvica, točke, Danska, Finska, Nova Zelandija, Južni Sudan, Sirija, Somalija, Madžarska, Hrvaška, Avstrija, povprečje, OECD Po zadnjih podatkih indeksa zaznane korupcije se stanje v Sloveniji slabša. S 56 točkami je v 10 letih nazadovala za pet...

#### Rank 5: RELEVANT

- Title: Seja komisije za nadzor javnih financ o korupciji prekinjena, padale tudi težke besede
- Decision: relevant
- Rationale: Directly about a public-finance commission session on corruption.
- Category/date: slovenija / 2026-02-17T10:29:32
- URL: https://www.rtvslo.si/slovenija/seja-komisije-za-nadzor-javnih-financ-o-korupciji-prekinjena-padale-tudi-tezke-besede/773708
- FAISS rank/score: 31 / 0.7326
- Reranker score: 1.8615
- Keywords: Komisija DZ za nadzor javnih finan, korupcija, prekinitev
- Excerpt: Seja komisije za nadzor javnih financ o korupciji prekinjena, padale tudi težke besede Ključne besede: Komisija DZ za nadzor javnih finan, korupcija, prekinitev Nujna seja komisije za nadzor javnih financ je bila ob odsotnosti poslancev Levice in SD-ja prekinjena zaradi nesklepčnosti. Predsednik komisije Jernej Vrtovec je sicer zavrnil predlog Svobode, da bi obravnavali tudi trgovino z orožjem in druge afere. Sejo, na kateri bi obravnavali sume sistemske korupcije v Sloveniji, so zahtevali posla...


### 16. Izstrelitev rakete v vesolje

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Video: Tako je iz vesolja videti izstrelitev rakete
- Decision: relevant
- Rationale: Directly about seeing a rocket launch from space.
- Category/date: znanost-in-tehnologija / 2018-11-25T11:06:09
- URL: https://www.rtvslo.si/znanost-in-tehnologija/video-tako-je-iz-vesolja-videti-izstrelitev-rakete/472829
- FAISS rank/score: 1 / 0.8347
- Reranker score: 6.0014
- Keywords: ISS, Mednarodna vesoljska postaja, Alexander Gerst, Poleti s posadko, Progress, Sojuz, raketa, vesolje, izstrelitev, vesoljsko plovilo, zaloge, Evropska vesoljska agencija, Esa, astronavt, poveljnik, kozmodrom, orbite, gorivo, kisik, preizkus, nesreča, senzor, Rusija, posadke, kupola, fotoaparat, fotografiranje.
- Excerpt: Video: Tako je iz vesolja videti izstrelitev rakete Ključne besede: ISS, Mednarodna vesoljska postaja, Alexander Gerst, Poleti s posadko, Progress, Sojuz, raketa, vesolje, izstrelitev, vesoljsko plovilo, zaloge, Evropska vesoljska agencija, Esa, astronavt, poveljnik, kozmodrom, orbite, gorivo, kisik, preizkus, nesreča, senzor, Rusija, posadke, kupola, fotoaparat, fotografiranje. Astronavt Alexander Gerst je posnel izstrelitev rakete z drugačne perspektive, kot smo je vajeni. Ujel je plovilo MS-1...

#### Rank 2: RELEVANT

- Title: Nasa uspešno izstrelila SpaceX-ovo raketo. Četverica bo v vesolju šest mesecev.
- Decision: relevant
- Rationale: Directly about a NASA/SpaceX rocket launch to space.
- Category/date: znanost-in-tehnologija / 2023-03-02T12:24:00
- URL: https://www.rtvslo.si/znanost-in-tehnologija/nasa-uspesno-izstrelila-spacex-ovo-raketo-cetverica-bo-v-vesolju-sest-mesecev/659714
- FAISS rank/score: 3 / 0.8073
- Reranker score: 5.7290
- Keywords: SpaceX, Dragon Crew-6, misija, Nasa, Elon Musk, mednarodna vesoljska postaja, posadka, izstrelitev, težave, vesolje, astronavt, orbita, Združeni arabski emirati, ISS, predaja, Zemlja, kapsula, Rusija, Sojuz, puščanje, Kazahstan
- Excerpt: Nasa uspešno izstrelila SpaceX-ovo raketo. Četverica bo v vesolju šest mesecev. Ključne besede: SpaceX, Dragon Crew-6, misija, Nasa, Elon Musk, mednarodna vesoljska postaja, posadka, izstrelitev, težave, vesolje, astronavt, orbita, Združeni arabski emirati, ISS, predaja, Zemlja, kapsula, Rusija, Sojuz, puščanje, Kazahstan Iz Nasinega vesoljskega centra Kennedy na Floridi so uspešno izstrelili raketo ameriškega podjetja SpaceX, ki je v lasti milijarderja Elona Muska. V okviru misije Dragon Crew-6...

#### Rank 3: RELEVANT

- Title: Kitajska prvič izstrelila raketo v vesolje z morja
- Decision: relevant
- Rationale: Directly about China launching a rocket into space.
- Category/date: znanost-in-tehnologija / 2019-06-05T14:56:54
- URL: https://www.rtvslo.si/znanost-in-tehnologija/kitajska-prvic-izstrelila-raketo-v-vesolje-z-morja/490292
- FAISS rank/score: 10 / 0.7967
- Reranker score: 5.6855
- Keywords: Kitajska, Kitajska vesolje, Kitajski vesoljski program, Izstrelitve, Izstrelitve 2019, Dolgi pohod 11, Dolgi pohod, raketa, vesolje, Nacionalna vesoljska administracija, izstrelitev, morje, satelit, znanstveni poskusi, komercialni, ladja, Rumeni morje, ekvator, hitrost, gorivo, konkurenčno, nosilna raketa, v orbito, novi generaciji, robotska sonda, vesoljska postaja
- Excerpt: Kitajska prvič izstrelila raketo v vesolje z morja Ključne besede: Kitajska, Kitajska vesolje, Kitajski vesoljski program, Izstrelitve, Izstrelitve 2019, Dolgi pohod 11, Dolgi pohod, raketa, vesolje, Nacionalna vesoljska administracija, izstrelitev, morje, satelit, znanstveni poskusi, komercialni, ladja, Rumeni morje, ekvator, hitrost, gorivo, konkurenčno, nosilna raketa, v orbito, novi generaciji, robotska sonda, vesoljska postaja Kitajska je prvič izstrelila raketo v vesolje z morja, je sporoč...

#### Rank 4: RELEVANT

- Title: Raketo s prvima slovenskima satelitoma le izstrelili: "V vesolju smo!"
- Decision: relevant
- Rationale: Directly about a rocket launch carrying Slovenian satellites into space.
- Category/date: znanost-in-tehnologija / 2020-09-03T06:47:51
- URL: https://www.rtvslo.si/znanost-in-tehnologija/raketo-s-prvima-slovenskima-satelitoma-le-izstrelili-v-vesolju-smo/535004
- FAISS rank/score: 2 / 0.8105
- Reranker score: 5.5919
- Keywords: satelit, izstrelitev, Vega, Nemo HD in Trisat, Francoska Gvajana, raketa, Nemo HD, Trisat, evropska znanost, Arianespace, vesoljski center, Kourou, vodja projekta, Centrer odličnosti Vesolje-SI, znanost, slovensko gospodarstvo, orbita, vesolje, mikrosatelit, nanosatelit, testiranje
- Excerpt: Raketo s prvima slovenskima satelitoma le izstrelili: "V vesolju smo!" Ključne besede: satelit, izstrelitev, Vega, Nemo HD in Trisat, Francoska Gvajana, raketa, Nemo HD, Trisat, evropska znanost, Arianespace, vesoljski center, Kourou, vodja projekta, Centrer odličnosti Vesolje-SI, znanost, slovensko gospodarstvo, orbita, vesolje, mikrosatelit, nanosatelit, testiranje Iz Francoske Gvajane so ponoči vendarle izstrelili raketo Vega, s katero sta v vesolje poletela tudi prva slovenska satelita Nemo...

#### Rank 5: RELEVANT

- Title: Salama, dimljeni sir in stranišče potujejo v vesolje
- Decision: relevant
- Rationale: About a supply rocket launch to the space station.
- Category/date: zabava-in-slog / 2020-10-03T14:29:12
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/salama-dimljeni-sir-in-stranisce-potujejo-v-vesolje/537952
- FAISS rank/score: 40 / 0.7814
- Reranker score: 5.3402
- Keywords: vesolje, izstrelitev, astornavti, raketa, ISS, ZDA, mednarodna vesoljska postaja, zaloge, testne naprave, sesalno vesoljsko stranišče, oskrbovalna raketa, tovor, posadka, Northrop Group, fekalije, breztežnostni prostor, astronavti, Cygnus, Virginija, življenje astronavtov, raziskave, astronavtke
- Excerpt: Salama, dimljeni sir in stranišče potujejo v vesolje Ključne besede: vesolje, izstrelitev, astornavti, raketa, ISS, ZDA, mednarodna vesoljska postaja, zaloge, testne naprave, sesalno vesoljsko stranišče, oskrbovalna raketa, tovor, posadka, Northrop Group, fekalije, breztežnostni prostor, astronavti, Cygnus, Virginija, življenje astronavtov, raziskave, astronavtke V ZDA so preteklo noč izstrelili raketo, ki je na mednarodno vesoljsko postajo popeljala nove zaloge in nekaj novih testnih naprav. Me...


### 17. Delnice Tesle padajo

Precision@5: 4/5 = 0.80

#### Rank 1: NOT RELEVANT

- Title: Vrnitev Tesle in vzpon indeksa S & P nad 5500 točk
- Decision: not_relevant
- Rationale: About Tesla and S&P rising/recovery, not Tesla shares falling.
- Category/date: gospodarstvo / 2024-07-03T06:32:32
- URL: https://www.rtvslo.si/gospodarstvo/borzni-komentar/vrnitev-tesle-in-vzpon-indeksa-s-p-nad-5500-tock/713666
- FAISS rank/score: 2 / 0.8155
- Reranker score: 2.8397
- Keywords: MMC-jev borzni komentar, S & P 500, rekord, Tesline delnice
- Excerpt: Vrnitev Tesle in vzpon indeksa S & P nad 5500 točk Ključne besede: MMC-jev borzni komentar, S & P 500, rekord, Tesline delnice Wall Street je v drugo polletje vstopil optimistično, zadnje izjave Jeroma Powlla pa vlivajo upanje, da Fed dobiva boj z inflacijo. Indeksa S & P 500 in NASDAQ sta na novem rekordu, med posameznimi papirji pa je včeraj blestela Tesla. Tesline delnice so krenile za deset odstotkov navzgor (tudi nad 230 dolarjev), potem ko je proizvajalec električnih vozil sporočil, da je...

#### Rank 2: RELEVANT

- Title: Tesla izgublja primat na trgu e-vozil; prodajni pritisk pri bitcoinu popušča
- Decision: relevant
- Rationale: About Tesla losing market primacy and sales pressure context.
- Category/date: gospodarstvo / 2024-01-28T06:24:02
- URL: https://www.rtvslo.si/gospodarstvo/borzni-komentar/tesla-izgublja-primat-na-trgu-e-vozil-prodajni-pritisk-pri-bitcoinu-popusca/696349
- FAISS rank/score: 7 / 0.7913
- Reranker score: 2.5613
- Keywords: MMC-jev borzni komentar, Intel, Tesla, četrtletni poslovni rezultati, BYD, PCE-inflacija, ameriški BDP, bitcoin, ETF-sklad, Bitcoin Trust, delnice, New York, indeksi, dobiček, čipov, umetna inteligenca, Nvidija, podatkovni centri, Mobileye, samovozeča vozila, konkurenca, Kitajska, električna vozila, prodaja, rezultati, trgovanje, finance
- Excerpt: Tesla izgublja primat na trgu e-vozil; prodajni pritisk pri bitcoinu popušča Ključne besede: MMC-jev borzni komentar, Intel, Tesla, četrtletni poslovni rezultati, BYD, PCE-inflacija, ameriški BDP, bitcoin, ETF-sklad, Bitcoin Trust, delnice, New York, indeksi, dobiček, čipov, umetna inteligenca, Nvidija, podatkovni centri, Mobileye, samovozeča vozila, konkurenca, Kitajska, električna vozila, prodaja, rezultati, trgovanje, finance Čeprav sta Intel in Tesla s črnogledimi napovedmi malce pokvarila r...

#### Rank 3: RELEVANT

- Title: Tesla v prvem četrtletju s 13-odstotnim padcem prodaje avtomobilov
- Decision: relevant
- Rationale: Directly about Tesla sales falling.
- Category/date: gospodarstvo / 2025-04-02T17:43:00
- URL: https://www.rtvslo.si/gospodarstvo/preberite-tudi/tesla-v-prvem-cetrtletju-s-13-odstotnim-padcem-prodaje-avtomobilov/741463
- FAISS rank/score: 4 / 0.7939
- Reranker score: 2.4292
- Keywords: Padec delnic, Bojkot, Elon Musk, Prodaja avtomobilov, Tesla
- Excerpt: Tesla v prvem četrtletju s 13-odstotnim padcem prodaje avtomobilov Ključne besede: Padec delnic, Bojkot, Elon Musk, Prodaja avtomobilov, Tesla Ameriški proizvajalec električnih avtomobilov Tesla je v prvem letošnjem četrtletju dobavil 336.681 avtomobilov, kar je 13 odstotkov manj kot leto prej, poroča francoska tiskovna agencija AFP. Manjša prodaja je posledica manjše proizvodnje zaradi posodabljanja tovarn in bojkota podjetja zaradi političnega delovanja direktorja Elona Muska. Število dobavlje...

#### Rank 4: RELEVANT

- Title: Musk po velikem padcu vrednosti Tesle obljublja, da bo podjetje najvrednejše na svetu
- Decision: relevant
- Rationale: Directly about a major fall in Tesla value.
- Category/date: gospodarstvo / 2022-12-29T16:28:18
- URL: https://www.rtvslo.si/gospodarstvo/musk-po-velikem-padcu-vrednosti-tesle-obljublja-da-bo-podjetje-najvrednejse-na-svetu/652623
- FAISS rank/score: 10 / 0.7861
- Reranker score: 2.1845
- Keywords: Tesla, Elon Musk, Avtomobili, delnice, borzni trg, zaposleni, elektronsko pismo, dobave, popusti, analitiki, četrtletje, vrednost, povpraševanje, električni avtomobili, tehnološko podjetje, Twitter, proizvodnja, napoved, družbeno omrežje, direktor
- Excerpt: Musk po velikem padcu vrednosti Tesle obljublja, da bo podjetje najvrednejše na svetu Ključne besede: Tesla, Elon Musk, Avtomobili, delnice, borzni trg, zaposleni, elektronsko pismo, dobave, popusti, analitiki, četrtletje, vrednost, povpraševanje, električni avtomobili, tehnološko podjetje, Twitter, proizvodnja, napoved, družbeno omrežje, direktor Potem ko so delnice avtomobilskega podjetja Tesla letos izgubile 70 odstotkov, je lastnik Elon Musk zatrdil, da bo podjetje na dolgi rok najvrednejše...

#### Rank 5: RELEVANT

- Title: Tehnološke delnice vidno sestopile z vrhov, še bolj pa Teslin dobiček
- Decision: relevant
- Rationale: Directly about technology stocks and Tesla profit falling.
- Category/date: gospodarstvo / 2024-07-28T06:17:32
- URL: https://www.rtvslo.si/gospodarstvo/borzni-komentar/tehnoloske-delnice-vidno-sestopile-z-vrhov-se-bolj-pa-teslin-dobicek/716161
- FAISS rank/score: 1 / 0.8250
- Reranker score: 2.1118
- Keywords: MMC-jev borzni komentar, četrtletni poslovni rezultati, Tesla, Alphabet, Ford, Ryanair, Krka, dividenda
- Excerpt: Tehnološke delnice vidno sestopile z vrhov, še bolj pa Teslin dobiček Ključne besede: MMC-jev borzni komentar, četrtletni poslovni rezultati, Tesla, Alphabet, Ford, Ryanair, Krka, dividenda Po treh dneh resnih razprodaj so tehnološke delnice v New Yorku v petek le okrevale, delno tudi zaradi novih znakov, da se inflacija umirja in bi moral Fed s septembrom končno začeti zniževati obrestne mere, ki so že več kot leto dni na 23-letnem vrhu. Potem ko smo še v prvi polovici julija spremljali nove re...


### 18. Nova verzija umetne inteligence

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Razvili umetno inteligenco, ki bo nadgradila izkušnjo športnih ljubiteljev
- Decision: relevant
- Rationale: About a newly developed AI feature/system.
- Category/date: zabava-in-slog / 2024-06-24T13:28:46
- URL: https://www.rtvslo.si/zabava-in-slog/zanimivosti/razvili-umetno-inteligenco-ki-bo-nadgradila-izkusnjo-sportnih-ljubiteljev/712824
- FAISS rank/score: 9 / 0.8003
- Reranker score: 3.8843
- Keywords: Generativna funkcija, Wimbledon, IBM, Športni podatki, Umetna inteligenca, skit scena
- Excerpt: Razvili umetno inteligenco, ki bo nadgradila izkušnjo športnih ljubiteljev Ključne besede: Generativna funkcija, Wimbledon, IBM, Športni podatki, Umetna inteligenca, skit scena Umetna inteligenca je dodobra vpeta v naš način življenja in je prisotna kot še nikoli doslej. Zdaj bo tehnologija vpeljana še v svet športa, natančneje tenisa, ki bo tako za tekmovalce kot navijače dodala novo dimenzijo. "Vi vidite tenis, mi vidimo podatke. Vi vidite golf, mi vidimo podatke," je za Euronews povedal Jonat...

#### Rank 2: RELEVANT

- Title: Google predstavil nov program umetne inteligence Bard
- Decision: relevant
- Rationale: Directly about Google presenting a new AI program.
- Category/date: znanost-in-tehnologija / 2023-02-07T11:00:00
- URL: https://www.rtvslo.si/znanost-in-tehnologija/google-predstavil-nov-program-umetne-inteligence-bard/657070
- FAISS rank/score: 3 / 0.8147
- Reranker score: 3.5533
- Keywords: Google, Bard, Umetna inteligenca, jezikovni model, intervju, Sundar Pichai, LaMDA, ChatGPT, OpenAI, Microsoft, investicija, partnerstvo, tehnološko podjetje, aplikacije za dialog, razvoj, napredki, zunanji vplivi, primerjava, inovacija, iskalnik
- Excerpt: Google predstavil nov program umetne inteligence Bard Ključne besede: Google, Bard, Umetna inteligenca, jezikovni model, intervju, Sundar Pichai, LaMDA, ChatGPT, OpenAI, Microsoft, investicija, partnerstvo, tehnološko podjetje, aplikacije za dialog, razvoj, napredki, zunanji vplivi, primerjava, inovacija, iskalnik Ameriški tehnološki velikan Google je uradno predstavil nov program umetne inteligence Bard. Kot poudarjajo v podjetju, gre za pomemben naslednji korak na področju umetne inteligence z...

#### Rank 3: RELEVANT

- Title: ChatGPT: "Če je bilo prej potrebnih pet ljudi za neko delo, bosta zdaj dva ali eden"
- Decision: relevant
- Rationale: About new/rapid AI development around ChatGPT and related systems.
- Category/date: znanost-in-tehnologija / 2023-04-21T06:07:00
- URL: https://www.rtvslo.si/znanost-in-tehnologija/chatgpt-ce-je-bilo-prej-potrebnih-pet-ljudi-za-neko-delo-bosta-zdaj-dva-ali-eden/665582
- FAISS rank/score: 25 / 0.7890
- Reranker score: 2.7521
- Keywords: ChatGPT, Midjourney, AI, umetna inteligenca, TruthGPT, papež, Ryan Reynolds, Aljaž Peklaj, Tim Waschl Luzar, OpenAI, marketing, Microsoft, Elon Musk, GPT-4, Apple, Steve Wozniak, lagati, Google, Larry Page, varnost, tožba
- Excerpt: ChatGPT: "Če je bilo prej potrebnih pet ljudi za neko delo, bosta zdaj dva ali eden" Ključne besede: ChatGPT, Midjourney, AI, umetna inteligenca, TruthGPT, papež, Ryan Reynolds, Aljaž Peklaj, Tim Waschl Luzar, OpenAI, marketing, Microsoft, Elon Musk, GPT-4, Apple, Steve Wozniak, lagati, Google, Larry Page, varnost, tožba "Če je bilo prej potrebnih pet ljudi za neko delo, bosta zdaj dva ali celo eden," pravi strokovnjak za celostni marketing Aljaž Peklaj. Toda vprašanje je, ali ob vsej tej optimi...

#### Rank 4: RELEVANT

- Title: Apple bo svoje naprave nadgradil s ChatGPT-jem in glasovni pomočnici Siri dal nove funkcije
- Decision: relevant
- Rationale: About new AI features for Apple devices with ChatGPT.
- Category/date: znanost-in-tehnologija / 2024-06-11T09:23:51
- URL: https://www.rtvslo.si/znanost-in-tehnologija/apple-bo-svoje-naprave-nadgradil-s-chatgpt-jem-in-glasovni-pomocnici-siri-dal-nove-funkcije/711352
- FAISS rank/score: 19 / 0.7909
- Reranker score: 2.5077
- Keywords: Apple, OpenAI, ChatGPT, Tim Cook
- Excerpt: Apple bo svoje naprave nadgradil s ChatGPT-jem in glasovni pomočnici Siri dal nove funkcije Ključne besede: Apple, OpenAI, ChatGPT, Tim Cook Ameriško tehnološko podjetje Apple je predstavilo nove funkcije umetne inteligence za svoje naprave Apple Intelligence in partnerstvo s podjetjem OpenAI, ki bo še letos vključilo storitev ChatGPT v Applove naprave. Glavni izvršni direktor Appla Tim Cook je na sedežu tehnološkega velikana v kalifornijskem mestu Cupertino v Silicijevi dolini odprl letno konfe...

#### Rank 5: RELEVANT

- Title: OpenAI predstavil najnovejši model umetne inteligence GPT-5 − pametnejši, hitrejši, uporabnejši
- Decision: relevant
- Rationale: Directly about a new/latest AI model version, GPT-5.
- Category/date: znanost-in-tehnologija / 2025-08-08T08:30:59
- URL: https://www.rtvslo.si/znanost-in-tehnologija/openai-predstavil-najnovejsi-model-umetne-inteligence-gpt-5-pametnejsi-hitrejsi-uporabnejsi/754133
- FAISS rank/score: 16 / 0.7963
- Reranker score: 2.3217
- Keywords: GPT-5, OpenAI, UI
- Excerpt: OpenAI predstavil najnovejši model umetne inteligence GPT-5 − pametnejši, hitrejši, uporabnejši Ključne besede: GPT-5, OpenAI, UI Podjetje OpenAI je predstavilo najnovejši in najnaprednejši model umetne inteligence velikega obsega GPT-5. GPT-5, ki je pametnejši, hitrejši in uporabnejši pri pisanju, programiranju in na drugih področjih, bo vsem na voljo brezplačno. OpenAI trdi, da je stopnja halucinacij GPT-5 nižja, kar pomeni, da si model manj pogosto izmišlja odgovore. V podjetju so pojasnili,...


### 19. Najbolj prodajan avtomobil

Precision@5: 5/5 = 1.00

#### Rank 1: RELEVANT

- Title: Tesla z dvema modeloma na lestvici najbolj prodajanih vozil na svetu
- Decision: relevant
- Rationale: Directly about best-selling vehicles worldwide.
- Category/date: zabava-in-slog / 2023-05-10T08:01:00
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/tesla-z-dvema-modeloma-na-lestvici-najbolj-prodajanih-vozil-na-svetu/667586
- FAISS rank/score: 3 / 0.8006
- Reranker score: 6.0795
- Keywords: Prodaja vozil, JATO Dynamics, Toyota RAV 4, Toyota, vozilo, prodaja, svet, avtomobili, modeli, Tesla, registracija, trg, razvoj, Severna Amerika, Evropa, Kitajska, padec, dobavna veriga, polprevodniki, motnje, Ukrajina, sankcije, Rusija, Volkswagen, Hyundai-Kia, Stellantis, General Motors, BYD, tržni delež, testiranje, Avtomobilnost.
- Excerpt: Tesla z dvema modeloma na lestvici najbolj prodajanih vozil na svetu Ključne besede: Prodaja vozil, JATO Dynamics, Toyota RAV 4, Toyota, vozilo, prodaja, svet, avtomobili, modeli, Tesla, registracija, trg, razvoj, Severna Amerika, Evropa, Kitajska, padec, dobavna veriga, polprevodniki, motnje, Ukrajina, sankcije, Rusija, Volkswagen, Hyundai-Kia, Stellantis, General Motors, BYD, tržni delež, testiranje, Avtomobilnost. Toyota je leta 2022 prodala največ vozil na svetu. Med desetimi najbolje prodaj...

#### Rank 2: RELEVANT

- Title: Dacia sandero premagala teslo Y
- Decision: relevant
- Rationale: Directly about a model beating Tesla Y in sales.
- Category/date: zabava-in-slog / 2024-03-23T07:37:23
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/dacia-sandero-premagala-teslo-y/702542
- FAISS rank/score: 7 / 0.7888
- Reranker score: 5.7634
- Keywords: Dacia sandero, Tesla model y, Volkswagen golf, Evropa, prodaja avtomobilov, Dataforce, sindikati, prodaja vozil, Teslina tovarna, Grünheide, Berlin, avtomobilska industrija, Peugeot 208, Citroen C3, kombilimuzina, električni avtomobili, avtomobilske tovarne, aktivisti, prodajne uspešnice, prodajne enote
- Excerpt: Dacia sandero premagala teslo Y Ključne besede: Dacia sandero, Tesla model y, Volkswagen golf, Evropa, prodaja avtomobilov, Dataforce, sindikati, prodaja vozil, Teslina tovarna, Grünheide, Berlin, avtomobilska industrija, Peugeot 208, Citroen C3, kombilimuzina, električni avtomobili, avtomobilske tovarne, aktivisti, prodajne uspešnice, prodajne enote Dacia Sandero je ponovno najbolje prodajani avto v Evropi. Premagala je teslo model Y, največjo uspešnico leta 2023. Dacia sandero je na dobri poti...

#### Rank 3: RELEVANT

- Title: Čeprav je prodaja vozil okrevala, je bilo leto 2023 eno najslabših v zadnjih 25 letih
- Decision: relevant
- Rationale: About car sales trends, sufficiently related to best-selling car.
- Category/date: zabava-in-slog / 2024-02-26T18:55:43
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/ceprav-je-prodaja-vozil-okrevala-je-bilo-leto-2023-eno-najslabsih-v-zadnjih-25-letih/699614
- FAISS rank/score: 12 / 0.7718
- Reranker score: 5.3133
- Keywords: Rabljeni avtomobili, Električna vozila, Volkswagen, AMZS, Prodaja vozil, avtomobili, prodaja električnih avtomobilov pa je v lanskem letu v primerjavi z letom 2022 narasla za 140 odstotkov. Na področju električnih vozil je najbolj prodajan model ostal Tesla Model 3, sledijo mu modeli Renault Zoe in Volkswagen ID.4. Kljub veliki rasti pa električni avtomobili še vedno predstavljajo manjši delež celotne prodaje vozil v Sloveniji. AMZS ocenjuje, da bo zanimanje za električna vozila še naprej raslo, predvsem zaradi okoljskih in davčnih spodbud vlade ter širše ponudbe električnih modelov na trgu.
- Excerpt: Čeprav je prodaja vozil okrevala, je bilo leto 2023 eno najslabših v zadnjih 25 letih Ključne besede: Rabljeni avtomobili, Električna vozila, Volkswagen, AMZS, Prodaja vozil, avtomobili, prodaja električnih avtomobilov pa je v lanskem letu v primerjavi z letom 2022 narasla za 140 odstotkov. Na področju električnih vozil je najbolj prodajan model ostal Tesla Model 3, sledijo mu modeli Renault Zoe in Volkswagen ID.4. Kljub veliki rasti pa električni avtomobili še vedno predstavljajo manjši delež c...

#### Rank 4: RELEVANT

- Title: V Sloveniji lani prodanih 8,4 odstotka več avtomobilov – največ Volkswagnovih
- Decision: relevant
- Rationale: Directly about car sales in Slovenia and top brands.
- Category/date: zabava-in-slog / 2025-01-08T13:22:41
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/v-sloveniji-lani-prodanih-8-4-odstotka-vec-avtomobilov-najvec-volkswagnovih/732724
- FAISS rank/score: 1 / 0.8124
- Reranker score: 4.8218
- Keywords: avtomobili, Slovenija, prodaja
- Excerpt: V Sloveniji lani prodanih 8,4 odstotka več avtomobilov – največ Volkswagnovih Ključne besede: avtomobili, Slovenija, prodaja V Sloveniji je bilo lani prvič registriranih 53.018 osebnih avtomobilov, kar je 8,4 odstotka več kot predlani. Med vsemi lani prodanimi osebnimi avtomobili je bilo električnih 9876 oziroma 27 odstotkov manj kot predlani. Največ osebnih avtomobilov je prodal Volkswagen (7924 oziroma skoraj 15-odstotni tržni delež), sledila sta Renault (5910 oziroma 11,2-odstotni delež) in Š...

#### Rank 5: RELEVANT

- Title: Tesla model Y leta 2023 najbolje prodajano vozilo v Evropi
- Decision: relevant
- Rationale: Directly about Tesla Model Y as best-selling vehicle in Europe.
- Category/date: zabava-in-slog / 2024-01-21T12:31:47
- URL: https://www.rtvslo.si/zabava-in-slog/avtomobilnost/tesla-model-y-leta-2023-najbolje-prodajano-vozilo-v-evropi/695612
- FAISS rank/score: 4 / 0.8005
- Reranker score: 4.4125
- Keywords: Tesla, Model Y, Prodaja vozil, električni avtomobil, Evropa, prodaja, Slovenija, leta 2023, registracije, cena, konkurenca, industrija, vozila, strokovnjaki, uspeh, popularnost, Dacia Sandero, Volkswagen T-Roc, Škoda Octavia
- Excerpt: Tesla model Y leta 2023 najbolje prodajano vozilo v Evropi Ključne besede: Tesla, Model Y, Prodaja vozil, električni avtomobil, Evropa, prodaja, Slovenija, leta 2023, registracije, cena, konkurenca, industrija, vozila, strokovnjaki, uspeh, popularnost, Dacia Sandero, Volkswagen T-Roc, Škoda Octavia Električni križanec tesla Y je prvi električni avtomobil, ki je do zdaj postal najbolje prodajano vozilo v Evropi v koledarskem letu. Tesla model Y je bil v Sloveniji sedmi najbolje prodajan model avt...


### 20. Obisk tujega predsednika

Precision@5: 3/5 = 0.60

#### Rank 1: RELEVANT

- Title: Zoran Milanović si je za prvo pot v tujino v drugem predsedniškem mandatu izbral Slovenijo
- Decision: relevant
- Rationale: Directly about a foreign president visiting Slovenia.
- Category/date: slovenija / 2025-02-19T13:19:48
- URL: https://www.rtvslo.si/slovenija/zoran-milanovic-si-je-za-prvo-pot-v-tujino-v-drugem-predsedniskem-mandatu-izbral-slovenijo/737062
- FAISS rank/score: 28 / 0.7157
- Reranker score: 3.9424
- Keywords: Uradni obisk, Slovenija, Zoran Milanović
- Excerpt: Zoran Milanović si je za prvo pot v tujino v drugem predsedniškem mandatu izbral Slovenijo Ključne besede: Uradni obisk, Slovenija, Zoran Milanović Hrvaški predsednik Zoran Milanović, ki je v torek v Zagrebu prisegel za drugi predsedniški petletni mandat, bo prihodnjo sredo na uradnem obisku v Sloveniji. Iz urada predsednice republike Nataše Pirc Musar so sporočili, da gre za prvo uradno pot Zorana Milanovića v tujino po nastopu drugega mandata predsednika republike. " Namen obiska je nadaljevan...

#### Rank 2: RELEVANT

- Title: Trump na prvo pot v tujino domnevno v Savdsko Arabijo
- Decision: relevant
- Rationale: About a president travelling abroad / foreign visit.
- Category/date: svet / 2025-03-31T12:40:39
- URL: https://www.rtvslo.si/svet/preberite-tudi/trump-na-prvo-pot-v-tujino-domnevno-v-savdsko-arabijo/741166
- FAISS rank/score: 24 / 0.7165
- Reranker score: 2.3492
- Keywords: Bližnjevzhodni konflikt, Savdska Arabija, Trump
- Excerpt: Trump na prvo pot v tujino domnevno v Savdsko Arabijo Ključne besede: Bližnjevzhodni konflikt, Savdska Arabija, Trump Ameriški predsednik Donald Trump naj bi se na svojo prvo pot v tujino, odkar je januarja drugič prisegel na položaju, odpravil v Savdsko Arabijo, je poročal portal Axios ob navajanju virov blizu vlade. Na pot naj bi se odpravil v sredini maja. Trump je na začetku meseca novinarjem v Ovalni pisarni že dejal, da bo verjetno v prihodnjem mesecu in pol obiskal Savdsko Arabijo. "Šel b...

#### Rank 3: NOT RELEVANT

- Title: Južnokorejskemu predsedniku Yoonu prepovedali potovanja v tujino
- Decision: not_relevant
- Rationale: About a travel ban for a president, not an actual visit.
- Category/date: svet / 2024-12-09T09:20:20
- URL: https://www.rtvslo.si/svet/azija-z-oceanijo/juznokorejskemu-predsedniku-yoonu-prepovedali-potovanja-v-tujino/729979
- FAISS rank/score: 10 / 0.7212
- Reranker score: -0.4011
- Keywords: Južna Koreja, Yoon Suk Yeol, vojno stanje
- Excerpt: Južnokorejskemu predsedniku Yoonu prepovedali potovanja v tujino Ključne besede: Južna Koreja, Yoon Suk Yeol, vojno stanje Južnokorejsko pravosodno ministrstvo je sporočilo, da je predsedniku države Yoon Suk Yeolu zaradi nedavne razglasitve vojnega stanja prepovedalo, da zapusti državo. Opozicija je medtem vladajočo stranko obtožila novega državnega udara. Predstavniki pravosodnega ministrstva so v okviru razprave v parlamentu dejali, da za predsednika zaradi preiskave velja prepoved potovanj in...

#### Rank 4: RELEVANT

- Title: Vučić zaradi slabosti skrajšal obisk v ZDA
- Decision: relevant
- Rationale: Directly about a president visiting the US.
- Category/date: svet / 2025-05-03T15:37:26
- URL: https://www.rtvslo.si/svet/evropa/vucic-zaradi-slabosti-skrajsal-obisk-v-zda/744558
- FAISS rank/score: 39 / 0.7131
- Reranker score: -0.5981
- Keywords: Srbsko blago, Rudy Giuliani, Obisk ZDA, Zdravstveno stanje, Vučić
- Excerpt: Vučić zaradi slabosti skrajšal obisk v ZDA Ključne besede: Srbsko blago, Rudy Giuliani, Obisk ZDA, Zdravstveno stanje, Vučić Srbski predsednik Aleksandar Vučić je zaradi slabosti nepričakovano prekinil uradni obisk v ZDA in se po posvetu z zdravniki vrnil v Srbijo. Po navedbah tamkajšnjega kardiologa se je Vučić iz ZDA vrnil zaradi visokega krvnega tlaka. Srbskega predsednika je v četrtek na Floridi sprejel nekdanji župan New Yorka Rudy Giuliani, v načrtu pa je imel še več srečanj z visokimi pre...

#### Rank 5: NOT RELEVANT

- Title: V Teheranu se poslavljajo od umrlega predsednika Raisija
- Decision: not_relevant
- Rationale: About a funeral for a president, not a foreign presidential visit.
- Category/date: svet / 2024-05-22T15:06:25
- URL: https://www.rtvslo.si/svet/bliznji-vzhod/v-teheranu-se-poslavljajo-od-umrlega-predsednika-raisija/709181
- FAISS rank/score: 47 / 0.7121
- Reranker score: -1.0610
- Keywords: Iran, Pogreb, Ebrahim Raisi
- Excerpt: V Teheranu se poslavljajo od umrlega predsednika Raisija Ključne besede: Iran, Pogreb, Ebrahim Raisi V Teheranu poteka pogrebna žalna slovesnost za predsednika Ebrahima Raisija, na kateri se je zbralo več milijonov ljudi. Molitev pred krstami Raisija in drugih žrtev nedeljske helikopterske nesreče je vodil vrhovni voditelj ajatola Ali Hamenej. Po molitvi na teheranski univerzi se je procesija s krstami Raisija, zunanjega ministra Hoseina Amirja- Abdolahiana in drugih premaknila izpred univerze v...

