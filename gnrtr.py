def abc():
    n = 1
    print("This is 1st statmnt")
    yield n

    n += 1
    print("This is 2nd stmnt")
    yield n

    n += 1
    print("This is 3rd stmnt")
    yield n


for item in abc():
    print(item)

"""
a = abc()   #genertr
next(a)
next(a)
next(a)
"""

d = [2,3,4,5,6]
print(x**2 for x in d)
print([x**2 for x in d])