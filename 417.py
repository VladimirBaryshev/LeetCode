# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/


from collections import deque
from typing import List, Deque, Set, Tuple

def bfs(heights: List[List[int]], queue: Deque) -> Set:

    row_l = len(heights)
    col_l = len(heights[0])

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    
    seen = set()

    while queue:

        x, y = queue.popleft()

        seen.add((x,y))

        for dx, dy in directions:

            new_x = x + dx
            new_y = y + dy

            if (0 <= new_x < row_l) and (0 <= new_y < col_l) and (heights[new_x][new_y] >= heights[x][y]):

                if (new_x, new_y) not in seen:
                    queue.append((new_x, new_y))

    return seen




def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:

    r = len(heights)
    c = len(heights[0])

    p = deque() # pacific
    a = deque() # atlantic

    for i in range(r):
        p.append((i, 0))
        a.append((i, c - 1))
    
    for j in range(c):
        p.append((0, j))
        a.append((r - 1, j))

    to_pacific = bfs(heights, p)
    to_atlantic = bfs(heights, a)

    return list(to_pacific.intersection(to_atlantic))


# [1,2,3],
# [8,9,4],
# [7,6,5]
heights_0 = [[1,2,3],[8,9,4],[7,6,5]]
# [[0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]

heights_1 = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

heights_2 = [[1]]
# Output: [[0,0]]

print(pacificAtlantic(heights_0))
print(pacificAtlantic(heights_1))
print(pacificAtlantic(heights_2))




