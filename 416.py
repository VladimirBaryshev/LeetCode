# 416. Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/


from typing import List


class Solution:

    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 > 0:
            return False

        target = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1 ,-1):

            next_dp = set()

            for t in dp:

                next_dp.add(nums[i]+t)
                next_dp.add(t)

                if nums[i]+t == target:
                    return True

            dp = next_dp

        # print(target, dp)
        return False



nums_1 = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

nums_2 = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

nums_3 = [1,1]
# Output: true

nums_4 = [1,2,5]
# Output: false

print(Solution().canPartition(nums_1))
print(Solution().canPartition(nums_2))
print(Solution().canPartition(nums_3))
print(Solution().canPartition(nums_4))







