a = [2,4,6,78]
b = iter(a)
print(next(b))

print(b.__next__())
print(b.__next__())