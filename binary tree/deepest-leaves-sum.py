# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        return self.level(root)
        
    def level(self, root):
        if root is None:
            return 0
        s = 0
        p = []
        p.append(root)

        while len(p) != 0:
            s = 0
            for _ in range(len(p)):
                a = p.pop(0)
                s+=a.val
                if a.left is not None:
                    p.append(a.left)
                if a.right is not None:
                    p.append(a.right)
        return s
            
            