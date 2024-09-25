# 2073. Time Needed to Buy Tickets


from typing import List


class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        result = 0

        for i, t in enumerate(tickets):
            
            if i <= k:
                result += min(tickets[i], tickets[k])
            else:
                result += min(tickets[i], tickets[k]-1)

        return result



tickets_1 = [2,3,2]
k_1 = 2
# Output: 6
# Explanation:
# The queue starts as [2,3,2], where the kth person is underlined.
# After the person at the front has bought a ticket, the queue becomes [3,2,1] at 1 second.
# Continuing this process, the queue becomes [2,1,2] at 2 seconds.
# Continuing this process, the queue becomes [1,2,1] at 3 seconds.
# Continuing this process, the queue becomes [2,1] at 4 seconds. Note: the person at the front left the queue.
# Continuing this process, the queue becomes [1,1] at 5 seconds.
# Continuing this process, the queue becomes [1] at 6 seconds. The kth person has bought all their tickets, so return 6.

tickets_2 = [5,1,1,1]
k_2 = 0
# Output: 8
# Explanation:
# The queue starts as [5,1,1,1], where the kth person is underlined.
# After the person at the front has bought a ticket, the queue becomes [1,1,1,4] at 1 second.
# Continuing this process for 3 seconds, the queue becomes [4] at 4 seconds.
# Continuing this process for 4 seconds, the queue becomes [] at 8 seconds. 
# The kth person has bought all their tickets, so return 8.     

tickets_3 = [84,49,5,24,70,77,87,8]
k_3 = 3
# Output: 154

print(Solution().timeRequiredToBuy(tickets_1, k_1))
print(Solution().timeRequiredToBuy(tickets_2, k_2))
print(Solution().timeRequiredToBuy(tickets_3, k_3))



