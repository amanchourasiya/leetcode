import copy

def lowestCommonManager(root, nodeA, nodeB):
    nodeAPath = []
    nodeBPath = []

    searchNode(root, nodeA, nodeB, '', nodeAPath, nodeBPath)

    return matchPath(nodeAPath, nodeBPath)

def printList(path):
    res = []
    for p in path:
        res.append(p.val)
    return res

def matchPath(path1, path2):
 
    index = 0
    while path1[index] == path2[index]:
        index+=1
    
    return path1[index-1]

def searchNode(root, nodeA, nodeB, currentPath,nodeAPath, nodeBPath):
    if root is None:
        return
    if len(nodeAPath) > 0 and len(nodeBPath) > 0:
        return


    if root == nodeA:
        nodeAPath.extend(copy.deepcopy(currentPath))

    if root == nodeB:
        nodeBPath.extend(copy.deepcopy(currentPath))

    searchNode(root.left, nodeA, nodeB, currentPath , nodeAPath, nodeBPath)
    searchNode(root.right, nodeA, nodeB, currentPath, nodeAPath, nodeBPath)

def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(kid, p, q)
                   for kid in (root.left, root.right))
    return root if left and right else left or right