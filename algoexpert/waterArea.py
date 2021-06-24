def maxWaterArea(towers):
    tc = len(towers)
    arr = [[0,0] for _ in range(tc)]

    #print(arr)
    # calculate the left largest tower
    for i in range(1, tc):
        arr[i][0] = max(towers[i-1], arr[i-1][0])
    print(arr)
    # calculate right largest tower

    for i in range(tc-2, -1, -1):
        #print(towers[i+1], arr[i+1][1])
        arr[i][1] = max(towers[i+1], arr[i+1][1])
    print(arr)
    res = 0
    for i in range(1, tc-1):
        if arr[i][0] == 0 or arr[i][1] == 0 or max(arr[i][0], arr[i][1], towers[i]) == towers[i] or towers[i] > min(arr[i][0], arr[i][1]):
            continue
        print(i,res)
        res += abs(min(arr[i][0],arr[i][1]) - towers[i])
        print(i,res)

    return res

towers = [0,1,0,2,1,0,1,3,2,1,2,1]
print(towers)
print(maxWaterArea(towers))