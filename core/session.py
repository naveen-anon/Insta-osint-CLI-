
# core/session.py
import requests

class Session:
    """Thin wrapper around requests.Session with defaults for Instagram."""
    def __init__(self, proxies=None):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        })
        if proxies:
            self.session.proxies.update(proxies)

    def get(self, url, **kwargs):
        return self.session.get(url, **kwargs)

    def post(self, url, **kwargs):
        return self.session.post(url, **kwargs)

    def close(self):
        self.session.close()
