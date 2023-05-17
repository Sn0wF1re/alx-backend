#!/usr/bin/env python3
"""
Create class MRUCache
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Implements MRU cache replacement policy
    """
    def __init__(self):
        """
        Initialize super class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value
        for the key key
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = next(reversed(self.cache_data))
            print(f"DISCARD: {mru_key}")
            self.cache_data.pop(mru_key)

        self.cache_data[key] = item

    def get(self, key):
        """
        Return value in self.cache_data linked to key
        """
        if key in self.cache_data:
            val = self.cache_data[key]
            self.cache_data.pop(key)
            self.cache_data[key] = val
            return val

        return None