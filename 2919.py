# 2919. Minimum Increment Operations to Make Array Beautiful

from typing import List

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        
        dp = [0,0,0]

        for n in nums:

            dp = [dp[-2], dp[-1], max(k-n, 0)+min(dp)]
            print(n, dp)

        return min(dp)



nums_1 = [2,3,0,0,2]
k_1 = 4
# [0,0,2]
# [0,2,1]
# [2,1,4]
# [1,4,5]
# [4,5,3]

# Output: 3
# Explanation: We can perform the following increment operations to make nums beautiful:
# Choose index i = 1 and increase nums[1] by 1 -> [2,4,0,0,2].
# Choose index i = 4 and increase nums[4] by 1 -> [2,4,0,0,3].
# Choose index i = 4 and increase nums[4] by 1 -> [2,4,0,0,4].
# The subarrays with a size of 3 or more are: [2,4,0], [4,0,0], [0,0,4], [2,4,0,0], [4,0,0,4], [2,4,0,0,4].
# In all the subarrays, the maximum element is equal to k = 4, so nums is now beautiful.
# It can be shown that nums cannot be made beautiful with fewer than 3 increment operations.
# Hence, the answer is 3.

nums_2 = [0,1,3,3]
k_2 = 5
# [0,0,5]
# [0,5,4]
# [5,4,2]
# [4,2,4]

# Output: 2
# Explanation: We can perform the following increment operations to make nums beautiful:
# Choose index i = 2 and increase nums[2] by 1 -> [0,1,4,3].
# Choose index i = 2 and increase nums[2] by 1 -> [0,1,5,3].
# The subarrays with a size of 3 or more are: [0,1,5], [1,5,3], [0,1,5,3].
# In all the subarrays, the maximum element is equal to k = 5, so nums is now beautiful.
# It can be shown that nums cannot be made beautiful with fewer than 2 increment operations.
# Hence, the answer is 2.

nums_3 = [1,1,2]
k_3 = 1
# [0,0,0]
# [0,0,0]
# [0,0,0]
# Output: 0
# Explanation: The only subarray with a size of 3 or more in this example is [1,1,2].
# The maximum element, 2, is already greater than k = 1, so we don't need any increment operation.
# Hence, the answer is 0.

print(Solution().minIncrementOperations(nums_1, k_1))
print(Solution().minIncrementOperations(nums_2, k_2))
print(Solution().minIncrementOperations(nums_3, k_3))

