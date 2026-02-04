def explain_clause(clause, risk):
    """
    Explain why a clause is risky in simple language.
    """

    level = risk.get("risk_level", "Low")

    if level == "High":
        explanation = (
            "This clause contains terms that can heavily disadvantage one party, "
            "such as penalties, indemnities, or unrestricted liabilities."
        )
    elif level == "Medium":
        explanation = (
            "This clause includes conditions that may create obligations or legal "
            "uncertainties depending on interpretation."
        )
    else:
        explanation = (
            "This clause appears standard and does not introduce significant legal risk."
        )

    return explanation


def suggest_alternative(clause, risk):
    """
    Suggest safer wording for risky clauses.
    """

    level = risk.get("risk_level", "Low")

    if level == "High":
        return (
            "Consider limiting liability, adding mutual obligations, "
            "or specifying clear termination conditions."
        )
    elif level == "Medium":
        return (
            "Clarify ambiguous terms, define responsibilities clearly, "
            "and include dispute resolution mechanisms."
        )
    else:
        return "No alternative required. Clause is acceptable."
