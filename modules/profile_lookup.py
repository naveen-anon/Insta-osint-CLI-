import requests


def fetch_public_profile(username: str):
    url = f"https://www.instagram.com/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers, timeout=15)

    return {
        "username": username,
        "status_code": r.status_code,
        "profile_url": url,
        "reachable": r.ok
    }
