# 27. Remove Element
# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List


def removeElement(nums: List[int], val: int) -> int:
    
    r = len(nums)-1

    for l in range(len(nums)):
        if nums[l] == val:
            while (nums[r] == val) and (l < r):
                r -= 1

            to_swap_to_right = nums[r]
            to_swap_to_left = nums[l]
            nums[l] = to_swap_to_right
            nums[r] = to_swap_to_left
            
    count = 0
    for i in nums:
        if i != val:
            count += 1
    return count, nums



nums_1 = [3,2,2,3]
val_1 = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

nums_2 = [0,1,2,2,3,0,4,2]
val_2 = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores). 

print(removeElement(nums_1, val_1))
print(removeElement(nums_2, val_2))




