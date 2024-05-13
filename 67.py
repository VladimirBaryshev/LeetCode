# 67. Add Binary
# https://leetcode.com/problems/add-binary/description/


class Solution:

    def addBinary(self, a: str, b: str) -> str:
        
        max_l = max(len(a), len(b))

        while len(a) != max_l:
            a = "0" + a

        while len(b) != max_l:
            b = "0" + b


        r = ""
        prev = 0
        for i,j in tuple(zip(a,b))[::-1]:

            cur = prev
            cur += int(i)
            cur += int(j)
            prev = cur // 2
            cur = cur % 2
            r = str(cur) + r

        if prev > 0:
            return str(prev) + r
        return r





a_1 = "11"
b_1 = "1"
# Output: "100"

a_2 = "1010"
b_2 = "1011"
# Output: "10101"

a_3 = "1111"
b_3 = "1111"
# Output: "11110"

print(Solution().addBinary(a_1, b_1))
print(Solution().addBinary(a_2, b_2))
print(Solution().addBinary(a_3, b_3))






