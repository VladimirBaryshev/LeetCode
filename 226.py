# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

root_1 = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

root_2 = [2,1,3]
# Output: [2,3,1]

root_3 = []
# Output: []



# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



def flatten(tree):
    
    r = []

    queue = [tree]

    while len(queue) > 0:

        node = queue.pop(0)

        r.append(node.val)

        if node.left != None and node.right != None:
            queue.append(node.left)
            queue.append(node.right)

    return r


root_1 = [4,2,7,1,3,6,9]
t_case_1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
print(root_1)
print(flatten(t_case_1))

s = Solution()
print(flatten(s.invertTree(t_case_1)))


output = [4,7,2,9,6,3,1]
print(output)




