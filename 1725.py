# 1725. Number Of Rectangles That Can Form The Largest Square

from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        minLen = tuple(min(i) for i in rectangles)
        maxLen = max(minLen)
        return len(tuple(i for i in minLen if maxLen == i))


rectangles_1 = [[5,8],[3,9],[5,12],[16,5]]
# Output: 3
# Explanation: The largest squares you can get from each rectangle are of lengths [5,3,5,5].
# The largest possible square is of length 5, and you can get it out of 3 rectangles.

rectangles_2 = [[2,3],[3,7],[4,3],[3,7]]
# Output: 3     

print(Solution().countGoodRectangles(rectangles_1))
print(Solution().countGoodRectangles(rectangles_2))