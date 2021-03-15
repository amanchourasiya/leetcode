# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.d=0
        if not root:
            return self.d
        self.temp=0
        
        def helper(root):
            if not root:
                return None
            self.temp+=1
            for c in root.children:
                helper(c)
            if self.temp>self.d:
                self.d=self.temp
            self.temp-=1
        
        helper(root)
        return self.d
        