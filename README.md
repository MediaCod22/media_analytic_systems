# Media Analytics Systems — Research Data Repository

> Репозиторий данных исследования «Режимы аналитической работы с медиаданными: от измерений к поддержке принятия решений»
> Полный реестр **52 инструментов медиааналитики** с весами упоминания по научным контурам

[![Open Science](https://img.shields.io/badge/Open%20Science-FAIR-blue)](https://www.go-fair.org/fair-principles/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--5237--4464-green)](https://orcid.org/0000-0002-5237-4464)

---

## 🎯 Research Summary

This repository accompanies the article *«Режимы аналитической работы с медиаданными: от измерений к поддержке принятия решений»* and provides:

- **Complete methodology** (PRISMA protocol, search strategy, codebook)
- **Full analytical corpus** statistics and derived tables
- **Comprehensive tools registry** — 52 media analytics systems with frequency weights
- **Reproducible scripts** for data validation
- **Open Science compliance** documentation

---

## 📊 Key Results at a Glance

| Metric | Value |
|--------|-------|
| Primary search results | 804 publications |
| Final analytical sample | 327 publications |
| Tools identified | **52 systems** |
| Russian tools | 18 |
| International tools | 24 |
| Chinese tools | 10 |
| DSS-link gap Russia/China | **4.4×** (8% vs 35%) |

---

## 🔧 Complete Tools Registry (52 Systems)

### Quick Stats by Mode

| Mode | Count | Top Tools |
|------|-------|-----------|
| Медиаизмерения | 2 | Mediascope (0.85), Nielsen (0.82) |
| Национальное медиапокрытие | 34 | Brand Analytics (0.72), Factiva (0.64), LexisNexis (0.61) |
| OSINT / data journalism | 5 | GDELT (0.38), Traackr (0.18), Onalytica (0.16) |
| Support / predictive analytics | 7 | Dataminr (0.45), Signal AI (0.42), Sprinklr (0.44) |
| AI-native layer | 4 | Midu (0.56), NetBase Quid (0.39) |

### Top 10 by Weight

| Rank | Tool | Contour | Weight |
|------|------|---------|--------|
| 1 | Mediascope | 🇷🇺 Russia | 0.85 |
| 2 | Nielsen | 🌍 International | 0.82 |
| 3 | Brand Analytics | 🇷🇺 Russia | 0.72 |
| 4 | СКАН-Интерфакс | 🇷🇺 Russia | 0.68 |
| 5 | Factiva | 🌍 International | 0.64 |
| 6 | LexisNexis | 🌍 International | 0.61 |
| 7 | Brandwatch | 🌍 International | 0.58 |
| 8 | Dataminr | 🌍 International | 0.45 |
| 9 | Sprinklr | 🌍 International | 0.44 |
| 10 | Cision | 🌍 International | 0.49 |

**[→ View Full Registry (52 tools)](TOOLS_REGISTRY.md)**

---

## 📁 Repository Structure

```
media_analytic_systems/
├── README.md                              # This file
├── TOOLS_REGISTRY.md                      # Full tools registry with methodology
├── CITATION.cff                           # Citation metadata
├── LICENSE                                # CC BY 4.0
├── data/
│   ├── derived/
│   │   ├── publication_statistics.csv     # Corpus stats
│   │   ├── dss_comparison.csv             # DSS-link comparison
│   │   ├── analytical_modes_typology.csv  # Mode classification
│   │   ├── prisma_flow_counts.csv         # PRISMA flow
│   │   └── tools_registry_full.csv        # ⭐ 52 tools with weights
│   └── raw_placeholder/
│       └── README.md
├── tables/
│   ├── table_1_comparative_sample.csv     # Table 1 from article
│   ├── table_2_analytical_modes.csv       # Table 2 from article
│   └── table_3_tools_registry.csv         # ⭐ Tools summary for article
├── methodology/
│   ├── prisma_protocol.md
│   ├── search_strategy.md
│   ├── codebook.md
│   ├── reproducibility_protocol.md
│   ├── limitations_and_bias.md
│   └── tools_identification_protocol.md   # ⭐ How 52 tools were identified
├── results/
│   ├── key_findings_open_science.md
│   └── interpretation_notes.md
├── scripts/
│   └── validate_tables.py
├── metadata/
│   ├── CITATION.cff
│   ├── codemeta.json
│   └── dataset_metadata.json
└── docs/
    ├── open_science_checklist.md
    └── github_release_notes.md
```

---

## 🔬 Methodology

### PRISMA Protocol
Systematic literature review following PRISMA 2020 guidelines. See `methodology/prisma_protocol.md`.

### Analytical Modes Typology

| Mode | Russian Example | International Example | Chinese Example | Output |
|------|-----------------|---------------------|-----------------|--------|
| **Медиаизмерения** | Mediascope | Nielsen | — | Attention, reach, contact |
| **Национальное медиапокрытие** | Brand Analytics, СКАН | Factiva, LexisNexis | Yuqing-платформы | System observation, narratives |
| **OSINT / data journalism** | OSINT + BA/СКАН | GDELT + OSINT tools | Yuqing-анализ | Event reconstruction |
| **Support / predictive analytics** | Талисман, risk-аналитика | Signal AI, Dataminr | Sina Yuqing / Wisers | Scenarios, early warning |
| **AI-native layer** | Research LLM pipelines | Dataminr, Signal AI | Midu / LLM reporting | Signal automation |

### Coding Reliability
- **Thematic classification:** Cohen's Kappa = **0.84**
- **DSS-link determination:** Cohen's Kappa = **0.91**

---

## 🛠️ Tools Identification Protocol

The registry of 52 tools was compiled through:
1. **Automated extraction** from 327 analytical publications + 477 extended Russian corpus
2. **Manual verification** against real product websites and documentation
3. **Expert classification** by 3 independent coders
4. **Weight normalization** by contour (Russian/International/Chinese)

See: `methodology/tools_identification_protocol.md`

---

## 📜 License

[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)

---

## 👤 Author

**Sergey Vyacheslavovich Vodopetov**
- ORCID: [0000-0002-5237-4464](https://orcid.org/0000-0002-5237-4464)
- RSCI Author ID: 835749 | SPIN: 5530-2581
- RUDN University, Moscow

---

## 📚 How to Cite

### APA 7
Vodopetov, S. V. (2025). *Modes of analytical work with media data: From measurement to decision support*. Vestnik PGU. https://github.com/MediaCod22/media_analytic_systems

### ГОСТ
Водопетов С.В. Режимы аналитической работы с медиаданными: от измерений к поддержке принятия решений // Вестник ПГУ. — 2025. — № X. — С. XX–XX.

---

*Repository created: 2026-05-14 | Last updated: 2026-05-14*
