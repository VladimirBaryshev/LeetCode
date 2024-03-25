from typing import List


def spiral(matrix: List[List[int]]) -> List[int]:

    res = []
    row_start, row_end = 0, len(matrix) - 1
    col_start, col_end = 0, len(matrix[0]) - 1
    
    while True:
        
        # UPPER ROW
        if row_start > row_end:
            break

        for i in range(col_start, col_end + 1):
            res.append(matrix[row_start][i])
        row_start += 1
        
        # if row_start > row_end:
        #     break
        
        # RIGHT COL
        if col_start > col_end:
            break
        for i in range(row_start, row_end + 1):
            res.append(matrix[i][col_end])
        col_end -= 1
        
        # if col_start > col_end:
        #     break
        
        # LOWER ROW
        if row_start > row_end:
            break
        for i in range(col_end, col_start - 1, -1):
            res.append(matrix[row_end][i])
        row_end -= 1

        # if row_start > row_end:
        #     break
        
        # LEFT COL
        if col_start > col_end:
            break
        for i in range(row_end, row_start - 1, -1):
            res.append(matrix[i][col_start])
        col_start += 1
        
        # if col_start > col_end:
        #     break
        
    return res  

print(spiral([[1,2,3],[4,5,6],[7,8,9]]))  
