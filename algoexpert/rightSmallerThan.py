def rightSmaller(arr):
    if len(arr) == 0:
        return []
    arr.reverse()
    res = []
    res.append(0)
    root = Node(arr[0])

    for i in range(1, len(arr)):
        insert(root, arr[i], res,0)
    
    res.reverse()
    return res

def insert(root,num, res, count):
    if num < root.val:
        root.small+=1
        if root.left is None:
            root.left = Node(num)
            res.append(count)
        else:
            insert(root.left, num, res, count)
    elif num > root.val:
        if root.right is None:
            root.right = Node(num)
            res.append(count+1+root.small)
        else:
            insert(root.right, num, res, count+1+root.small)
    else:
        if root.right is None:
            root.right = Node(num)
            res.append(count+ root.small)
        else:
            
            insert(root.right, num, res, count+root.small)
            


# time O(nlogn)
# space O(n)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.small = 0

#print(rightSmaller([8,5,11,-1,3,4,2]))