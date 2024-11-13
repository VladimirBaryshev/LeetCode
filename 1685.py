# 1685. Sum of Absolute Differences in a Sorted Array


from collections import defaultdict
from typing import List


class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix = [0 for i in range(n)]
        suffix = [0 for i in range(n)]

        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]

        suffix[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] + nums[i]

        result = []
        for i in range(n):
            # Calculate left and right sums efficiently using prefix and suffix sums
            left_sum = i * nums[i] - prefix[i]
            right_sum = suffix[i] - (n - i - 1) * nums[i]

            # Calculate the total sum of absolute differences
            result.append(left_sum + right_sum)

        return result

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