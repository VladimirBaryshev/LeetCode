# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/


from typing import List
import heapq



def findKthLargest(nums: List[int], k: int) -> int:
    
    heapq.heapify(nums)
    return heapq.nlargest(k, nums)[-1]



nums_1 = [3,2,1,5,6,4]
k_1 = 2
# Output: 5

nums_2 = [3,2,3,1,2,4,5,5,6]
k_2 = 4
# Output: 4

print(findKthLargest(nums_1, k_1))
print(findKthLargest(nums_2, k_2))

