# py4dummies/classes/RBXGroup.py - RBXGroup class
# (C) Copyright 2026 Ben Daws. BSD-3 License

"""
Holds the RBXGroup class.
"""

import math
from typing import Callable

from .RBXUser import RBXUser

class RBXGroup:
    """
    A Roblox group.
    """

    _id = 0
    _name = "Group"

    _member_count = 0
    _owner: RBXUser = RBXUser.none()

    def __init__(self, group_id: int):
        _id = group_id

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
    def members(self) -> list[RBXUser]:
        """
        Table of all members of the group. Warning: Based on group size, this may be a very memory-heavy list.
        If you plan to search through all members in the group, consider using filter_members().
        """

        return [ ]
    
    @property
    def member_count(self) -> int:
        """
        The amount of members inside of this group.
        """

        return self._member_count
    
    def get_member_chunk(self, page: int, chunk_size = 100) -> list[RBXUser]:
        """
        Gets a list of members with the length of `chunk_size` on `page`.

        Parameters:
            `page` (int): The page of members to get (ex. `page = 2` would return members 100 - 200 with a `chunk_size` of 100.)
            `chunk_size` (int): The amount of members that are assigned each page.
        
        Returns:
            `list[RBXUser]`: A list of members designated by parameters.
        """
        return [ ]
    
    async def filter_members(self, filter: Callable[[RBXUser], bool], chunk_size = 100) -> list[RBXUser]:
        """
        Passes each member of the group through the filter asynchronously, which allows for more optimized searching.

        Parameters:
            `filter` (Callable[[RBXUser], bool]): Each member is passed through the filter. If the filter returns false, the user is truncated from the list.
            `chunk_size` (int): The amount of users to fetch each request. The lower the number, the more requests that are made. We recommend 100 - 500.

        Returns:
            `list[RBXUser]`: A list of every member of the group that passed the filter. Warning: Based on the group size, this list may be very memory-heavy. Dispose of results when complete to keep performance.
        """
        
        returning_members = [ ]

        for page in range(1, math.ceil(self.member_count / chunk_size)):
            members = self.get_member_chunk(page, chunk_size)

            for member in members:
                if filter(member):
                    returning_members.append(member)
        
        return returning_members
            
    async def each_member(self, each: Callable[[RBXUser], None], chunk_size = 100) -> None:
        """
        Passes each member of the group through the function asynchronously, which allows for more optimized searching.
        This is functionally the same as filter_members(), but the lion does not concern himself with the output.
        
        Parameters:
            `each` (Callable[[RBXUser], None]): Each member is passed through the function.
            `chunk_size` (int): The amount of users to fetch each request. The lower the number, the more requests that are made. We recommend 100 - 500.
        """

        for page in range(1, math.ceil(self.member_count / chunk_size)):
            members = self.get_member_chunk(page, chunk_size)

            for member in members:
                each(member)