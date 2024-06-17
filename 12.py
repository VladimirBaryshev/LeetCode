# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/description




class Solution:

    def intToRoman(self, num: int) -> str:
        
        nums = {
                "I" : 1,
                "IV" : 4,
                "V" : 5,
                "IX" : 9,
                "X" : 10,
                "XL" : 40,
                "L" : 50,
                "XC" : 90,
                "C" : 100,
                "CD" : 400,
                "D" : 500,
                "CM" : 900,
                "M" : 1000,
            }


        result = ""

        for k,v in reversed(nums.items()):
            
            while v <= num:
                result += k
                num -= v

        return result








num_1 = 3749

# Output: "MMMDCCXLIX"

# Explanation:

# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) 
# because the conversion is based on decimal places

num_2 = 58

# Output: "LVIII"

# Explanation:

# 50 = L
#  8 = VIII

num_3 = 1994

# Output: "MCMXCIV"

# Explanation:

# 1000 = M
#  900 = CM
#   90 = XC
#    4 = IV

print(Solution().intToRoman(num_1))
print(Solution().intToRoman(num_2))
print(Solution().intToRoman(num_3))




