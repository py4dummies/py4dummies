# py4dummies/classes/filterable/FilterableItem.py - FilterableList class
# (C) Copyright 2026 Ben Daws. BSD-3 License

from .FilterableList import FilterableList

class FilterableItem[T]():
    """
    Represents an item inside of a FilterableList.
    """

    __key = None
    __value: T = None # type: ignore
    __parent: FilterableList[T] = None # type: ignore

    @property
    def value(self) -> T:
        """
        The value of the FilterableItem.
        """
        return self.__value

    def remove(self):
        """
        Remove this item from it's owning FilterableList. This will make the FilterableItem none, beware
        """

        del self.__parent[self.__key]
        del self


    def __init__(self, key, value: T, parent: FilterableList[T]):
        """
        Create a new FilterableItem.
        This should only be done by FilterableList and derivatives, do not create instances yourself.
        """

        self.__key = key
        self.__value = value
        self.__parent = parent
