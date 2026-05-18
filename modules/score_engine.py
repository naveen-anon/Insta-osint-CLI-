SECURITY_KEYWORDS = [
    "cyber",
    "security",
    "privacy",
    "ethical",
    "hack",
    "defense"
]


def calculate_score(text: str, links_count: int = 0):
    score = 0
    matched_keywords = []

    content = text.lower()

    for keyword in SECURITY_KEYWORDS:

        if keyword in content:
            score += 15
            matched_keywords.append(
                keyword
            )

    score += links_count * 5

    if score > 100:
        score = 100

    return {
        "score": score,
        "matched_keywords": matched_keywords
    }
