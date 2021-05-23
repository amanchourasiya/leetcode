def findFirstDuplicate(arr, n): # Arr[] = {2, 1,4 , 2, 4}     1 <= Arr[i] <= N
    n = n
    for num in range(n):
        index = arr[num] % n
        arr[index] = arr[index] + n

    #print(arr)
    for index in range(n):
        if arr[index] >= 2* n:
            return index

    return -1
    

print(findFirstDuplicate([2,1,4,2,4], 5))
print(findFirstDuplicate([2,1,1,2,4], 5))
print(findFirstDuplicate([2,1,4,3,4], 5))

def findFirstDuplicateNew(arr, n):
    for i in range(n):
        num = abs(arr[i])
        if arr[num-1] < 0:
            return num
        arr[num-1] = 0-arr[num-1]


print(findFirstDuplicateNew([2,1,4,2,4], 5))
print(findFirstDuplicateNew([2,1,1,2,4], 5))
print(findFirstDuplicateNew([2,1,4,3,4], 5))