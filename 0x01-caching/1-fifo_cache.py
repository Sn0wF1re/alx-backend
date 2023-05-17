#!/usr/bin/env python3
"""
Create class FIFOCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Implements FIFO cache replacement policy
    """
    def __init__(self):
        """
        Initialize super class
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value
        for the key key
        """
        if key is None or item is None:
            pass

        else:
            length = len(self.cache_data)
            if key not in self.cache_data and length >= BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                self.cache_data.pop(first_key)
            self.cache_data[key] = item

    def get(self, key):
        """
        return value in self.cache_data linked to key
        """
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        return None
