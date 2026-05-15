# auth/cookies.py
"""
Convenience wrapper for saving/loading cookie jars.
"""

import pickle
from pathlib import Path
from .logger import logger

COOKIE_FILE = Path.home() / ".insta_osint_cookies.pkl"

def save_cookies(session):
    with open(COOKIE_FILE, "wb") as f:
        pickle.dump(session.cookies, f)
    logger.info(f"Cookies saved to {COOKIE_FILE}")

def load_cookies(session):
    if not COOKIE_FILE.is_file():
        logger.warning("No cookie file found")
        return
    with open(COOKIE_FILE, "rb") as f:
        session.cookies.update(pickle.load(f))
    logger.info(f"Cookies loaded from {COOKIE_FILE}")
