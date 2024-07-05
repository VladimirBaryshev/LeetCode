# 728. Self Dividing Numbers
# https://leetcode.com/problems/self-dividing-numbers/description/

class Solution:

    def selfDividingNumbers(self, left, right):
        
        result = []
        for value in range(left, right+1):

            flag = 0

            for i in str(value):
                
                if (i == "0") or (value % int(i) != 0):
                    flag = 1

            if flag == 0:
                result.append(value)
        
        return result
        