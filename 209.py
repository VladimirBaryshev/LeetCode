# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/


target_1 = 7
nums_1 = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

target_2 = 4
nums_2 = [1,4,4]
# Output: 1

target_3 = 11
nums_3 = [1,1,1,1,1,1,1,1]
# Output: 0

def minSubArrayLen(target: int, nums: list[int]) -> int:

    min_lenght = 10**9
    l = 0
    total = 0

    for r in range(len(nums)):

        total += nums[r]

        while total >= target:
            min_lenght = min(r-l + 1, min_lenght)
            total -= nums[l]
            l += 1

    if min_lenght == 10**9:
        return 0
    return min_lenght

print(minSubArrayLen(target_1, nums_1))
print(minSubArrayLen(target_2, nums_2))
print(minSubArrayLen(target_3, nums_3))






