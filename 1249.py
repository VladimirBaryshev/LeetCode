# 1249. Minimum Remove to Make Valid Parentheses

class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        
        s = list(s)
        stack = []

        for i,v in enumerate(s):
            if v == "(":
                stack.append(i)
            elif v == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        while stack:
            s[stack.pop()] = ""

        return "".join(s)







s_1 = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

s_2 = "a)b(c)d"
# Output: "ab(c)d"

s_3 = "))(("
# Output: ""
# Explanation: An empty string is also valid.       

print(Solution().minRemoveToMakeValid(s_1))
print(Solution().minRemoveToMakeValid(s_2))
print(Solution().minRemoveToMakeValid(s_3))
