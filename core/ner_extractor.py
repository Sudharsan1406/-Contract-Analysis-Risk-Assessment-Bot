import re


def extract_entities(text):
    """
    Extract basic legal entities from contract text.
    Returns a dictionary of entities.
    """

    entities = {
        "parties": [],
        "dates": [],
        "amounts": [],
        "locations": []
    }

    # ---- Parties (simple heuristic) ----
    party_patterns = [
        r"between\s+(.*?)\s+and\s+(.*?)[\.,\n]",
        r"this agreement is made by\s+(.*?)[\.,\n]"
    ]

    for pattern in party_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            if isinstance(match, tuple):
                entities["parties"].extend([m.strip() for m in match])
            else:
                entities["parties"].append(match.strip())

    # ---- Dates ----
    date_pattern = r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b|\b\d{1,2}\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}\b"
    entities["dates"] = list(set(re.findall(date_pattern, text, re.IGNORECASE)))

    # ---- Monetary amounts ----
    amount_pattern = r"(₹|\$|Rs\.?)\s?\d+(?:,\d+)*(?:\.\d+)?"
    entities["amounts"] = list(set(re.findall(amount_pattern, text)))

    # ---- Locations (very basic) ----
    location_keywords = ["india", "chennai", "bangalore", "delhi", "mumbai", "usa", "uk"]
    for loc in location_keywords:
        if loc.lower() in text.lower():
            entities["locations"].append(loc.title())

    return entities
