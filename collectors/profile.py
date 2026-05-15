# collectors/profile.py
"""
Collect public profile metadata (username, full name, bio, followers, etc.).
"""

from ..core.session import Session
from ..core.logger import logger
import json

def collect_profile(username: str) -> dict:
    url = f"https://www.instagram.com/{username}/?__a=1"
    sess = Session()
    resp = sess.get(url, timeout=10)
    if resp.status_code != 200:
        logger.error(f"Failed to fetch profile: {resp.status_code}")
        return {}

    # Instagram may return a JSON blob inside the HTML – parse it
    try:
        data = resp.json()
        user = data.get("graphql", {}).get("user", {})
        profile = {
            "username": user.get("username"),
            "full_name": user.get("full_name"),
            "biography": user.get("biography"),
            "followers": user.get("edge_followed_by", {}).get("count"),
            "following": user.get("edge_follow", {}).get("count"),
            "media_count": user.get("edge_owner_to_timeline_media", {}).get("count"),
            "profile_pic_url": user.get("profile_pic_url_hd"),
        }
        return profile
    except Exception as e:
        logger.exception("JSON parsing error")
        return {}
