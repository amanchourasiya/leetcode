def longest_repeating_subsequence(str1):
    str2 = str1[::]
    len1 = len(str1)
    dp = [[0 for _ in range(len1+1)] for _ in range(len1+1)]

    for row in range(1,len1+1):
        for col in range(1, len1+1):
            if str1[row-1] == str2[col-1] and row != col:
                dp[row][col] = 1 + dp[row-1][col-1]
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])
    return dp[-1][-1]

