# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/


from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:

        result = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    result[i] = max(result[i], 1+result[j])

        # return list(zip(nums, result))
        return max(result)


nums_1 = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

nums_2 = [0,1,0,3,2,3]
# Output: 4

nums_3 = [7,7,7,7,7,7,7]
# Output: 1

print(Solution().lengthOfLIS(nums_1))
print(Solution().lengthOfLIS(nums_2))
print(Solution().lengthOfLIS(nums_3))

