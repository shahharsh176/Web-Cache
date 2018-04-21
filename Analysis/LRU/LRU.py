from time import sleep
from datetime import datetime
import os

#LRU with name_list

"""
---------------------------------------------------
testing
--------------------------------------------------------------------
site		with name_list			without name_list
--------------------------------------------------------------------
facebook	0.0030880000000000005		0.0026900000000000014
google		0.003355999999999998		0.003911999999999999
facebook	0.00039100000000000246		0.00027500000000000094
yahoo		0.0038010000000000058		0.004617000000000003
yahoo		0.00026500000000000135		0.0003009999999999957
youtube		0.0035329999999999945		0.0031160000000000007
geeks		0.070503			0.073835
youtube		0.0003070000000000017		0.0002580000000000082
geeks		0.00233499999999999		0.002371999999999999
"""

hit = 0
miss = 0
class LRUCacheItem(object):
    """Data structure of items stored in cache"""
    def __init__(self, name):
        # self.key = key
        self.name = name
        self.timestamp = datetime.now()


class LRUCache(object):
    """A sample class that implements LRU algorithm"""
    def __init__(self, length):
        self.length = length
        self.item_list = []
        self.name_list = []

    def insertItem(self, item):
        """Insert new items to cache"""
        # ls = []
        # for i in self.item_list:
        # 	ls.append(i.name)
        # if any(item.name in s.name for s in self.item_list):
        if item.name in self.name_list:
            global hit
            hit += 1.0
            # print("yes")
            # Move the existing item to the head of item_list.
            item_index = self.name_list.index(item.name)
            try:
                self.item_list[:] = self.item_list[:item_index] + self.item_list[item_index+1:]
                self.item_list.insert(0, item)
                self.name_list[:] = self.name_list[:item_index] + self.name_list[item_index+1:]
                self.name_list.insert(0, item.name)
            except:
                print("error")
        else:
            # print("no")
            # Remove the last item if the length of cache exceeds the upper bound.
            global miss
            miss += 1.0
            if len(self.item_list) >= self.length:
                self.removeItem(self.item_list[-1])

            # If this is a new item, just append it to
            # the front of item_list.
            self.item_list.insert(0, item)
            self.name_list.insert(0,item.name)

    def removeItem(self, item):
        """Remove those invalid items"""
        del self.item_list[self.item_list.index(item)]
        del self.name_list[self.name_list.index(item.name)]
        # os.remove(item.name)

def hitratio():
    print "Hit: ",hit," Miss: ",miss," Hit-ratio: ",float(hit/(hit+miss))
    global hit
    hit = 0
    global miss
    miss = 0


def print_cache(cache):
    print "---------------------------------------------"
    print "Current cache:"
    for i, item in enumerate(cache.item_list):
        print ("index: {0} "
               "name: {1} "
               "timestamp: {2}".format(i,
                                  item.name,
                                  item.timestamp))
    print "---------------------------------------------"



# one = LRUCacheItem(1, 'one')
# two = LRUCacheItem(2, 'two')
# three = LRUCacheItem(3, 'three')

# print ("Initial cache items.")
# cache = LRUCache(length=3, delta=5)
# cache.insertItem(one)
# cache.insertItem(two)
# cache.insertItem(three)
# print_cache(cache)
# print ("#" * 20)

# print ("Insert a existing item: {0}.".format(one.key))
# cache.insertItem(one)
# print_cache(cache)
# print ("#" * 20)

# print ("Insert another existing item: {0}.".format(two.key))
# cache.insertItem(two)
# print_cache(cache)
# print ("#" * 20)

# print ("Validate items after a period of time")
# sleep(6)
# cache.validateItem()
# print_cache(cache)
# print ("#" * 20)
