# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.s = 0
        self.p = []

    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.sumUtil(root)
        return self.s

    def sumUtil(self, root):
        if root is None:
            return
        
        self.p.append(root.val)

        # Check for leaf
        if root.left is None and root.right is None:
            self.calc()
            return

        if root.left is not None:
            self.sumUtil(root.left)
            self.p.pop(-1)
        if root.right is not None:
            self.sumUtil(root.right)    
            self.p.pop(-1)     
    
    def calc(self):
        self.p = list(map(str, self.p))
        self.s += int(''.join(self.p), 2)
