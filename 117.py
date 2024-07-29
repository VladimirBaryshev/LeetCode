# 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/


from typing import collections


"""
# Definition for a Node.
"""
class Node:

    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        queue = [[0, root, root.val]]

        while queue:
            
            l = len(queue)
            for i in range(l):

                cur_level, cur_node, cur_val = queue.pop(0)

                if i < l-1:
                    cur_node.next = queue[0][1]

                # print(cur_level, cur_node.val, cur_node.next)

                if cur_node.left != None:
                    queue.append([cur_level+1, cur_node.left, cur_node.left.val])
                if cur_node.right != None:
                    queue.append([cur_level+1, cur_node.right, cur_node.right.val])

        return root
        


# Input: root = [1,2,3,4,5,null,7]
t_1 = Node(
        val=1, 
        left=Node(
                    val=2,
                    left=Node(val=4),
                    right=Node(val=5)
                ), 
        right=Node(
                    val=3,
                    left=None,
                    right=Node(val=7)
                )
    )


# Input: root = []
t_2 = Node()

print(Solution().connect(t_1))
print(Solution().connect(t_2))


