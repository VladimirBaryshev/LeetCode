# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

tokens_1 = ["2","1","+","3","*"] # 9

tokens_2 = ["4","13","5","/","+"] # 6

tokens_3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] # 22


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = []

        for i in tokens:

            if i == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)

            elif i == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            elif i == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)

            elif i == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))

            else:
                stack.append(int(i))

        return stack[0]


s = Solution()
print(s.evalRPN(tokens_1))
print(s.evalRPN(tokens_2))
print(s.evalRPN(tokens_3))


