# 1608. Special Array With X Elements Greater Than or Equal X

from typing import List

class Solution:

    def specialArray(self, nums: List[int]) -> int:
        
        nums.sort()

        for x in range(len(nums)+1):

            count = len(list(i for i in nums if i >= x))
            
            if count == x:
                return x

        return -1
            


nums_1 = [3,5]
# Output: 2
# Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

nums_2 = [0,0]
# Output: -1
# Explanation: No numbers fit the criteria for x.
# If x = 0, there should be 0 numbers >= x, but there are 2.
# If x = 1, there should be 1 number >= x, but there are 0.
# If x = 2, there should be 2 numbers >= x, but there are 0.
# x cannot be greater since there are only 2 numbers in nums.

nums_3 = [0,4,3,0,4]
# Output: 3
# Explanation: There are 3 values that are greater than or equal to 3.

nums_4 = [1]
# Output: 1

nums_5 = [3,6,7,7,0]
# Output: -1

print(Solution().specialArray(nums_1))
print(Solution().specialArray(nums_2))
print(Solution().specialArray(nums_3))
print(Solution().specialArray(nums_4))
print(Solution().specialArray(nums_5))
