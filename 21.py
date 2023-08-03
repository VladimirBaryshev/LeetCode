# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# https://leetcode.com/problems/merge-two-sorted-lists/solutions/3857605/heavy-concept-for-those-who-write-in-python-only/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = []

        cur_1 = list1
        cur_2 = list2

        while cur_1 and cur_2:

            # print('!', result, cur_1, cur_2)

            if cur_1.val != None and cur_2.val != None:
                if cur_1.val <= cur_2.val:
                    result.append(cur_1.val)
                    cur_1 = cur_1.next

                else:
                    result.append(cur_2.val)
                    cur_2 = cur_2.next
            else:
                break

        while cur_1:

            # print('!', result, cur_1.val)
            if cur_1.val != None:
                result.append(cur_1.val)
                cur_1 = cur_1.next
            else:
                break

        while cur_2:

            # print('!YO', result, cur_2.val)
            if cur_2.val != None:
                result.append(cur_2.val)
                # print('!YOYO', result)
                cur_2 = cur_2.next
            else:
                break
        
        prev = None
        while result:
            prev = ListNode(result.pop(), prev)


        return prev



list1_t1 = ListNode(1, ListNode(2, ListNode(4)))
list2_t1 = ListNode(1, ListNode(3, ListNode(4)))
# Output: [1,1,2,3,4,4]


list1_t2 = ListNode()
list2_t2 = ListNode()
# Output: []

list1_t3 = ListNode()
list2_t3 = ListNode(0)
# Output: [0]   


t = Solution()
print(t.mergeTwoLists(list1_t1, list2_t1))

t = Solution()
print(t.mergeTwoLists(list1_t2, list2_t2))

t = Solution()
print(t.mergeTwoLists(list1_t3, list2_t3))
