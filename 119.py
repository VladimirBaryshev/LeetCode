# 119. Pascal's Triangle II

from typing import List

class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
        
        # triangle = [[1], [1,1]]

        # if rowIndex <= 1:
        #     return triangle[rowIndex]

        # for j in range(2, rowIndex+1):

        #     row = [1]

        #     for i in range(1,len(triangle[-1])):
        #         row.append(triangle[-1][i-1] + triangle[-1][i])

        #     row.append(1)
        #     triangle.append(row)

        # return triangle[rowIndex]

        triangle = [1]
        while len(triangle) <= rowIndex:
            triangle = [sum(i) for i in zip([0]+triangle, triangle+[0])]

        return triangle



rowIndex_1 = 3
# Output: [1,3,3,1]

rowIndex_2 = 0
# Output: [1]

rowIndex_3 = 1
# Output: [1,1]

print(Solution().getRow(rowIndex_1))
print(Solution().getRow(rowIndex_2))
print(Solution().getRow(rowIndex_3))