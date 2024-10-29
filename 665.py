# 665. Non-decreasing Array


from typing import List


class Solution:
    
    def checkPossibility(self, nums: List[int]) -> bool:
        
    def checkPossibility(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        res1 = 0
        temp = nums[:]
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                res1+=1
                nums[i+1] = nums[i]
                
        res2 = 0
        for i in range(len(temp)-1,0,-1):
            if temp[i-1]>temp[i]:
                res2+=1
                temp[i-1] = temp[i]

        return min(res1,res2) <= 1


nums_1 = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

nums_2 = [4,2,1]
# Output: false
# Explanation: You cannot get a non-decreasing array by modifying at most one element.

nums_3 = [3,4,2,3]
# Output: false

nums_4 = [5,7,1,8]
# Output: true

print(Solution().checkPossibility(nums_1))
print(Solution().checkPossibility(nums_2))
print(Solution().checkPossibility(nums_3))
print(Solution().checkPossibility(nums_4))

