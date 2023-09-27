# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/


from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:

    result = []

    stack = [[[], candidates, target]]

    while stack:

        op, candidates, t = stack.pop()

        if t == 0:
            result.append(op)

        for i in range(len(candidates)):
            if t - candidates[i] < 0:
                pass
            elif t - candidates[i] >= 0:
                stack.append([op + [candidates[i]], candidates[i:], t-candidates[i]])

    return result


candidates_0 = [2, 3]
target_0 = 6
# Output: [[2,2,2],[3,3]]

candidates_1 = [2,3,6,7]
target_1 = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.

candidates_2 = [2,3,5]
target_2 = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

candidates_3 = [2]
target_3 = 1
# Output: []


# FAILED CASE
candidates_4 = [7,3,2]
target_4 = 18
# Output: [[7,7,2,2],[7,3,3,3,2],[7,3,2,2,2,2],[3,3,3,3,3,3],[3,3,3,3,2,2,2],[3,3,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2]]

print(combinationSum(candidates_0, target_0), '\n')
print(combinationSum(candidates_1, target_1), '\n')
print(combinationSum(candidates_2, target_2), '\n')
print(combinationSum(candidates_3, target_3), '\n')
print(combinationSum(candidates_4, target_4), '\n')



