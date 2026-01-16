# py4dummies/classes/RBXAccessory.py - RBXAccessory class
# (C) Copyright 2026 Ben Daws. BSD-3 License

"""
Holds the RBXAccessory class.
"""

accessory_cache: dict[int, RBXAccessory] = { }
"""
The cache of already loaded accessories. Please access this list
with `RBXAccessory.Get()` to include null safety.
"""

class RBXAccessory:
    """
    Represents an item on the Roblox catalog.
    """

    _id = 1
    _display_name = ""
    _preview_url = ""

    @staticmethod
    def Get(id: int) -> RBXAccessory:
        """
        Gets or creates a new RBXAccessory. This is recommended to use over
        creating a new object to prevent duplicate RBXAccessories from being created.

        Parameters:
            `id` (int): The item ID of the accessory.
        
        Returns:
            (RBXAccessory): The RBXAccessory associated with the item.
        """
        
        if accessory_cache[id] != None:
            return accessory_cache[id]
        else:
            accessory = RBXAccessory(id)
            accessory_cache[id] = accessory

            return accessory

    def __init__(self, id: int):
        """
        Create a new RBXAccessory. This will not add itself to the accessory cache,
        which may cost performance if working with large amounts of items. Use
        `RBXAccessory.Get()` instead.

        Parameters:
            `id` (int): The item ID of the accessory.
        
        Returns:
            (RBXAccessory): The RBXAccessory associated with the item.
        """
        self._id = id
    
    def __del__(self):
        """
        Called when the accessory is destroyed.
        Removes itself from the accessory cache to prevent future errors.
        """
        accessory_cache.pop(self._id)