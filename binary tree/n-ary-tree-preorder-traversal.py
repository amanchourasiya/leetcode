# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.arr = []
        self.traverse(root)
        return self.arr

    def traverse(self,root):
        if root is None:
            return None
        self.arr.append(root.val)
        for child in root.children:
            self.traverse(child)
        return root

