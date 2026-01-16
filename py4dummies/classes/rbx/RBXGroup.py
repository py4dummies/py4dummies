# py4dummies/classes/RBXGroup.py - RBXGroup class
# (C) Copyright 2026 Ben Daws. BSD-3 License

"""
Holds the RBXGroup class.
"""

from .RBXUser import RBXUser
from ..bufferable.BufferableList import BufferableList
from ...utils import *

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
    def members(self) -> BufferableList[RBXUser]:
        """
        A FilterableList of all members of the group.
        """

        def member_fetch(page: int) -> list[RBXUser]:
            endpoint = f"https://groups.roblox.com/v1/groups/{self.id}/users?sortOrder=Asc&limit=100&Cursor={page}"
            api_data = fetch_dict(endpoint)

            items = []

            for user in api_data["data"]:
                items.append(RBXUser(user["user"], True))

            return items


        return BufferableList[RBXUser](member_fetch, 100)
    
    @property
    def member_count(self) -> int:
        """
        The amount of members inside of this group.
        """

        return self._member_count