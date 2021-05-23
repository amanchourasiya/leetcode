t = int(input())

for _ in range(t):
    def getNterm(n):
        #print(n)
        return (n* (n+1)) //2
        
    g = int(input())
    
    res = 1
    for i in range(1,g):
        nterm = getNterm(i)
        if nterm >= g:

            break
        if (g-nterm) % (i+1) == 0:
            #print('ans')
            res+=1
            
    print(res)
    