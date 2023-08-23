#!/usr/bin/env python3
"""BasicCache that inherits from BaseCaching"""
from base_caching import BaseCaching
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system.
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """stores key and value in the cache"""
        if item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves value in the cached data linked to key."""
        if key is None or not key:
            return None
        else:
            return self.cache_data.get(key)
