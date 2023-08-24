#!/usr/bin/env python3
"""LIFOCache module inherits from BaseCaching"""
from base_caching import BaseCaching

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """A caching system."""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """stores key and value in the cache

        Args:
            key[str] - to check
            item - value of key

        Return:
            None if no item else
            implement a LIFO caching
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item = list(self.cache_data.keys())[-1]
            print(f"DISCARD: {last_item}")
            del self.cache_data[last_item]

        self.cache_data[key] = item

        def get(self, key):
            """Retrieves the value linked to key

            Args:
                key[str] - to check

            Returns:
                value linked to key
            """
            if key is None or key not in self.cache_data[key]:
                return None
            else:
                return self.cache_data[key]
