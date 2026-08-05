# Inter-Coder Reliability Report

> Version: v1.1.0 | Version date: 2026-08-06

## Overview

This report documents the reliability check for the descriptive systematic mapping of media analytics and decision support. Reliability was evaluated on a random 10% subsample of the final analytical corpus.

## Procedure

1. **Sample selection:** random subsample of 33 publications from the final corpus of 327.
2. **Independent coding:** two coders independently assigned DSS-link and analytical-mode codes.
3. **Codebook:** operational definitions are provided in `methodology/codebook.md`.
4. **Adjudication:** a third expert resolved all cases of disagreement.
5. **Calculation:** Cohen's Kappa was calculated for the binary DSS indicator and the nominal five-category mode indicator.

## Results

| Dimension | Cohen's Kappa | Landis & Koch Level | N |
|---|---:|---|---:|
| DSS-link determination | **0.91** | Almost perfect | 33 |
| Thematic mode classification | **0.84** | Almost perfect | 33 |

### Interpretation

Per Landis & Koch (1977), values above 0.80 indicate almost perfect agreement. The reported values support the reliability of the two article-level coding dimensions.

## Data and Script

- `data/derived/intercoder_sample.csv` — anonymized 33-record reliability sample;
- `scripts/calculate_kappa.py` — binary and nominal Kappa calculation;
- `data/derived/intercoder_reliability.csv` — reported summary values.

## Limitations

1. The reliability file is anonymized and does not include protected full-text material.
2. DSS coding is binary; nuanced cases were adjudicated by the third expert.
3. Mode coding uses five nominal categories and full marginal-based Kappa calculation.
4. The reliability sample documents coding consistency; it is not an additional analytical corpus.

## References

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46.

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174.

---

*Report version: v1.1.0 | Version date: 2026-08-06*
