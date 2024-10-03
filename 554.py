# 554. Brick Wall


from typing import List


class Solution:

    def leastBricks(self, wall: List[List[int]]) -> int:
        
        edge_counts = dict()

        for row in wall:
            edge_pos = 0
            for brick_width in row[:-1]:
                edge_pos += brick_width
                edge_counts[edge_pos] = edge_counts.get(edge_pos, 0) + 1
                
        return len(wall) - max(edge_counts.values(), default=0)



wall_1 = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# Output: 2

wall_2 = [[1],[1],[1]]
# Output: 3

print(Solution().leastBricks(wall_1))
print(Solution().leastBricks(wall_2))

