# analyzers/timeline.py
"""
Analyze posting patterns – e.g., average posts per day, peak hours.
"""

from datetime import datetime, timedelta
from collections import Counter
from ..core.logger import logger

def analyze_timeline(posts: list) -> dict:
    if not posts:
        return {}

    timestamps = [datetime.fromtimestamp(p["timestamp"]) for p in posts]
    days = [t.date() for t in timestamps]
    posts_per_day = Counter(days)

    # Average posts per day
    avg_posts = sum(posts_per_day.values()) / len(posts_per_day)

    # Peak hour
    hours = [t.hour for t in timestamps]
    peak_hour = Counter(hours).most_common(1)[0][0]

    return {
        "average_posts_per_day": round(avg_posts, 2),
        "peak_hour": peak_hour,
        "posts_per_day": dict(posts_per_day),
    }
