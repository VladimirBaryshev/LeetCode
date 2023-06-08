# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

nums_1 = [4,5,6,7,0,1,2]
target_1 = 0
# Output: 4

nums_2 = [4,5,6,7,0,1,2]
target_2 = 3
# Output: -1

nums_3 = [1]
target_3 = 0
# Output: -1

nums_4 =[4,5,6,7,8,1,2,3]
target_4 = 8
# Output: 4


def search(nums: list[int], target: int) -> int:

    l = 0
    r = len(nums) - 1

    while l <= r:

        mid = (l + r) // 2

        if target == nums[mid]:
            return mid

        # Left sided
        if nums[l]<= nums[mid]:

            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1 

        # Right sided
        else:

            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1


print(search(nums_1, target_1))
print(search(nums_2, target_2))
print(search(nums_3, target_3))
print(search(nums_4, target_4))




