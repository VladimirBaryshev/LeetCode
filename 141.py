# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# [3,2,0,-4]
i_3 = ListNode(-4)
i_2 = ListNode(0)
i_1 = ListNode(2)
i_0 = ListNode(3)

i_0.next = i_1
i_1.next = i_2
i_2.next = i_3
i_3.next = i_1

head_1 = i_0
# pos = 1
# Output: true

t = Solution()
print(t.hasCycle(head_1))





# [1,2]
i_1 = ListNode(2)
i_0 = ListNode(1)
i_0.next = i_1

head_2 = i_0
# pos = 0
# Output: true

t = Solution()
print(t.hasCycle(head_1))



# [1]
i_0 = ListNode(1)
head_3 = i_0
# Output: false

t = Solution()
print(t.hasCycle(head_3))