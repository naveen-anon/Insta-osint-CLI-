# analyzers/content.py
"""
Keyword / caption analysis – simple frequency count.
"""

from collections import Counter
import re

def analyze_content(posts: list) -> dict:
    words = []
    for p in posts:
        caption = p.get("caption", "")
        # Basic tokenization
        words.extend(re.findall(r"\w+", caption.lower()))
    freq = Counter(words)
    return {"top_keywords": freq.most_common(10)}
