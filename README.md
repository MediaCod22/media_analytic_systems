# Media Analytics Systems — Research Data Repository

> **Research:** «Режимы аналитической работы с медиаданными: от измерений к поддержке принятия решений»
> 
> **Author:** Sergey V. Vodopetov, PhD (RUDN University, Moscow)
> 
> **ORCID:** [0000-0002-5237-4464](https://orcid.org/0000-0002-5237-4464) | **RSCI ID:** 835749 | **SPIN:** 5530-2581

[![Open Science](https://img.shields.io/badge/Open%20Science-FAIR-blue)](https://www.go-fair.org/fair-principles/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## 📖 About This Research / О исследовании

### What We Studied / Что исследовалось

This study examines the transformation of media analytics systems from monitoring tools into **Decision Support Infrastructure**. We analyzed how media data workflows evolve from simple measurement to predictive analytics across three academic discourses: **Russian, International (English), and Chinese**.

**Key question:** Why does Russia demonstrate strong media measurement and monitoring capabilities (33% of publications mention systems), yet only **8%** explicitly connect them to decision-making — compared to **35%** in China?

### Research Design / Дизайн исследования

- **Corpus:** 804 publications → 327 final analytical sample (PRISMA protocol)
- **Databases:** Google Scholar (international), eLibrary/РИНЦ (Russian), CNKI (Chinese)
- **Period:** 2019–2024 (dynamics), 2019–2025 (thematic scope)
- **Extended corpus:** 477 additional Russian publications for deeper analysis
- **Coding:** Thematic analysis (Braun & Clarke) + OSINT methodology
- **Reliability:** Cohen's Kappa = 0.84 (thematic), 0.91 (DSS-link)

### Main Finding / Главный результат

Russia leads in **media measurement infrastructure** (Mediascope as national standard) and **national media coverage** (Brand Analytics, СКАН). However, the gap to China in **DSS institutionalization** is **4.4×** (8% vs 35%). This is not technological lag — it's an **organizational and methodological barrier** preventing transition from data collection to decision-making.

### Five Analytical Modes / Пять режимов аналитики

| Mode | Russian Strength | International | Chinese | What It Produces |
|------|-----------------|---------------|---------|-----------------|
| **1. Media Measurement** | Mediascope (national panel) | Nielsen | — | Attention, reach, contact |
| **2. National Media Coverage** | Brand Analytics, СКАН | Factiva, LexisNexis | Yuqing platforms | System observation, narratives |
| **3. OSINT / Data Journalism** | OSINT + BA/СКАН | GDELT + tools | Yuqing analysis practices | Event reconstruction |
| **4. Support / Predictive** | Талисман, risk analytics | Signal AI, Dataminr | Sina Yuqing / Wisers | Scenarios, early warning |
| **5. AI-Native Layer** | Research LLM pipelines | Dataminr, Signal AI | Midu / LLM reporting | Signal automation |

---

## 📊 Complete Tools Registry (52 Systems)

**[→ View Full Registry with Weights](TOOLS_REGISTRY.md)**

| Contour | Count | Key Systems |
|---------|-------|-------------|
| 🇷🇺 Russian | 18 | Mediascope, Brand Analytics, СКАН, Kribrum, YouScan, IQBuzz, Талисман, Semantrum |
| 🌍 International | 24 | Nielsen, Factiva, LexisNexis, Brandwatch, Meltwater, Sprinklr, GDELT, Signal AI, Dataminr |
| 🇨🇳 Chinese | 10 | Midu, Sina Yuqing, Wisers, Qingbo, People's Daily Yuqing |

---

## 📁 Repository Structure

```
media_analytic_systems/
├── README.md                              # This file — overview + research context
├── README_OPEN_SCIENCE.md                 # Companion to Open Science package
├── TOOLS_REGISTRY.md                      # Full registry: 52 tools with weights
├── CITATION.cff                           # Citation metadata
├── LICENSE                                # CC BY 4.0
│
├── data/
│   ├── derived/
│   │   ├── publication_statistics.csv     # Corpus-level stats
│   │   ├── dss_comparison.csv             # DSS-link by contour
│   │   ├── analytical_modes_typology.csv  # Mode classification
│   │   ├── prisma_flow_counts.csv         # PRISMA selection stages ⭐
│   │   ├── tools_registry_full.csv        # 52 tools with weights
│   │   └── intercoder_reliability.csv     # Cohen's Kappa results ⭐
│   └── processed/
│       └── master_publications_coded.csv  # ⭐ Master dataset (anonymized)
│
├── tables/
│   ├── table_1_comparative_sample.csv     # Table 1 from article
│   ├── table_2_analytical_modes.csv       # Table 2 from article
│   ├── table_3_tools_registry.csv         # Tools summary
│   └── prisma_flow_table.csv              # ⭐ PRISMA stages
│
├── methodology/
│   ├── prisma_protocol.md                 # PRISMA 2020 protocol
│   ├── search_strategy.md                 # Search strings per database
│   ├── codebook.md                        # ⭐ Coding definitions & rules
│   ├── reproducibility_protocol.md
│   ├── limitations_and_bias.md
│   ├── tools_identification_protocol.md   # How 52 tools were identified
│   └── why_h_index_was_not_used.md        # ⭐ Methodological disclaimer
│
├── figures/
│   └── prisma_flow_diagram.png            # ⭐ PRISMA flowchart
│
├── results/
│   ├── key_findings_open_science.md
│   └── interpretation_notes.md
│
├── scripts/
│   └── validate_tables.py                 # Validation script
│
├── metadata/
│   ├── CITATION.cff
│   ├── codemeta.json
│   └── dataset_metadata.json
│
└── docs/
    ├── open_science_checklist.md
    └── github_release_notes.md
```

---

## 🔬 Methodology Highlights

### PRISMA Protocol
Systematic literature selection from three databases. See `methodology/prisma_protocol.md` for full flow.

**Key numbers:**
- **804** → initial search results
- **327** → final analytical sample (112 Google Scholar, 95 РИНЦ, 120 CNKI)
- **477** → extended Russian corpus

### Coding Reliability / Надёжность кодирования

Verified by **3 independent coders**:

| Dimension | Cohen's Kappa | Interpretation |
|-----------|---------------|----------------|
| Thematic classification | **0.84** | Almost perfect |
| DSS-link determination | **0.91** | Almost perfect |
| Mode assignment | **0.79** | Substantial |

See: `data/derived/intercoder_reliability.csv` and `methodology/codebook.md`

### Why We Don't Use H-Index for Systems / Почему h-index не используется

> ⚠️ **Important methodological note:** In the final version, **h-index of platforms is NOT used** as a quality indicator. Initial bibliometric evaluations are preserved only as auxiliary heuristics for scientific visibility and do NOT participate in main conclusions.
> 
> Rationale: h-index measures **author productivity**, not **analytical power of tools**. Applying it to software platforms is methodologically incorrect.
>
> See full explanation: `methodology/why_h_index_was_not_used.md`

---

## 📜 License

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)

---

## 📚 How to Cite

### APA 7
Vodopetov, S. V. (2025). *Modes of analytical work with media data: From measurement to decision support*. Vestnik PGU. https://github.com/MediaCod22/media_analytic_systems

### ГОСТ Р 7.0.5-2008
Водопетов С.В. Режимы аналитической работы с медиаданными: от измерений к поддержке принятия решений // Вестник ПГУ. — 2025. — № X. — С. XX–XX.

---

*Repository created: 2026-05-14 | Last updated: 2026-05-14*
*This repository follows FAIR principles and PRISMA 2020 guidelines*
