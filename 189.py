# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/description/


from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """

        return nums[k:] + nums[:k]


nums_1 = [1,2,3,4,5,6,7]
k_1 = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

nums_2 = [-1,-100,3,99]
k_2 = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

nums_3 = [1,2,3,4]
k_3 = 0

print(Solution().rotate(nums_1, k_1))
print(Solution().rotate(nums_2, k_2))
print(Solution().rotate(nums_3, k_3))
