# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/description/


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

    def firstBadVersion(self, n):   


        l = 0
        r = n

        while l <= r:
            mid = (l+r)//2

            if isBadVersion(mid) : # 1
                r = mid -1 
            else: # 0
                l = mid + 1
        
        return l




n_1 = 5
bad_1 = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

n_2 = 1
bad_2 = 1
# Output: 1


