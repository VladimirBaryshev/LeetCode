# 912. Sort an Array


from typing import List


class Solution:

    # QuickSort
    def sortArrayQS(self, nums: List[int]) -> List[int]:
        
        if len(nums) <= 1:
            return nums

        return self.sortArray([i for i in nums[1:] if i < nums[0]]) + [nums[0]] + self.sortArray([i for i in nums[1:] if i >= nums[0]])


    # Selection Sort
    def sortArraySS(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        return [nums.pop(min(range(lenght-i), key=lambda x: nums[x])) for i in range(lenght)]

nums_1 = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), 
# while the positions of other numbers are changed (for example, 1 and 5).

nums_2 = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
 

print(Solution().sortArraySS(nums_1))
print(Solution().sortArraySS(nums_2))


