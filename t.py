def findCool(n):
    s = bin(n)[2:]
    res = 0
    index = 0
    while index < len(s)-2:
        index = s.find('101', index, len(s))
        if index == -1:
            break
        res+=1
        index+=1

    return res

def findVeryCool(r, k):
    res = 0
    for i in range(5, r):
        if findCool(i) >= k:
            res+=1
    return res

print(findCool(21))