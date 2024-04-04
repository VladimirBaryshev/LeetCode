# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:

    def romanToInt(self, s: str) -> int:

        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
            }

        if len(s) == 1:
            return roman[s] 

        r = 0

        for i in range(len(s)-1):
            
            if roman[s[i]] < roman[s[(i+1)]]:
                r -= roman[s[i]]
            else:
                r += roman[s[i]]

        return r + roman[s[(i+1)]]
            




s_1 = "III"
# Output: 3
# Explanation: III = 3.

s_2 = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

s_3 = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
s_4 = "D"

# print(Solution().romanToInt(s_1))
# print(Solution().romanToInt(s_2))
# print(Solution().romanToInt(s_3))
print(Solution().romanToInt(s_4))


