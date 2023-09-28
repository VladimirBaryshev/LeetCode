# 46. Permutations
# https://leetcode.com/problems/permutations/


from typing import List
import itertools


def permute(nums: List[int]) -> List[int]:
	
	return list(itertools.permutations(nums))



nums_1 = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

nums_2 = [0,1]
# Output: [[0,1],[1,0]]

nums_3 = [1]
# Output: [[1]]

print(permute(nums_1))
print(permute(nums_2))
print(permute(nums_3))



