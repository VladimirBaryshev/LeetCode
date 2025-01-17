# 1351. Count Negative Numbers in a Sorted Matrix

from typing import List

class Solution:

    def binary(self, row: List[int]) -> int:
        l = 0
        r = len(row)-1

        while l < r:
            cur = (l+r)//2
            if row[cur] < 0:
                r = cur
            if row[cur] >= 0:
                l = cur+1

        return l


    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        for g in grid:
            cur = self.binary(g)
            if g[cur] < 0:
                count += (len(g) - cur)

        return count

        



grid_1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

grid_2 = [[3,2],[1,0]]
# Output: 0

print(Solution().countNegatives(grid_1))
print(Solution().countNegatives(grid_2))