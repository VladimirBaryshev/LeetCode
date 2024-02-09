# 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/


from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
    
    points.sort(key=lambda x: x[0])
    
    result = []
    min_max = points[0]
    for s, e in points[1:]:

        if s > min_max[1]:
            result.append(min_max)
            min_max = [s,e]

        min_max = [max(min_max[0], s), min(min_max[1], e)]

    result.append(min_max)
    return result



points_1 = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

points_2 = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

points_3 = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

print(findMinArrowShots(points_1))
print(findMinArrowShots(points_2))
print(findMinArrowShots(points_3))
