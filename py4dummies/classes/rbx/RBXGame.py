# py4dummies/classes/RBXGame.py - RBXGame class
# (C) Copyright 2026 Ben Daws. BSD-3 License

"""
Holds the RBXGame class.
"""

from .RBXGroup import RBXGroup
from .RBXUser import RBXUser

class RBXGame:
    """
    Represents a Roblox game.
    """

    _id = 0
    _owner_is_group = False

    _owner_group: RBXGroup = RBXGroup(-1)
    _owner_user: RBXUser = RBXUser.none()

    _title = "Game Name"

    @property
    def title(self) -> str:
        """
        The name of the game.
        """

        return self._title

    @property
    def owner(self) -> RBXGroup | RBXUser:
        """
        The owner of the Roblox game.
        This can be a RBXGroup or RBXUser, so make sure you check the type before using.
        """
        return self._owner_group if self._owner_is_group else self._owner_user
    
    @property
    def absolute_owner(self) -> RBXUser:
        """
        The absolute owner of the Roblox game. If the game is owned by a group, this will
        be the owner of that group.
        """

        return self._owner_group.owner if self._owner_is_group else self._owner_user