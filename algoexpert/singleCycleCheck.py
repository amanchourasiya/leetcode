# Space O(1) | time O(n)

def hasCycle(arr):
    n = len(arr)
    startIndex = 0
    currIndex = 0
    for i in range(n-1):
        index = getIndex(currIndex, arr[currIndex], n)
        print(currIndex, index)
        if index == startIndex:
            return False
        
        currIndex = index
    
    if getIndex(currIndex, arr[currIndex],n) != startIndex:
        return False

    return True


def getIndex(currIndex, move, n):
    print('getIndex', currIndex, move)
    m = currIndex + move
    if m < 0:
        m = 0- (abs(m)%n)
        return n+m
    return m % n

arr = [2,3,1,-4,-4,2] 
print(hasCycle(arr))