#Write a Python program to test whether a number is within 100 of 1000 or 2000
def thous(no):
    return ((abs(1000-no)<=100) or (abs(2000-no)<=100))

print(thous(1000))
print(thous(900))
print(thous(21000))

# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
print(abs.__doc__)
