# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/


s_1 = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

s_2 = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

s_3 = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

s_4 = "Today is a nice day"
# Output: 3


class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        
        s = [i for i in s.split(" ") if i != ""]
        

        return len(s[-1])


print(Solution().lengthOfLastWord(s_1))
print(Solution().lengthOfLastWord(s_2))
print(Solution().lengthOfLastWord(s_3))
print(Solution().lengthOfLastWord(s_4))


