# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/


from typing import List


class Solution:

    def __init__(self):

        self.grid = None
        self.directions = [(0,1),(1,0),(-1,0),(0,-1)]
        self.seen = set()


    def dfs(self, row_i, column_i):

        coords = (row_i, column_i)
        self.seen.add(coords)
        stack = [coords]
        island = [coords]
        rottens = set()

        while stack:

            coords = stack.pop()
            x,y = coords

            if self.grid[x][y] == 2:
                rottens.add((x,y))

            for d_x, d_y in self.directions:

                if x+d_x >= 0 and x+d_x < len(self.grid):
                    temp_x = x + d_x
                else:
                    temp_x = x

                if y+d_y >=0 and y+d_y < len(self.grid[0]):
                    temp_y = y + d_y
                else:
                    temp_y = y

                if (temp_x, temp_y) not in self.seen and self.grid[temp_x][temp_y] > 0:

                    island.append((temp_x, temp_y))
                    self.seen.add((temp_x, temp_y))
                    stack.append((temp_x, temp_y))

        if rottens and len(island) > 1:
            rot_count = 0
            while True:

                if set(island).issubset(rottens):
                    return island, rot_count

                for rot_x, rot_y in rottens.copy():
                    for x,y in self.directions:
                        rottens.add((rot_x+x, rot_y+y))

                rot_count += 1        

        if rottens and len(island) == 1:
            rot_count = 0
            return island, rot_count

        else:
            return island, -1


    def orangesRotting(self, grid: List[List[int]]) -> int:

        self.grid = grid

        islands = []

        for row_i in range(len(grid)):
            for column_i in range(len(grid[0])):
                if (row_i, column_i) not in self.seen and self.grid[row_i][column_i] > 0:
                    island = self.dfs(row_i, column_i)
                    islands.append(island)
        
        print(islands)
        max_rot_min = 0
        for _, rot_minutes in islands:
            if rot_minutes == -1:
                return -1
            max_rot_min = max(max_rot_min, rot_minutes)
        return max_rot_min


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
# print(Solution().orangesRotting(grid_2))
# print(Solution().orangesRotting(grid_3))
# print(Solution().orangesRotting(grid_4))
# print(Solution().orangesRotting(grid_5))
print(Solution().orangesRotting(grid_6))


'''
    TODO
'''



