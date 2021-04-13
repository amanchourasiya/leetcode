def is_sequence(str1, str2, len1, len2):
    if len1 == 0:
        return True
    if len2 == False:
        return False
    
    if str1[len1-1] == str2[len2-1]:
        return is_sequence(str1, str2, len1-1, len2-1)
    
    return is_sequence(str1, str2, len1, len2-1)

print(is_sequence('gksrek', 'geeksforgeeks'))
