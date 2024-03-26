# 2013. Detect Squares
# https://leetcode.com/problems/detect-squares/description/

from typing import List
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        
        self.pointsCount = defaultdict(int)
        self.points = list()

        

    def add(self, point: List[int]) -> None:
        
        self.pointsCount[tuple(point)] += 1
        self.points.append(point)
        

    def count(self, point: List[int]) -> int:
        
        res = 0
        px, py = point

        for x,y in self.points:
            if (abs(px - x) != abs(py-y)) or (x == px) or (y == py):
                # print('IF YO', px, py, x, y)
                continue
            # print('AFTER YO', px, py, x, y, self.pointsCount)
            res += (self.pointsCount[(px, y)])*(self.pointsCount[(x, py)]) # (11,2) * (3,10)

        # return print(res)
        return res
        

# ["DetectSquares",
# "add","add","add",
# "count","count",
# "add",
# "count"]
# [[],
# [[3,10]],[[11,2]],[[3,2]],
# [[11,10]],[[14,8]],
# [[11,2]],
# [[11,10]]]


obj = DetectSquares()
obj.add([3,10])
obj.add([11,2])
obj.add([3,2])
obj.count([11,10])
obj.count([14,8])
obj.add([11,2])
obj.count([11,10])
