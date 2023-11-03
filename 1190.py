# 1190. Reverse Substrings Between Each Pair of Parentheses
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/



class Solution:

    def reverseParentheses(self, s: str) -> str:

        result_stack = []

        for char in s:

            # print(char)

            if char != ")":
                result_stack.append(char)
            else:
                substr = []
                while True:
                    cur_char = result_stack.pop()
                    if cur_char != '(':
                        substr.append(cur_char)
                    else:
                        result_stack.extend(substr)
                        break
        return ''.join(result_stack)





s_1 = "(abcd)"
# Output: "dcba"

s_2 = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.

s_3 = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.


print(Solution().reverseParentheses(s_1))
print(Solution().reverseParentheses(s_2))
print(Solution().reverseParentheses(s_3))

