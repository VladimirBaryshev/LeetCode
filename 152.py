# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/


from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        result = nums[0]
        cur_max = 1
        cur_min = 1
        for n in nums:

            tmp = n*cur_max
            cur_max = max(n*cur_min, cur_max*n, n)
            cur_min = min(n*cur_min, tmp, n)
            result = max(result, cur_max)

        return result




nums_1 = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

nums_2 = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

nums_3 = [-4,-3,-2] 
# Output: 12

print(Solution().maxProduct(nums_1))
print(Solution().maxProduct(nums_2))
print(Solution().maxProduct(nums_3))





