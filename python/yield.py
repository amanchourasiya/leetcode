def foo():
    yield 1 
    yield 2
    yield 3


def p():
    
    for val in foo():
        print(val)

print(p())
l = [1,2,3]
l1 = [1,2,3]


if l is l1:
    print("l=l1")
else:
    print('not')
