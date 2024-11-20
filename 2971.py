# 2971. Find Polygon With the Largest Perimeter


from typing import List


class Solution:

    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()

        s = sum(nums)

        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= (s-nums[i]):
                s -= nums[i]
                nums.pop(i)

        if len(nums) > 2:
            return s
        return -1



nums_1 = [5,5,5]
# Output: 15
# Explanation: The only possible polygon that can be made from nums has 3 sides: 5, 5, and 5. 
# The perimeter is 5 + 5 + 5 = 15.

nums_2 = [1,12,1,2,5,50,3]
# Output: 12
# Explanation: The polygon with the largest perimeter which can be made from nums has 5 sides: 1, 1, 2, 3, and 5. 
# The perimeter is 1 + 1 + 2 + 3 + 5 = 12.
# We cannot have a polygon with either 12 or 50 as the longest side because it is not possible to include 2 
# or more smaller sides that have a greater sum than either of them.
# It can be shown that the largest possible perimeter is 12.

nums_3 = [5,5,50]
# Output: -1
# Explanation: There is no possible way to form a polygon from nums, 
# as a polygon has at least 3 sides and 50 > 5 + 5.

print(Solution().largestPerimeter(nums_1))
print(Solution().largestPerimeter(nums_2))
print(Solution().largestPerimeter(nums_3))