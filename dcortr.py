def first(msg):
    print(msg)

first("Hello")
second = first
second("Bye")



def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result

print(operate(inc, 4))
print(operate(dec, 0))



def make_pretty(func):
    def inner():
        print("Decorated")
        func()
    return inner
"""
def ordinary():
    print("Ordinary")

pretty = make_pretty(ordinary)
pretty()
"""

@make_pretty
def ordinary():
    print("I'm ordinary")

make_pretty(ordinary())

def works_for(func):
    def innr(*args, **kwargs):
        print("I can do anything")
        return func(*args, **kwargs)
    return innr