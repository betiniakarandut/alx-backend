#!/usr/bin/env python3
"""LIFOCache module inherits from BaseCaching"""
from base_caching import BaseCaching

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
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
            implement a FIFO caching
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f"DISCARD: {first_key}")
            self.cache_data.pop(first_key)

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
                return self.cache_data[key]

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache() 
