# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/

class Solution:

    def numDecodings(self, s: str) -> int:

        dp = {len(s): 1}

        for i in range(len(s)-1, -1, -1):

            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]        

            if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                dp[i] += dp[i+2]

        # print(s, dp)
        return dp[0]




s_1 = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

s_2 = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

s_3 = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").


print(Solution().numDecodings(s_1))
print(Solution().numDecodings(s_2))
print(Solution().numDecodings(s_3))
