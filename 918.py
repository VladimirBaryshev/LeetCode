# 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/description/


from typing import List


class Solution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        best = float("-inf")
        cur_sum = 0

        for i in nums:
            
            cur_sum = max(best, best+i)
            best = max(cur_sum, best)

        return best

        