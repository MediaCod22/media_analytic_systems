#!/usr/bin/env python3
"""
Cohen's Kappa Calculator for Inter-Coder Reliability
Usage: python scripts/calculate_kappa.py

Calculates Cohen's Kappa for DSS-link and analytical-mode coding.
Input: data/derived/intercoder_sample.csv
Protocol: two independent coders; a third expert resolves disagreements.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


def cohens_kappa(values1: list[str], values2: list[str]) -> tuple[float, float, float, int]:
    """Return (kappa, observed agreement, expected agreement, n)."""
    if len(values1) != len(values2):
        raise ValueError("Coder vectors have different lengths")
    n = len(values1)
    if n == 0:
        raise ValueError("Empty reliability sample")

    observed = sum(a == b for a, b in zip(values1, values2)) / n
    counts1 = Counter(values1)
    counts2 = Counter(values2)
    categories = set(counts1) | set(counts2)
    expected = sum((counts1.get(c, 0) / n) * (counts2.get(c, 0) / n) for c in categories)
    kappa = 1.0 if expected == 1 else (observed - expected) / (1 - expected)
    return kappa, observed, expected, n


def interpret_kappa(kappa: float) -> str:
    """Interpret Kappa value per Landis & Koch (1977)."""
    if kappa < 0:
        return "Poor / less than chance agreement"
    if kappa <= 0.20:
        return "Slight agreement"
    if kappa <= 0.40:
        return "Fair agreement"
    if kappa <= 0.60:
        return "Moderate agreement"
    if kappa <= 0.80:
        return "Substantial agreement"
    return "Almost perfect agreement"


def main() -> None:
    sample_path = Path(__file__).resolve().parents[1] / "data" / "derived" / "intercoder_sample.csv"
    with sample_path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    coder1_dss = [row["coder_1_dss"] for row in rows]
    coder2_dss = [row["coder_2_dss"] for row in rows]
    coder1_mode = [row["coder_1_mode"] for row in rows]
    coder2_mode = [row["coder_2_mode"] for row in rows]

    kappa_dss, po_dss, pe_dss, n = cohens_kappa(coder1_dss, coder2_dss)
    kappa_mode, po_mode, pe_mode, _ = cohens_kappa(coder1_mode, coder2_mode)

    print("=" * 60)
    print("INTER-CODER RELIABILITY RESULTS")
    print("=" * 60)
    print(f"Sample size: {n} publications (random 10% subsample)")
    print("Protocol: two independent coders; third expert adjudication")
    print()
    print("DSS-LINK CODING")
    print(f"  Observed agreement: {po_dss:.4f}")
    print(f"  Expected agreement: {pe_dss:.4f}")
    print(f"  Cohen's Kappa:      {kappa_dss:.4f} ({interpret_kappa(kappa_dss)})")
    print()
    print("ANALYTICAL MODE CODING")
    print(f"  Observed agreement: {po_mode:.4f}")
    print(f"  Expected agreement: {pe_mode:.4f}")
    print(f"  Cohen's Kappa:      {kappa_mode:.4f} ({interpret_kappa(kappa_mode)})")
    print()
    print("Reference: Cohen, J. (1960). A coefficient of agreement for nominal scales.")
    print("Educational and Psychological Measurement, 20(1), 37–46.")


if __name__ == "__main__":
    main()
