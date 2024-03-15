# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/description/




def minDistance(word1: str, word2: str) -> int:
    
    dp = [[float('inf')]*(len(word2)+1) for i in range(len(word1)+1)]


    for j in range(len(word2)+1):
        dp[len(word1)][j] = len(word2)-j
    for i in range(len(word1)+1):
        dp[i][len(word2)] = len(word1)-i    


    for i in range(len(word1)-1,-1,-1):
        for j in range(len(word2)-1,-1,-1):

            if word1[i] == word2[j]:
                dp[i][j] = dp[i+1][j+1] 
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

    return dp[0][0]


word1_1 = "horse"
word2_1 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

word1_2 = "intention"
word2_2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

print(minDistance(word1_1, word2_1))
print(minDistance(word1_2, word2_2))
