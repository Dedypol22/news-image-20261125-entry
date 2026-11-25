# The World in One Day — Wednesday 25 November 2026: 37 dated stories, 9 regions, 13 illustrated panels, world map, UTC timeline and date check

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Dedypol22/news-image-20261125-entry/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Dedypol22/news-image-20261125-entry/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One front page that sums up the world's news of **Wednesday 25 November 2026**:
**37 dated stories** across **9 regions**, **13 illustrated panels** (3 hero + 10
medium, every illustration drawn as vector shapes — no photos), a **world map
with 13 numbered pins**, a **24-story brief**, a **UTC timeline 22–25 Nov** and
an explicit **date-check audit box**. Every story is tagged with its real
date; claims are labelled CLAIM and reports are labelled REPORT.

`main.py` is standard library only. It decodes the embedded PNG, validates it
(PNG signature, 1024×1024 IHDR, 8-bit depth, CRC of every chunk, nothing after
IEND, at most 1 MiB) and writes it byte-for-byte. `render.py` is the local
PIL build script that drew the page; `assets/entry.png` is its output
(1024×1024, 73,622 bytes).

## The 37 stories

### Hero panels (3)

1. **East Asia — Wed 25 Nov — SHENZHOU-24 LAUNCHES.** China launches
   Shenzhou-24, 08:18 Beijing, Long March-2F from Jiuquan. Crew of 3 incl.
   Muhammad Zeeshan Ali — first foreign astronaut (Pakistani) aboard Tiangong;
   5–10 day stay, 4 biotech experiments. (Reuters, Nature)
2. **North America — Tue 24 Nov — CIA & ODNI BREACHED.** Hackers breach
   UNCLASSIFIED systems of CIA + Office of the Director of National
   Intelligence (OSINT analysis network). Classified systems NOT affected;
   already fixed. Culprit + data stolen unknown; suspected tool "ARTEX".
   (Reuters, AP)
3. **North America — Wed 25 Nov — US PROPOSES TARIFFS ON 14 PARTNERS.**
   Trump administration proposes new tariffs on 14 major trading partners
   over excess factory capacity; highest rates on China. S&P futures −2.1%,
   Nasdaq −3.1%. (Reuters)

### Medium panels (10)

4. **Middle East — Wed 25 Nov — HOUTHIS HIT RAS TANURA REFINERY.** Houthis
   say they attacked Saudi Aramco's Ras Tanura refinery + Riyadh financial
   district; coalition says air defences intercepted 4 drones at Ras Tanura;
   11 hurt Tue in Riyadh tower strike. (Reuters)
5. **Middle East — Tue 24 Nov — HOUTHI DRONE HITS RIYADH TOWER.** Second
   strike in <1 week hits 80-floor PIF Tower (Saudi wealth fund HQ, ~$1tn
   assets), 11 hurt; first strike Thu 19 Nov broke windows on 7–8 floors, NO
   casualties. (Reuters)
6. **North America — Tue 24 Nov — HUAWEI GUILTY 10 OF 12.** Brooklyn jury
   convicts Huawei: bank/wire fraud, sanctions violations, stealing trade
   secrets (incl. Cisco router code); ACQUITTED on heaviest charges (RICO +
   obstruction); sentencing 14 Sep 2027; Huawei to appeal. (Reuters, AP)
7. **Europe — Wed 25 Nov — PUIGDEMONT TO RETURN TO SPAIN 12 DEC.** Catalan
   separatist leader ends ~decade of self-imposed exile; to unveil renewed
   independence push 17 Dec. (Reuters)
8. **Africa — Wed 25 Nov — SAUDI NATIONAL KIDNAPPED IN NIGER.** Suspected
   IS-affiliate militants kidnap Saudi national in Niger (weekend 21/22 Nov),
   holding hostage; reported Wed 25 Nov. (Reuters)
9. **East Asia — Wed 25 Nov — NORTH KOREA EXPELS SWISS DIPLOMAT.** Pyongyang
   declares Sylvain Astier, head of Switzerland's newly reopened office,
   persona non grata; orders him out in 48h; demands office closure. (AP)
10. **Central Asia — Wed 25 Nov — KAZAKHSTAN ARRESTS URANIUM MINER BOARD
    MEMBER.** Security service detains Kazatomprom board member Kuanysh
    Omarbekov in widening corruption probe tied to ex-Samruk-Kazyna
    executives. (AnewZ)
