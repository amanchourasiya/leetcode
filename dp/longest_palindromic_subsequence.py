def palindromic_subsequece(str1):
    str2 = str1[::-1]
    len1 = len(str1) # No need for len2 since both strings will be of same length
    
    dp = [[0 for _ in range(len1+1)] for _ in range(len1+1)]

    for row in range(1, len1+1):
        for col in range(1, len1+1):
            if str1[row-1] == str2[col-1]:
                dp[row][col] = 1 + dp[row-1][col-1]
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])
    
    # Now we have got the length of longest palindromic subsequense in dp[len1][len1]
    # Time to find the string
    print(dp)
    row = len1
    col = len1
    res = []
    while (row != 0 and col != 0):
        if str1[row-1] == str2[col-1]:
            res.append(str1[row-1])
            col-=1
            row-=1
        elif dp[row-1][col] > dp[row][col-1]:
            row-=1
        else:
            col-=1
    return ''.join(res)

print(palindromic_subsequece('abcxxba'))


