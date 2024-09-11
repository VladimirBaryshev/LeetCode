# 896. Monotonic Array


from typing import List


class Solution:

    def isMonotonic(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True

        ascends = 0
        descends = 0
        equals = 0

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                ascends += 1
            if nums[i-1] > nums[i]:
                descends += 1
            if nums[i-1] == nums[i]:
                equals += 1

        return len(nums)-1 == (abs(ascends - descends) + equals)



nums_1 = [1,2,2,3]
# Output: true

nums_2 = [6,5,4,4]
# Output: true

nums_3 = [1,3,2]
# Output: false     

nums_4 = [1]
# Output: true

nums_5 = [1,1,1,1,1,5]
# Output: true

nums_6 = [1,1,1,1,1,5,1]
# Output: false

print(Solution().isMonotonic(nums_1))
print(Solution().isMonotonic(nums_2))
print(Solution().isMonotonic(nums_3))
print(Solution().isMonotonic(nums_4))
print(Solution().isMonotonic(nums_5))
print(Solution().isMonotonic(nums_6))

