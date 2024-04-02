# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        
        r = []
        s = set()
        cur = 0
        for i in range(len(nums)):
            if nums[i] in s:
                cur += 1
            else:
                r.append(nums[i])
                s.add(nums[i])

        for i in range(len(r)):
            nums[i] = r[i]
            
        return len(s)



nums_1 = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums 
# being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

nums_2 = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums 
# being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

print(Solution().removeDuplicates(nums_1))
print(Solution().removeDuplicates(nums_2))



