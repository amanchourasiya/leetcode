def findLCS(str1, str2):
    dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

    for row in range(1, len(str1)+1):
        for col in range(1, len(str2)+1):
            #print(row,col)
            if str1[row-1] == str2[col-1]:
                dp[row][col] = dp[row-1][col-1] + 1
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])

    res = []
    row = len(str1)
    col = len(str2)
    while row >=1 and  col>=1:
        print(row,col)
        if str1[row-1] == str2[col-1]:
            res.append(str1[row-1])
            row-=1
            col-=1
        elif dp[row][col-1] < dp[row-1][col]:
            row-=1
        else:
            col-=1

    res.reverse()
    return ''.join(res)


str1 = "axyb"
str2 = "abyxb"
print(findLCS(str1, str2))