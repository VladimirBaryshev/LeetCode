# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/


import heapq
from collections import deque
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
    if n == 0:
        return len(tasks)
    
    char_counter = dict()

    for char in tasks:

        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1

    mx = max(char_counter.values())
    x = sum((1 for v in char_counter.values() if v == mx))
    # print(mx, x)
    return max( len(tasks), ((mx-1)*(n+1)+x))

# ["A","A","B","B"]
# n = 3
# A B _ _ A B

# ["A","A","B","B"]
# n = 2
# A B _ A B

# ["A","A","B","B"]
# n = 1
# A B A B



tasks_1 = ["A","A","A","B","B","B"]
n_1 = 2
# Output: 8
# Explanation: 
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.

tasks_2 = ["A","A","A","B","B","B"]
n_2 = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.

tasks_3 = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n_3 = 2
# Output: 16
# Explanation: 
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A    

tasks_4 = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
n_4 = 2
# Output: 12

# leastInterval(["A","A","A","B","B","B","C","C","D","D"], 3)
print(leastInterval(tasks_1, n_1))
print(leastInterval(tasks_2, n_2))
print(leastInterval(tasks_3, n_3))
print(leastInterval(tasks_4, n_4))







