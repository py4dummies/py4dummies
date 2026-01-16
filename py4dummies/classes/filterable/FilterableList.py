# py4dummies/classes/filterable/FilterableList.py - FilterableList class
# (C) Copyright 2026 Ben Daws. BSD-3 License

from typing import Any, Callable
from .FilterableItem import FilterableItem

class FilterableList[T]:
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

    def remove(self, key: Any):
        """
        Remove the key from this FilterableList.
        """

        del self.__items[key]
    
    def cherry_pick(self, filter: Callable[[FilterableItem[T]], bool]) -> FilterableList[T]:
        """
        Run each element in the FilterableList through `filter`, which will
        remove the item from the FilterableList and add it to your "basket" if `filter` returns `True`.

        Arguments:
            `filter` (Callable[[FilterableItem], bool]): The filter that each item in the list will be passed through. If the filter returns `False`, the item is removed.
        
        Returns:
            (FilterableList[T]) A list where all cherry-picked items are placed.
        """ 
        
        basket: FilterableList[T] = FilterableList[T]()

        for idx in range(len(self.__items)):
            value = self.__items[idx]
            filterableItem = FilterableItem[T](idx, value)

            pick = filter(filterableItem)

            if pick:
                del self.items[filterableItem.key]
                basket.append(filterableItem.value)
        
        return basket

    def pass_through(self, filter: Callable[[FilterableItem[T]], None]) -> None:
        """
        Run each element in the FilterableList through `filter` without any post-processing,
        making filter responsible for the management of items.

        Arguments:
            `filter` (Callable[[FilterableItem], None]): The filter that each item in the list will be passed through.
        """

        for idx in range(len(self.__items)):
            value = self.__items[idx]
            filterableItem = FilterableItem[T](idx, value)

            filter(filterableItem)
    
    def __getitem__(self, key: Any) -> T:
        """
        Gets the value of an item at `key`.
        """
        return self.__items[key]
    
    def __setitem__(self, key: Any, value: Any):
        """
        Sets the value of `key` to `value` in the FilterableList.
        """
        self.__items[key] = value
    
    def __delitem__(self, key: Any):
        """
        Deletes `key` and its corresponding value from the FilterableList.
        """
        del self.__items[key]
    
    def __sizeof__(self) -> int:
        return len(self.__items)

    def __init__(self, items: list[T] = []):
        """
        Creates a new instance of FilterableList.
        """
        
        self.__items = items