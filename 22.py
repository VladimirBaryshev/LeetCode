# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/




class Solution:

    def generateParenthesis(self, n: int) -> list[str]:

        stack = []
        res = []

        def backtrack(opened, closed):
            
            if opened == closed == n:
                res.append("".join(stack))
                # print("\n opened == closed == n", res, '\n')

                return 

            if opened < n:

                # print("opened < n", stack)

                stack.append("(") 
                backtrack(opened+1, closed)
                stack.pop()

            if closed < opened:

                # print("closed < opened", stack)

                stack.append(")")
                backtrack(opened, closed+1)
                stack.pop()


        backtrack(0, 0)
        return res



algo = Solution()
print(algo.generateParenthesis(2)) # ["(())", "()()"]
print(algo.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(algo.generateParenthesis(1)) # ["()"]



