# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/


from typing import List


def maxSubArray(nums: List[int]) -> int:
    
    maxSum = nums[0]
    curSum = 0

    for i in nums:

        if curSum < 0:
            curSum = 0
        curSum += i

        maxSum = max(curSum, maxSum)

    return maxSum



nums_1 = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

nums_2 = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

nums_3 = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
print(maxSubArray(nums_1))
print(maxSubArray(nums_2))
print(maxSubArray(nums_3))
