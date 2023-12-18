# 590. N-ary Tree Postorder Traversal
# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

from typing import List, Optional 

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def postorder(self, root: 'Node') -> List[int]:
        result = [l]
        stack = [root]
        
        while stack:
            cur_node = stack.pop()
            if cur_node: # if None we don’t pass it
                result.append(cur_node.val)
                if cur_node.children:
                    for node in cur_node.children:
                        stack.append(node)

        result.reverse()
        return result


root_1 = [1,null,3,2,4,null,5,6]
# Output: [5,6,3,2,4,1]

root_2 = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
