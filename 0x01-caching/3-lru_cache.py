#!/usr/bin/env python3
"""
Create class LRUCache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()
        self.accessed = []

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value
        for the key key
        """
        if key and item:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print(f"DISCARD: {self.accessed[0]}")
                self.cache_data.pop(self.accessed[0])
                del self.accessed[0]

            if key in self.accessed:
                self.accessed.remove(key)
            self.accessed.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        return None
