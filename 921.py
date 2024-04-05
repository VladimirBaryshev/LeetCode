# 921. Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/


class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []

        for i in s:

            if i == "(":
                
                stack.append(i)

            else:

                if len(stack) > 0 and stack[-1] == "(": # true/false
                    stack.pop() # stack[-1] = “(“ and i = “)”

                else:
                    stack.append(i) # stack[-1] = “(“ and i = “)”

        return len(stack)




s_1 = "())"
# Output: 1

s_2 = "((("
# Output: 3

print(Solution().minAddToMakeValid(s_1))
print(Solution().minAddToMakeValid(s_2))