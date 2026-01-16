# py4dummies/classes/filterable/FilterableList.py - FilterableList class
# (C) Copyright 2026 Ben Daws. BSD-3 License

class FilterableList[T]():
    """
    FilterableList allows you to filter items.
    """
    __items: list[T] = []

    @property
    def items(self):
        """
        All items in the FilterableList.
        """
        return self.__items
    
    def append(self, item: T):
        """
        Appends `item` to the end of the FilterableList.
        """
        self.__items.append(item)
    
    def __getitem__(self, key) -> T:
        """
        Gets the value of an item at `key`.
        """
        return self.__items[key]
    
    def __setitem__(self, key, value):
        """
        Sets the value of `key` to `value` in the FilterableList.
        """
        self.__items[key] = value
    
    def __delitem__(self, key):
        """
        Deletes `key` and its corresponding value from the FilterableList.
        """
        del self.__items[key]

    def __init__(self, items: list[T] = []):
        """
        Creates a new instance of FilterableList.
        """
        
        self.__items = items