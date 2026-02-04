def evaluate_clause_risk(clause):
    """
    clause is a DICT with key 'text'
    """
    text = clause["text"].lower()

    if any(k in text for k in ["terminate without notice", "indemnify", "penalty", "liable"]):
        return {
            "risk_level": "High",
            "reason": "This clause gives one-sided power or heavy liability."
        }

    if any(k in text for k in ["terminate", "penalty", "notice period"]):
        return {
            "risk_level": "Medium",
            "reason": "This clause may negatively affect one party."
        }

    return {
        "risk_level": "Low",
        "reason": "This clause appears balanced."
    }


def compute_contract_risk(analyzed_clauses):
    """
    analyzed_clauses: list of dicts with key 'risk'
    """

    score_map = {"Low": 1, "Medium": 2, "High": 3}

    if not analyzed_clauses:
        return {
            "level": "Low",
            "score": 1.0
        }

    scores = [score_map[c["risk"]] for c in analyzed_clauses]
    avg_score = sum(scores) / len(scores)

    if avg_score >= 2.5:
        level = "High"
    elif avg_score >= 1.5:
        level = "Medium"
    else:
        level = "Low"

    return {
        "level": level,
        "score": round(avg_score, 2)
    }
