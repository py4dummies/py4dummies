# py4dummies/classes/RBXGroup.py - RBXGroup class
# (C) Copyright 2026 Ben Daws. BSD-3 License

"""
Holds the RBXGroup class.
"""

from .RBXUser import RBXUser
from ..filterable.FilterableList import FilterableList

class RBXGroup:
    """
    A Roblox group.
    """

    _id = 0
    _name = "Group"

    _members: list[RBXUser] = []
    _member_count = 0
    _owner: RBXUser = RBXUser.none()

    def __init__(self, group_id: int):
        self._id = group_id

    @property
    def id(self) -> int:
        """
        The group ID.
        """

        return self._id
    
    @property
    def name(self) -> str:
        """
        The name of the group.
        """
        
        return self._name
    
    @property
    def owner(self) -> RBXUser:
        """
        The owner of the group.
        """

        return self._owner
    
    @property
    def members(self) -> FilterableList[RBXUser]:
        """
        A FilterableList of all members of the group.
        """

        return FilterableList(self._members)
    
    @property
    def member_count(self) -> int:
        """
        The amount of members inside of this group.
        """

        return self._member_count