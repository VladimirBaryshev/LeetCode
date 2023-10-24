# 695. Max Area of Island
# https://leetcode.com/problems/max-area-of-island/

from typing import List


class Solution:

    def __init__(self):

        self.grid = None
        self.visited = set()
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


    def dfs(self, row: int, column: int) -> List[str]:

        stack = [[row, column]]

        island = [[row, column]]
        self.visited.add((row, column))

        while stack:

            x,y = stack.pop()

            for d_x, d_y in self.directions:

                if x+d_x >= 0 and x+d_x < len(self.grid):
                    temp_x = x + d_x
                else:
                    temp_x = x

                if y+d_y >=0 and y+d_y < len(self.grid[0]):
                    temp_y = y + d_y
                else:
                    temp_y = y


                if (temp_x, temp_y) not in self.visited and self.grid[temp_x][temp_y] == 1:
                        island.append([temp_x, temp_y])
                        self.visited.add((temp_x, temp_y))
                        stack.append([temp_x, temp_y])

        return island



    def maxAreaOfIsland(self, grid) -> int:

        self.grid = grid

        max_island = 0
        
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):

                if (row, column) not in self.visited and self.grid[row][column] == 1:
                    t = self.dfs(row, column)
                    max_island = max(max_island, len(t))

        return max_island


grid_1 = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

grid_2 = [[0,0,0,0,0,0,0,0]]
# Output: 0

grid_3 = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]
# Output: 1

print(Solution().maxAreaOfIsland(grid_1))
print(Solution().maxAreaOfIsland(grid_2))
print(Solution().maxAreaOfIsland(grid_3))


