#!/usr/bin/env python3
"""LIFOCache module inherits from BaseCaching"""
from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """A caching system."""
    def __init__(self):
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        """stores key and value in the cache

        Args:
            key[str] - to check
            item - value of key

        Return:
            None if no item else
            implement a FIFO caching
        """
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.queue.popleft()
            print(f"DISCARD: {discard}")
            del self.cache_data[discard]

        self.queue.append(key)
        self.cache_data[key] = item

        def get(self, key):
            """Retrieves the value linked to key

            Args:
                key[str] - to check

            Returns:
                value linked to key
            """
            if key is None or not key:
                return None
            else:
                return self.cache_data.get(key)
