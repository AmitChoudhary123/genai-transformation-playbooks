def roi_priority(annual_value_musd: float, complexity: int, risk: int) -> dict:
    """Rank a GenAI initiative for executive portfolio planning."""
    score = (annual_value_musd * 20) - (complexity * 3) - (risk * 4)
    priority = "P1" if score >= 50 else "P2" if score >= 20 else "P3"
    return {"score": round(score, 2), "priority": priority}