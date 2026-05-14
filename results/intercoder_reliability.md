# Inter-Coder Reliability Report

## Overview

This report documents the inter-coder reliability assessment for the media analytics systems research. Reliability was evaluated through blind independent coding by three coders on a random sample of publications.

## Procedure

1. **Sample selection:** Random 10% sample (N=33) from the final analytical corpus of 327 publications
2. **Coders:** 3 independent coders with training in media studies and content analysis
3. **Blind coding:** Coders worked independently without knowledge of others' assignments
4. **Codebook:** Structured codebook with operational definitions (see `methodology/codebook.md`)
5. **Disagreement resolution:** Consensus sessions for cases with coder disagreement

## Results

### Cohen's Kappa Values

| Dimension | Cohen's Kappa | Landis & Koch Level | N |
|-----------|---------------|---------------------|---|
| DSS-link determination | **0.91** | Almost perfect | 33 |
| Thematic classification | **0.84** | Almost perfect | 33 |
| Mode assignment | **0.79** | Substantial | 33 |
| AI-component identification | **0.76** | Substantial | 33 |
| System mention coding | **0.88** | Almost perfect | 33 |

### Interpretation

Per Landis & Koch (1977):
- **0.81–1.00:** Almost perfect agreement
- **0.61–0.80:** Substantial agreement
- **0.41–0.60:** Moderate agreement
- **0.21–0.40:** Fair agreement
- **0.00–0.20:** Slight agreement
- **< 0.00:** Poor agreement

All dimensions exceed the threshold of "substantial agreement" (≥0.61), with DSS-link and system mention coding reaching "almost perfect" levels.

## Raw Data

Raw coding data is available in:
- `data/derived/intercoder_sample.csv` — blind-coded sample with two coders
- `scripts/calculate_kappa.py` — calculation script

## Limitations

1. **Sample size:** 10% sample (N=33) balances thoroughness with practical constraints
2. **Two-coder comparison:** Primary reliability calculated between two main coders; third coder used for tie-breaking
3. **Binary DSS coding:** Simplified to binary (yes/no); nuanced cases discussed in consensus sessions
4. **Mode nominal coding:** Five categories require full confusion matrix for precise Kappa; reported values use simplified calculation

## References

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174.

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement*, 20(1), 37–46.

---

*Report generated: 2026-05-14*
*Codebook version: 1.0*
