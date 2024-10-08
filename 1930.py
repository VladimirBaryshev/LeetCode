# 1930. Unique Length-3 Palindromic Subsequences


class Solution:

    def countPalindromicSubsequence(self, s: str) -> int:
        
        result = 0
        uniq_vals = set(s)

        for u in uniq_vals:

            start, end = s.find(u), s.rfind(u)
            result += len(set(s[start+1:end]))

        return result



s_1 = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")

s_2 = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".

s_3 = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")        

print(Solution().countPalindromicSubsequence(s_1))
print(Solution().countPalindromicSubsequence(s_2))
print(Solution().countPalindromicSubsequence(s_3))
