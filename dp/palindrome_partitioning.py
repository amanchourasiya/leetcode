import sys
res = []
def isPalindrome(str1, i, j):
    while i<=j:
        if str1[i] != str1[j]:
            return False
        i+=1
        j-=1
    
    return True

# Test isPalindrome func
#print(isPalindrome('abad', 0, 3))

dp = {}

def minPalindromicPartition(str, i, j):
    

    print(i,j)
    if i >= j:
        return 0
    if isPalindrome(str, i,j):
        return 0
    
    if dp.get((i,j), -1) != -1:
        return dp[(i,j)] 

    mn = sys.maxsize

    for k in range(i, j): # Very important either take k from i to j-1 or i+1 to j
        left = 0
        if dp.get((i,k), -1 ) == -1:
            left = minPalindromicPartition(str, i, k)
            dp[(i,k)] = left
        else:
            left = dp[(i,k)]
 
        right  = 0
        if dp.get((k+1,j), -1 ) == -1:
            right = minPalindromicPartition(str, k+1, j)
            dp[(k+1,j)] = right
        else:
            right = dp[(k+1,j)]
        
        ans = 1+  left + right
        if ans < mn:
            mn = ans
        
    
    dp[(i,j)] = mn
    print(dp)
    return mn  

print(minPalindromicPartition('abaaa', 0,4))
