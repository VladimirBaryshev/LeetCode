# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/


from typing import List


class Solution:

    def main(self, nums: List[int]) -> int:

        # print('nums', nums)

        rob_1, rob_2 = 0, 0

        for i in range(len(nums)):

            # print(f'i={i} max({rob_1}+{nums[i]}, {rob_2})')
            temp = max(rob_1+nums[i], rob_2)
            rob_1 = rob_2
            rob_2 = temp

        return rob_2


    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.main(nums[1:]), self.main(nums[:-1]))

nums_2 = [2,7,9,3,1]
print(Solution().rob(nums_2))
# Output 11




