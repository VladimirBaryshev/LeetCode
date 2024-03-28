# 15. 3Sum
# https://leetcode.com/problems/3sum/description/


from typing import List
from itertools import permutations


def check_sum(i,j,x,d):

    d[i] -= 1
    d[j] -= 1
    if x in d.keys():
        if d[x] > 0:
            return True
    return False


def threeSum(nums: List[int]) -> List[List[int]]:

    d = dict()
        
    for i in nums:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1

    pairs = set()
    if len(d.keys()) < 2:
        for i in permutations(nums, r=2):
            pairs.add(tuple(sorted(i)))
    else:
        for i in permutations(d.keys(), r=2):
            pairs.add(tuple(sorted(i)))


    triplets = set()
    for i,j in pairs:
        x = -1*(i+j)
        if tuple(sorted((i,j,x))) not in triplets:
            if check_sum(i,j,x, dict((k,v) for k,v in d.items() if k in [i,j,x])):
                t = tuple(sorted((i,j,x)))
                triplets.add(t)
    
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





