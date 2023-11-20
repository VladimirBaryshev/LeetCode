# 1679. Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/


from typing import List
from collections import defaultdict


class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:

        counter = defaultdict(int)
        result = 0 

        for digit in nums:
            cur = k - digit
            if counter[cur] > 0: # if counter[cur] do not exist by calling if statement default dict will create counter[cur]=0
                counter[cur] -= 1
                result += 1
                print('if', digit, cur, counter)
            else:
                counter[digit] += 1
                print('else', digit, cur, counter)


        return result


nums_1 = [1,2,3,4]
k_1 = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

nums_2 = [3,1,3,4,3]
k_2 = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
 
nums_3 = [1,2,3,4, 1, 4]
k_1 = 5
# Output: 3


print(Solution().maxOperations(nums_1, k_1))
print(Solution().maxOperations(nums_2, k_2))
print(Solution().maxOperations(nums_3, k_3))


