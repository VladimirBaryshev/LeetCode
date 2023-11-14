# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List

class Solution:

    def minCostClimbingStairs(self, costs: List[int]) -> int:
        
        possible_steps = [1,2]

        stack = [
                    [0, 0, [costs[0]]], 
                    [1, 0, [costs[1]]]
                ]

        min_cost = float("inf")

        while stack:

            cur_i, cur_cost, path = stack.pop()

            for p_s in possible_steps:

                if cur_i+p_s < len(costs):
                    stack.append([cur_i+p_s, cur_cost+costs[cur_i], path[::]+[costs[cur_i+p_s]]])
                elif cur_i+p_s == len(costs):
                    min_cost = min(min_cost, cur_cost+costs[cur_i])
                    # print(cur_i, cur_i+p_s, cur_cost+costs[cur_i], path)

        return min_cost






cost_1 = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

cost_2 = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.

print(Solution().minCostClimbingStairs(cost_1))
print(Solution().minCostClimbingStairs(cost_2))

