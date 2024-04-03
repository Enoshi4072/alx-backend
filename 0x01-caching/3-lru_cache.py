#!/usr/bin/python3
""" Last recently used(LRU) algorithm """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching

class LRUCache(BaseCaching):
    """ Implementing the LRU algo """

    def __init__(self):

        """ Initializing all to be used """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Inserting an item to the cache """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > self.MAX_ITEMS:
                removed_item, _ = self.cache_data.popitem(True)
                print("DISCARD: {}".format(removed_item))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """ Retrieving an item from the cache """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
