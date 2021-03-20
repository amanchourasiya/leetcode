# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None or target == original:
            return cloned
        
        res = self.getTargetCopy(original.left, cloned.left, target)
        if res is not None:
            return res
        return self.getTargetCopy(original.right, cloned.right, target)