# 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/description/


def checkValidString(s: str) -> bool:

    leftMin = 0
    leftMax = 0

    for c in s:

        if c == "(":
            leftMin += 1
            leftMax += 1
        elif c == ")":
            leftMin -= 1
            leftMax -= 1
        else:
            leftMin -= 1
            leftMax += 1
        if leftMax < 0:
            return False
        if leftMin < 0:
            leftMin = 0

    return leftMin == 0

# leftMin = 1
# leftMax = 2
# (*) (
# false

s_1 = "()"
# Output: true

s_2 = "(*)"
# Output: true

s_3 = "(*))"
# Output: true

s_4 = "(*)("
# Output: false



print(checkValidString(s_1))
print(checkValidString(s_2))
print(checkValidString(s_3))
print(checkValidString(s_4))




