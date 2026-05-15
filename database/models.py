# database/models.py
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class UserProfile:
    username: str
    full_name: Optional[str] = None
    bio: Optional[str] = None
    followers: Optional[int] = None
    following: Optional[int] = None
    media_count: Optional[int] = None
    profile_pic_url: Optional[str] = None
    collected_at: datetime = field(default_factory=datetime.utcnow)

@dataclass
class Post:
    id: str
    shortcode: str
    caption: Optional[str] = None
    timestamp: int = 0
    media_type: int = 0
    like_count: int = 0
    comment_count: int = 0
    image_url: Optional[str] = None
