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

This study examines the relationship between media analytics practices and decision-making frameworks across three academic discourses: **Russian, International (English), and Chinese**. The analysis focuses on how publications in each contour conceptualize the connection between media data analysis and decision support systems (DSS).

**Research question:** How does the frequency of DSS-linking in media analytics publications differ across Russian, international, and Chinese academic discourses?

### Research Design / Дизайн исследования

- **Corpus:** 804 publications identified → 327 final analytical sample (PRISMA 2020 protocol)
- **Databases:** Google Scholar (international), eLibrary/РИНЦ (Russian), CNKI (Chinese)
- **Period:** 2019–2024 (dynamics), 2019–2025 (thematic scope)
- **Extended corpus:** 477 additional Russian publications for contour-specific analysis
- **Coding:** Thematic analysis (Braun & Clarke) with structured codebook
- **Inter-coder reliability:** Cohen's Kappa = 0.84 (thematic classification), 0.91 (DSS-link)

### Key Observations / Ключевые наблюдения

The data indicate varying patterns of DSS-link representation across contours:

| Contour | System mentions | DSS-link | DSS dynamics 2019–2024 |
|---------|----------------|----------|----------------------|
| Google Scholar | 16% | 13% | 8% → 14% |
| РИНЦ | 33% | 8% | 2% → 3% |
| CNKI | 45% | 35% | 28% → 37% |

The Russian corpus demonstrates higher representation of measurement and monitoring modes, while the Chinese corpus shows higher DSS-link frequency. These patterns are descriptive and require further contextual interpretation.

### Analytical Modes Typology / Типология аналитических режимов

The study identifies five conceptual modes of working with media data, based on the analytical outputs described in publications:

| Mode | Representative systems | Primary analytical output |
|------|----------------------|-------------------------|
| **Media Measurement** | Mediascope, Nielsen | Attention, reach, contact metrics |
| **National Media Coverage** | Brand Analytics, СКАН, Factiva, LexisNexis, Yuqing platforms | System observation, narrative identification |
| **OSINT / Data Journalism** | GDELT, OSINT tools | Event reconstruction |
| **Support / Predictive** | Signal AI, Dataminr, Талисман | Scenarios, early warning signals |
| **AI-Native Layer** | Midu, NetBase Quid | Automated signal extraction |

*Note: Mode assignments reflect dominant analytical outputs described in the literature, not evaluative rankings.*

---

## 📊 Complete Tools Registry (52 Systems)

**[→ View Full Registry with Weights](TOOLS_REGISTRY.md)**

| Contour | Count | Key Systems |
|---------|-------|-------------|
| 🇷🇺 Russian | 18 | Mediascope, Brand Analytics, СКАН, Kribrum, YouScan, IQBuzz, Талисман, Semantrum |
| 🌍 International | 24 | Nielsen, Factiva, LexisNexis, Brandwatch, Meltwater, Sprinklr, GDELT, Signal AI, Dataminr |
| 🇨🇳 Chinese | 10 | Midu, Sina Yuqing, Wisers, Qingbo, People's Daily Yuqing |

The registry presents 52 media analytics systems with normalized frequency weights derived from the scientific corpus. Weights indicate relative frequency of mention within each contour, not market share or functional quality.

---

## 📁 Repository Structure

