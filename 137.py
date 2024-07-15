# 137. Single Number II
# https://leetcode.com/problems/single-number-ii/description/

from collections import defaultdict
from typing import List

class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        
        d = defaultdict(int)

        for i in nums:
            d[i] += 1

        return [k for k,v in d.items() if v == 1][0]





nums_1 = [2,2,3,2]
# Output: 3

nums_2 = [0,1,0,1,0,1,99]
# Output: 99


print(Solution().singleNumber(nums_1))
print(Solution().singleNumber(nums_2))

