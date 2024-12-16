# 813. Largest Sum of Averages

from typing import List
from itertools import accumulate

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        s = list(accumulate(nums, initial=0))

        # @cache
        def dp(n,p):
            if p == 1: return s[n]/n
            return max((s[n]-s[j])/(n-j)+dp(j,p-1) for j in range(p-1,n))
            
        return dp(len(nums),k)


nums_1 = [9,1,2,3,9]
k_1 = 3
# Output: 20.00000
# Explanation: 
# The best choice is to partition nums into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
# We could have also partitioned nums into [9, 1], [2], [3, 9], for example.
# That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

nums_2 = [1,2,3,4,5,6,7]
k_2 = 4
# Output: 20.50000      

nums_3 = [4,1,7,5,6,2,3]
k_3 = 4
# 18.16667

# print(Solution().largestSumOfAverages(nums_1, k_1))
# print(Solution().largestSumOfAverages(nums_2, k_2))
print(Solution().largestSumOfAverages(nums_3, k_3))  