# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/


def isSubsequence(s: str, t: str) -> bool:

    i, j = 0, 0

    while i < len(s) and j < len(t):

        if s[i] == t[j]:
            i += 1
        j += 1

    return len(s) == i


s_1 = "abc"
t_1 = "ahbgdc"
# Output: true

s_2 = "axc"
t_2 = "ahbgdc"
# Output: false

s_3 = "acb"
t_3 = "ahbgdc"
# Output: false

s_4 = "ab"
t_4 = "baab"
# Output: true

        # i, j = 0, 0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        # return i == len(s)

        # a != b --> i = 0 and j = 1
        # a = b --> i = 1 and j = 1
        # a != b --> i = 1 and j = 2
        # a != b --> i = 1 and j = 3
        # a == b --> i = 2 and j = 3

print(isSubsequence(s_1, t_1))
print(isSubsequence(s_2, t_2))
print(isSubsequence(s_3, t_3))
print(isSubsequence(s_4, t_4))




