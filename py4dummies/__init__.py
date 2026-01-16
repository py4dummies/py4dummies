# py4dummies/__init__.py - Handles the global namespace
# (C) Copyright 2026 Ben Daws. BSD-3 License

"""
Py4Dummies simplifies interactions between your Python script and Roblox
APIs, web content, and other topics that are worth simplifying.
"""

from .classes.rbx.RBXAccessory import RBXAccessory
from .classes.rbx.RBXGroup import RBXGroup
from .classes.rbx.RBXUser import RBXUser
from .classes.rbx.RBXGame import RBXGame

from .classes.filterable.FilterableList import FilterableList
from .classes.filterable.FilterableItem import FilterableItem

from .utils import fetch, conversions
from .connection import can_reach_url, can_connect

__all__ = [
    # classes
    "RBXAccessory", "RBXGroup", "RBXUser", "RBXGame",
    "FilterableItem", "FilterableList",

    # namespaces
    "fetch",
    "conversions",

    # functions
    "can_reach_url", "can_connect" # connection.py
]