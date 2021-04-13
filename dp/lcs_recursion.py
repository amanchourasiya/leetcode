def find_lcs_length(str1, str2, len1, len2):
    if len1 <= 0 or len2 <= 0 :
        return 0
    
    if str1[len1-1] == str2[len2-1]:
        return 1 + find_lcs_length(str1, str2, len1-1, len2-1)
    else:
        return max(find_lcs_length(str1,str2, len1, len2-1), find_lcs_length(str1, str2, len1-1, len2))

print(find_lcs_length("ABCDGH",  "AEDFHR", 6,6 ))
