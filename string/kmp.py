# KMP string algo

# pattern: ababd
def findPattern(text, pattern):
    # create prefix list for pattern
    lps = [0] * len(pattern)
    lps[0] = 0
    for i in range(1,len(pattern)):
        if lps[i-1] > 0:
            if pattern[lps[i-1]] == pattern[i]:
                lps[i] = lps[i-1] +1

        else:
            if pattern[0] == pattern[i]:
                lps[i] = 1
    print(lps)
    lp = -1
    t = 0
    while t < len(text):
        print(lp, t)
        if lp == len(lps) -2:
            return "found string"

        if  pattern[lp+1] == text[t]:
            print('match', pattern[lp+1], text[t])
            t+=1
            lp+=1
        else:
            if lp < 0:
                t+=1
            else:
                lp = lps[lp] -1

    return None
print(findPattern('abcababd', 'ababd'))