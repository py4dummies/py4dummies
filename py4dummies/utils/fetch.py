# py4dummies/utils/fetch.py - Get content in several format from web addresses
# (C) Copyright 2026 Ben Daws. BSD-3 License

import json
import requests

def fetch_dict(address: str) -> dict:
    """
    Returns a dictionary representing the JSON at `address`.

    Parameters:
        `address` (str): The address to fetch the content of.
    
    Returns:
        (dict): A dictionary representing the JSON at `address`.
    
    Raises:
        `AssertionError`: Thrown when the HTTP status code is not 200 (OK). Message formatted as "HTTPError (Err {code})".
    """

    response = requests.get(address)
    assert (response.status_code == 200), f"HTTPError (Err {response.status_code})"

    try:
        result = json.loads(response.content)
        return result
    except Exception as err:
        print(f"Failed to decode JSON from \"{address}\":")
        print(f"Exception: {err}")

        return { "__err" : err }

def fetch_string(address: str) -> str:
    """
    Returns a string of the content at `address`.

    Parameters:
        `address` (str): The address to fetch the content of.
    
    Returns:
        (str): A string of the content at `address`.
    
    Raises:
        `AssertionError`: Thrown when the HTTP status code is not 200 (OK). Message formatted as "HTTPError (Err {code})".
    """

    response = requests.get(address)
    assert (response.status_code == 200), f"HTTPError (Err {response.status_code})"

    return response.content.decode("utf-8")