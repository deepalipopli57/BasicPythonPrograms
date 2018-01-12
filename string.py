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


#Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.
from 23 https://www.w3resource.com/python-exercises/python-basic-exercise-23.php










