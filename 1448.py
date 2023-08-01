# 1448. Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = [[root, root.val]]
        counter = 0

        while stack:

            node, max_val = stack.pop()
            val = node.val
            
            if val >= max_val:
                max_val = val
                counter += 1

            if node.left != None:
                stack.append([node.left, max_val])
            if node.right != None:
                stack.append([node.right, max_val]) 

        return counter


root_1 = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
# Output: 4

root_2 = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
# Output: 3

root_3 = TreeNode(1)
# Output: 1

t = Solution()
print(t.goodNodes(root_1))

t = Solution()
print(t.goodNodes(root_2))

t = Solution()
print(t.goodNodes(root_3))