# 463. Island Perimeter
# https://leetcode.com/problems/island-perimeter/description/


from typing import List


class Solution:
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited_ones = set()

        for y, row in enumerate(grid):
            for x, col in enumerate(row):

                if grid[y][x] == 1:
                    visited_ones.add((y,x))

        count = len(visited_ones) * 4
        for y,x in visited_ones:
            if (y-1,x) in visited_ones:
                count -= 1
            if (y,x-1) in visited_ones:
                count -= 1
            if (y+1,x) in visited_ones:
                count -= 1
            if (y,x+1) in visited_ones:
                count -= 1

        return count


grid_1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

grid_2 = [[1]]
# Output: 4

grid_3 = [[1,0]]
# Output: 4

print(Solution().islandPerimeter(grid_1))
print(Solution().islandPerimeter(grid_2))
print(Solution().islandPerimeter(grid_3))