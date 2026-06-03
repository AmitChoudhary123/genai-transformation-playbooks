from src.transformation_playbooks.main import roi_priority


def test_high_value_use_case_is_p1():
    assert roi_priority(5.0, 4, 3)["priority"] == "P1"


def test_low_value_high_risk_use_case_is_p3():
    assert roi_priority(1.0, 8, 8)["priority"] == "P3"