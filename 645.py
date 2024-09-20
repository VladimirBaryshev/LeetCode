# 645. Set Mismatch


from typing import List
from collections import defaultdict

class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        d = defaultdict(int)
        for i in range(len(nums)):
            d[i+1]

        for i, val in enumerate(nums):
            d[val] += 1

        doubled_val = None
        missing_val = None
        
        for k,v in d.items():
            if v == 0:
                missing_val = k
            if v == 2:
                doubled_val = k

        return doubled_val, missing_val
            



nums_1 = [1,2,2,4]
# Output: [2,3]

nums_2 = [1,1]
# Output: [1,2]

nums_3 = [3,2,3,4,6,5]
# [3,1]

nums_4 = [3,2,2]
# [2,1]

print(Solution().findErrorNums(nums_1))
print(Solution().findErrorNums(nums_2))
print(Solution().findErrorNums(nums_3))
print(Solution().findErrorNums(nums_4))