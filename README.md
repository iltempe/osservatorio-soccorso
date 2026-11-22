# Osservatorio Sottopasso del Soccorso

Monitoraggio civico del raddoppio della Declassata (SS 719, viale Leonardo da Vinci) al Soccorso, a Prato: costi, cronoprogramma, atti e finanziamenti, dall'annuncio a oggi. Ogni dato ha la sua fonte.

Aggiornato al **2026-11-22**. A cura di Matteo Tempestini (@iltempe) – PratoMiMuovo.

## Sito

Online: https://iltempe.github.io/osservatorio-soccorso/

Il sito è `index.html`, una pagina unica senza dipendenze esterne.

## Dati

File CSV in UTF-8, separatore virgola. Ogni riga ha la colonna `fonti` (codici F01…) e `fonti_url` (link completi).

| File | Contenuto |
|---|---|
| [`dati/cronoprogramma_gantt.csv`](dati/cronoprogramma_gantt.csv) | Cronoprogramma (solo date ufficiali): fasi, atti, date previste, ritardi |
| [`dati/cronoprogramma.csv`](dati/cronoprogramma.csv) | Passi dell'iter con data ufficiale, previsione ufficiale e ritardo |
| [`dati/costi.csv`](dati/costi.csv) | Costo del tunnel nel tempo (solo cifre ufficiali) |
| [`dati/quadro_economico.csv`](dati/quadro_economico.csv) | Quadro economico del progetto definitivo (29/10/2024) |
| [`dati/coperture.csv`](dati/coperture.csv) | Coperture finanziarie del quadro economico |
| [`dati/atti_finanziamento.csv`](dati/atti_finanziamento.csv) | Atti di finanziamento (Governo, CIPE/CIPESS, Anas) |
| [`dati/opere_collegate.csv`](dati/opere_collegate.csv) | Opere collegate: complanari e strada Prato-Campi |
| [`dati/fasi_cantiere.csv`](dati/fasi_cantiere.csv) | Le quattro fasi del cantiere (Comune 2026 e cronoprogramma Anas 2018) |
| [`dati/eventi.csv`](dati/eventi.csv) | Cronologia completa degli eventi, con fonti |
| [`dati/promesse.csv`](dati/promesse.csv) | Date di avvio annunciate (anche riportate dalla stampa) |
| [`dati/documenti_progetto.csv`](dati/documenti_progetto.csv) | Documenti di progetto e dove leggerli |
| [`dati/fonti.csv`](dati/fonti.csv) | Elenco delle fonti con URL |
| [`dati/soccorso.json`](dati/soccorso.json) | Tutti i dati in un unico file JSON |

## Metodo

- Il **cronoprogramma** e i **costi aggiornati** usano solo atti e siti ufficiali (Anas, Commissario straordinario, Ministeri, CIPE/CIPESS, Regione Toscana, Comune di Prato). Nessuna stima né proiezione.
- Il **ritardo** è indicato solo quando un ente aveva dichiarato una data ufficiale ed è calcolato tra due date ufficiali.
- Le date annunciate a voce e riportate dalla stampa sono nella sezione «Promesse sui tempi», separate dal cronoprogramma.
- Le somme fatte da noi (es. totale tunnel + opere collegate) sono segnalate come tali.
- Per rigenerare sito e CSV: `python3 sorgente/build.py` (legge `sorgente/data.json` e `sorgente/template.html`).

## Fonti

