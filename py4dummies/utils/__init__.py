# py4dummies/utils/__init__.py - Handles the utils namespace
# (C) Copyright 2026 Ben Daws. BSD-3 License

"""
Utilities for fetching content, sending webhooks to Discord, etc.
"""

from .fetch import fetch_dict, fetch_string
from .conversions import to_int

__all__ = ["fetch_dict", "fetch_string", "to_int"]