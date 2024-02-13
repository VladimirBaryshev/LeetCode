# 268. Missing Number
# https://leetcode.com/problems/missing-number/description/


from typing import List


def missingNumber(nums: List[int]) -> int:

    res = len(nums)

    for i in range(0, len(nums)):

        # print(i, nums[i], res, i - nums[i])
        res += (i - nums[i])

    return res



nums_1 = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 
# 2 is the missing number in the range since it does not appear in nums.

nums_2 = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 
# 2 is the missing number in the range since it does not appear in nums.

nums_3 = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 
# 8 is the missing number in the range since it does not appear in nums.

print(missingNumber(nums_1))
print(missingNumber(nums_2))
print(missingNumber(nums_3))

