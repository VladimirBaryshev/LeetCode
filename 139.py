# 139. Word Break
# https://leetcode.com/problems/word-break/


from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (len(w)+i) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i] == True:
                    break
        return dp[0]





s_1 = "leetcode"
wordDict_1 = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

s_2 = "applepenapple"
wordDict_2 = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

s_3 = "catsandog"
wordDict_3 = ["cats","dog","sand","and","cat"]
# Output: false     

print(Solution().wordBreak(s_1, wordDict_1))
print(Solution().wordBreak(s_2, wordDict_2))
print(Solution().wordBreak(s_3, wordDict_3))




