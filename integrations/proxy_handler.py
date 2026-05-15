# integrations/proxy_handler.py
"""
Configure HTTP(S) proxies for sessions.
"""

def build_proxy_dict(http_proxy: str = None, https_proxy: str = None) -> dict:
    return {
        "http": http_proxy or "",
        "https": https_proxy or "",
    }
