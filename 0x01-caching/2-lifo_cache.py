#!/usr/bin/python3
""" Implementing the LIFO algorithm """
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Lifo algorithm taking place """

    def __init__(self):
        """ Initializing from the master class """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Putting an item to the cache """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if (len(self.cache_data) + 1) > self.MAX_ITEMS:
                last_item, _ = self.cache_data.popitem(last=True)
                print("DISCARD: {}".format(last_item))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ Retrieving an Item """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data[key]
