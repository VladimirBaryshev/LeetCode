# 229. Majority Element II


from collections import defaultdict
from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:
        
        d = defaultdict(int)

        for i in nums:
            d[i] += 1

        l = len(nums)/3
        return [k for k in d.keys() if d[k] > l]


nums_1 = [3,2,3]
# Output: [3]

nums_2 = [1]
# Output: [1]

nums_3 = [1,2]
# Output: [1,2]

print(Solution().majorityElement(nums_1))
print(Solution().majorityElement(nums_2))
print(Solution().majorityElement(nums_3))
