# 1817. Finding the Users Active Minutes
# https://leetcode.com/problems/finding-the-users-active-minutes/description/

'''
Edges and constraints:
len(unique users) >= 1
k >= 1
logs[i][0] >= 0 # user_id >=0
logs[i][1] >= 1 # time_i >= 1


Solution ideas_1 O(N logn):
[[0,5],[1,2],[0,2],[0,5],[1,3]]

#iter_1
[ 
[0,5],[0,2],[0,5],
[1,2],[1,3]
 ]
user_id = 0
output_temp = [0 for i len(k)]
 [0,5],[0,2],[0,5] → sum([0,1,0,0,1])
result_k = [0, 1,0,0,0] # Output should be: [0,2,0,0,0]

#iter_2
[[0,5],[0,2],[0,5],   
[1,2],[1,3]   
]
user_id = 1
output_temp = [0 for i len(k)] # make mask empty on new user
[1,2],[1,3]   →  sum([0,2,0,0,0]) but better implement via set() upon new user appears in iter object

Solution ideas_2 O(N):
[[0,5],[1,2],[0,2],[0,5],[1,3]]
{0:{5,2}, 1:{2,3}} # default_dict(int : set())

'''


from typing import List
from collections import defaultdict

def findingUsersActiveMinutes(logs: List[List[int]], k: int) -> List[int]:

    output = [0 for i in range(k+1)]
    storage = defaultdict(set)
    
    for i in logs: 
        storage[i[0]].add(i[1])

    for user in storage.keys(): # for _, minutes in storage.items()
        user_active_minutes = len(storage[user])
        output[user_active_minutes] += 1
    
    return output[1:]
    

logs_1 = [[0,5],[1,2],[0,2],[0,5],[1,3]]
k_1 = 5
# Output: [0,2,0,0,0]
# Explanation:
# The user with ID=0 performed actions at minutes 5, 2, and 5 again. Hence, they have a UAM of 2 (minute 5 is only counted once).
# The user with ID=1 performed actions at minutes 2 and 3. Hence, they have a UAM of 2.
# Since both users have a UAM of 2, answer[2] is 2, and the remaining answer[j] values are 0.

logs_2 = [[1,1],[2,2],[2,3]]
k_2 = 4
# Output: [1,1,0,0]


print(findingUsersActiveMinutes(logs_1, k_1))
print(findingUsersActiveMinutes(logs_2, k_2))



