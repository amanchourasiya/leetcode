# find kth largest element

def quickSelect(arr,k):
    l = len(arr)-1
    return quickSelectHelper(arr,k,l)


def quickSelectHelper(arr, k,l):
    start = 0
    end = len(arr)-1
    while True:
        #print(start,end, left, right)
        left = start+1
        right = end
        pivotElement = arr[start]
        pivotIndex = start

        while left <= right:
            while left < len(arr) and arr[left] <= pivotElement:
                left+=1

            while right > 0 and arr[right] > pivotElement :
                right-=1

            if left < right:
                swap(left,right, arr)

        swap(pivotIndex, right,arr)
        if right == l-k+1:
            return arr[right]
        
        if right > l-k+1:
            end = right-1
        else:
            start = right+1

            
def swap(left, right, arr):
    arr[left], arr[right] = arr[right],arr[left]

print(quickSelect([2,35,25,64,2,1], 1))