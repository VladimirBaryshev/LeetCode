# 442. Find All Duplicates in an Array

from collections import defaultdict
from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        c = defaultdict(int)

        for i in nums:
            c[i] += 1

        return [k for k,v in c.items() if v > 1]


nums_1 = [4,3,2,7,8,2,3,1]
# Output: [2,3]

nums_2 = [1,1,2]
# Output: [1]

nums_3 = [1]
# Output: []

print(Solution().findDuplicates(nums_1))
print(Solution().findDuplicates(nums_2))
print(Solution().findDuplicates(nums_3))
