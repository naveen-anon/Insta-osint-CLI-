# core/utils.py
import os
import yaml
from pathlib import Path
from .logger import logger

def load_yaml(file_path: str) -> dict:
    path = Path(file_path)
    if not path.is_file():
        logger.error(f"Config file not found: {file_path}")
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def read_wordlist(file_path: str) -> list:
    path = Path(file_path)
    if not path.is_file():
        logger.error(f"Wordlist missing: {file_path}")
        return []
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def safe_write(file_path: str, content: str):
    Path(file_path).write_text(content, encoding="utf-8")
