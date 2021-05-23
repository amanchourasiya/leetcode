def moveElementToEnd(arr, element):
    i = 0
    j = len(arr) -1

    while i < j:
        while j>=0 and arr[j] == element:
            j-=1

        while i<len(arr) and arr[i] != element:
            i+=1
        if i>len(arr)-1 or j<0 or i>j:
            break

        arr[i], arr[j] = arr[j],arr[i]


    return arr

print(moveElementToEnd([2,1,2,2,2,4,2], 2))