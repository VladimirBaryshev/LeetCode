# 2684. Maximum Number of Moves in a Grid

from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        dp={}

        def dfs(i,j):

            n=0
            n1=0
            n2=0

            if((i,j) in dp):
                return dp[(i,j)]

            if(i-1>=0 and j+1<len(grid[0]) and grid[i][j]<grid[i-1][j+1]):
                n=1+dfs(i-1,j+1)

            if(i>=0 and i<len(grid) and j+1<len(grid[0])):
                
                if(i+1<len(grid) and grid[i+1][j+1]>grid[i][j]):
                    n1=1+dfs(i+1,j+1)

                if(grid[i][j+1]>grid[i][j]):
                    n2=1+dfs(i,j+1)

            dp[(i,j)]=max(n,n1,n2)

            return dp[(i,j)]
            
        res=0
        for i in range(len(grid)):
            res=max(res,dfs(i,0))
        
        return res


grid_1 = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
# Output: 3
# Explanation: We can start at the cell (0, 0) and make the following moves:
# - (0, 0) -> (0, 1).
# - (0, 1) -> (1, 2).
# - (1, 2) -> (2, 3).
# It can be shown that it is the maximum number of moves that can be made.

grid_2 = [[3,2,4],[2,1,9],[1,1,7]]
# Output: 0
# Explanation: Starting from any cell in the first column we cannot perform any moves.

print(Solution().maxMoves(grid_1))
# print(Solution().maxMoves(grid_2))