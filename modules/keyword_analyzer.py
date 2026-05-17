from collections import Counter
import re


def analyze_keywords(text: str):
    words = re.findall(r'\b\w+\b', text.lower())

    common_words = Counter(words).most_common(10)

    return {
        "keywords": common_words,
        "total_words": len(words)
    }
