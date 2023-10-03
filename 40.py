# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/


from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    
    candidates.sort()

    result = []

    def backtrack(idx, path, cur_target):

        if cur_target > target:
            return 

        elif cur_target == target:
            result.append(path)
            return

        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            backtrack(i+1, path+[candidates[i]], cur_target+candidates[i])

    backtrack(0, [], 0)
    return result


candidates_1 = [10,1,2,7,6,1,5]
target_1 = 8
# Output: 
# [
    # [1,1,6],
    # [1,2,5],
    # [1,7],
    # [2,6]
# ]

candidates_2 = [2,5,2,1,2]
target_2 = 5
# Output: 
# [
    # [1,2,2],
    # [5]
# ]

candidates_3 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target_3 = 27

print(combinationSum2(candidates_1, target_1))
print(combinationSum2(candidates_2, target_2))
print(combinationSum2(candidates_3, target_3))

