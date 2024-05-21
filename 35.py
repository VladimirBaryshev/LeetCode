# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/description/


from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        while left <= right:

            # mid = left + (right-left)//2
            mid = (left + right)//2


            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid+1

            else:
                right = mid-1

        return left

            




nums_1 = [1,3,5,6]
target_1 = 5
# Output: 2

nums_2 = [1,3,5,6]
target_2 = 2
# Output: 1

nums_3 = [1,3,5,6]
target_3 = 7
# Output: 4

nums_4 = [1]
target_4 = 4
# Output: 1

print(Solution().searchInsert(nums_1, target_1))
print(Solution().searchInsert(nums_2, target_2))
print(Solution().searchInsert(nums_3, target_3))
print(Solution().searchInsert(nums_4, target_4))

