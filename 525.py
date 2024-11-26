# 525. Contiguous Array

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        hashmap = {0:-1}
        count = 0
        answer = 0

        for i,v in enumerate(nums):

            if v == 0:
                count -= 1
            else:
                count += 1

            if count in hashmap.keys():
                answer = max(answer, i - hashmap[count])
            else:
                hashmap[count] = i

        return answer






nums_1 = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

nums_2 = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

nums_3 = [0,0,1,0,0,0,1,1]
# Output: 6

nums_4 = [0, 1, 1, 0, 1, 1, 1, 0]
# Output: 4

# print(Solution().findMaxLength(nums_1))
# print(Solution().findMaxLength(nums_2))
# print(Solution().findMaxLength(nums_3))
print(Solution().findMaxLength(nums_4))

