# 2870. Minimum Number of Operations to Make Array Empty

from collections import defaultdict
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        d = defaultdict(int)
        for i in nums:
            d[i] += 1

        r = 0
        for _,v in d.items():
            if v == 1:
                return -1
            r += v//3
            if v%3:
                r += 1

        return r









nums_1 = [2,3,3,2,2,4,2,3,4]
# Output: 4
# Explanation: We can apply the following operations to make the array empty:
# - Apply the first operation on the elements at indices 0 and 3. The resulting array is nums = [3,3,2,4,2,3,4].
# - Apply the first operation on the elements at indices 2 and 4. The resulting array is nums = [3,3,4,3,4].
# - Apply the second operation on the elements at indices 0, 1, and 3. The resulting array is nums = [4,4].
# - Apply the first operation on the elements at indices 0 and 1. The resulting array is nums = [].
# It can be shown that we cannot make the array empty in less than 4 operations.

nums_2 = [2,1,2,2,3,3]
# Output: -1
# Explanation: It is impossible to empty the array.

print(Solution().minOperations(nums_1))
# print(Solution().minOperations(nums_2))
