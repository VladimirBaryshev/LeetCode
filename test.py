from typing import List


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        l = m-1
        r = n-1
        cursor = m+n-1

        while r >= 0:
            if (l >= 0) and (nums1[l] > nums2[r]):
                nums1[cursor] = nums1[l]
                l -= 1
            else:
                nums1[cursor] = nums2[r]
                r -= 1
            cursor -= 1

        return nums1








        




t1 = {
    "nums1" : [1,2,3,0,0,0], 
    "m": 3, 
    "nums2" : [2,5,6], 
    "n" : 3    
}

# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.


t2 = {
    "nums1" : [1], 
    "m" : 1, 
    "nums2" : [], 
    "n" : 0    
}
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

t3 = {
    "nums1" : [0], 
    "m" : 0, 
    "nums2" : [1], 
    "n" : 1    
}
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
#         


t4 = {
    "nums1" : [4,5,6,0,0,0],
    "m" : 3,
    "nums2" : [1,2,3],
    "n" : 3
}

# [1,2,3,4,5,6]

print(Solution().merge(**t1))
print(Solution().merge(**t2))
print(Solution().merge(**t3))
print(Solution().merge(**t4))
