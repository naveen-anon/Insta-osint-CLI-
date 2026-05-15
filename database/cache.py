# database/cache.py
"""
Simple in‑memory cache for repeated lookups – can be swapped for Redis later.
"""
from functools import lru_cache

@lru_cache(maxsize=256)
def get_cached_profile(username: str):
    # Query DB or API – placeholder
    return None
