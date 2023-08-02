# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        stack = []
        curr = head

        while curr:
            stack.append(curr.val)
            # print(curr.val)
            curr = curr.next

        curr = head
        while curr:
            curr.val = stack.pop()
            # print(curr.val)
            curr = curr.next


        return head



head_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# Output: [5,4,3,2,1]

head_2 = ListNode(1, ListNode(2))
# Output: [2,1]

head_3 = ListNode()
# Output: []

t = Solution()
print(t.reverseList(head_1))

t = Solution()
print(t.reverseList(head_2))

t = Solution()
print(t.reverseList(head_3))