# 118. Pascal's Triangle

from typing import List

class Solution:

    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        result = [[1], [1,1]]

        for i in range(2, numRows):
            new_row = [1]
            for j in range(1, len(result[-1])):
                new_row.append(result[-1][j-1] + result[-1][j])
            new_row.append(1)
            result.append(new_row)

        return result
            




numRows_1 = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

numRows_2 = 1
# Output: [[1]]

print(Solution().generate(numRows_1))
print(Solution().generate(numRows_2))
 
