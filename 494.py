# 494. Target Sum
# https://leetcode.com/problems/target-sum/description/


from typing import List


def findTargetSumWays(nums: List[int], target: int) -> int:
        
    cache = dict()

    def backtrack(i, total):

        if i == len(nums):
            if total == target:
                return 1
            else:
                return 0

        if (i, total) in cache:
            return cache[(i, total)]

        cache[(i, total)] = backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i])

        return cache[(i, total)]

    return backtrack(0, 0)



nums_1 = [1,1,1,1,1]
target_1 = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

nums_2 = [1]
target_2 = 1
# Output: 1

print(findTargetSumWays(nums_1, target_1))
print(findTargetSumWays(nums_2, target_2))