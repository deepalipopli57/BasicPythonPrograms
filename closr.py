def print_msg(msg):
# outer fnctn
    def message():
        #nested fnctn
        print(msg)
    message()
print_msg("Hii")
print_msg("Byee")



def multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

a = multiplier_of(3)
print(a(6))