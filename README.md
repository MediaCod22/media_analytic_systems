# Media Analytics Systems — Research Data Repository

> **Research:** «Медиааналитика и поддержка принятия решений в научном дискурсе: систематическое картирование российского, англоязычного и китайского корпусов публикаций»
>
> **Author:** Sergey V. Vodopetov, PhD (RUDN University, Moscow)
>
> **ORCID:** [0000-0002-5237-4464](https://orcid.org/0000-0002-5237-4464) | **RSCI ID:** 835749 | **SPIN:** 5530-2581

[![Open Science](https://img.shields.io/badge/Open%20Science-FAIR-blue)](https://www.go-fair.org/fair-principles/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/version-v1.1.0-blue.svg)](https://github.com/MediaCod22/media_analytic_systems)

---

## 📖 About This Research / О исследовании

### What We Studied / Что исследовалось

The repository accompanies a descriptive systematic mapping of scholarly discourse on media analytics and decision support. The article compares three independently formed publication corpora — **Russian (eLibrary/РИНЦ), international English-language (Google Scholar), and Chinese (CNKI)** — rather than national markets, platform quality, or the actual effectiveness of particular systems.

**Research question:** How is the connection between media analytics and decision support represented in the Russian, international, and Chinese publication corpora?

### Research Design / Дизайн исследования

- **Corpus:** 804 records identified → 477 excluded at screening → 327 publications in the final analytical sample
- **Final sample:** 112 Google Scholar, 95 eLibrary/РИНЦ, 120 CNKI
- **Period:** 2019–2025
- **Method:** descriptive systematic mapping with an adapted PRISMA 2020 selection protocol
- **Coding:** thematic coding by four features — media-data type, system purpose, analytical product, and DSS connection
- **Reliability check:** random 10% subsample (N=33); two independent coders, with a third expert resolving disagreements
- **Cohen's Kappa:** 0.91 (DSS connection), 0.84 (thematic classification)

### Key Observations / Ключевые наблюдения

| Corpus | Publications | Publications mentioning systems | Publications with DSS connection |
|---|---:|---:|---:|
| Google Scholar / international English-language | 112 | 18 (≈16%) | 15 (≈13%) |
| eLibrary/РИНЦ / Russian | 95 | 31 (≈33%) | 8 (≈8%) |
| CNKI / Chinese | 120 | 54 (45%) | 42 (35%) |

These indicators describe the formed scholarly corpora. They must not be interpreted as market shares, platform quality scores, or measures of national technological development.

### Analytical Modes Typology / Типология аналитических режимов

The study identifies five modes of working with media data, distinguished by the analytical product described in publications:

| Mode | Russian example | International example | Chinese example | Analytical product |
|---|---|---|---|---|
| **Media measurement / Медиаизмерения** | Mediascope | Nielsen | — | Reach and contact metrics |
| **Media-space monitoring / Мониторинг медиапространства** | Brand Analytics, СКАН | Factiva, LexisNexis | Yuqing platforms | Mentions, topics, dynamics, narratives |
| **OSINT and data journalism / OSINT и дата-журналистика** | OSINT + BA/СКАН | GDELT + OSINT | Yuqing analysis | Event reconstruction |
| **Decision support and predictive analytics / Поддержка решений и предиктивная аналитика** | Talisman, risk analytics | Signal AI, Dataminr | Sina Yuqing, Wisers | Forecasts, risk assessments, scenarios, recommendations |
| **AI-native mode / ИИ-нативный режим** | Research LLMs | NetBase Quid | Midu | Contextual answer to an open query |

*Note: the typology is not a ranking, software classification, market-maturity model, or sequence of obligatory developmental stages.*

---

## 📊 Complete Tools Registry (50 Systems)

**[→ View Full Registry with Weights](TOOLS_REGISTRY.md)**

| Corpus | Count | Systems |
|---|---:|---|
| 🇷🇺 Russian | 13 | Mediascope; Brand Analytics; СКАН-Интерфакс; Талисман; Kribrum; Medialogia/Медиалогия; YouScan; IQBuzz; Инфосфера; Постман; Semantrum; Полигон; Dalion |
| 🌍 International | 30 | Nielsen; Factiva; LexisNexis; GDELT; Signal AI; Dataminr; Brandwatch; Meltwater; Sprinklr; Talkwalker; Synthesio; Cision; Pulsar; Mention; Hootsuite Insights; Sprout Social; NetBase Quid; Digimind; Agorapulse; Emplifi; Khoros; Reputation.com; Keyhole; Radian6; Buffer Analyze; Later; Traackr; Onalytica; Awario; Zoho Social |
| 🇨🇳 Chinese | 7 | Midu; Sina Yuqing; Wisers; Qingbo; People’s Daily Yuqing; Shiwei; Zhongke Click |

The registry presents the final 50-system version used in the article. Weights indicate normalized mention frequency within each publication corpus, not market share or functional quality.

---

## 📁 Repository Structure

```text
media_analytic_systems/
├── README.md                              # Overview and research context
├── README_OPEN_SCIENCE.md                 # Open Science companion documentation
├── TOOLS_REGISTRY.md                      # Final registry: 50 tools with weights
├── LICENSE                                # CC BY 4.0
│
├── data/
│   ├── derived/
│   │   ├── publication_statistics.csv     # Corpus-level statistics
│   │   ├── dss_comparison.csv             # DSS-link indicators by corpus
│   │   ├── analytical_modes_typology.csv  # Five-mode typology
│   │   ├── prisma_flow_counts.csv         # PRISMA selection stages
│   │   ├── tools_registry_full.csv        # 50 tools with weights
│   │   ├── intercoder_reliability.csv     # Reported Kappa values
│   │   └── intercoder_sample.csv          # Anonymized reliability sample
│   ├── processed/
│   │   └── master_publications_coded.csv  # Anonymized coding-frame excerpt (100 records)
│   └── raw_placeholder/
│       └── README.md                      # Raw-data placement and access policy
│
├── tables/
│   ├── table_1_comparative_sample.csv     # Corpus comparison table
│   ├── table_2_analytical_modes.csv       # Mode characteristics table
│   ├── table_3_tools_registry.csv         # Tools registry CSV
│   └── prisma_flow_table.csv              # PRISMA stages summary
│
├── methodology/
│   ├── prisma_protocol.md                 # Adapted PRISMA 2020 protocol
│   ├── search_strategy.md                 # Database search strings
│   ├── codebook.md                        # Coding definitions and operational rules
│   ├── reproducibility_protocol.md        # Indicator calculation rules
│   ├── limitations_and_bias.md            # Limitations and interpretation boundaries
│   ├── tools_identification_protocol.md   # Tool identification procedure
│   └── why_h_index_was_not_used.md        # Methodological note on h-index
│
├── figures/
│   └── prisma_flow_diagram.md             # Textual PRISMA flowchart
│
├── results/
│   ├── key_findings_open_science.md       # Corpus-bound key findings
│   ├── interpretation_notes.md            # Interpretation notes
│   └── intercoder_reliability.md          # Reliability report
│
├── scripts/
│   ├── validate_tables.py                 # Table validation script
│   └── calculate_kappa.py                 # Cohen's Kappa calculation script
│
├── metadata/
│   ├── CITATION.cff                       # Citation metadata
│   ├── codemeta.json                      # Code metadata
│   └── dataset_metadata.json              # Dataset metadata
│
└── docs/
    ├── open_science_checklist.md
    └── github_release_notes.md
```

---

## 🔬 Methodology

### PRISMA Protocol

Systematic selection from three databases follows an adapted PRISMA 2020 logic. See `methodology/prisma_protocol.md` and `figures/prisma_flow_diagram.md`.

| Stage | Google Scholar | РИНЦ | CNKI | Total |
|---|---:|---:|---:|---:|
| Records identified | 342 | 198 | 264 | **804** |
| Excluded at screening | 230 | 103 | 144 | **477** |
| Final analytical sample | 112 | 95 | 120 | **327** |

### DSS Connection vs. Analytical Mode

Присвоение основного тематического режима и кодирование DSS-связи представляли собой две самостоятельные аналитические процедуры. Тематический режим определялся по доминирующей постановке проблемы и характеру рассматриваемого аналитического продукта. DSS-связь кодировалась более узко — только при наличии в публикации явного перехода от результата анализа к оценке риска, прогнозированию, рекомендации или выбору действия. Поэтому публикации режима поддержки решений не во всех случаях получали значение DSS = 1, тогда как отдельные публикации, отнесённые к мониторинговому или ИИ-нативному режиму, могли содержать явную DSS-связь.

### Inter-Coder Reliability

Reliability was checked on a random 10% subsample (N=33). Two coders independently coded DSS connection and thematic mode; a third expert resolved disagreements.

| Dimension | Cohen's Kappa | Interpretation |
|---|---:|---|
| DSS connection | **0.91** | Almost perfect |
| Thematic classification | **0.84** | Almost perfect |

Materials:

- `data/derived/intercoder_sample.csv` — anonymized 33-record reliability sample;
- `scripts/calculate_kappa.py` — binary and nominal Kappa calculation;
- `results/intercoder_reliability.md` — full reliability report.

### Data Availability Note

Article-level totals are calculated for the full 327-publication corpus. The file `data/processed/master_publications_coded.csv` is an anonymized 100-record coding-frame excerpt provided to document the coding schema; it is not a substitute for the complete corpus. Full texts and protected database exports are not redistributed.

### Why We Don't Use H-Index for Systems

> ⚠️ **Methodological note:** the final version does not use platform h-index as a quality indicator. Initial bibliometric evaluations are retained only as auxiliary heuristics of scholarly visibility and do not participate in the article's conclusions.
>
> See: `methodology/why_h_index_was_not_used.md`

---

## 📜 License

**Data and tables:** [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)

**Scripts:** MIT License (see individual file headers)

**Note:** this repository contains derived data and anonymized metadata only. Full-text publications are not redistributed in compliance with copyright law and database terms.

---

## 📚 How to Cite

### Dataset citation (APA 7)

Vodopetov, S. V. (2026). *Media Analytics Systems Research Data Repository* (Version 1.1.0) [Data set]. GitHub. https://github.com/MediaCod22/media_analytic_systems

### ГОСТ Р 7.0.5-2008

Водопетов С.В. Media Analytics Systems Research Data Repository: набор данных и материалы воспроизводимости. Версия 1.1.0. GitHub, 2026. URL: https://github.com/MediaCod22/media_analytic_systems (дата обращения: 06.08.2026).

### Associated manuscript

Водопетов С.В. Медиааналитика и поддержка принятия решений в научном дискурсе: систематическое картирование российского, англоязычного и китайского корпусов публикаций. Рукопись научной статьи.

---

## 📦 Release

- **Current version:** v1.1.0
- **Version date:** 2026-08-06
- **Archive:** GitHub Releases

---

*Repository version: v1.1.0 | Version date: 2026-08-06*
*This repository follows FAIR principles and uses an adapted PRISMA 2020 selection protocol*
