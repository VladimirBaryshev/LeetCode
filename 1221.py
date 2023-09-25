# 1221. Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced-strings/description/


def balancedStringSplit(string: str) -> int:

    '''
        string should contains only L and R
    '''

    result_counter = 0
    balance = 0

    for char in string:

        if char == "L":
            balance += 1
        else:
            balance -= 1
            
        if balance == 0:
            result_counter += 1

    return result_counter




s_1 = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

s_2 = "RLRRRLLRLL"
# Output: 2
# Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
# Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.

s_3 = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".  


print(balancedStringSplit(s_1))
print(balancedStringSplit(s_2))
print(balancedStringSplit(s_3))


