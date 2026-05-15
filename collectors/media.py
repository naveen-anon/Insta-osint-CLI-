# collectors/media.py
"""
Collect recent posts/reels metadata for a user.  Handles pagination via the GraphQL cursor.
"""

from ..core.session import Session
from ..core.logger import logger
import time

def collect_media(username: str, limit: int = 20) -> list:
    base = f"https://www.instagram.com/{username}/?__a=1"
    sess = Session()
    posts = []
    url = base
    while len(posts) < limit:
        resp = sess.get(url, timeout=10)
        if resp.status_code != 200:
            logger.error(f"Failed to fetch media page: {resp.status_code}")
            break
        data = resp.json()
        edges = data.get("graphql", {}).get("user", {}).get(
            "edge_owner_to_timeline_media", {}
        ).get("edges", [])
        for edge in edges:
            node = edge.get("node", {})
            posts.append({
                "id": node.get("id"),
                "shortcode": node.get("shortcode"),
                "caption": node.get("edge_media_to_caption", {}).get("edges", [{}])[0].get("node", {}).get("text"),
                "timestamp": node.get("taken_at_timestamp"),
                "media_type": node.get("media_type"),  # 1=photo, 2=video, 8=carousel
                "like_count": node.get("edge_liked_by", {}).get("count"),
                "comment_count": node.get("edge_media_to_comment", {}).get("count"),
                "image_url": node.get("display_url"),
            })
            if len(posts) >= limit:
                break
        # Pagination
        page_info = data.get("graphql", {}).get("user", {}).get(
            "edge_owner_to_timeline_media", {}
        ).get("page_info", {})
        if not page_info.get("has_next_page"):
            break
        url = f"https://www.instagram.com/graphql/query/?query_hash=xxxx&variables={page_info.get('end_cursor')}"
        time.sleep(1)  # polite pause
    return posts
