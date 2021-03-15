# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = tail = TreeNode()
        while root is not None:
            if root.left is not None:
                pre = root.left
                while pre.right is not None:
                    pre = pre.right
                pre.right = root
                left, root.left = root.left, None
                root = left
            else:
                tail.right = tail = root
                root = root.right
        return dummy.right
