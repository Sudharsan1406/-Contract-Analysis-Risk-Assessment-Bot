import re
from rules.clause_keywords import CLAUSE_KEYWORDS


def split_into_clauses(text):
    if not text:
        return []

    raw_chunks = text.split(".")
    clauses = []

    for i, chunk in enumerate(raw_chunks):
        if not chunk:
            continue

        cleaned = chunk.strip()
        if len(cleaned) < 20:
            continue

        clauses.append({
            "clause_id": i + 1,
            "category": "General",
            "text": cleaned
        })

    return clauses



def _basic_split(text):
    """
    Basic clause splitting using numbering and headings.
    """
    # Split on numbered headings (1., 2., 1.1, etc.)
    parts = re.split(r"\n\s*\d+(\.\d+)*\s+", text)

    # Fallback: split by paragraphs if numbering fails
    if len(parts) <= 1:
        parts = text.split("\n\n")

    return parts


def _detect_clause_category(text):
    """
    Assign clause category based on keyword matching.
    """
    text_lower = text.lower()

    for category, keywords in CLAUSE_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                return category

    return "GENERAL"
