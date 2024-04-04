#!/usr/bin/python3
""" Impoer OrderedDict for ordered dictionary functionality"""
from collections import OrderedDict, defaultdict
from datetime import datetime
#Import the basecaching
from base_caching import BaseCaching
#define LFU cache algo
class LFUCache(BaseCaching):
    #Initialize
    def __init__(self):
        #call the parent class's constructor
        super().__init__()
        self.frequency = defaultdict(int)
        self.cache_time = {}

    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        elif len(self.cache_data) + 1 > self.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
            if len(lfu_keys) == 1:
                removed_key = lfu_keys[0]
            else:
                removed_key = min(self.cache_data, key=lambda k: self.cache_time[k])
            print("DISCARD: {}".format(removed_key))
            self.cache_data.pop(removed_key)
            self.frequency.pop(removed_key)
            self.cache_time.pop(removed_key)
        else:
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.cache_time[key] = datetime.now()

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.cache_data[key]
