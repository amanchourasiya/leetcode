def buildTree(arr, start, end, treeArr, currentNode):
    if start == end:
        treeArr[currentNode] = arr[start]
        return

    mid = (start+end) //2

    buildTree(arr, start, mid, treeArr, 2*currentNode+1)
    buildTree(arr, mid+1, end, treeArr, 2*currentNode + 2)

    treeArr[currentNode] = treeArr[2*currentNode+1] + treeArr[2*currentNode+2]

def updateTree(arr, start, end, treeArr, currentNode, targetIndex, targetValue):
    #print(treeArr, currentNode, start, end)
    if start == end:
        arr[targetIndex] = targetValue
        treeArr[currentNode] = targetValue
        print(treeArr)
        return
    
    mid = (start+end)//2
    if mid < targetIndex:
        updateTree(arr, mid+1, end, treeArr, 2*currentNode+2, targetIndex, targetValue)
    else:
        updateTree(arr, start, mid, treeArr, 2*currentNode+1, targetIndex, targetValue)
    #print('calculate', currentNode, treeArr[2*currentNode+1], treeArr[2*currentNode+2])
    treeArr[currentNode] = treeArr[2*currentNode+1] + treeArr[2*currentNode+2]

def segmentTree(arr):
    treeArr = [0 for _ in range(2*len(arr))]
    buildTree(arr, 0, len(arr)-1, treeArr, 0)
    print(treeArr)
    #updateTree(arr, 0, len(arr)-1, treeArr, 0, 5, 120)
    print(treeArr, arr)
    print(query(treeArr, 0, 0, len(arr)-1, 0,8))

def query(treeArr,currentNode, start, end, left, right):
    # completely outside current range
    if start > right or end < left:
        return 0

    # completely inside
    if start >= left and end <=right:
        return treeArr[currentNode]

    # partialy inside ot outside
    mid = (start+end) //2 
    return query(treeArr, 2*currentNode+1, start, mid, left, right) + query(treeArr, 2*currentNode+2, mid+1, end, left , right)





segmentTree([1,2,3,4,5,6,7,8,9])
