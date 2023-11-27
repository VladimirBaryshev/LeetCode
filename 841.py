# 841. Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/description/

'''
Edges and constraints:
len(rooms) >= 1
len(rooms[i]) >= 0
each rooms[i] are unique

Solution ideas:
Create list named “visited_rooms” (len of rooms) that padded with 0 or False values in it
Create stack and put each value (room_key) from *rooms[0]
Pop room_key and visit room
Don’t forget to add each index to stack
pad visited_rooms[i] where i equals to room_key
add room_key from popped stack only if “visited[index] == False” to avoid infinite loop
Return sum(visited_rums) == len(rooms)

'''

from typing import List

class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited_rooms = [False for i in rooms]
        visited_rooms[0] = True
        stack = [*rooms[0]] # [0]
        
        while stack:

            room_key = stack.pop() 
            visited_rooms[room_key] = True
            
            for k in rooms[room_key]:
                if not visited_rooms[k]:
                    stack.append(k)

        return sum(visited_rooms) == len(rooms)



 


rooms_1 = [[1],[2],[3],[]]
# Output: true
# Explanation: 
# We visit room 0 and pick up key 1.
# We then visit room 1 and pick up key 2.
# We then visit room 2 and pick up key 3.
# We then visit room 3.
# Since we were able to visit every room, we return true.

rooms_2 = [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.


print(Solution().canVisitAllRooms(rooms_1))
print(Solution().canVisitAllRooms(rooms_2))

