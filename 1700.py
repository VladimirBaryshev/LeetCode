# 1700. Number of Students Unable to Eat Lunch


from typing import List
from collections import defaultdict

class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        d = defaultdict(int)

        for s in students:
            d[s] += 1

        for i, sandwich in enumerate(sandwiches):
            if d[sandwich] == 0:
                return len(sandwiches) - i
            else:
                d[sandwich] -= 1

        return 0




students_1 = [1,1,0,0]
sandwiches_1 = [0,1,0,1]
# Output: 0 
# Explanation:
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
# - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
# - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
# - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
# - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
# Hence all students are able to eat.

students_2 = [1,1,1,0,0,1]
sandwiches_2 = [1,0,0,0,1,1]
# Output: 3     

print(Solution().countStudents(students_1, sandwiches_1))
print(Solution().countStudents(students_2, sandwiches_2))