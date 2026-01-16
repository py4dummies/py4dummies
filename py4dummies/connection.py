# py4dummies/connection.py - Tests connection to Roblox platform
# (C) Copyright 2026 Ben Daws. BSD-3 License

import requests

def can_reach_url(url="http://1.1.1.1", timeout=5):
    """
    Ping the specified URL.
    """
    try:
        response = requests.head(url, timeout=timeout)
        return response.status_code == 200
    except requests.ConnectionError:
        return False
    except requests.Timeout:
        return False

def can_connect():
    """
    Runs a connection test.
    """

    can_reach_cloudflare = can_reach_url() # Cloudflare 1.1.1.1 (canonically one.one.one.one)
    can_reach_roblox = can_reach_url("https://www.roblox.com") # Roblox

    return can_reach_cloudflare & can_reach_roblox
