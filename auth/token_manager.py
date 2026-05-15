# auth/token_manager.py
"""
Store and refresh access tokens.  Simple file‑based persistence.
"""
import json
import os
from pathlib import Path
from .logger import logger

TOKEN_FILE = Path.home() / ".insta_osint_tokens.json"

def load_tokens() -> dict:
    if not TOKEN_FILE.is_file():
        logger.warning("Token file not found – please run auth flow.")
        return {}
    return json.loads(TOKEN_FILE.read_text(encoding="utf-8"))

def save_tokens(data: dict):
    TOKEN_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    logger.info(f"Tokens written to {TOKEN_FILE}")
