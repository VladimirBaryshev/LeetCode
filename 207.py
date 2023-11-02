# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/


from typing import List


class Solution:

	def __init__(self):

		self.numCources = None
		self.prereq = None


	def define_if_graph_cycled(self):

		start_points = dict()
		end_points = dict()

		for e, s in self.prereq:
			if e not in end_points.keys():
				end_points[e] = False
			if s not in start_points.keys():
				start_points[s] = False		


		for end_point, start_point in self.prereq:
			start_points[start_point] = True
			end_points[end_point] = True

		print('visited:', end_points, 'recStack:', start_points)


	def canFinish(self, numCources: int, prereq: List[List[int]]) -> bool:

		self.numCources = numCources
		self.prereq = prereq

		self.define_if_graph_cycled()



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

# print(Solution().canFinish(numCourses_1, prerequisites_1))
print(Solution().canFinish(numCourses_2, prerequisites_2))
print(Solution().canFinish(numCourses_3, prerequisites_3))