```
media_analytic_systems/
├── README.md                              # Overview and research context
├── README_OPEN_SCIENCE.md                 # Open Science companion documentation
├── TOOLS_REGISTRY.md                      # Full registry: 52 tools with weights
├── CITATION.cff                           # Citation metadata
├── LICENSE                                # CC BY 4.0
│
├── data/
│   ├── derived/
│   │   ├── publication_statistics.csv     # Corpus-level statistics
│   │   ├── dss_comparison.csv             # DSS-link frequency by contour
│   │   ├── analytical_modes_typology.csv  # Mode classification table
│   │   ├── prisma_flow_counts.csv         # PRISMA selection stages
│   │   ├── tools_registry_full.csv        # 52 tools with weights
│   │   ├── intercoder_reliability.csv     # Inter-coder agreement statistics
│   │   └── intercoder_sample.csv          # Blind-coded sample for verification
│   └── processed/
│       └── master_publications_coded.csv  # Master dataset (anonymized)
│
├── tables/
│   ├── table_1_comparative_sample.csv     # Table 1 from article
│   ├── table_2_analytical_modes.csv       # Table 2 from article
│   ├── table_3_tools_registry.csv         # Tools summary
│   └── prisma_flow_table.csv              # PRISMA stages summary
│
├── methodology/
│   ├── prisma_protocol.md                 # PRISMA 2020 protocol
│   ├── search_strategy.md                 # Database search strings
│   ├── codebook.md                        # Coding definitions and operational rules
│   ├── reproducibility_protocol.md
│   ├── limitations_and_bias.md
│   ├── tools_identification_protocol.md   # Tool identification procedure
│   └── why_h_index_was_not_used.md        # Methodological note on h-index
│
├── figures/
│   └── prisma_flow_diagram.md             # PRISMA flowchart
│
├── results/
│   ├── key_findings_open_science.md
│   ├── interpretation_notes.md
│   └── intercoder_reliability.md          # Inter-coder reliability report
│
├── scripts/
│   ├── validate_tables.py                 # Table validation script
│   └── calculate_kappa.py                 # Cohen's Kappa calculation script
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

## 🔬 Methodology

### PRISMA Protocol
Systematic literature selection from three databases following PRISMA 2020 guidelines. See `methodology/prisma_protocol.md` and `figures/prisma_flow_diagram.md` for full selection flow.

**Key numbers:**
- **804** → initial search results
- **327** → final analytical sample (112 Google Scholar, 95 РИНЦ, 120 CNKI)
- **477** → extended Russian corpus for contour-specific analysis

### Inter-Coder Reliability

Verified through independent blind coding by **3 coders** on a random sample of 33 publications (10%):

| Dimension | Cohen's Kappa | Landis & Koch level |
|-----------|---------------|---------------------|
| DSS-link determination | **0.91** | Almost perfect |
| Thematic classification | **0.84** | Almost perfect |
| Mode assignment | **0.79** | Substantial |
| AI-component identification | **0.76** | Substantial |
| System mention coding | **0.88** | Almost perfect |

Raw coding data and calculation scripts are available:
- `data/derived/intercoder_sample.csv` — blind-coded sample
- `scripts/calculate_kappa.py` — Kappa calculation
- `results/intercoder_reliability.md` — full reliability report

### Why We Don't Use H-Index for Systems

> ⚠️ **Methodological note:** The final version does not use h-index of platforms as a quality indicator. Initial bibliometric evaluations are preserved only as auxiliary heuristics for scientific visibility and do not participate in main conclusions.
> 
> See: `methodology/why_h_index_was_not_used.md`

---

## 📜 License

**Data and tables:** [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)

**Scripts:** MIT License (see individual file headers)

**Note:** This repository contains derived data and anonymized metadata only. Full-text publications are not redistributed in compliance with copyright law and publisher agreements.

---

## 📚 How to Cite

### APA 7
Vodopetov, S. V. (2025). *Modes of analytical work with media data: From measurement to decision support*. Vestnik PGU. https://github.com/MediaCod22/media_analytic_systems

### ГОСТ Р 7.0.5-2008
Водопетов С.В. Режимы аналитической работы с медиаданными: от измерений к поддержке принятия решений // Вестник ПГУ. — 2025. — № X. — С. XX–XX.

**Recommended repository citation for data reuse:**
> Vodopetov, S. V. (2025). Media Analytics Systems Research Data Repository (Version 1.0.0) [Data set]. GitHub. https://github.com/MediaCod22/media_analytic_systems

---

## 📦 Release

- **Current version:** v1.0.0
- **Release date:** 2026-05-14
- **Archive:** Available via GitHub Releases

---

*Repository created: 2026-05-14 | Last updated: 2026-05-14*
*This repository follows FAIR principles and PRISMA 2020 guidelines*
