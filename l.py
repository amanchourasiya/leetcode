t = int(input())
for i in range(t):
    r, c = list(map(int, input().split()))
    l = []
    for _ in range(r):
        l.append(list(map(int, input().split())))
    #print(l)
    dp = [[[0,0,0,0] for i in range(c)] for j in range(r) ]
    #up
    for j in range(c):
        for k in range(r):
            if k == 0:
                dp[k][j][0] = l[k][j]
                continue
            if l[k][j] == 0:
                dp[k][j][0] = 0
            else:
                dp[k][j][0] = dp[k-1][j][0] + 1
    #print(dp)

    # down
    for j in range(c):
        for k in range(r-1,-1, -1):
            if k == r-1:
                dp[k][j][1] = l[k][j]
                #print(k)
                continue
            if l[k][j] == 0:
                dp[k][j][1] = 0
            else:
                dp[k][j][1] = dp[k+1][j][1] + 1
    

    for j in range(r):
        for k in range(c):
            if k == 0:
                dp[j][k][2] = l[j][k]
                #print(k)
                continue
            if l[j][k] == 0:
                dp[j][k][2] = 0
            else:
                dp[j][k][2] = dp[j][k-1][2] + 1


    for j in range(r):
        for k in range(c-1, -1, -1 ):
            if k == c-1:
                dp[j][k][3] = l[j][k]
                #print(k)
                continue
            if l[j][k] == 0:
                dp[j][k][3] = 0
            else:
                dp[j][k][3] = dp[j][k+1][3] + 1
    #print(dp)


    s = 0

    for r1 in range(r):
        for c1 in range(c):
            #ur
            if r1 > 0 and c1 <c -1 and l[r1][c1] == 1:
                if l[r1-1][c1] == 1 and l[r1][c1+1] == 1:
                    n1 = dp[r1][c1][0]
                    n2 = dp[r1][c1][3]
                    if n1 > n2:
                        n1, n2 = n2, n1
                    ans = ((n1//2) -1) *2
                    ans = ans + (n2//2) - (n1//2)
                    s+=ans

            #ul
            if r1 > 0 and c1 >0 and l[r1][c1] == 1:
                if l[r1-1][c1] == 1 and l[r1][c1-1] == 1:
                    n1 = dp[r1][c1][0]
                    n2 = dp[r1][c1][2]
                    if n1 > n2:
                        n1, n2 = n2, n1
                    ans = ((n1//2) -1) *2
                    ans = ans + (n2//2) - (n1//2)
                    s+=ans
            
            #br
            if r1 <r-1 and c1 <c-1 and l[r1][c1] == 1:
                if l[r1+1][c1] == 1 and l[r1][c1+1] == 1:
                    n1 = dp[r1][c1][1]
                    n2 = dp[r1][c1][3]
                    if n1 > n2:
                        n1, n2 = n2, n1
                    ans = ((n1//2) -1) *2
                    ans = ans + (n2//2) - (n1//2)
                    s+=ans
            
            #bl
            if r1 < r-1 and c1 >0 and l[r1][c1] == 1:
                if l[r1+1][c1] == 1 and l[r1][c1-1] == 1:
                    n1 = dp[r1][c1][1]
                    n2 = dp[r1][c1][2]
                    if n1 > n2:
                        n1, n2 = n2, n1
                    ans = ((n1//2) -1) *2
                    ans = ans + (n2//2) - (n1//2)
                    s+=ans
    st = 'Case #' + str(i+1) + ': ' + str(s)
    print(st)