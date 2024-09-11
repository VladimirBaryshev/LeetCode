# 1464. Maximum Product of Two Elements in an Array

from typing import List

class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        val_1, val_2 = 0, 0

        for num in nums:

            if num > val_1:
                val_1, val_2 = num, val_1

            elif num > val_2:
                val_2 = num

        return (val_1 - 1) * (val_2 - 1)

        


nums_1 = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), 
# you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

nums_2 = [1,5,4,5]
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), 
# you will get the maximum value of (5-1)*(5-1) = 16.

nums_3 = [3,7]
# Output: 12

# nums_4 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 16
# Explanation: 4 * 4 = 16


print(Solution().maxProduct(nums_1))
print(Solution().maxProduct(nums_2))
print(Solution().maxProduct(nums_3))




