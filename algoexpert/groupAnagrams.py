def groupAnagrams(words):
    
    table = {}
    for word in words:
        if word in table:
            table[''.join(sorted(word))].append(word)
        else:
            table[''.join(sorted(word))] = [word]

    return table.values