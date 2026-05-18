import requests


def fetch_public_profile(username: str):
    url = f"https://www.instagram.com/{username}/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    return {
        "username": username,
        "status_code": response.status_code,
        "profile_url": url,
        "reachable": response.ok,
        "html_content": response.text
    }
