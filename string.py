#Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

def new_str(str):
    if len(str)>=2 and str[:2]=="Is":
        return str
    return "Is" + str

print(new_str("H"))
print(new_str("Is"))


#Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def repeat(str,n):
    result = ""
    for i in range(n):
        result=result+str
    return result

print(repeat("Hi",2))
print(repeat("Deepi",4))

