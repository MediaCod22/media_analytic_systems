from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    dss_path = ROOT / "data" / "derived" / "dss_comparison.csv"
    modes_path = ROOT / "data" / "derived" / "analytical_modes_typology.csv"
    stats_path = ROOT / "data" / "derived" / "publication_statistics.csv"

    for path in [dss_path, modes_path, stats_path]:
        require(path.exists(), f"Missing required file: {path}")

    dss = read_csv(dss_path)
    require(len(dss) == 3, "dss_comparison.csv must contain exactly three contours")

    sample_sum = sum(int(row["final_sample"]) for row in dss)
    require(sample_sum == 327, f"Expected final sample sum 327, got {sample_sum}")

    values = {row["contour"]: float(row["dss_link_percent"]) for row in dss}
    gap = values["chinese"] / values["russian"]
    require(round(gap, 1) == 4.4, f"Expected China/Russia DSS gap 4.4, got {gap:.3f}")

    modes = read_csv(modes_path)
    require(len(modes) == 5, "analytical_modes_typology.csv must contain five analytical modes")

    print("All Open Science package tables validated successfully.")


if __name__ == "__main__":
    main()
