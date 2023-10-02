# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/


from typing import List



def subsetWithDup(nums: List[int]) -> List[List[int]]:

    res = []
    nums.sort()
    stack = [[0, []]]

    while stack:

        i, subset = stack.pop()

        if i == len(nums):
            res.append(subset[::])

        elif i < len(nums):
            subset.append(nums[i])
            stack.append([i+1, subset[::]])
            subset.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            stack.append([i+1, subset[::]])
        else:
            pass


    return res



nums_1 = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

nums_2 = [0]
# Output: [[],[0]]

nums_3 = [1,1,2,2]
# Output: [[],[1],[1,1],[1,1,2],[1,1,2,2],[1,2],[1,2,2],[2],[2,2]]

nums_4 = [1,2,3]
# Output: [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]

nums_5 = [4,4,4,1,4]
# Output: [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]


print(subsetWithDup(nums_1), '\n')
print(subsetWithDup(nums_2), '\n')
print(subsetWithDup(nums_3), '\n')
print(subsetWithDup(nums_4), '\n')
print(subsetWithDup(nums_5), '\n')