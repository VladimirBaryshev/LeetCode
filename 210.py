# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

from typing import List

class Solution:

    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:

        end_points = {i:[] for i in range(numCourses)}

        for end_point, start_point in prereq:
            end_points[end_point].append(start_point)

        visited = set()
        cycle = set()
        output = []

        def dfs(end_point):
            
            if end_point in cycle:
                return False

            if end_point in visited:
                return True

            cycle.add(end_point)
            for s in end_points[end_point]:
                if dfs(s) == False:
                    return False

            cycle.remove(end_point)
            visited.add(end_point)
            output.append(end_point)
            return True


        for e in range(numCourses):
            if dfs(e) == False:
                return []
        
        return output






numCourses_1 = 2
prerequisites_1 = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So the correct course order is [0,1].

numCourses_2 = 4
prerequisites_2 = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. 
# To take course 3 you should have finished both courses 1 and 2. 
# Both courses 1 and 2 should be taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

numCourses_3 = 1
prerequisites_3 = []
# Output: [0


print(Solution().findOrder(numCourses_1, prerequisites_1))
print(Solution().findOrder(numCourses_2, prerequisites_2))
print(Solution().findOrder(numCourses_3, prerequisites_3))


