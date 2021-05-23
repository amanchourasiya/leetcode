def is_match(text, pattern):
  # need to search for wildcards
  return match_helper(text, pattern , 0, 0)
 
def match_helper(text, pattern, textIndex, patIndex):
  print(textIndex, patIndex)
  if textIndex >= len(text):
    if patIndex >= len(pattern):
      return True
    else:
      if patIndex+1 < len(pattern) and  pattern[patIndex+1] == '*':
        return match_helper(text, pattern, textIndex, patIndex+2)
      else:
        print('false first')
        return False
  # if pattern index finished and text index not finished
  
  elif patIndex >= len(pattern) and textIndex < len(text):
    print('false second')
    return False
  
  elif patIndex + 1 < len(pattern) and pattern[patIndex+1] == '*':
    if pattern[patIndex] == '.' or text[textIndex] == pattern[patIndex]:
      return match_helper(text, pattern, textIndex, patIndex+2) or match_helper(text, pattern, textIndex +1, patIndex)
    else:
      return match_helper(text, pattern, textIndex, patIndex+2)
    
  elif pattern[patIndex] == '.' or pattern[patIndex] == text[textIndex]:
    return match_helper(text, pattern, textIndex+1, patIndex+1)
  else:
    print('default false')
    return False
  
print(is_match("abbdbb", "ab*d"))