# 2348. Number of Zero-Filled Subarrays


from typing import List


class Solution:

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        result = []

        l = 0
        r = 0

        while r < len(nums):            
            if nums[r] == 0:
                result.append(len(nums[l:r+1]))
                r += 1
            else:
                l = r+1
                r += 1

        return sum(result)



nums_1 = [1,3,0,0,2,0,0,4]
# Output: 6
# Explanation: 
# There are 4 occurrences of [0] as a subarray.
# There are 2 occurrences of [0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.

nums_2 = [0,0,0,2,0,0]
# Output: 9
# Explanation:
# There are 5 occurrences of [0] as a subarray.
# There are 3 occurrences of [0,0] as a subarray.
# There is 1 occurrence of [0,0,0] as a subarray.
# There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.

nums_3 = [2,10,2019]
# Output: 0
# Explanation: There is no subarray filled with 0. Therefore, we return 0.



print(Solution().zeroFilledSubarray(nums_1))
print(Solution().zeroFilledSubarray(nums_2))
print(Solution().zeroFilledSubarray(nums_3))