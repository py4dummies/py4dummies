# py4dummies/classes/RBXUser.py - RBXUser class
# (C) Copyright 2026 Ben Daws. BSD-3 License

"""
Holds the RBXUser class.
"""

from .RBXAccessory import RBXAccessory
from ..filterable.FilterableList import FilterableList

_ournone = None

class RBXUser:
    """
    A Roblox user.
    """

    _id = 1

    _display_name = "Roblox"
    _user_name = "Roblox"

    _friends: list[RBXUser] = [ ]

    @staticmethod
    def __createnone() -> RBXUser:
        nan = RBXUser(-1)

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
    
    def __init__(self, id: int):
        """
        Create a new instance of RBXUser.
        """

        self._id = id