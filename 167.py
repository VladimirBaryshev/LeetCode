# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


numbers_1 = [2,7,11,15]
target_1 = 9
# Output: [1,2]

numbers_2 = [2,3,4]
target_2 = 6
# Output: [1,3]

numbers_3 = [-1,0]
target_3 = -1
# Output: [1,2]

 
def twoSum(numbers: list[int], target: int) -> list[int]:
    l = 0
    r = len(numbers)-1

    while l < r:

        curSum = numbers[l] + numbers[r]

        if curSum > target:
            r -= 1

        elif curSum < target:
            l += 1

        else:
            return [l + 1, r + 1]


print(twoSum(numbers_1, target_1)) # [1,2]
print(twoSum(numbers_2, target_2)) # [1,3]
print(twoSum(numbers_3, target_3)) # [1,2]

