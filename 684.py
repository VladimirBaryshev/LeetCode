# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/

from typing import List
import collections

class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        graph_so_far = collections.defaultdict(lambda: [])

        def is_connected(u, v):
            
            if u == v:
                return True

            visited.add(u)

            for neighbor in graph_so_far[u]:
                if not neighbor in visited:
                    if is_connected(neighbor, v):
                        return True
            return False


        for u,v in edges:

            visited = set()

            if is_connected(u,v):
                return [u,v]
            else:
                graph_so_far[u].append(v)
                graph_so_far[v].append(u)




edges_1 = [[1,2],[1,3],[2,3]]
# Output: [2,3]

edges_2 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]

edges_3 = [[1,3],[3,4],[1,5],[3,5],[2,3]]
# Output: [3,5]


edges_4 = [[3,4],[1,2],[2,4],[3,5],[2,5]]
# Output: [2,5]

print(Solution().findRedundantConnection(edges_1))
print(Solution().findRedundantConnection(edges_2))
print(Solution().findRedundantConnection(edges_3))
print(Solution().findRedundantConnection(edges_4 ))

