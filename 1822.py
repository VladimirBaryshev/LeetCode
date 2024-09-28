# 1822. Sign of the Product of an Array


from typing import List


class Solution:

    def arraySign(self, nums: List[int]) -> int:
        
        less_then_zero = 0
        zeros = 0

        for i in nums:
            if i < 0:
                less_then_zero += 1

            if i == 0:
                return 0

        if less_then_zero % 2 == 0:
            return 1

        return -1




nums_1 = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1

nums_2 = [1,5,0,2,-3]
# Output: 0
# Explanation: The product of all values in the array is 0, and signFunc(0) = 0

nums_3 = [-1,1,-1,1,-1]
# Output: -1
# Explanation: The product of all values in the array is -1, and signFunc(-1) = -1


print(Solution().arraySign(nums_1))
print(Solution().arraySign(nums_2))
print(Solution().arraySign(nums_3))

