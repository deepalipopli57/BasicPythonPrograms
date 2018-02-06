def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def prcnt(func):
    def inner(*args, **kwargs):
        print("%" * 40)
        func(*args, **kwargs)
        print("%" * 40)
    return inner

@star
@prcnt
def logic(msg):
    print(msg)
logic("Hello")


