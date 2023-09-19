# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List
import heapq
from math import sqrt

# return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance 
# (i.e., √(x1 - x2)2 + (y1 - y2)2).

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    
    x2, y2 = 0, 0

    distances = dict()

    for point in points:

        x1, y1 = point

        distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)

        if distance in distances:
            distances[distance].append(point)
        else:
            distances[distance] = [point]

    d = list(distances.keys())
    heapq.heapify(d)
    
    result = []

    while len(result) != k:
        result.extend(distances[heapq.heappop(d)])

    return result




points_1 = [[1,3],[-2,2]]
k_1 = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

points_2 = [[3,3],[5,-1],[-2,4]]
k_2 = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.

points_3 = [[0,1],[1,0]]
k_3 = 2

points_4 = [[1,3],[-2,2],[2,-2]]
k_4 = 2
# Output: [[-2,2],[2,-2]]

print(kClosest(points_1, k_1))
print(kClosest(points_2, k_2))
print(kClosest(points_3, k_3))
print(kClosest(points_4, k_4))


