# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/


from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    
    candidates.sort()


    result = []
    stack = [[0, [], 0]]

    while stack:

        idx, path, cur_target = stack.pop()

        if cur_target > target:
            pass

        elif cur_target == target:
            result.append(path)
            pass

        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            stack.append([i+1, path+[candidates[i]], cur_target+candidates[i]])


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

