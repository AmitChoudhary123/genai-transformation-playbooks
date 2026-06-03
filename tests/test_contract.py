from pathlib import Path
from src.transformation_playbooks.main import load_initiatives, rank_transformation_portfolio, roi_priority


def test_transformation_demo_ranks_portfolio():
    ranked = rank_transformation_portfolio(load_initiatives(Path("data/genai_initiatives.csv")))
    assert ranked[0]["priority"] == "P1"
    assert any(item["governance"] == "board review" for item in ranked)


def test_low_value_high_risk_use_case_is_p3():
    assert roi_priority(1.0, 8, 8)["priority"] == "P3"