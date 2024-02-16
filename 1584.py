# 1584. Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/

import heapq
from typing import List


def minCostConnectPoints(points: List[List[int]]) -> int:
    
    N = len(points)

    adj = {i : [] for i in range(N)}

    for i in range(0, N):

        x1, y1 = points[i]

        for j in range(i+1, N):

            x2, y2 = points[j]

            dist = abs(x1-x2) + abs(y1 - y2)

            adj[i].append([dist, j])
            adj[j].append([dist, i])

    res = 0

    visited = set()

    minH = [[0,0]]

    while len(visited) < N:

        cost, i = heapq.heappop(minH)

        if i in visited:
            continue
        
        visited.add(i)
        res += cost

        for neigh_cost, neigh in adj[i]:
            if neigh not in visited:
                heapq.heappush(minH, [neigh_cost, neigh])

    return res







points_1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20

points_2 = [[3,12],[-2,5],[-4,1]]
# Output: 18

print(minCostConnectPoints(points_1))
print(minCostConnectPoints(points_2))

