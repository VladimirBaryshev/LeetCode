# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element

# Edge cases and constraints:
# len(nums) >= 1
# nums[i] != nums[i+1]
# nums belongs to + and - numbers

# Algo ideas:
# sliding window as O(n)
# quicksort nlog(n)
# binary search:
# case1 (base) compare mid with mid-1 < mid > mid+1, if it is a peak, return it
# case 2 (left side search)
# case 3 (right side search)

from typing import List

def findPeak(nums: List[int]) -> int:

    l = 0
    h = len(nums) - 1

    while( l < h ):

        mid = (l+h)//2

        print(f'l:{l} h:{h} mid:{mid}')

        if(nums[mid] < nums[mid+1]):
            l = mid+1
        else:
            h = mid

    return l

nums_1 = [1,2,3,1] #Output: 2
nums_2 = [1,2,1,3,5,6,4] #Output: 5

print(findPeak(nums_1))
print(findPeak(nums_2))