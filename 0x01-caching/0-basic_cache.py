#!/usr/bin/env python3
"""
Create class BasicCache that inherits from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Create class BasicCache
    """
    def __init__(self):
        """
        Initialize with base class
        """
        super().__init__()

    def put(self, key, item):
        """
        Assign to the dictionary the item value for the key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        return value in self.cache_data linked to key
        """
        if key in self.cache_data and key is not None:
            return self.cache_data[key]
        return None
