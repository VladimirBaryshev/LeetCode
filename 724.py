# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/description/


from typing import List


# solution ideas:
# sum(nums) # O(n)
# for i in nums # O(n)
# incremental_sum of left_side # O(n)

def find_pivot_index(nums: List[int]) -> int:
    
    pivot = -1
    total = sum(nums)
    left_sum = 0 

    for i,v in enumerate(nums):

        if left_sum == total - left_sum - v:
            pivot = i
            return pivot

        left_sum += v

    return pivot

print(find_pivot_index([1,7,3,6,5,6])) # 3
print(find_pivot_index([1,2,3])) # -1
