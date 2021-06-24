'''def isSameBST(arr1, arr2):
    larr1 = len(arr1)
    larr2 = len(arr2)
    if larr1 == 0 and larr2 == 0:
        return True

    if arr1[0] != arr2[0]:
        return False

    if len(arr1) != len(arr2):
        return False
    if len(arr1) == 1:
        return True

    smaller1 = []
    larger1 = []
    smaller2 = []
    larger2 = []

    for i in range(1, len(arr1)):
        if arr1[i] < arr1[0]:
            smaller1.append(arr1[i])
        else:
            larger1.append(arr1[i])

    for i in range(1, len(arr2)):
        if arr2[i] < arr2[0]:
            smaller2.append(arr2[i])
        else:
            larger2.append(arr2[i])

    return isSameBST(smaller1, smaller2) and isSameBST(larger1, larger2)

'''

def isSameBST(arr1, arr2): # Space O(depth) | time O(N)
    return isSameBSTHelper(arr1, arr2, 0, 0, float("-inf"), float("inf"))


def isSameBSTHelper(arr1, arr2, rootIdx1, rootIdx2, minVal, maxVal):
    if rootIdx1 == -1 or rootIdx2 == -1:
        return rootIdx1 == rootIdx2

    if arr1[rootIdx1] != arr2[rootIdx2]:
        return False

    leftRootIdx1 = getIdxFirstSmaller(arr1, rootIdx1, minVal)
    leftRootIdx2 = getIdxFirstSmaller(arr2, rootIdx2, minVal)
    rightRootIdx1 = getIdxFirstGreaterOrEqual(arr1, rootIdx1, maxVal)
    rightRootIdx2 = getIdxFirstGreaterOrEqual(arr2, rootIdx2, maxVal)
    
    currVal = arr1[rootIdx1]
    leftAreSame = isSameBSTHelper(arr1, arr2, leftRootIdx1, leftRootIdx2, minVal, currVal)
    rightAreSame = isSameBSTHelper(arr1, arr2, rightRootIdx1, rightRootIdx2, currVal, maxVal)

    return leftAreSame and rightAreSame



def getIdxFirstSmaller(arr, startIdx, minVal):
    for i in range(startIdx+1, len(arr)) :
        if arr[i] < arr[startIdx] and arr[i] >= minVal:
            return i
    return -1


def getIdxFirstGreaterOrEqual(arr, startIdx, maxVal):
    for i in range(startIdx+1, len(arr)):
        if arr[i] >= arr[startIdx] and arr[i] < maxVal:
            return i
    return -1



arr1 = [10,15,8,12,94,81,5,2,11]
arr2 = [10,8,5,15,2,12,11,94,81]

print(isSameBST(arr1, arr2))
    