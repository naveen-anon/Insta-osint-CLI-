import re


def analyze_username(username: str):
    parts = re.findall(r'[a-zA-Z]+|\d+', username)

    return {
        "username": username,
        "length": len(username),
        "has_numbers": any(ch.isdigit() for ch in username),
        "segments": parts
    }
