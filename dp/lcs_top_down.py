def find_lcs_length(str1, str2, len1, len2):
  
    if len1 == 0 or len2 == 0:
        return 0

    dp = [[0 for _ in range(len1+1)] for _ in range(len2+1)]
    for row in range(1,len2+1):
        for col in range(1, len1+1):
            if str1[col-1] == str2[row-1]:
                dp[row][col] = 1 + dp[row-1][col-1]
            else:
                dp[row][col] = max(dp[row-1][col], dp[row][col-1])
    
    # Finding substring
    res = []
    row = len2
    col = len1
    while(row != 0 and col !=0):
        print(row,col)
        if str1[col-1] == str2[row-1]:
            res.append(str1[col-1])
            row-=1
            col-=1
        elif dp[row][col-1] > dp[row-1][col]:
            col = col-1
        else:
            row = row -1

    res.reverse() 
    
    return ''.join(res)

print(find_lcs_length("mbadm",  "mdabm", 5,5 ))