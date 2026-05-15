# analyzers/similarity.py
"""
Compute similarity between usernames or bios using Jaro‑Winkler or Levenshtein.
"""

def username_similarity(u1: str, u2: str) -> float:
    # Simple ratio of matching characters
    matches = sum(c1 == c2 for c1, c2 in zip(u1, u2))
    return matches / max(len(u1), len(u2))
