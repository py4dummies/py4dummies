# py4dummies/classes/filterable/FilterableItem.py - FilterableList class
# (C) Copyright 2026 Ben Daws. BSD-3 License

from typing import Any, Callable

class FilterableItem[T]:
    """
    Represents an item inside of a FilterableList.
    """

    __key: Any = None
    __value: T = None # type: ignore

    @property
    def key(self) -> Any:
        """
        The key of the FilterableItem.
        """
        return self.__key

    @property
    def value(self) -> T:
        """
        The value of the FilterableItem.
        """
        return self.__value

    def __init__(self, key, value: T):
        """
        Create a new FilterableItem.
        This should only be done by FilterableList and derivatives, do not create instances yourself.
        """

        self.__key = key
        self.__value = value
