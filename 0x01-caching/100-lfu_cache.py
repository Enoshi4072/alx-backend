#!/usr/bin/env python3
"""Least Frequently Used caching module.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents a caching system using the LFU algorithm."""

    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.keys_freq = {}
        self.frequency = {}

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.keys_freq[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.__evict()
            self.cache_data[key] = item
            self.keys_freq[key] = 1
        freq = self.keys_freq[key]
        if freq not in self.frequency:
            self.frequency[freq] = []
        self.frequency[freq].append(key)

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is None or key not in self.cache_data:
            return None
        self.keys_freq[key] += 1
        freq = self.keys_freq[key] - 1
        self.frequency[freq].remove(key)
        if not self.frequency[freq]:
            del self.frequency[freq]
        if self.keys_freq[key] not in self.frequency:
            self.frequency[self.keys_freq[key]] = []
        self.frequency[self.keys_freq[key]].append(key)
        return self.cache_data[key]

    def __evict(self):
        """Evict the least frequently used item(s) from the cache."""
        min_freq = min(self.frequency.keys())
        lfu_key = self.frequency[min_freq][0]
        print("DISCARD:", lfu_key)
        del self.cache_data[lfu_key]
        del self.keys_freq[lfu_key]
        self.frequency[min_freq].pop(0)
        if not self.frequency[min_freq]:
            del self.frequency[min_freq]
