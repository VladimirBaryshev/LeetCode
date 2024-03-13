# 97. Interleaving String
# https://leetcode.com/problems/interleaving-string/description/


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
    dp[len(s1)][len(s2)] = True


    for i in range(len(s1), -1, -1):
        for j in range(len(s2), -1, -1):
            if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                dp[i][j] = True
            if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                dp[i][j] = True

    return dp[0][0]



s1_1 = "aabcc"
s2_1 = "dbbca"
s3_1 = "aadbbcbcac"
# Output: true
# Explanation: One way to obtain s3 is:
# Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
# Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
# Since s3 can be obtained by interleaving s1 and s2, we return true.

s1_2 = "aabcc" 
s2_2 = "dbbca" 
s3_2 = "aadbbbaccc"
# Output: false
# Explanation: Notice how it is impossible to interleave s2 
# with any other string to obtain s3.

s1_3 = ""
s2_3 = ""
s3_3 = ""
# Output: true

s1 = "a"
s2 = ""
s3 = "a"

print(isInterleave(s1_1, s2_1, s3_1))
print(isInterleave(s1_2, s2_2, s3_2))
print(isInterleave(s1_3, s2_3, s3_3))
print(isInterleave(s1, s2, s3))


