# 143. Reorder List
# https://leetcode.com/problems/reorder-list/


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next



def reorderList(nums):

    ordered_lst = []
    curr = nums
    while curr:
        ordered_lst.append(curr.val)
        curr = curr.next


    r = []

    while ordered_lst:
        r.append(ordered_lst.pop(0))
        if len(ordered_lst) > 0:
            r.append(ordered_lst.pop(-1))

    curr = nums
    while curr:
        curr.val = r.pop(0)
        curr = curr.next

head_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# Output: [1,4,2,3]

head_2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# Output: [1,5,2,4,3]


reorderList(head_1)
reorderList(head_2)
