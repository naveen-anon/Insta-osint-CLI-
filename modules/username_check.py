import requests


def username_exists(username: str):
    url = f"https://www.instagram.com/{username}/"
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
    return r.status_code == 200
  
