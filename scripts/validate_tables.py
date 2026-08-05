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
    registry_path = ROOT / "data" / "derived" / "tools_registry_full.csv"

    for path in [dss_path, modes_path, stats_path, registry_path]:
        require(path.exists(), f"Missing required file: {path}")

    dss = read_csv(dss_path)
    require(len(dss) == 3, "dss_comparison.csv must contain exactly three corpora")
    require(sum(int(row["final_sample"]) for row in dss) == 327, "Final sample must sum to 327")
    require(sum(int(row["dss_link_count"]) for row in dss) == 65, "DSS-linked publications must sum to 65")

    expected_dss = {"international": (112, 15), "russian": (95, 8), "chinese": (120, 42)}
    for row in dss:
        contour = row["contour"]
        require((int(row["final_sample"]), int(row["dss_link_count"])) == expected_dss[contour],
                f"Unexpected DSS values for {contour}")

    modes = read_csv(modes_path)
    expected_modes = {
        "Медиаизмерения",
        "Мониторинг медиапространства",
        "OSINT и дата-журналистика",
        "Поддержка решений и предиктивная аналитика",
        "ИИ-нативный режим",
    }
    require({row["mode_name_ru"] for row in modes} == expected_modes,
            "analytical_modes_typology.csv must contain the five final modes")

    registry = read_csv(registry_path)
    require(len(registry) == 50, f"Expected 50 tools, got {len(registry)}")
    counts = {"Россия": 0, "Международный": 0, "Китай": 0}
    for row in registry:
        counts[row["contour"]] += 1
    require(counts == {"Россия": 13, "Международный": 30, "Китай": 7},
            f"Unexpected registry distribution: {counts}")

    stats = {row["metric"]: row["value"] for row in read_csv(stats_path)}
    require(stats["primary_records_identified"] == "804", "Primary records must equal 804")
    require(stats["excluded_at_screening"] == "477", "Excluded records must equal 477")
    require(stats["final_analytical_sample"] == "327", "Final sample must equal 327")
    require(stats["tools_total"] == "50", "Tools total must equal 50")

    print("All Open Science package tables validated successfully.")


if __name__ == "__main__":
    main()
