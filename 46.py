# 46. Permutations
# https://leetcode.com/problems/permutations/


from typing import List
import itertools


def permute(nums: List[int]) -> List[int]:
    
    # return list(itertools.permutations(nums))

    nums_l = len(nums)
    result = []
    stack = [[[], nums]]

    while stack:

        perm, nums = stack.pop()

        for i in range(len(nums)):

            if nums[i] not in perm:

                stack.append([perm+[nums[i]], nums])

            if stack and len(stack[-1][0]) == nums_l and stack[-1][0] not in result:
                temp_perm, _ = stack.pop()
                result.append(temp_perm)

    return result


nums_1 = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

nums_2 = [0,1]
# Output: [[0,1],[1,0]]

nums_3 = [1]
# Output: [[1]]

print(permute(nums_1), '\n')
print(permute(nums_2), '\n')
print(permute(nums_3), '\n')



