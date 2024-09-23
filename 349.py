# 349. Intersection of Two Arrays


from typing import List


class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        return set.intersection(set(nums1), set(nums2))


nums1_a = [1,2,2,1]
nums2_a = [2,2]
# Output: [2]

nums1_b = [4,9,5]
nums2_b = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.      
        
print(Solution().intersection(nums1_a, nums2_a))
print(Solution().intersection(nums1_b, nums2_b))




