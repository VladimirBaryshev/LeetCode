# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/


from typing import List


class Solution:

    def canFinish(self, numCources: int, prereq: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(numCources)}

        for end_point, start_point in prereq:
            adj[end_point].append(start_point)

        visited = set()


        def dfs(end_point):
            
            if end_point in visited:
                return False

            if adj[end_point] == []:
                return True

            visited.add(end_point)

            for start_point in adj[end_point]:
                if dfs(start_point) == False:
                    return False

            visited.remove(end_point)
            adj[end_point] = []
            return True


        for end_point in range(numCources):
            if dfs(end_point) == False:
                return False
        return True



numCourses_1 = 2
prerequisites_1 = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. 
# So it is possible.

numCourses_2 = 2
prerequisites_2 = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, 
# and to take course 0 you should also have finished course 1. 
# So it is impossible.      

numCourses_3 = 5
prerequisites_3 = [[1,4],[2,4],[3,1],[3,2]]
# Output: true


numCourses_4 = 3
prerequisites_4 = [[2,1],[1,0]]
# Output: true

numCourses_5 = 1
prerequisites_5 = []
# Output: true


numCourses_6 = 20
prerequisites_6 = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
# Output: false


print(Solution().canFinish(numCourses_1, prerequisites_1))
print(Solution().canFinish(numCourses_2, prerequisites_2))
print(Solution().canFinish(numCourses_3, prerequisites_3))
print(Solution().canFinish(numCourses_4, prerequisites_4))
print(Solution().canFinish(numCourses_5, prerequisites_5))
print(Solution().canFinish(numCourses_6, prerequisites_6))



