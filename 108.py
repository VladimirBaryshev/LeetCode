# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/


from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        mid = len(nums)//2

        root = TreeNode(val=nums[mid])
        lefts = nums[:mid]
        rights = nums[mid+1:]

        queue = []
        queue.append([root, lefts, 0])
        queue.append([root, rights, 1])

        while queue:

            # print(queue)

            # direction: 0 means go left and 1 means go right 
            parent, elems, direction = queue.pop(0)

            if elems:
                
                mid = len(elems) // 2
                node = TreeNode(val=elems[mid])

                if direction == 0:
                    parent.left = node

                if direction == 1:
                    parent.right = node

                queue.append([node, elems[:mid], 0])
                queue.append([node, elems[mid+1:], 1])

        return root


        


nums_1 = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted

nums_2 = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

print(Solution().sortedArrayToBST(nums_1))
print(Solution().sortedArrayToBST(nums_2))








