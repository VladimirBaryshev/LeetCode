# 2966. Divide Array Into Arrays With Max Difference

from typing import List

class Solution:

    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        r = []
        for i in range(0, len(nums), 3):
            _slice = nums[i:i+3]
            if _slice[-1] - _slice[0] <= k:
                r.append(_slice)
            else:
                return []

        return r



nums_1 = [1,3,4,8,7,9,3,5,1]
k_1 = 2

# Output: [[1,1,3],[3,4,5],[7,8,9]]
# Explanation:
# The difference between any two elements in each array is less than or equal to 2.


nums_2 = [2,4,2,2,5,2]
k_2 = 2
# Output: []
# Explanation:
# Different ways to divide nums into 2 arrays of size 3 are:
# [[2,2,2],[2,4,5]] (and its permutations)
# [[2,2,4],[2,2,5]] (and its permutations)
# Because there are four 2s there will be an array with the elements 2 and 5 no matter how we divide it. 
# since 5 - 2 = 3 > k, the condition is not satisfied and so there is no valid division.

nums_3 = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11]
k_3 = 14

# Output: [[2,2,12],[4,8,5],[5,9,7],[7,8,5],[5,9,10],[11,12,2]]
# Explanation:
# The difference between any two elements in each array is less than or equal to 14.

print(Solution().divideArray(nums_1, k_1))
print(Solution().divideArray(nums_2, k_2))
print(Solution().divideArray(nums_3, k_3))
