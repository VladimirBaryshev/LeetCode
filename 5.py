# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:

    def longestPalindrome(self, s: str) -> str:

        def is_two_shoulder_palindrome(s, left, right):

            count = 1
            p = s[left:right+1]
            while (left >= 0 and right < len(s)) and (s[left] == s[right]):
                if len(s[left:right+1]) > count:
                    count = len(s[left:right+1])
                    p = s[left:right+1]
                left -= 1
                right += 1

            return p

        def is_one_shoulder_palindrome(s, i):

            init_i = i
            p = s[i]

            while i+1 < len(s) and s[init_i] == s[i+1]:
                if len(s[init_i:i+2]) > len(p):
                    p = s[init_i:i+2]
                i += 1
            return p


            

        max_p = s[0]

        for i in range(1, len(s)-1):

            cur = is_two_shoulder_palindrome(s, i, i)
            if len(cur) > len(max_p):
                max_p = cur
            # print(i, 'is_two_shoulder_palindrome(s, i, i)', cur)    

        for i in range(0, len(s)):
            cur = is_one_shoulder_palindrome(s, i)
            if len(cur) > len(max_p):
                max_p = cur
            # print(i, 'is_one_shoulder_palindrome(s, i)', cur)
        return max_p




s_1 = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

s_2 = "cbbd"
# Output: "bb"

s_3 = "bb"
# Output: "bb"

s_4 = "ccc"
# Output: "ccc"

s_5 = "aaaa"
# Output: "aaaa"

s_6 = "tattarrattat"
# Output:"tattarrattat"

print(Solution().longestPalindrome(s_1))
print(Solution().longestPalindrome(s_2))
print(Solution().longestPalindrome(s_3))
print(Solution().longestPalindrome(s_4))
print(Solution().longestPalindrome(s_5))


print(Solution().longestPalindrome(s_6)) # TODO !!!!
