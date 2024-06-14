# 201. Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/



class Solution:

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        # for i in range(left, right+1):
        #   print(i, "{0:b}".format(i))
        bitc=0

        while left!=right:
            #check from last bit of each
            #As they not equal means current checked last bit 0 in answer
            print("{0:b}".format(left), "{0:b}".format(right), bitc)
            left = left >>1
            print("{0:b}".format(left), "{0:b}".format(right), bitc)
            right = right >>1
            print("{0:b}".format(left), "{0:b}".format(right), bitc)
            bitc+=1
            print("{0:b}".format(left), "{0:b}".format(right), bitc)

            print('')

        return "{0:b}".format(right<<bitc), right<<bitc
        # return right<<bitc



left_1 = 5
right_1 = 7
# Output: 4

left_2 = 0
right_2 = 0
# Output: 0

left_3 = 1
right_3 = 2147483647
# Output: 0


print(Solution().rangeBitwiseAnd(left_1, right_1))
print(Solution().rangeBitwiseAnd(left_2, right_2))
print(Solution().rangeBitwiseAnd(left_3, right_3))




