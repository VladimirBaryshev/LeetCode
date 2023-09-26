# 78. Subsets
# https://leetcode.com/problems/subsets/


from typing import List
from itertools import combinations


def subsets(nums: List[int]) -> List[List[int]]:
    
    result = [()]
    for l in range(1, len(nums)+1):
        for combination in (combinations(nums, l)):
            result.append(combination)

    return result


nums_1 = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

nums_2 = [0]
# Output: [[],[0]]

print(subsets(nums_1))
print(subsets(nums_2))

