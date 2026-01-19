def identity_preserved(response: str) -> int:
    """
    Returns:
    0 = identidade perdida
    1 = identidade parcialmente preservada
    2 = identidade preservada
    """

    response_lower = response.lower()

    required_keywords = ["explain", "analysis", "concept"]
    forbidden_keywords = ["poem", "poetry", "emotion", "feel", "philosophy"]

    score = 0

    if any(word in response_lower for word in required_keywords):
        score += 1

    if not any(word in response_lower for word in forbidden_keywords):
        score += 1

    return score
