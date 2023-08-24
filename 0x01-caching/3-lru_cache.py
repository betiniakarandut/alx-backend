#!/usr/bin/env python3
"""
LRU Caching
"""
from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    a class that inherits from 'BaseCaching' class
    and is a caching system -
    LEAST RECENTLY USED
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        A method to assign to the dictionary 'self.cache_data'
        the item value for the key 'key' following the LRU caching system

        Args:
            key - The key for an item
            item - The item belonging to a key
        """
        if (key is None) or (item is None):
            pass
        else:
            if key not in self.cache_data:
                if ((len(self.cache_data) + 1) > self.MAX_ITEMS):
                    dict_key, dict_value = (self.cache_data).popitem()
                    print("DISCARD: {}".format(dict_key))
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
            else:
                self.cache_data[key] = item

    def get(self, key):
        """
        A method to return the value
        in 'self.cache_data' linked to a key

        Args:
            key - The key for an item in 'self.cache_data'
        """
        if (key is None) or (key not in self.cache_data):
            return None
        else:
            (self.cache_data).move_to_end(key, last=False)
            return self.cache_data[key]
