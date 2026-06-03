from __future__ import annotations

import csv
from pathlib import Path


def roi_priority(annual_value_musd: float, complexity: int, risk: int) -> dict:
    score = (annual_value_musd * 20) - (complexity * 3) - (risk * 4)
    priority = "P1" if score >= 50 else "P2" if score >= 20 else "P3"
    return {"score": round(score, 2), "priority": priority}


def load_initiatives(path: str | Path) -> list[dict]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["annual_value_musd"] = float(row["annual_value_musd"])
        row["complexity"] = int(row["complexity"])
        row["risk"] = int(row["risk"])
    return rows


def rank_transformation_portfolio(rows: list[dict]) -> list[dict]:
    ranked = []
    for row in rows:
        decision = roi_priority(row["annual_value_musd"], row["complexity"], row["risk"])
        governance = "board review" if row["risk"] >= 8 else "portfolio council"
        ranked.append({**row, **decision, "governance": governance})
    return sorted(ranked, key=lambda row: row["score"], reverse=True)