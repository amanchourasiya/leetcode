def find_longest_substring(str1, str2, len1, len2):
    dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
    mx = 0
    for row in range(1, len1+1):
        for col in range(1, len2+1):
            if str1[row-1] == str2[col-1]:
                dp[row][col] = 1 + dp[row-1][col-1]
                if mx<dp[row][col]:
                    mx = dp[row][col]
            else:
                dp[row][col] = 0
    
    return mx

print(find_longest_substring("12321",  "12344", 5,5 ))