from rules.contract_keywords import EMPLOYMENT, SERVICE, NDA


def classify_contract(text):
    """
    Classify contract type using keyword scoring.
    Returns dict with type and confidence.
    """
    text_lower = text.lower()

    scores = {
        "Employment": _score_keywords(text_lower, EMPLOYMENT),
        "Service": _score_keywords(text_lower, SERVICE),
        "NDA": _score_keywords(text_lower, NDA)
    }

    contract_type = max(scores, key=scores.get)
    max_score = scores[contract_type]
    total_score = sum(scores.values()) or 1  # avoid division by zero

    confidence = max_score / total_score

    if max_score == 0:
        return {
            "type": "Other",
            "confidence": 0.0
        }

    return {
        "type": contract_type,
        "confidence": round(confidence, 2)
    }


def _score_keywords(text, keywords):
    """
    Count keyword occurrences in text.
    """
    score = 0
    for kw in keywords:
        if kw in text:
            score += 1
    return score
