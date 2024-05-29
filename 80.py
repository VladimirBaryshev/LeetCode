# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description


from typing import List
from collections import defaultdict


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        
        d = defaultdict(int)
        to_be_popped = []

        for i,v in enumerate(nums):
            d[v] += 1
            if d[v] > 2:
                to_be_popped.append(i)

        while to_be_popped:
            i = to_be_popped.pop()
            nums.pop(i)

        return len(nums)



nums_1 = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, 
# with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

nums_2 = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, 
# with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

print(Solution().removeDuplicates(nums_1))
print(Solution().removeDuplicates(nums_2))



