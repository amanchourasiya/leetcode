'''
link from child to parent is given but not from parent to child
'''

from typing import no_type_check_decorator


def youngestCommonAncestor(root, nodeA, nodeB):
    if root is None:
        return None

    # Calculate depth of nodeA and nodeB
    tmp = nodeA
    nodeADepth = 0
    nodeBDepth = 0

    while tmp != root:
        tmp = tmp.parent
        nodeADepth+=1
    
    tmp = nodeB
    while tmp != root:
        tmp = tmp.parent
        nodeBDepth+=1

    if nodeADepth < nodeBDepth:
        for _ in range(nodeBDepth - nodeADepth):
            nodeB = nodeB.parent

    else:
        for _ in range(nodeADepth - nodeBDepth):
            nodeA = nodeA.parent

    if nodeA == nodeB:
        return nodeA
    
    while nodeA != nodeB:
        nodeA = nodeA.parent
        nodeB = nodeB.parent

    return nodeA