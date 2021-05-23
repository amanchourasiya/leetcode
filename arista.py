
'''Given an array A[], find the maximum number of consecutive
 elements just before the given element A[I], so that A[i] 
 is greater than or equal to elements to its left
{80, 45, 40, 50, 40, 55, 65}
'''
#s = [(80,0), (45, 0)]
# [1, 1, 1, 2, 1, 4, 6]

def maxconsucutive(arr): # [80, 45, 40, 50, 40, 55, 65]
    stack = [] # push append, pop() pop(-1) (value, #elelment)
    res = []
    for val in arr:
        if len(stack) == 0:
            res.append(1)
            stack.append((val, 0))
            continue
        # TOS is less than curr value
        tmpans = 0
        while len(stack) >0 and  stack[-1][0] <= val:
            tmpans+=stack[-1][1] + 1
            stack.pop(-1)
        stack.append((val, tmpans))
        res.append(tmpans+1)

    return res

arr1 = [1,2,3,4,5] # [1, 2,3,4,5]
arr2 = [5,4,3,2,1] # [1,1,1,1,1]
arr3 = [1,1,1,1,1,0] # [1,2,3,4,5, 1]
arr4 = [1,2,3,-4,5,-4,3,-2,1] # [1, 2,3, 1, 5, 1, 2, 1, 2]
arr5 = [] # []

print(maxconsucutive(arr1))
print(maxconsucutive(arr2))
print(maxconsucutive(arr3))
print(maxconsucutive(arr4))
print(maxconsucutive(arr5))


        


