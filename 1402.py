# 1402. Reducing Dishes
# https://leetcode.com/problems/reducing-dishes/description/


from typing import List


class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort(reverse=True)
        # print(satisfaction)

        prefix_sum = 0
        res = 0

        for i in satisfaction: # [5,0,-1, -8,-9]
            prefix_sum += i # -4

            if prefix_sum < 0:
                return res

            res += prefix_sum #5 + 5 + 4

        return res





satisfaction_1 = [-1,-8,0,5,-9]
# Output: 14
# Explanation: After Removing the second and last dish, the maximum total like-time 
# coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
# Each dish is prepared in one unit of time.

satisfaction_2 = [4,3,2]
# Output: 20
# Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)

satisfaction_3 = [-1,-4,-5]
# Output: 0
# Explanation: People do not like the dishes. No dish is prepared.

print(Solution().maxSatisfaction(satisfaction_1))
print(Solution().maxSatisfaction(satisfaction_2))
print(Solution().maxSatisfaction(satisfaction_3))
