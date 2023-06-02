# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/


nums_1 = [2,0,2,1,1,0] #[0,0,1,1,2,2]

nums_2 = [2,0,1] #[0,1,2]


def inplace_sorter(nums: list[int]) -> None:

    counts = [0,0,0]

    for i in nums:
        counts[i] += 1

    print(counts)

    i = 0

    if counts[0] > 0:
        while i < counts[0]:
            nums[i] = 0
            i += 1

    if counts[1] > 0:
        while i < counts[0]+counts[1]:
            nums[i] = 1
            i += 1

    if counts[2] > 0:
        while i < counts[0]+counts[1]+counts[2]:
            nums[i] = 2
            i += 1

print(nums_1)
inplace_sorter(nums_1)
print(nums_1)