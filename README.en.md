# Soccorso Underpass Observatory (Prato, Italy)

🇬🇧 English · 🇮🇹 [Italiano](README.md)

Civic monitoring of the doubling of the Declassata ring road (SS 719, viale Leonardo da Vinci) at Soccorso, Prato, Italy: a 400 m four-lane cut-and-cover tunnel built by Anas. Costs, schedule, records and funding from the first announcement to today. **Every figure links to its source.**

Updated **2026-11-22**. By Matteo Tempestini – [github.com/iltempe](https://github.com/iltempe) – mtempestini@gmail.com

**Site (in Italian):** https://iltempe.github.io/osservatorio-soccorso/

## Key figures (official records only)

| | |
|---|---|
| Cost estimate, March 2017 | €31 million |
| Cost estimate, feasibility study 2018 | €43.4 million |
| Cost estimate, final design (29 Oct 2024) | €67.3 million (+117% vs 2017) |
| Works duration | 900 days (2018 schedule) → 1,100 days (2024 final design) |
| Contract awarded | September 2025 |
| Construction start | not yet started; the City expects end of 2026 |
| Actual spend | not published |

## Method

- Schedule and costs come only from official records and public bodies' websites (Anas, the Extraordinary Commissioner, Italian ministries, CIPE/CIPESS, Tuscany Region, City of Prato). No estimates, no projections.
- A delay is shown only when an authority had set an official date, and it is computed between two official dates.
- Dates announced verbally and reported by the press are kept apart, in the "Promesse sui tempi" (statements on timing) section.
- Sums we computed are flagged as such.
- Missing data is declared, not estimated.
- To rebuild the site and the CSVs: `python3 sorgente/build.py`.

## Data

UTF-8 CSV files in [`dati/`](dati/), comma-separated, column names in Italian. Each row carries `fonti` (source codes F01…) and `fonti_url` (full links). Main files:

| File | Content |
|---|---|
| `cronoprogramma_gantt.csv` | Schedule (official dates only): phases, records, planned dates, delays |
| `cronoprogramma.csv` | Approval steps with official date, official planned date, delay |
| `costi.csv` | Tunnel cost over time |
| `quadro_economico.csv` | Approved cost breakdown of the final design |
| `coperture.csv`, `atti_finanziamento.csv` | Funding sources and funding decisions |
| `opere_collegate.csv` | Related works: side roads and the Prato-Campi road |
| `fasi_cantiere.csv` | The four construction phases |
| `eventi.csv` | Full timeline |
| `promesse.csv` | Announced start dates, including press reports |
| `documenti_progetto.csv` | Design documents and where to read them |
| `fonti.csv` | The 60 sources with URLs |
| `soccorso.json` | All data in one JSON file |

The full source list is in the [Italian README](README.md#fonti) and in [`dati/fonti.csv`](dati/fonti.csv).

## Reuse it for your city

The generic version of this observatory, with an English template and a Claude skill, is at **[iltempe/osservatorio-civico](https://github.com/iltempe/osservatorio-civico)**.

## License

Data, text and site: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit: "Osservatorio Sottopasso del Soccorso – Matteo Tempestini", with a link to this repository. Source documents remain the property of their owners.

## Corrections

Found an error or a missing record? Open an issue with a link to the source, or write to mtempestini@gmail.com.

Keywords: civic tech, civic hacking, open data, public works monitoring, infrastructure accountability, government transparency, budget tracking, Gantt, Prato, Tuscany, Italy.
