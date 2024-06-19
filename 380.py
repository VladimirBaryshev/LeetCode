# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/

import random
from collections import defaultdict


class RandomizedSet:

    def __init__(self):
        
        self.d = defaultdict(bool)
        

    def insert(self, val: int) -> bool:
        
        if self.d[val]:
            return False
        else:
            self.d[val] = True
            return True

    def remove(self, val: int) -> bool:

        if self.d[val]:
            self.d.pop(val)
            return True
        else:
            self.d.pop(val)
            return False

    def getRandom(self) -> int:
        print(self.d.keys())
        return random.choice(tuple(self.d.keys()))


# # Your RandomizedSet object will be instantiated and called as such:
# randomizedSet = RandomizedSet();
# print(randomizedSet.insert(1)) # // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# print(randomizedSet.remove(2)) # // Returns false as 2 does not exist in the set.
# print(randomizedSet.insert(2)) # // Inserts 2 to the set, returns true. Set now contains [1,2].
# print(randomizedSet.getRandom()) # // getRandom() should return either 1 or 2 randomly.
# print(randomizedSet.remove(1))# // Removes 1 from the set, returns true. Set now contains [2].
# print(randomizedSet.insert(2))# // 2 was already in the set, so return false.
# print(randomizedSet.getRandom())# // Since 2 is the only number in the set, getRandom() will always return 2.


randomizedSet = RandomizedSet();
print(randomizedSet.insert(0))
print(randomizedSet.remove(0))
print(randomizedSet.insert(-1))
print(randomizedSet.remove(0))
print(randomizedSet.getRandom())


