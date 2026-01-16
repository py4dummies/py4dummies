# py4dummies/classes/bufferable/BufferableList.py - BufferableList class
# (C) Copyright 2026 Ben Daws. BSD-3 License

from typing import Callable, Any

class BufferableList[T]:
    """
    BufferableList allows you to fetch data in chunks.
    """

    fetch: Callable[[int], list[T]] = None # type: ignore
    chunk_size = 100

    def for_each(self, action: Callable[[T], None]):
        """
        Calls `action` for every item in the list. This will repeat until `fetch`
        returns a list with less items than `chunk_size`.
        """

        current_page = 1

        while True:
            # Not a true forever loop, just continues until the new chunk has
            # less items than the chunk size
            chunk = self.fetch(current_page)

            for item in chunk:
                action(item)
            
            if len(chunk) < self.chunk_size:
                break
        

    def __init__(self, fetch: Callable[[int], list[T]], chunk_size: int = 100):
        """
        Create a new BufferableList.

        `fetch` should return a list of the next list of items given (int) page number.
        """

        self.fetch = fetch
        self.current_page = -1
        self.current_chunk = []
        self.chunk_size = chunk_size