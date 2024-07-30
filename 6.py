# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/description/



class Solution:

    def convert(self, s: str, numRows: int) -> str:

        s_count = 0
        row_count = 0
        col_count = 0

        total_coords = []
        while s_count < len(s):

            if row_count % 2 == 0:
                coords = []
                for i in range(0, numRows):
                    if s_count < len(s):
                        coords.append([i, col_count, s[s_count]])
                        s_count += 1
                col_count += 1
                total_coords.extend(coords)


            else:
                p = [i for i in range(1, numRows-1)]
                p.reverse()

                coords = []
                for i in p:
                    if s_count < len(s):
                        coords.append([i, col_count, s[s_count]])
                        col_count += 1
                        s_count += 1
                total_coords.extend(coords)
            row_count += 1

        matrix = [["" for j in range(col_count)] for i in range(numRows)]
        for col, row, val in total_coords:
            matrix[col][row] = val
        
        result = ""
        for i in matrix:
            result += "".join(i)

        return result


        



        

        

s_1 = "PAYPALISHIRING"
numRows_1 = 3
# Output: "PAHNAPLSIIGYIR"

s_2 = "PAYPALISHIRING"
numRows_2 = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

s_3 = "A"
numRows_3 = 1
# Output: "A"

s_4 = "ABCDE"
numRows_4 = 4

print(Solution().convert(s_1, numRows_1))
print(Solution().convert(s_2, numRows_2))
print(Solution().convert(s_3, numRows_3))
print(Solution().convert(s_4, numRows_4))




