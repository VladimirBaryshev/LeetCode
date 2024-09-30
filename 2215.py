# 2215. Find the Difference of Two Arrays


from typing import List


class Solution:

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
    	
    	return [list(set(nums1).difference(set(nums2))), list(set(nums2).difference(set(nums1)))]


nums1_1 = [1,2,3]
nums2_1 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. 
# Therefore, answer[0] = [1,3].

# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. 
# Therefore, answer[1] = [4,6].

nums1_2 = [1,2,3,3]
nums2_2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], 
# their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
 
print(Solution().findDifference(nums1_1, nums2_1))
print(Solution().findDifference(nums1_2, nums2_2))