11. **Africa — Tue 24 Nov — SENEGAL REINSTATED AFCON CHAMPIONS.** CAS
    unanimously restores Senegal as 2025 Africa Cup winners, overturning CAF;
    Senegal beat hosts Morocco 1-0 in Jan 2026 final (Pape Gueye); Morocco to
    challenge. (Reuters, CNN)
12. **Europe — Mon 23 Nov — NATO VOWS SPACE DEFENCE.** Sec-Gen Rutte after
    Western intel REPORT that Russia assembled nuclear-armed "Sputnik-S"
    satellite, launchable within 60 days — REPORT, Kremlin denies; Germany's
    Merz calls it "shocking". (BBC)
13. **Oceania/Pacific — Wed 25 Nov — AUSTRALIA PASSES ONLINE SAFETY LAW.**
    Australia passes online safety law putting Big Tech at risk of
    multibillion-dollar fines. (AP)

### The brief — 24 more stories

14. **North America — Mon 23 Nov — HUANG BACK AS NVIDIA CEO.** Returns 11
    days after resigning after Trump intervention; shares +30% Mon, −6–7%
    Tue. (Reuters, BBC)
15. **North America — Tue 24 Nov — MICROSOFT DECLARES "CODE RED".** After
    historic 12–13 Nov outage (Exchange, Outlook, Teams, Copilot down ~24h);
    new target: fix future incidents within 1 hour. (Reuters)
16. **North America — Wed 25 Nov — ABREGO GARCIA LEAVES US FOR SPAIN.**
    Salvadoran migrant mistakenly deported leaves voluntarily for Spain. (AP)
17. **Latin America — Mon 23 Nov — CAR BOMB WOUNDS 23 IN COLOMBIA.** Blast
    outside regional government offices in Villavicencio (Meta dept), 23 hurt,
    no deaths; 80–100 kg pentolite; blamed on FARC-EMC commander Antonio
    Medina. (AP, BBC)
18. **Latin America — Tue 24 Nov — MEXICO INFLATION 3.96%.** Six-month high
    (INEGI); core eases to 3.68%; central bank seen on hold in December.
    (Reuters)
19. **Latin America — Mon 23 Nov — WOMEN'S WORLD CUP 2031: USA, MEXICO,
    COSTA RICA, JAMAICA.** FIFA: first 48-team edition, first in 4 nations;
    2035 to UK & Ireland. (FIFA, CNN)
20. **Latin America — Wed 25 Nov — CITI WEIGHS RETURN TO VENEZUELA.** 5
    years after exit (Reuters 25 Nov); US to control Venezuela oil sales
    indefinitely. (Reuters)
21. **Europe — Tue 24 Nov — SARKOZY & BRUNI TO STAND TRIAL.** Witness-tampering
    case over Libya-funding testimony; trial Nov–Dec 2027, up to 10 years; 11
    defendants. (Reuters, Le Monde)
22. **Europe — Tue 24 Nov — GERMAN IFO RISES TO 90.6.** November business
    sentiment, above consensus 90.5. (Reuters)
23. **Europe — Tue 24 Nov — MOST GERMANS NOW OPPOSE ARMS AID TO KYIV.**
    Koerber Stiftung survey; reversal from a year ago. (Reuters)
24. **Africa — Sun 22 Nov — UKRAINE SINKS RUSSIAN CORVETTE MERKURY.** 7 sea
    drones sink Steregushchiy-class corvette (1,800 t, commissioned 2023) at
    Benghazi naval base, Libya; Ka-27 helicopter destroyed; cargo ship MV
    Angara hit. (CNN, WSJ)
25. **Africa — Sun 22 Nov, reported Tue 24 Nov — CONGO PLANE MISSING; REBELS
    CLAIM SHOOT-DOWN.** Cessna 208 lost Beni→Kalemie; FRN rebels CLAIM they
    shot it down (CLAIM — unverified, BBC).
26. **Africa — Tue 24 Nov — NIGERIA KING, 92, SUSPENDED.** After sexual
    misconduct allegation (BBC headline only — no name or kingdom details).
