# database/sqlite_db.py
import sqlite3
from pathlib import Path
from .models import UserProfile, Post

DB_FILE = Path.home() / ".insta_osint.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS profiles (
            username TEXT PRIMARY KEY,
            full_name TEXT,
            bio TEXT,
            followers INTEGER,
            following INTEGER,
            media_count INTEGER,
            profile_pic_url TEXT,
            collected_at TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id TEXT PRIMARY KEY,
            shortcode TEXT,
            caption TEXT,
            timestamp INTEGER,
            media_type INTEGER,
            like_count INTEGER,
            comment_count INTEGER,
            image_url TEXT
        )
    """)
    conn.commit()
    conn.close()
