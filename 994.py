# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/

from collections import deque
from typing import List


class Solution:

    def __init__(self):

        self.grid = None
        self.directions = [(0,1),(1,0),(-1,0),(0,-1)]
        self.ROW = None
        self.COLS = None


    def orangesRotting(self, grid: List[List[int]]) -> int:

        self.grid = grid
        self.ROW = len(grid)
        self.COLS = len(grid[0])

        q = deque()

        fresh = 0
        time = 0

        for row in range(self.ROW):
            for col in range(self.COLS):
                if self.grid[row][col] == 1:
                    fresh += 1
                if self.grid[row][col] == 2:
                    q.append((row,col))

        while fresh > 0 and q:

            lenght = len(q)

            for i in range(lenght): # iterate each rotten orange
                r,c = q.popleft()


                for dr, dc in self.directions:

                    row = r + dr
                    col = c + dc

                    if (
                            (row >= 0 and row < self.ROW)
                            and (col >= 0 and col < self.COLS)
                            and (self.grid[row][col] == 1)
                        ):
                        self.grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            time += 1

        if fresh == 0:
            return time
        else:
            return -1











grid_1 = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# [
#     [2,1,1],
#     [1,1,0],
#     [0,1,1]
# ]

grid_2 = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# [
#     [2,1,1],
#     [0,1,1],
#     [1,0,1]
# ]

# Explanation: The orange in the bottom left corner (row 2, column 0)
# is never rotten, because rotting only happens 4-directionally.


grid_3 = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, 
# the answer is just 0.

grid_4 = [[1,1,1],[0,2,1],[1,0,1]]
# Output: -1
# [
#     [1,1,1],
#     [0,2,1],
#     [1,0,1]
# ]

grid_5 = [[1,1,1],[0,2,1],[0,0,1]]
# Output: 2
# [
#     [1,1,1],
#     [0,2,1],
#     [0,0,1]
# ]


grid_6 = [[0,2,2]]
# Output: 0



print(Solution().orangesRotting(grid_1))
print(Solution().orangesRotting(grid_2))
print(Solution().orangesRotting(grid_3))
print(Solution().orangesRotting(grid_4))
print(Solution().orangesRotting(grid_5))
print(Solution().orangesRotting(grid_6))



