# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/description/


class Solution:

    def mySqrt(self, x: int) -> int:
        
        low = 0
        high = x
        ans = 1

        while low <= high:              
            mid = (low+high)//2
            if mid*mid <= x:
                ans = mid
                low = mid+1
            else:
                high = mid-1

        return ans



x_1 = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

x_2 = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., 
# and since we round it down to the nearest integer, 2 is returned.


print(Solution().mySqrt(x_1))
print(Solution().mySqrt(x_2))