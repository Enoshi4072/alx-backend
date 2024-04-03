#!/usr/bin/python3
""" Importing the base class for caching """
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ The methods in the class """
    def put(self, key, item):
        """ Assigning a key to a item """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Getting a value from a given key """
        if key is None:
            return None
        return self.cache_data.get(key)
