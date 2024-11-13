# 1685. Sum of Absolute Differences in a Sorted Array


from collections import defaultdict
from typing import List


class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        d = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                r = abs(nums[i] - nums[j])
                d[i] += r
                d[j] += r

        return [d[k] for k in d.keys()]




nums_1 = [2,3,5]
# Output: [4,3,5]
# Explanation: Assuming the arrays are 0-indexed, then
# result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
# result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
# result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.

nums_2 = [1,4,6,8,10]
# Output: [24,15,13,15,21]

print(Solution().getSumAbsoluteDifferences(nums_1))
print(Solution().getSumAbsoluteDifferences(nums_2))
