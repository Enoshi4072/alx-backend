#!/usr/bin/python3
""" Implementing the Most Recently Used(LRU) Algorithm"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Implementing LRU keeping in mind the limit"""
    def __init__(self):
        """ Initializing the class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Assigning items to the cache """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
        if key not in self.cache_data:
            if (len(self.cache_data) + 1) > self.MAX_ITEMS:
                removed_item, _ = self.cache_data.popitem(last=True)
                print("DISCARD: {}".format(removed_item))
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieving items from the cache """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
        return self.cache_data.get(key)
