# 2970. Count the Number of Incremovable Subarrays I

from typing import List

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                # print(nums[:i], nums[j:])
                t = [*nums[:i], *nums[j:]]
                if t == sorted(t) and len(t) == len(set(t)):
                    count += 1

        return count

        

nums_1 = [1,2,3,4]
# Output: 10
# Explanation: The 10 incremovable subarrays are: 
# [1], [2], [3], [4], [1,2], [2,3], [3,4], [1,2,3], [2,3,4], and [1,2,3,4], 
# because on removing any one of these subarrays nums becomes strictly increasing. 
# Note that you cannot select an empty subarray.

nums_2 = [6,5,7,8]
# Output: 7
# Explanation: The 7 incremovable subarrays are: [5], [6], [5,7], [6,5], [5,7,8], [6,5,7] and [6,5,7,8].
# It can be shown that there are only 7 incremovable subarrays in nums.

nums_3 = [8,7,6,6]
# Output: 3
# Explanation: The 3 incremovable subarrays are: [8,7,6], [7,6,6], and [8,7,6,6]. 
# Note that [8,7] is not an incremovable subarray because after removing [8,7] nums becomes [6,6], 
# which is sorted in ascending order but not strictly increasing.

# print(Solution().incremovableSubarrayCount(nums_1))
# print(Solution().incremovableSubarrayCount(nums_2))
# print(Solution().incremovableSubarrayCount(nums_3))
print(Solution().incremovableSubarrayCount([1,2,3,4,5,6,7,8,9,10]))
