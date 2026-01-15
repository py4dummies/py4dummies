# py4dummies/__init__.py - Handles the global namespace
# (C) Copyright 2026 Ben Daws. BSD-3 License

"""
Py4Dummies simplifies interactions between your Python script and Roblox
APIs, web content, and other topics that are worth simplifying.
"""

from .classes import RBXAccessory, RBXGroup, RBXUser
from .utils import fetch, conversions

__all__ = ["RBXAccessory", "RBXGroup", "RBXUser", "fetch", "conversions"]