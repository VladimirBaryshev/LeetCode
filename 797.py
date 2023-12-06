# https://leetcode.com/problems/all-paths-from-source-to-target/description/

'''
    Edges and constraints:
    len(graph) >= 1 where len(graph[i]) > 1
    len(graph[i]) >= 0 and len(graph[i]) < n
    each vertex is unique

    Solution ideas:
    Use stack as base data structure DFS where each elem is named as path
    put to stack [[0]]
    pop last elem (cur_path) from stack while it is not empty
    else:
    extend popped elem with each option from graph[cur_path[-1]] and put them to stack again
    if 
    popped stack[i] starts with 0 and ends with last vertex(n-1) put popped elem to result

'''


from typing import List


class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        result = []
        stack = [[0]]

        while stack:

            cur_path = stack.pop(0) # pop(0) = bfs

            if cur_path[0] == 0 and cur_path[-1] == len(graph)-1:
                result.append(cur_path)

            for i in graph[cur_path[-1]]:
                cur = cur_path[::] # cur_path.copy()
                cur.append(i)
                stack.append(cur)

        return result


graph_1 = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

graph_2 = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]


print(Solution().allPathsSourceTarget(graph_1))
print(Solution().allPathsSourceTarget(graph_2))


