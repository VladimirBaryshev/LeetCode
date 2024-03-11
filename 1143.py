# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/description/


def longestCommonSubsequence(text1: str, text2: str) -> int:
    
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(len(text1)-1, -1, -1):
        for j in range(len(text2)-1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])
    # print(dp)
    return dp[0][0]

text1_1 = "abcde"
text2_1 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

text1_2 = "abc"
text2_2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

text1_3 = "abc"
text2_3 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0. 

text1 = "abcba"
text2 = "abcbcba"
# Output: 5

# print(longestCommonSubsequence(text1_1, text2_1))
# print(longestCommonSubsequence(text1_2, text2_2))
# print(longestCommonSubsequence(text1_3, text2_3))
print(longestCommonSubsequence(text1, text2))