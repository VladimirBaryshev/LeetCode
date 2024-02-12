# 136. Single Number
# https://leetcode.com/problems/single-number/description/


from typing import List


def singleNumber(nums: List[int]) -> int:

    res = 0

    for n in nums:
        # print(res, n)
        res = res ^ n

    return res





nums_1 = [2,2,1]
# Output: 1

nums_2 = [4,1,2,1,2]
# Output: 4

nums_3 = [1]
# Output: 1

print(singleNumber(nums_1))
print(singleNumber(nums_2))
print(singleNumber(nums_3))



