# 15. 3Sum
# https://leetcode.com/problems/3sum/description/


from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    triplets = set()
    nums.sort()
    for i in range(len(nums)):
        first = i
        second = i + 1
        third = len(nums) - 1
        while second < third:
            curSum = nums[first] + nums[second] + nums[third]
            if curSum > 0:
                third -= 1
            elif curSum < 0:
                second += 1
            else:
                triplets.add((nums[first] , nums[second] , nums[third]))
                second += 1
    return triplets


nums_1 = [-1,0,1,2,-1,-4] # [-4, -1, -1, 0, 1, 2]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

nums_2 = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

nums_3 = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

nums_4 = [-2,0,1,1,2]
# [[-2,0,2],[-2,1,1]]
 
print(threeSum(nums_1))
print(threeSum(nums_2))
print(threeSum(nums_3))
print(threeSum(nums_4))





