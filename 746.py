# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List

class Solution:

    def minCostClimbingStairs(self, costs: List[int]) -> int:
        
        costs.append(0)

        for i in range(len(costs)-3, -1, -1):
            costs[i] += min(costs[i+1], costs[i+2])

        return min(costs[0], costs[1])





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

