# FInd the lowest common subsequence and then form a result string by pnly copying the lcs once

def lcs(str1, str2, len1, len2):
    if len1 == 0 or len2 == 0:
        return ""
    
    dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]

    for row in range(1, len1+1):
        for col in range(1, len2+1):
            if str1[row-1] == str2[col-1]:
                dp[row][col] = 1 + dp[row-1][col-1]
            else:
                dp[row][col] = max(dp[row][col-1], dp[row-1][col])
     
    # Now we have to find lcs string
    row=len1
    col=len2
    res = []
    while(row !=0 and col !=0):
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

def shortest_com_subs(str1, str2, len1, len2):
    l = lcs(str1, str2, len1, len2)
    i,j = 0,0
    res = []
    for c in l:
        while str1[i] != c:
            res.append(str1[i])
            i+=1
        while str2[j] != c:
            res.append(str2[j])
            j+=1
        res.append(c)
        i+=1
        j+=1

    return ''.join(res) + str1[i:] + str2[j:]

print(shortest_com_subs("geek", "eke", 4,3))