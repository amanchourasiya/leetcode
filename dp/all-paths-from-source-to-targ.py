# https://leetcode.com/problems/all-paths-from-source-to-target/
import copy 

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.res = []
        self.osf = []
        self.dfs(0, len(self.graph)-1)
        return self.res
       
    
    def dfs(self, start, target):
        self.osf.append(start)
        if  start == target:
            self.res.append(copy.deepcopy(self.osf))
            return
        
        if len(self.graph[start]) == 0:
            return
        
        for node in self.graph[start]:
            self.dfs(node, target)
            self.osf.pop(-1)
