# 92. Reverse Linked List II

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        cur = head
        result = []
        head_pointers = []
        while cur.next != None:
            result.append(cur.val)
            head_pointers.append(cur)
            cur = cur.next
        result.append(cur.val)
        head_pointers.append(cur)

        t = result[left-1:right]
        t.reverse()
        result[left-1:right] = t

        for v,hp in zip(result, head_pointers):
            hp.val = v

        return head


# [1,2,3,4,5]
head_1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
left_1 = 2
right_1 = 4
# Output: [1,4,3,2,5]

# [5]
head_2 = ListNode(val=5)
left_2 = 1
right_2 = 1
# Output: [5]

print(Solution().reverseBetween(head_1, left_1, right_1))
print(Solution().reverseBetween(head_2, left_2, right_2))