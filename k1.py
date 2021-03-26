t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    s = input()
    k1 = 0
        
    for j in range(n//2):
        if s[j] != s[n-j-1]:
            #print(s[j], s[n-j-1])
            k1+=1
    k1 = abs(k-k1)
    st = 'Case #' + str(i) + ': ' + str(k1)
    print(st)