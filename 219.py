# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/description/


from typing import List
from collections import defaultdict


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], less_or_equal_k: int) -> bool:
        
        d = defaultdict(list) # key = items from nums, and value is list of indexes

        for i, k in enumerate(nums):
            d[k].append(i)

            if len(d[k]) > 1:
                if abs(d[k][-1] - d[k][-2]) <= less_or_equal_k:
                    return True

        return False



nums_1 = [1,2,3,1]
k_1 = 3
# Output: true

nums_2 = [1,0,1,1]
k_2 = 1
# Output: true

nums_3 = [1,2,3,1,2,3]
k_3 = 2
# Output: false     


nums_4 = [0,1,2,3,4,0,0,7,8,9,10,11,12,0]
k_4 = 1
# Output: true

print(Solution().containsNearbyDuplicate(nums_1, k_1))
print(Solution().containsNearbyDuplicate(nums_2, k_2))
print(Solution().containsNearbyDuplicate(nums_3, k_3))
print(Solution().containsNearbyDuplicate(nums_4, k_4))






