def evaluate_response(text: str) -> float:
    """
    Simple rule-based evaluator.
    Returns score between 0 and 1.
    """
    score = 0.0

    if len(text) > 50:
        score += 0.4
    if "explain" in text.lower() or "because" in text.lower():
        score += 0.3
    if "example" in text.lower():
        score += 0.3

    return min(score, 1.0)
