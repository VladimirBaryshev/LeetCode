# 1913. Maximum Product Difference Between Two Pairs


from typing import List


class Solution:

    def maxProductDifference(self, nums: List[int]) -> int:
        
        nums.sort()

        return (nums[-1]*nums[-2]) - (nums[0]*nums[1])





nums_1 = [5,6,2,7,4]
# Output: 34
# Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
# The product difference is (6 * 7) - (2 * 4) = 34.

nums_2 = [4,2,5,9,7,4,8]
# Output: 64
# Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
# The product difference is (9 * 8) - (2 * 4) = 64.

print(Solution().maxProductDifference(nums_1))
print(Solution().maxProductDifference(nums_2))
