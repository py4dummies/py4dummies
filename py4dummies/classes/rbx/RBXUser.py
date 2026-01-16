# py4dummies/classes/RBXUser.py - RBXUser class
# (C) Copyright 2026 Ben Daws. BSD-3 License

"""
Holds the RBXUser class.
"""

from .RBXAccessory import RBXAccessory
from ..filterable.FilterableList import FilterableList
from ...utils import *

class RBXUser:
    """
    A Roblox user.
    """

    # Internal
    _id = 1

    _display_name = "Roblox"
    _user_name = "Roblox"
    _bio = ""

    _partial_reference = False

    _friends: list[RBXUser] = [ ]

    # Public
    @staticmethod
    def none() -> RBXUser:
        """
        Represents either an unknown or non-existant player.
        RBXUser is non-nullable, however, this is the best representation
        of None avaliable.
        """

        nan = RBXUser({"nan": True}, True)

        nan._display_name = "John Doe"
        nan._user_name = "John Doe"

        return nan

    @property
    def id(self) -> int:
        """
        The user ID of the RBXUser.
        """

        return self._id
    
    @property
    def display_name(self) -> str:
        """
        The display name of the user.
        """

        return self._display_name
    
    @property
    def user_name(self) -> str:
        """
        The user name of the user. Does not contain the `@` symbol.
        """
        return self._user_name
    
    @property
    def url(self) -> str:
        """
        A formatted URL to the user's profile.
        """

        return f"https://www.roblox.com/users/{self.id}" if self.id != -1 else "about:blank"
    
    @property
    def avatar_items(self) -> FilterableList[RBXAccessory]:
        """
        All accessories currently worn by this user.
        """

        if self._partial_reference:
            self.complete_load()
        
        return FilterableList[RBXAccessory]()

    @property
    def inventory(self) -> FilterableList[RBXAccessory]:
        """
        All accessories owned by this user.
        """

        if self._partial_reference:
            self.complete_load()

        return FilterableList[RBXAccessory]()
    
    @property
    def friends(self) -> FilterableList[RBXUser]:
        """
        All users friended to this user.
        """

        if self._partial_reference:
            self.complete_load()

        return FilterableList[RBXUser](self._friends)

    def __eq__(self, other):
        """
        Determines if RBXUser is equal to the other by matching their user ID.
        """
        return self.id == other.id

    @staticmethod
    def from_id(id: int) -> RBXUser:
        """
        Create a Roblox user from their Player ID.
        """

        user = RBXUser(fetch_dict(f"https://users.roblox.com/v1/users/{id}"))
        
        return user

    def complete_load(self):
        """
        Exits the RBXUser out of partial reference mode and loads all avaliable data.
        """

        self.load_friends()

        self._partial_reference = False

    def load_friends(self):
        """
        Loads all friends of the user, replacing any old data.
        """

        friends_api_data = fetch_dict(f"https://friends.roblox.com/v1/users/{self.id}/friends")

        for friend_api_data in friends_api_data["data"]:
            self._friends.append(RBXUser(friend_api_data, True))
    
    def __init__(self, data: dict, partial_reference = False):
        """
        Create a new instance of RBXUser with the raw API data.
        To get a RBXUser from their player ID, use RBXUser.from_id().

        Arguments:
            `data` (dict): The raw API data.
            `partial_reference` (bool): If True, will only partially load the profile to save memory.
        """

        if "nan" in data:
            return

        self._id = data["id"]

        self._display_name = data["displayName"]
        self._user_name = data["name"]

        if partial_reference:
            self._partial_reference = True
            return
        
        self.load_friends()
        