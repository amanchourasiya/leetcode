def longest_palindrome_substring(str1):
    l = len(str1)
    mx = 1
    # Find max odd palindrome
    i = 0
    gi = 0
    gj = 0
    while i < l:
        j = 1
        while (i-j) >=0 and (i+j) < l:
            if str1[i-j] != str1[i+j]:
                break
            
            if (2*j +1) > mx:
                mx = 2*j +1
                gi = i-j
                gj = i+j
            j+=1
        i+=1

    i = 0.5
    while int(i) < l:
        j = 0.5
        while (int(i-j) >=0) and (int(i+j) < l):
            if str1[int(i-j)] != str1[int(i+j)]:
                break
            
            if (int(2*j + 1)) > mx:
                mx = int(2*j+1)
                gi = int(i-j)
                gj = int(i+j)
                
            j+=1
        i+=1
    
    return gi, gj

    # find max even palindrome

print(longest_palindrome_substring('abcba'))
