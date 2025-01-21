# 2967. Minimum Cost to Make Array Equalindromic

import numpy as np
from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        median = int(np.median(nums))

        candidates = set() # unique candidates palindromic numbers for values of all indices. Maximum 3 values
        
        if str(median) == str(median)[-1::-1]:
            candidates.add(median)
        
        m = median # right side candidate from median
        while True:
            if str(m+1) == str(m+1)[-1::-1]:
                candidates.add(m+1)
                break
            else:
                m += 1

        m = median # left side candidate from median
        while True:
            if str(m-1) == str(m-1)[-1::-1]:
                candidates.add(m-1)
                break
            else:
                m -= 1

            
        d = dict()
        for i in candidates: # any unique candidate of palindromic numbers might be the best
            d[i] = 0
            for n in nums:
                d[i] += abs(n-i)

        return min([v for k,v in d.items()])




        

nums_1 = [1,2,3,4,5]
# Output: 6
# Explanation: We can make the array equalindromic by changing all elements to 3 which is a palindromic number. 
# The cost of changing the array to [3,3,3,3,3] using 4 special moves is given by |1 - 3| + |2 - 3| + |4 - 3| + |5 - 3| = 6.
# It can be shown that changing all elements to any palindromic number other than 3 cannot be achieved at a lower cost.

nums_2 = [10,12,13,14,15]
# Output: 11
# Explanation: We can make the array equalindromic by changing all elements to 11 which is a palindromic number. 
# The cost of changing the array to [11,11,11,11,11] using 5 special moves
#  is given by |10 - 11| + |12 - 11| + |13 - 11| + |14 - 11| + |15 - 11| = 11.
# It can be shown that changing all elements to any palindromic number other than 11 cannot be achieved at a lower cost.

nums_3 = [22,33,22,33,22]
# Output: 22
# Explanation: We can make the array equalindromic by changing all elements to 22 which is a palindromic number. 
# The cost of changing the array to [22,22,22,22,22] using 2 special moves is given by |33 - 22| + |33 - 22| = 22.
# It can be shown that changing all elements to any palindromic number other than 22 cannot be achieved at a lower cost.

print(Solution().minimumCost(nums_1))
print(Solution().minimumCost(nums_2))
print(Solution().minimumCost(nums_3))
