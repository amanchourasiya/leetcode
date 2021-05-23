def findMissingNum(arr):
    n = len(arr) + 2 # n = 5
    # 1245
    expectedSum = n* (n+1) //2 # 15
    currentSum = sum(arr) # 12
    
    sumab = expectedSum-currentSum # 5
    
    currentProduct = 1 #9
    for value in arr:
        currentProduct*=value
       
    expectedProduct = 1 # 54
    for value in range(1,n+1):
        expectedProduct*=value
    
    c = expectedProduct // currentProduct # 6
    
    # a * (5-a)  = 6a -a^2
    # 5a - 1a^2 - c = 0
    # ax^2 + bx +c = 0
    
    # calculate(-1, 5, -6, , 5)
    return calculate(-1, sumab, -1*(c), sumab)
    
    
def calculate(a,b,c, sumab):
    
    bsac = pow(b,2) - (4 *a *c)
    
    
    tmpans = -b + pow(bsac, 0.5)
    
    tmpans = tmpans / (2*a)
    
    
    #ans1 =  ((-b) +  (pow((pow(b,2) - 4*a*c), 0.5))) // (2*a)
    ans1 = tmpans
    ans2 = sumab-ans1
    return ans1, ans2
    

print(findMissingNum([1,4,5]))
         
    