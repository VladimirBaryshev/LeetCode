# 304. Range Sum Query 2D - Immutable

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.prefix = [[0]*(COLS+1) for _ in range(ROWS+1)]
        
        for row in range(ROWS):
            row_prefix = 0
            for col in range(COLS):
                row_prefix += matrix[row][col]
                col_prefix = self.prefix[row][col+1]
                self.prefix[row+1][col+1] = row_prefix + col_prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
print(numMatrix.sumRegion(2, 1, 4, 3)) # return 8 (i.e sum of the red rectangle)
print(numMatrix.sumRegion(1, 1, 2, 2)) # return 11 (i.e sum of the green rectangle)
print(numMatrix.sumRegion(1, 2, 2, 4)) # return 12 (i.e sum of the blue rectangle)