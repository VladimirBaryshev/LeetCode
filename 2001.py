# 2001. Number of Pairs of Interchangeable Rectangles


from math import factorial
from typing import List
from collections import defaultdict

class Solution:

    def count(self, value):
        
        # 4!/(2!*(4-2)!)
        return int(factorial(value)/(factorial(2)*factorial(value-2)))

    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        
        d = defaultdict(int)

        for i in rectangles:
            division = i[0]/i[1]

            d[division] += 1

        return sum([self.count(v) for k,v in d.items() if v > 1])




rectangles_1 = [[4,8],[3,6],[10,20],[15,30]]
# Output: 6
# Explanation: The following are the interchangeable pairs of rectangles by index (0-indexed):
# - Rectangle 0 with rectangle 1: 4/8 == 3/6.
# - Rectangle 0 with rectangle 2: 4/8 == 10/20.
# - Rectangle 0 with rectangle 3: 4/8 == 15/30.
# - Rectangle 1 with rectangle 2: 3/6 == 10/20.
# - Rectangle 1 with rectangle 3: 3/6 == 15/30.
# - Rectangle 2 with rectangle 3: 10/20 == 15/30.

rectangles_2 = [[4,5],[7,8]]
# Output: 0
# Explanation: There are no interchangeable pairs of rectangles.

print(Solution().interchangeableRectangles(rectangles_1))
print(Solution().interchangeableRectangles(rectangles_2))

