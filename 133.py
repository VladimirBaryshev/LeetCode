# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/


from collections import deque
from typing import Optional, List



# Definition for a Node.
class Node:

    def __init__(self, val=0, neighbors=None):

        self.val = val
        self.neighbors = neighbors # if neighbors is not None else []



class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return node

        queue = deque([node])
        clones = {node.val: Node(node.val, [])}

        while queue:

            cur = queue.popleft()
            cur_clone = clones[cur.val]

            for neighbor in cur.neighbors:
                if neighbor.val not in clones.keys():
                    clones[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                cur_clone.neighbors.append(clones[neighbor.val])

        return clones[node.val]



# adjList_1 = [[2,4],[1,3],[2,4],[1,3]]
adjList_1 = Node(1, [
                        Node(2, [
                                    Node(1, []), 
                                    Node(3, [])
                                ]
                            ), 
                        Node(4, [
                                    Node(1, []), 
                                    Node(3, [])
                                ]
                            )
                        ]
                )

# Output: [[2,4],[1,3],[2,4],[1,3]]

        #               1, [2,4]
        # 2, [1,3]                      4, [1,3]
        #       3, [2,4]

# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# adjList_2 = [[]]
adjList_2 = Node(1, [])
# Output: [[]]
# Explanation: Note that the input contains one empty list. 
# The graph consists of only one node with val = 1 and it does not have any neighbors.

# adjList_3 = []
adjList_3 = None
# Output: []
# Explanation: This an empty graph, it does not have any nodes.


print(Solution().cloneGraph(adjList_1))
print(Solution().cloneGraph(adjList_2))
print(Solution().cloneGraph(adjList_3))

