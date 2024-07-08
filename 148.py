# 148. Sort List
# https://leetcode.com/problems/sort-list/description/


from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None
        
        arrs = []
        cur = head
        while cur:
            arrs.append(cur.val)
            cur = cur.next
        
        cur = head
        for i in sorted(arrs):
            cur.val = i
            cur = cur.next
        
        return head

        