t = int(input())
for _ in range(t):
    a,y,x = list(map(int,input().split()))
    res = 0

    if a < y:
        #print("a<y")
        res+=1
    
    res = res + (a * x)
    print('res before', res)
    res = res - (x * (a+1 - y))
    print('res after', res)
    
    print(res)