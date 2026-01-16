# py4dummies/classes/RBXUser.py - RBXUser class
# (C) Copyright 2026 Ben Daws. BSD-3 License

"""
Holds the RBXUser class.
"""

from .RBXAccessory import RBXAccessory
from ..filterable.FilterableList import FilterableList
from ...utils import *

_ournone = None

class RBXUser:
    """
    A Roblox user.
    """

    _id = 1

    _display_name = "Roblox"
    _user_name = "Roblox"

    _bio = ""

    _is_banned = False

    _friends: list[RBXUser] = [ ]
    _friend_ids: list[int] = []

    @staticmethod
    def __createnone() -> RBXUser:
        nan = RBXUser({"nan": True})

        nan._display_name = "John Doe"
        nan._user_name = "John Doe"

        _ournone = nan
        return nan

    @staticmethod
    def none() -> RBXUser:
        """
        Represents either an unknown or non-existant player.
        RBXUser is non-nullable, however, this is the best representation
        of None avaliable.
        """

        return _ournone if _ournone != None else RBXUser.__createnone()

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
        return FilterableList[RBXAccessory]()

    @property
    def inventory(self) -> FilterableList[RBXAccessory]:
        """
        All accessories owned by this user.
        """
        return FilterableList[RBXAccessory]()
    
    @property
    def friends(self) -> FilterableList[RBXUser]:
        """
        All users friended to this user.
        """
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
    
    def __init__(self, data: dict, wasCreatedFromFriends = False):
        """
        Create a new instance of RBXUser with the raw API data.
        To get a RBXUser from their player ID, use RBXUser.from_id().
        """

        if "nan" in data:
            return

        self._id = data["id"]

        self._display_name = data["displayName"]
        self._user_name = data["name"]

        if wasCreatedFromFriends:
            return

        friends_api_data = fetch_dict(f"https://friends.roblox.com/v1/users/{self.id}/friends")

        for friend_api_data in friends_api_data["data"]:
            self._friends.append(RBXUser(friend_api_data, True))
        