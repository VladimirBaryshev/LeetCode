# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/

from typing import List, Tuple

class Solution:

    def __init__(self):

        self.visited = set()
        self.directions = [[0,1], [1,0], [0, -1], [-1, 0]]


    def dfs(self, board: List[List[int]], coords: List[int]) -> List[List[int]]:

        self.visited.add(coords)
        stack = [coords]
        island = [coords]

        while stack:

            x, y = stack.pop()

            for d_x, d_y in self.directions:

                if x+d_x >= 0 and x+d_x < len(board):
                    temp_x = x + d_x
                else:
                    temp_x = x

                if y+d_y >=0 and y+d_y < len(board[0]):
                    temp_y = y + d_y
                else:
                    temp_y = y

                if (temp_x, temp_y) not in self.visited and board[temp_x][temp_y] == "O":

                    island.append((temp_x, temp_y))
                    self.visited.add((temp_x, temp_y))
                    stack.append((temp_x, temp_y))

        return island


    def solve(self, board: List[List[str]]) -> None:

        """

            Do not return anything, modify board in-place instead.

        """

        edges = set()

        for m in range(len(board)):
            edges.add((m, 0))
            edges.add((m, len(board[0])-1))

        for n in range(len(board[0])):
            edges.add((0, n))
            edges.add((len(board)-1, n))

        # print(edges)

        for row in range(len(board)):
            for column in range(len(board[0])):

                if (row, column) not in self.visited and board[row][column] == 'O':
                    island = self.dfs(board, (row, column))
                    # print('island', island)
                    if set(island).intersection(edges) == set():
                        
                        for x,y in island:
                            board[x][y] = "X"
        print(board)        
        return None



board_1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.

board_2 = [["X"]]
# Output: [["X"]]

print(Solution().solve(board_1))
print(Solution().solve(board_2))




