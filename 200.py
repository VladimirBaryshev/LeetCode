# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:

    def __init__(self, grid):

        self.grid = grid
        self.visited = set()
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


    def dfs(self, row: int, column: int) -> List[str]:
        
        stack = [[row, column]]

        island = []

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


                if (temp_x, temp_y) not in self.visited and self.grid[temp_x][temp_y] == '1':
                        island.append([temp_x, temp_y])
                        self.visited.add((temp_x, temp_y))
                        stack.append([temp_x, temp_y])

        return island



    def numIslands(self) -> int:

        islands = []
        
        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):

                if (row, column) not in self.visited and self.grid[row][column] == '1':
                    islands.append(self.dfs(row, column))

        return len(islands)



grid_0 = [
    ["0", "1"],
    ["0", "1"]
]
# Output: 1

grid_1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# Output: 1


grid_2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# Output: 3

grid_3 = [["1"]]
# Output: 1

grid_4 = [
    ["0","1","0"],
    ["1","0","1"],
    ["0","1","0"]
]
# Output: 4

grid_5 = [
    ["1","1","1"],
    ["0","0","0"],
    ["0","0","0"]
]
# Output: 1

grid_6 = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]
# Output: 1

t = Solution(grid_0)
print(t.numIslands())

t = Solution(grid_1)
print(t.numIslands())

t = Solution(grid_2)
print(t.numIslands())

t = Solution(grid_3)
print(t.numIslands())

t = Solution(grid_4)
print(t.numIslands())

t = Solution(grid_5)
print(t.numIslands())

t = Solution(grid_6)
print(t.numIslands())


