#!/usr/bin/python3
""" Implementing fifo caching """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Intializing the ordered list """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Assigning a key to an item """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            removed_item, _ = self.cache_data.popitem(False)
            print("DISCARD: {}".format(removed_item))

    def get(self, key):
        """ Retriving a items relating to a given key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
