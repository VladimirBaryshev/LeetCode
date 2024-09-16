# 1422. Maximum Score After Splitting a String


class Solution:

    def maxScore(self, s: str) -> int:

        count_zeros = 0
        count_ones = s.count("1")
        max_score = 0

        for i in range(len(s)-1):

            if s[i] == "1":
                count_ones -= 1
            if s[i] == "0":
                count_zeros += 1
            max_score = max(max_score, count_zeros+count_ones)

        return max_score





s_1 = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3

s_2 = "00111"
# Output: 5
# Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

s_3 = "1111"
# Output: 3

s_4 = "11100"
# Output: 2

s_5 = "00"
# Output: 1

print(Solution().maxScore(s_1))
print(Solution().maxScore(s_2))
print(Solution().maxScore(s_3))
print(Solution().maxScore(s_4))
print(Solution().maxScore(s_5))

