# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

from typing import List
import heapq


def accumulate_(islands):

    accumulates = []
    
    heapq.heapify(islands)

    while islands:
        coord = heapq.heappop(islands)

        if accumulates == []:
            accumulates.append([coord])
        else:
            cand_r = [coord[0], coord[1]-1]
            cand_d = [coord[0]-1, coord[1]]

            if cand_d in accumulates[-1] or cand_r in accumulates[-1]:
                accumulates[-1].append(coord)
            else:
                accumulates.append([coord])

    return accumulates


def numIslands(grid: List[List[str]]) -> int:

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    visited = [[False]*len(grid[0]) for i in range(len(grid))]

    d_x, d_y = 0, 0
    stack = [[0,0]]

    islands = []

    while stack:

        x,y = stack.pop()

        for d_x, d_y in directions:

            if x+d_x >= 0 and x+d_x < len(grid):
                temp_x = x + d_x
            else:
                temp_x = x

            if y+d_y >=0 and y+d_y < len(grid[0]):
                temp_y = y + d_y
            else:
                temp_y = y


            if visited[temp_x][temp_y] == False:

                if grid[temp_x][temp_y] == '1':

                    # print('YO:1', temp_x, temp_y)
                    islands.append([temp_x, temp_y])

                visited[temp_x][temp_y] = True
                stack.append([temp_x, temp_y])


    islands = accumulate_(islands)

    return len(islands), islands


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

print(numIslands(grid_0))
print(numIslands(grid_1))
print(numIslands(grid_2))
print(numIslands(grid_3))
print(numIslands(grid_4))
print(numIslands(grid_5))
print(numIslands(grid_6))







