# 448. Find All Numbers Disappeared in an Array


from typing import List


class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        return list(set([i for i in range(1, len(nums)+1)]).difference(set(nums)))



nums_1 = [4,3,2,7,8,2,3,1]
# Output: [5,6]

nums_2 = [1,1]
# Output: [2]

print(Solution().findDisappearedNumbers(nums_1))
print(Solution().findDisappearedNumbers(nums_2))