# 2976. Minimum Cost to Convert String I

import heapq
from typing import List
from collections import defaultdict

class Solution:

    def dijkstra(self, adj, src):

        heap = [(0, src)]
        min_cost_map = {}

        while heap:

            cost, node = heapq.heappop(heap)

            if node in min_cost_map: 
                continue

            min_cost_map[node] = cost

            for nei, nei_cost in adj[node]:
                heapq.heappush(heap,(cost+nei_cost, nei))

        return min_cost_map

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        adj = defaultdict(list)

        for src, dst, cst in zip(original, changed, cost):
            adj[src].append((dst, cst))

        min_cost_maps = {c: self.dijkstra(adj, c) for c in set(source)}

        res = 0
        for src, dst in zip(source, target):
            if dst not in min_cost_maps[src]: 
                return -1
            res += min_cost_maps[src][dst]

        return res




source_1 = "abcd"
target_1 = "acbe"
original_1 = ["a","b","c","c","e","d"]
changed_1 =  ["b","c","b","e","b","e"]
cost_1 =     [ 2,  5,  5,  1,  2,  20]
# Output: 28
# Explanation: To convert the string "abcd" to string "acbe": "abcd" to string "acbe":
# - Change value at index 1 from 'b' to 'c' at a cost of 5.   "accd" to string "acbe":
# - Change value at index 2 from 'c' to 'e' at a cost of 1.   "aced" to string "acbe":
# - Change value at index 2 from 'e' to 'b' at a cost of 2.   "acbd" to string "acbe":
# - Change value at index 3 from 'd' to 'e' at a cost of 20.  "acbe" to string "acbe":
# The total cost incurred is 5 + 1 + 2 + 20 = 28.
# It can be shown that this is the minimum possible cost.

source_2 = "aaaa"
target_2 = "bbbb"
original_2 = ["a","c"]
changed_2 = ["c","b"]
cost_2 = [1,2]
# Output: 12
# Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, 
# followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. 
# To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.

source_3 = "abcd"
target_3 = "abce"
original_3 = ["a"]
changed_3 = ["e"]
cost_3 = [10000]
# Output: -1
# Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.

print(Solution().minimumCost(source_1, target_1, original_1, changed_1, cost_1))
print(Solution().minimumCost(source_2, target_2, original_2, changed_2, cost_2))
print(Solution().minimumCost(source_3, target_3, original_3, changed_3, cost_3))
 


