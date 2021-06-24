dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'x':1, 'y':2, 'z':3}

# when I do comparison of values , it doesn't work

print(dict1.values())
print(dict2.values())

if dict1.values() == dict2.values():
    print("Equal")
else:
    print("Not Equal")