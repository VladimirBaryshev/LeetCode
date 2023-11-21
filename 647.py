# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/


class Solution:

    def countSubstrings(self, s: str) -> int:

        def is_palindrome(s, left, right):

            count = 1
            p = [[left, s[left]]]
            while (left >= 0 and right < len(s)) and (s[left] == s[right]):
                if len(s[left:right+1]) > count:
                    count = len(s[left:right+1])
                    p.append([left,right+1, s[left:right+1]])
                left -= 1
                right += 1

            return p

        palindroms = []

        for i in range(0, len(s)):

            cur = is_palindrome(s, i, i)

            palindroms.extend(cur)

            cur = is_palindrome(s, i, i+1)

            palindroms.extend(cur)

        return len({tuple(x) for x in palindroms})

        




s_1 = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

s_2 = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".



print(Solution().countSubstrings(s_1))
print(Solution().countSubstrings(s_2))


