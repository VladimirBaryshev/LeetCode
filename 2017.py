# 2017. Grid Game


from typing import List


class Solution:

    def gridGame(self, grid: List[List[int]]) -> int:

        upper_right, lower_left, ans = sum(grid[0]), 0, math.inf
        
        for upper, lower in zip(grid[0], grid[1]):
            upper_right -= upper
            ans = min(ans, max(upper_right, lower_left))
            lower_left += lower
        return ans




grid_1 = [[2,5,4],[1,5,1]]
# Output: 4
# Explanation: The optimal path taken by the first robot is shown in red, 
# and the optimal path taken by the second robot is shown in blue.
# The cells visited by the first robot are set to 0.
# The second robot will collect 0 + 0 + 4 + 0 = 4 points.       
        

grid_2 = [[3,3,1],[8,5,2]]
# Output: 4
# Explanation: The optimal path taken by the first robot is shown in red, 
# and the optimal path taken by the second robot is shown in blue.
# The cells visited by the first robot are set to 0.
# The second robot will collect 0 + 3 + 1 + 0 = 4 points.        

grid_3 = [[1,3,1,15],[1,3,3,1]]
# Output: 7
# Explanation: The optimal path taken by the first robot is shown in red, 
# and the optimal path taken by the second robot is shown in blue.
# The cells visited by the first robot are set to 0.
# The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.


print(Solution().gridGame(grid_1))
# print(Solution().gridGame(grid_2))
# print(Solution().gridGame(grid_3))

