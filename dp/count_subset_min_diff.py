'''
s1 = (diff + sum(arr)) // 2
'''

# count subset sum with value s1

def count_subset_sum_diff(arr, diff):
    l = len(arr)
    s = sum(arr)
    s1 = (s+diff)
    if s1 & 1 == 1:
        return 0

    # count 0
    c = arr.count(0)
    s1 = s1//2

    dp = [[0 for _ in range(s1+1)] for _ in range(l+1)]
    
    dp[0][0] = 1 # becaues 0 may also be included
    
    for row in range(1, l+1):
        for col in range(s1 + 1): # Special case because 0 also may be included
            if arr[row - 1] <= col:
                dp[row][col] = dp[row-1][col-arr[row-1]] + dp[row-1][col]
            else:
                dp[row][col] = dp[row-1][col]
    #print(dp)
    if c >1:
        return dp[l][s1] * (2**c)
    else:
        return dp[l][s1]

min_diff_s_count = count_subset_sum_diff([9,7,0,3,9,8,6,5,7,6],2)
print(min_diff_s_count)