# https://leetcode.com/problems/range-sum-of-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.s = 0
        self.traverse(root,low, high)
        return self.s
        
    def traverse(self, root, l, h):
        if root is None:
            return
        if root.val >= l:
            self.traverse(root.left, l, h)
        if root.val >= l and root.val <= h:
            self.s+=root.val
        if root.val <= h:
            self.traverse(root.right, l,h)
        
        