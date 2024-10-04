# 560. Subarray Sum Equals K


from typing import List


class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        
        result = 0
        d = {0:1}
        prefix_sum = 0

        for i in nums:
            
            prefix_sum = prefix_sum + i

            if prefix_sum - k in d.keys():
                result = result + d[prefix_sum - k]

            if prefix_sum not in d.keys():
                d[prefix_sum] = 1
            else:
                d[prefix_sum] = d[prefix_sum] + 1

        return result





nums_1 = [1,1,1]
k_1 = 2
# Output: 2

nums_2 = [1,2,3]
k_2 = 3
# Output: 2     

nums_3 = [1,-1,0]
k_3 = 0
# Output: 3

print(Solution().subarraySum(nums_1, k_1))
print(Solution().subarraySum(nums_2, k_2))
print(Solution().subarraySum(nums_3, k_3))

