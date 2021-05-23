def partition(arr, low, high):
    if low>=high:
        return
    i = low
    j = high
    pivotIndex = low
    pivotElement = arr[low]
    while i < j:

        while i<= high and arr[i] <= pivotElement:
            i+=1

        while  arr[j] > pivotElement:
            j-=1

        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
        
    
    arr[j], arr[pivotIndex] = arr[pivotIndex], arr[j]
    return j


def quickSort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quickSort(arr, start, p-1)
        quickSort(arr, p+1, end)
        

arr = [10,3,4,23,2,3,4,5]
quickSort(arr, 0, len(arr)-1)
print(arr)