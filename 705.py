# 705. Design HashSet
# https://leetcode.com/problems/design-hashset/description/

class MyHashSet:

    def __init__(self):
        self.d = dict()
        # self.vector = [False for i in range(10**34)]


    def add(self, key: int) -> None:
        self.d[key] = True
        # self.vector[key] = True
    

    def remove(self, key: int) -> None:
        self.d[key] = False
        # self.vector[key] = False

        # if self.contains(key):
            # del self.d[key]
            

    def contains(self, key: int) -> bool:
        # return key in self.d
        # return self.vector[key]
        if key in self.d.keys():
            if self.d[key] == True:
                return True
            else:
                return False
        else:
            return False



