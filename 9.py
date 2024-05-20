# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/


class Solution:

    def isPalindrome(self, x: int) -> bool:

        x = [i for i in str(x)]

        while len(x) >= 2:
            if x.pop(0) != x.pop():
                return False

        return True



x_1 = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

x_2 = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

x_3 = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


print(Solution().isPalindrome(x_1))
print(Solution().isPalindrome(x_2))
print(Solution().isPalindrome(x_3))
