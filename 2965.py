# 2965. Find Missing and Repeated Values

from typing import List
from collections import defaultdict


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        d = dict((i+1,0) for i in range(len(grid)*len(grid)))

        for i, row in enumerate(grid):
            for j,col in enumerate(row):
                d[grid[i][j]] += 1

        return [k for k,v in d.items() if v == 2][0], [k for k,v in d.items() if v == 0][0]





grid_1 = [[1,3],[2,2]]
# Output: [2,4]
# Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

grid_2 = [[9,1,7],[8,9,2],[3,4,6]]
# Output: [9,5]
# Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].


print(Solution().findMissingAndRepeatedValues(grid_1))
print(Solution().findMissingAndRepeatedValues(grid_2))