- **F01** – [Comune di Prato – Relazione generale VIA, raddoppio viale Leonardo da Vinci in sopraelevazione (giugno 2011)](https://va.mite.gov.it/File/Documento/58815) – Comune di Prato (portale VIA del Ministero dell'Ambiente) (atto ufficiale)
- **F02** – [Tunnel Soccorso, presto il nome della ditta](https://www.lanazione.it/prato/cronaca/tunnel-soccorso-presto-il-1e3d405a) – La Nazione (stampa)
- **F03** – [Raddoppio Declassata al Soccorso: un piano per evitare la paralisi del traffico durante i lavori (maggio 2015)](https://www.tvprato.it/archivio/2015/05/raddoppio-declassata-al-soccorso-un-piano-per-evitare-la-paralisi-del-traffico-ma-il-comune-deve-acquisire-i-terreni-e-va-abbattuto-un-capannone/?mobile=true) – TV Prato (stampa)
- **F04** – [Prato: firmato protocollo tra Comune e Anas per il raddoppio di un tratto di strada nel centro urbano (20/10/2016)](https://stradeanas.it/it/printpdf/82960) – Anas (comunicato ufficiale)
- **F05** – [Presentato il progetto da 31 milioni di raddoppio della Declassata al Soccorso (2/3/2017)](https://www.territorialmente.it/wordpress/wp-content/uploads/2017/03/2-mar-TIRR-PO.-Prato.-Tunnel-parco-e-nuova-strada-a-due-corsie.pdf) – Il Tirreno (rassegna Territorialmente) (stampa)
- **F06** – [Ecco gli ultimi 5 milioni per il sottopasso al Soccorso (19/4/2017)](https://iltirreno.gelocal.it/prato/cronaca/2017/04/19/news/ecco-gli-ultimi-5-milioni-per-il-sottopasso-al-soccorso-1.15216935) – Il Tirreno (stampa)
- **F07** – [Prato: il progetto del sottopasso al Soccorso (19/3/2018)](https://www.pratosfera.com/2018/03/19/progetto-sottopasso-soccorso-prato/) – Pratosfera (stampa)
- **F08** – [Consiglio comunale, atto n. 228 del 02/07/2020 – Interrogazione sullo stato manutentivo della Declassata](https://pubblicazioneatti.comune.prato.it/doc/prato/IM_2020_0000228_6.pdf) – Comune di Prato (atto ufficiale)
- **F09** – [La seconda complanare al Soccorso sarà pronta entro primavera (ottobre 2019)](https://www.tvprato.it/2019/10/la-seconda-complanare-al-soccorso-sara-pronta-entro-primavera-tempi-piu-lunghi-per-il-sottopasso-foto/) – TV Prato (stampa)
- **F10** – [Inaugurate le complanari del Soccorso, ma per il raddoppio della Declassata altri anni di attesa (febbraio 2021)](https://www.tvprato.it/archivio/2021/02/inaugurate-le-complanari-del-soccorso-ma-per-il-raddoppio-della-declassata-altri-anni-di-attesa-foto/) – TV Prato (stampa)
- **F11** – [Inaugurata la seconda complanare al Soccorso. I lavori per il tunnel al via entro la primavera 2024 (2021)](https://www.notiziediprato.it/vita-in-citta/inaugurata-la-seconda-complanare-al-soccorso-i-lavori-per-il-tunnel-al-via-entro-la-primavera-2024/) – Notizie di Prato (stampa)
- **F12** – [Commissario straordinario SS64 – Determinazione motivata di conclusione della Conferenza di Servizi (firmata 3/10/2023)](https://accountability-backend.mit.gov.it/storage/documents/294/RmpNJJ84iNuxZcSqOKovocRlIQp4cHkSkJ0bkFdz.pdf) – Commissario straordinario Anas (portale MIT) (atto ufficiale)
- **F13** – [Commissario straordinario SS64 – Approvazione del progetto definitivo per appalto integrato (firmata 29/10/2024)](https://accountability-backend.mit.gov.it/storage/documents/294/DUdsBh8IZdeJr6NMhPimkRhGj56X4PeoofgAqYWg.pdf) – Commissario straordinario Anas (portale MIT) (atto ufficiale)
- **F14** – [Regione Toscana – parere sul procedimento VIA nazionale (documento sul portale VIA)](https://va.mite.gov.it/File/Documento/817515) – Regione Toscana (portale VIA del Ministero dell'Ambiente) (atto ufficiale)
- **F15** – [Sottopasso Soccorso: i costi lievitano a 69 milioni e ne mancano ancora 30 (febbraio 2024)](https://www.tvprato.it/2024/02/sottopasso-soccorso-i-costi-lievitano-a-69-milioni-e-ne-mancano-ancora-30-incognita-sui-tempi-di-appalto-della-gara/) – TV Prato (stampa)
- **F16** – [Soccorso, i soldi ci sono tutti. Da Roma 29 milioni per il tunnel (2024)](https://www.lanazione.it/prato/cronaca/soccorso-i-soldi-ci-sono-tutti-da-roma-29-milioni-per-il-tunnel-anas-puo-procedere-con-la-gara-5c915711) – La Nazione (stampa)
- **F17** – [La storia infinita. Tunnel del Soccorso, attesa gara d'appalto (2024)](https://www.lanazione.it/prato/cronaca/declassata-dfoxio8j) – La Nazione (stampa)
- **F18** – [Declassata Soccorso, Anas aggiudica i lavori alla Manelli Impresa Spa (settembre 2025)](https://www.tvprato.it/2025/09/declassata-soccorso-anas-aggiudica-i-lavori-alla-mannelli-impresa-spa/) – TV Prato (stampa)
- **F19** – [Raddoppio Declassata al Soccorso, Anas aggiudica i lavori per realizzare il tunnel (24/9/2025)](https://www.lanazione.it/prato/cronaca/raddoppio-declassata-soccorso-x3c1ssb8) – La Nazione (stampa)
- **F20** – [Sottopasso del Soccorso, il via al cantiere tra un anno (5/11/2025)](https://www.tvprato.it/sottopasso-del-soccorso-il-via-al-cantiere-tra-un-anno/) – TV Prato (stampa)
- **F21** – [Sottopasso Soccorso, Anas detta le tempistiche: il cantiere aprirà a fine 2026, poi 1.100 giorni di lavoro](https://www.notiziediprato.it/attualita/sottopasso-soccorso-anas-detta-le-tempistiche-il-cantiere-aprira-a-fine-2026-poi-1-100-giorni-di-lavoro-via-al-tavolo-tecnico-per-mitigare-i-disagi/) – Notizie di Prato (stampa)
- **F22** – [Sottopasso Soccorso, i lavori saranno realizzati dalla CMC guidata da Antonio Politano (aprile 2026)](https://www.tvprato.it/sottopasso-soccorso-i-lavori-saranno-realizzati-dalla-cmc-guidata-da-antonio-politano/) – TV Prato (stampa)
- **F23** – [Tunnel del Soccorso. In campo Cmc di Politano. Progetto da 47 milioni (2/4/2026)](https://www.lanazione.it/prato/cronaca/tunnel-del-soccorso-in-436c206d) – La Nazione (stampa)
- **F24** – [Raddoppio Soccorso, entro qualche mese il progetto esecutivo poi l'inizio dei lavori (17/7/2026)](https://www.notiziediprato.it/attualita/raddoppio-soccorso-entro-qualche-mese-il-progetto-esecutivo-poi-linizio-dei-lavori-il-sindaco-cantiere-impattante-ma-opera-vitale/) – Notizie di Prato (stampa)
- **F25** – [Sottopasso del Soccorso. Finalmente c'è il piano (3/10/2026)](https://www.quotidiano.net/economia/mobilita/sottopasso-del-soccorso-finalmente-ce-75cb2aff) – QN Mobilità (stampa)
- **F26** – [Consiglio comunale: il sindaco rassicura sui lavori del sottopasso al Soccorso (8/10/2026)](https://www.notiziediprato.it/politica/consiglio-comunale-prima-lo-scontro-tra-maggioranza-e-opposizione-sulle-procedure-poi-il-sindaco-rassicura-sui-lavori-del-sottopasso-al-soccorso/) – Notizie di Prato (stampa)
- **F27** – [Finanziata la strada Prato-Campi, Biffoni: opzione di viabilità alternativa al tunnel del Soccorso, ma potrebbe arrivare tardi (21/11/2026)](https://www.tvprato.it/finanziata-la-strada-prato-campi-biffoni-opzione-viabilita-alternativa-tunnel-soccorso-ma-potrebbe-arrivare-tardi/) – TV Prato (stampa)
- **F28** – [Scheda dell'intervento – Commissario straordinario Mucilli, SS64 Collegamento svincoli Prato Est-Ovest](https://www.stradeanas.it/sites/default/files/commissari_anas/ANAS_Mucilli_SS64_Prato.pdf) – Anas (atto ufficiale)
- **F29** – [Sottopasso del Soccorso – elenco completo dei documenti in consultazione](https://comune.prato.it/muoversi/viabilita-e-lavori-pubblici/sottopasso-del-soccorso/elenco-completo-di-tutti-i-documenti-in-consultazione/media2057.php) – Comune di Prato (sito ufficiale)
- **F30** – [Sottopasso del Soccorso – pagina del progetto (aggiornata al 3/3/2026)](https://www.comune.prato.it/it/muoversi/viabilita/sottopasso-soccorso/pagina242.html) – Comune di Prato (sito ufficiale)
- **F31** – [Nuove strade per la viabilità alternativa (Complanari)](https://www.comune.prato.it/it/muoversi/viabilita/sottopasso-soccorso/complanari/pagina1290.html) – Comune di Prato (sito ufficiale)
- **F32** – [Verifica di assoggettabilità a VIA – Sottopasso del Soccorso](https://www.comune.prato.it/it/muoversi/viabilita/sottopasso-soccorso/verifica-via-sottopasso/pagina1291.html) – Comune di Prato (sito ufficiale)
- **F33** – [Elenco completo dei documenti del progetto di fattibilità (forniti da Anas)](https://www.comune.prato.it/it/muoversi/viabilita/sottopasso-soccorso/verifica-via-sottopasso/elaborati/pagina1308.html) – Comune di Prato (sito ufficiale)
- **F34** – [VIA sul progetto di raddoppio Declassata al Soccorso](https://www.comune.prato.it/it/muoversi/viabilita/sottopasso-soccorso/via/pagina1791.html) – Comune di Prato (sito ufficiale)
- **F35** – [Progetto di fattibilità – Computo metrico estimativo](https://www.comune.prato.it/sito-comunale/muoversi/viabilita-e-lavori-pubblici/sottopasso-del-soccorso/elenco-completo-di-tutti-i-documenti-in-consultazione/media2040.php) – Anas (pubblicato dal Comune di Prato) (atto ufficiale)
- **F36** – [Parere ARPAT sulla verifica di assoggettabilità a VIA (2018)](https://www.comune.prato.it/muoversi/viabilita-e-lavori-pubblici/sottopasso-del-soccorso/osservazioni-e-pareri-al-progetto-del-sottopasso/media2103.php) – ARPAT (pubblicato dal Comune di Prato) (atto ufficiale)
- **F37** – [Relazione di riscontro alle osservazioni (giugno 2018)](https://www.comune.prato.it/muoversi/viabilita-e-lavori-pubblici/sottopasso-del-soccorso/osservazioni-e-pareri-al-progetto-del-sottopasso/media2107.php) – Anas (pubblicato dal Comune di Prato) (atto ufficiale)
- **F38** – [Consiglio comunale, adunanza del 9 marzo 2017 – verbale (variante per il Soccorso)](https://odg.comune.prato.it/doc/ODG1074.pdf) – Comune di Prato (atto ufficiale)
- **F39** – [Consuntivo Piano della Performance 2016 – obiettivo 2016-GS03](https://archiviositi.comune.prato.it/trasparenza/performance/performance-relazione/archivio/2016/consuntivo-obiettivi-2016.pdf) – Comune di Prato (atto ufficiale)
- **F40** – [Consuntivo PEG/Piano della Performance 2018](https://archiviositi.comune.prato.it/trasparenza/performance/performance-relazione/archivio/2018/consuntivo-peg-2018-obiettivi.pdf) – Comune di Prato (atto ufficiale)
- **F41** – [PUMS – stato di attuazione (ottobre 2022), intervento R3](https://www2.comune.prato.it/pums/doc-pums/media3963.php) – Comune di Prato (atto ufficiale)
- **F42** – [Progetto definitivo – Relazione generale (procedura VIA)](https://va.mite.gov.it/File/Documento/500234) – Anas (portale VIA del Ministero dell'Ambiente) (atto ufficiale)
- **F43** – [Progetto definitivo – Relazione della cantierizzazione (procedura VIA)](https://va.mite.gov.it/File/Documento/500349) – Anas (portale VIA del Ministero dell'Ambiente) (atto ufficiale)
- **F44** – [Studio di impatto ambientale – Atmosfera (procedura VIA)](https://va.mite.gov.it/File/Documento/500187) – Anas (portale VIA del Ministero dell'Ambiente) (atto ufficiale)
- **F45** – [Delibera CIPE n. 54 del 1/12/2016 – FSC 2014-2020, Piano operativo infrastrutture (GU n. 88 del 14/4/2017)](https://territorio.regione.emilia-romagna.it/qualita-urbana/misure-e-contributi/bando-ru/norme-bando-ru/dcipe-54-2016/@@download/file) – CIPE (copia della Gazzetta Ufficiale) (atto ufficiale)
- **F46** – [Piano operativo FSC Infrastrutture 2014-2020 (delibera CIPE 54/2016) – documentazione](https://mit.gov.it/documentazione/secondo-addendum-piano-operativo-fondo-sviluppo-e-coesione-infrastrutture-del-cipe-n) – Ministero delle Infrastrutture e dei Trasporti (atto ufficiale)
- **F47** – [CIPE, esito della seduta del 7 agosto 2017 – Contratto di programma Anas 2016-2020](https://programmazioneeconomica.gov.it/media/ball4odl/esito.pdf) – CIPE (atto ufficiale)
- **F48** – [Contratto di programma 2016-2020 MIT-Anas e aggiornamento 2018-2019 (delibera CIPE 36/2019)](https://mit.gov.it/node/7410) – Ministero delle Infrastrutture e dei Trasporti (atto ufficiale)
- **F49** – [CIPESS, esito della seduta del 21 marzo 2024 – Contratto di programma Anas 2021-2025](https://programmazioneeconomica.gov.it/media/z2ljmlw5/esito-cipess-21-marzo-2024.pdf) – CIPESS (atto ufficiale)
- **F50** – [Contratto di programma MIT-Anas 2021-2025 – Aggiornamento 2025 (premesse: delibera CIPESS 6/2024, firma 24/9/2024, efficacia 22/10/2024)](https://www.mit.gov.it/nfsmitgov/files/media/documentazione/2025-10/Articolato_AllegatiAggiornamento2025CdP2021-2025-signed.pdf) – Ministero delle Infrastrutture e dei Trasporti (atto ufficiale)
- **F51** – [Bilancio di fine mandato del Comune di Prato](https://governo.comune.prato.it/sito-comunale/governo/sindaco/relazione-fine-mandato/media16529.php) – Comune di Prato (atto ufficiale)
- **F52** – [Presentazione del progetto del Sottopasso a cura di Anas (19 marzo 2018)](https://www.comune.prato.it/sito-comunale/muoversi/viabilita-e-lavori-pubblici/sottopasso-del-soccorso/media1989.php) – Anas (pubblicato dal Comune di Prato) (atto ufficiale)
- **F53** – [Progetto di fattibilità 2018 – Quadro economico (elaborato T00_CM00_CMS_EC01_A)](https://www.comune.prato.it/sito-comunale/muoversi/viabilita-e-lavori-pubblici/sottopasso-del-soccorso/elenco-completo-di-tutti-i-documenti-in-consultazione/media2041.php) – Anas (pubblicato dal Comune di Prato) (atto ufficiale)
- **F54** – [Progetto di fattibilità 2018 – Cronoprogramma (elaborato T00_CM00_CMS_EC02_A, emissione 22/02/2018)](https://www.comune.prato.it/sito-comunale/muoversi/viabilita-e-lavori-pubblici/sottopasso-del-soccorso/elenco-completo-di-tutti-i-documenti-in-consultazione/media2042.php) – Anas (pubblicato dal Comune di Prato) (atto ufficiale)
- **F55** – [VIA nazionale – parere favorevole, documento integrale](https://www.comune.prato.it/sito-comunale/muoversi/viabilita-e-lavori-pubblici/sottopasso-del-soccorso/media15574.php) – Comune di Prato (atto ufficiale)
- **F56** – [Procedura VIA sul portale del Ministero dell'Ambiente – documentazione](https://va.mite.gov.it/it-IT/Oggetti/Documentazione/7897/11566) – Ministero dell'Ambiente (atto ufficiale)
- **F57** – [Regione Toscana, Delibera di Giunta n. 478 del 20/04/2026 – Protocollo d'intesa Regione-Prato-Campi per il collegamento viale Aldo Moro-viale Narciso Parigi](https://www301.regione.toscana.it/bancadati/atti/Contenuto.xml?id=5510836&nomeFile=Delibera_n.478_del_20-04-2026) – Regione Toscana (atto ufficiale)
- **F58** – [Allegato 1 alla DGR 478/2026 – Schema di Protocollo d'intesa (con le premesse del Comune di Prato sul cantiere della SS 719)](https://www301.regione.toscana.it/bancadati/atti/Contenuto.xml?id=5510837&nomeFile=Delibera_n.478_del_20-04-2026-Allegato-1) – Regione Toscana (atto ufficiale)
- **F59** – [Prato Campi Bisenzio, Giani: sei milioni per realizzare la variante di Capalle (20/11/2026)](https://www.toscana-notizie.it/-/prato-campi-bisenzio-giani-sei-milioni-per-realizzare-la-variante-di-capalle-) – Regione Toscana – Toscana Notizie (comunicato ufficiale)
- **F60** – [Bilancio regionale 2026-2028, il Consiglio approva la terza variazione (18/11/2026)](https://www.gonews.it/2026/11/18/bilancio-regionale-2026-2028-il-consiglio-approva-la-terza-variazione/) – gonews.it (stampa)

## Licenza

Dati, testi e sito sono distribuiti con licenza [Creative Commons Attribuzione 4.0 Internazionale (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.it). Puoi riusarli citando: «Osservatorio Sottopasso del Soccorso – PratoMiMuovo (Matteo Tempestini)», con il link a questo repository. I documenti delle fonti restano dei rispettivi titolari.

## Correzioni

Se trovi un errore o un atto mancante, apri una issue con il link alla fonte.

