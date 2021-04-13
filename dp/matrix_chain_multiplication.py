import sys

dp = {}
def solve(arr, i, j):
    if i >= j:
        return 0
    if dp.get((i,j), -1) != -1:
        return dp[(i,j)]
    '''if j-i == 1:
        dp[(i,j)] = arr[i] *2
        return dp[(i,j)]
    '''
    mn = sys.maxsize
    
    for k in range(i, j):
        ans = solve(arr, i, k) + solve(arr, k+1, j) + (arr[i-1] * arr[k] * arr[j])
        if ans < mn:
            mn = ans
        dp[(i,j)] = mn
        
    return mn

print(solve([1,2,3,4,5], 1, 4))