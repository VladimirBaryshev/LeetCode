# 2124. Check if All A's Appears Before All B's

class Solution:
    def checkString(self, s: str) -> bool:
        
        min_b_i = -1
        max_a_i = -1

        for i,v in enumerate(s[::]):
          if v == "a":
            max_a_i = i

        for i,v in enumerate(s[::]):
            if v == "b":
                min_b_i = i
                break

        if min_b_i == -1 or max_a_i == -1:
            return True #, min_b_i, max_a_i

        if min_b_i < max_a_i:
            return False #, min_b_i, max_a_i
        else:
            return True #, min_b_i, max_a_i




s_1 = "aaabbb"
# Output: true
# Explanation:
# The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
# Hence, every 'a' appears before every 'b' and we return true.

s_2 = "abab"
# Output: false
# Explanation:
# There is an 'a' at index 2 and a 'b' at index 1.
# Hence, not every 'a' appears before every 'b' and we return false.

s_3 = "bbb"
# Output: true
# Explanation:
# There are no 'a's, hence, every 'a' appears before every 'b' and we return true.

s_4 = 'a'
# Output: true

print(Solution().checkString(s_1))
print(Solution().checkString(s_2))
print(Solution().checkString(s_3))
print(Solution().checkString(s_4))
