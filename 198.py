# 198. House Robber
# https://leetcode.com/problems/house-robber/


from typing import List


class Solution:

    def rob(self, nums: List[int]) -> int:

        # print('nums', nums)

        rob_1, rob_2 = 0, 0

        for i in range(len(nums)):

            print(f'i={i} max({rob_1}+{nums[i]}, {rob_2})')
            temp = max(rob_1+nums[i], rob_2)
            rob_1 = rob_2
            rob_2 = temp

        return rob_2



nums_1 = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

nums_2 = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

nums_3 = [0]
# Output: 0

nums_4 = [2,1,1,2]
# Output: 4


# print(Solution().rob(nums_1))
print(Solution().rob(nums_2))
# print(Solution().rob(nums_3))
# print(Solution().rob(nums_4))


