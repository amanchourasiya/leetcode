'''
Given a binary calculate sum of all nodes
'''
""" 
def alldepth(root,currdepth=0):
    if root is None:
        return 0

    return currdepth+ alldepth(root.left, currdepth+1) + alldepth(root.right, currdepth+1)
    

def allNodesDepth(root):
    allNodesDepthSum = 0
    stack = [root]

    while len(stack) > 0:
        node = stack.pop()
        allNodesDepthSum+=alldepth(node)
        if node is not None:
            stack.append(node.left)
            stack.append(node.right)
    return allNodesDepthSum 
 """

def allKindsOfNodeDepth(root):
    nodeCount = {}
    allNodeCounts(root, nodeCount)
    nodeDepth = {}
    allNodeDepths(root, nodeDepth, nodeCount)
    return sumAllNodesDepth(root, nodeDepth)

def allNodeCounts(node, nodeCount):
    nodeCount[node] = 1

    if node.left is not None:
        allNodeCounts(node.left, nodeCount)
        nodeCount[node] += nodeCount[node.left]
    if node.right is not None:
        allNodeCounts(node.right, nodeCount)
        nodeCount[node] += nodeCount[node.right]


def allNodeDepths(node, nodeDepth, nodeCount):
    nodeDepth[node] = 0

    if node.left is not None:
        allNodeDepths(node.left, nodeDepth, nodeCount)
        nodeDepth[node] += nodeDepth[node.left] + nodeCount[node.left]
    if node.right is not None:
        allNodeDepths(node.right, nodeDepth, nodeCount)
        nodeDepth[node] += nodeDepth[node.right] + nodeCount[node.right]


def sumAllNodesDepth(root, nodeDepth):
    sm = 0
    for node in nodeDepth:
        sm+= nodeDepth[node]

    return sm


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.nodeDepth = 0
        self.noOfNodes = 0

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.left = Node(6)
root.right.right = Node(7)

print(allKindsOfNodeDepth(root))