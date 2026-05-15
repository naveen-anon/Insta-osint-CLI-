# integrations/meta_api.py
"""
Thin wrapper around Facebook Graph API (Meta) – useful if you have an app token.
"""

class MetaGraph:
    def __init__(self, access_token: str):
        self.base = "https://graph.facebook.com/v18.0"
        self.token = access_token

    def get_user(self, user_id: str) -> dict:
        url = f"{self.base}/{user_id}"
        params = {"access_token": self.token}
        return requests.get(url, params=params).json()
