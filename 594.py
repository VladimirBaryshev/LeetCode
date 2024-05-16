# 594. Longest Harmonious Subsequence
# https://leetcode.com/problems/longest-harmonious-subsequence/description/


from collections import defaultdict
from typing import List

 
class Solution:
 
    def findLHS(self, nums: List[int]):

        d = defaultdict(int)
        for i in nums:
            d[i] += 1

        max_len = 0
        for k,v in d.items():
            if k+1 in d.keys():
                max_len = max(v + d[k+1], max_len)

        return max_len



nums_1 = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

nums_2 = [1,2,3,4]
# Output: 2

nums_3 = [1,1,1,1]
# Output: 0

print(Solution().findLHS(nums_1))
print(Solution().findLHS(nums_2))
print(Solution().findLHS(nums_3))

