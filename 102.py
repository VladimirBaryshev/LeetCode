# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level = 0
        result = []
        queue = [[root, level]]

        while queue:

            node, level = queue.pop(0)

            if node and len(result)-1 < level:
                result.append([])
            
            if  node and node.val != None:
                result[level].append(node.val)

            if node and node.left:
                queue.append([node.left, level+1])

            if node and node.right:
                queue.append([node.right, level+1])

        return result



root_1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# Output: [[3],[9,20],[15,7]]

root_2 = TreeNode(1)
# Output: [[1]]

root_3 = TreeNode()
# Output: []        

root_4 = TreeNode(0, TreeNode(2), TreeNode(4))

t = Solution()
print(t.levelOrder(root_1))
t = Solution()
print(t.levelOrder(root_2))
t = Solution()
print(t.levelOrder(root_3))
t = Solution()
print(t.levelOrder(root_4))



