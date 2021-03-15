# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.arr = []
        self.traverse(root)
        return self.arr

    def traverse(self,root):
        if root is None:
            return None
        for child in root.children:
            self.traverse(child)
        self.arr.append(root.val)
        return root
