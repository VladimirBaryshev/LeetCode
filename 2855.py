# 2855. Minimum Right Shifts to Sort the Array

from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        
        count = 0
        max_val = max(nums)
        sorted_nums = sorted(nums)

        slice_ = []
        while nums[-1] != max_val:
            s = nums.pop()
            slice_.append(s)
            count += 1

        slice_.reverse()
        nums = slice_ + nums

        if nums != sorted_nums:
            return -1
        return count





nums_1 = [3,4,5,1,2]
# Output: 2
# Explanation: 
# After the first right shift, nums = [2,3,4,5,1].
# After the second right shift, nums = [1,2,3,4,5].
# Now nums is sorted; therefore the answer is 2.

nums_2 = [1,3,5]
# Output: 0
# Explanation: nums is already sorted therefore, the answer is 0.

nums_3 = [2,1,4]
# Output: -1
# Explanation: It's impossible to sort the array using right shifts.


print(Solution().minimumRightShifts(nums_1))
print(Solution().minimumRightShifts(nums_2))
print(Solution().minimumRightShifts(nums_3))
         