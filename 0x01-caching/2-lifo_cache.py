#!/usr/bin/env python3
"""
Create class LIFOCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Create a class LIFOCache that inherits
    from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        Initialize class
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value
        for the key key
        """
        if key:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                last_key = next(reversed(self.cache_data))
                self.cache_data.pop(last_key)
                print(f"DISCARD: {last_key}")
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
