# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.s = 0
        self.util(root)
        return self.s

    def util(self, root):
        if root is None:
            return
        
        if root.val % 2 == 0: # even
            if root.left is not None:
                if root.left.left is not None:
                    self.s+= root.left.left.val
                if root.left.right is not None:
                    self.s+= root.left.right.val
            if root.right is not None:
                if root.right.left is not None:
                    self.s+= root.right.left.val
                if root.right.right is not None:
                    self.s+= root.right.right.val
        self.util(root.left)
        self.util(root.right)