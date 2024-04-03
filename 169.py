# 169. Majority Element
# https://leetcode.com/problems/majority-element/


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        d = dict()
        max_elem = -1
        max_elem_count = -1

        for k in nums:
            if k in d.keys():
                d[k] += 1
            else:
                d[k] = 1

            max_elem_count = max(max_elem_count, d[k])
            if max_elem_count == d[k]:
                max_elem = k 

        return max_elem




nums_1 = [3,2,3]
# Output: 3

nums_2 = [2,2,1,1,1,2,2]
# Output: 2

print(Solution().majorityElement(nums_1))
print(Solution().majorityElement(nums_2))