27. **Middle East — Tue 24 Nov — ISRAEL KILLS HAMAS SECURITY CHIEF.**
    Airstrike kills Naeem Abu Nahel, Hamas internal security director (2
    months in post) + 6 others in western Gaza City, amid fragile ceasefire.
    (Al Jazeera, BBC)
28. **Middle East — Mon 23 Nov — IRGC CLAIMS 3 TANKERS HIT MINES IN HORMUZ.**
    6 tankers since Sun 22 Nov (CLAIM — no ship names/flags; CENTCOM silent;
    present as a claim, NOT fact). (AP, Reuters)
29. **Middle East — Tue 24 Nov — SYRIA LANDMINE TOLL SOARS.** 1,602
    killed/wounded by landmines in 2025 (+50%); children ~37%; only Myanmar
    higher (1,891). (BBC, UN News)
30. **Middle East — Wed 25 Nov — JORDAN SENTENCES MAN TO DEATH.** State
    Security Court sentences man to death over attack that killed an officer.
    (Reuters)
31. **East Asia — Tue 24 Nov — CHINA PROBES POLITBURO MEMBER.** Chen Jining,
    Shanghai party chief, under investigation (Xinhua); 4th member of top
    leadership body probed since 2025. (Reuters)
32. **South & Southeast Asia — Tue 24 Nov — NEPAL QUAKE 5.6.** Near Tibet
    border (Taplejung); felt to Dhaka; no major casualties reported. NOT the
    2023 quake. (Himalayan Times)
33. **South & Southeast Asia — Mon 23 Nov — 14 NATIONS BACK ICJ ROHINGYA
    GENOCIDE RULING.** UK, Spain, Canada, Australia among them; Myanmar ruled
    to have committed genocide. (Al Jazeera)
34. **South & Southeast Asia — Tue 24 Nov — HASINA PLANS RETURN 16 DEC.**
    Ex-PM to end 2+ years exile in India (PLANNED, not happened). (Reuters)
35. **Oceania/Pacific — Sun 22 Nov — COP31 COLLAPSES WITH NO DEAL.** Antalya;
    longest COP ever; fossil-fuel transition language dropped; >190 nations
    present (no US). (CNN, Reuters)
36. **Oceania/Pacific — Sun 22 Nov — AUSTRALIA SWEEPS FRANCE 4-0, BJK CUP.**
    Play-off in Le Portel; Maya Joint wins 2 rubbers in a day; Australia to
    April 2027 qualifiers. (AAP)
37. **Oceania/Pacific — Tue 24 Nov — UNAIDS: AIDS DEATHS LOWEST IN 20 YEARS.**
    ~570,000 in 2025; but funding down 18%, US contribution −26%. (Reuters)

### Region count (9 regions, 37 stories)

North America 6 · Latin America 4 · Europe 5 · Africa 5 · Middle East 6 ·
Central Asia 1 · East Asia 3 · South & Southeast Asia 3 · Oceania/Pacific 4.

## DATE CHECK

Every story is tagged with its REAL date. 34 stories are 23–25 Nov; 3 are
SUN 22 NOV and are tagged so: #24 Merkury sunk, #35 COP31 collapses, #36 BJK
Cup 4-0 — all still headline news on 25 Nov.

NOT included on purpose: Hurricane Melissa (date unverified for 25 Nov 2026)
and "Democrats clinch House majority" (exact date unverified). Claims are
labelled CLAIM: #25 FRN shoot-down claim, #28 IRGC tanker claim; #12 is a
REPORT (Western intel report of a nuclear-armed "Sputnik-S" satellite),
not a confirmed launch. The CIA breach (#2) hit UNCLASSIFIED systems only;
classified systems were NOT affected.

## How it runs

```sh
# Mode 1: output directory from the environment (the grader's mode)
MAKEFUN_OUTPUT_DIR=out python3 main.py        # writes out/entry.png

# Mode 2: standard output (binary PNG on stdout)
python3 main.py > entry.png

# Mode 3: explicit path argument
python3 main.py out/entry.png
```

All three modes write byte-identical output: the decoded, validated PNG
(1024×1024, 73,622 bytes, sha256
`faad68087a65a30fb07c9de2c741d46ef5dd0dfe54f52d35e0d70a7fd5c73d5c`).
Standard library only — no Pillow, no network, no system fonts. To rebuild
the image from scratch: `python3 render.py` (needs Pillow locally).
