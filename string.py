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
def character(str,n):
    first_len = 2
    if first_len>len(str):
        first_len = len(str)
    substr = str[:first_len]

    result = ""
    for i in range(n):
        result = result + substr
    return result

print(character("Deepali",3))
print(character("Hi",3))


#Write a Python program to test whether a passed letter is a vowel or not.
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels

print(is_vowel('a'))
print(is_vowel('ae'))
print(is_vowel('do'))




#replace
oldstring = 'I like Guru99'
newstring = oldstring.replace('like', 'love')
print(newstring)

print(newstring.upper())
print(newstring.lower())
print(newstring.capitalize())


#join
print(":".join("Python3"))


#reverse
a = "12345"  #can use string too
print(''.join(reversed(a)))


#split
a = "Deepali"
print(a.split('l'))



#return 0 before output
print ("%02d" % (1,))
print (str(1).zfill(2))


"""
Summary of various fnctn
Since Python is an object-oriented programming language, many functions can be applied to Python objects. A notable feature of Python is its indenting source statements to make the code easier to read.

Accessing values through slicing - square brackets are used for slicing along with the index or indices to obtain a substring.
In slicing, if range is declared [1:5], it can actually fetch the value from range [1:4]
You can update Python String by re-assigning a variable to another string
Method replace() returns a copy of the string in which the occurrence of old is replaced with new.
Syntax for method replace: oldstring.replace("value to change","value to be replaced")
String operators like [], [ : ], in, Not in, etc. can be applied to concatenate the string, fetching or inserting specific characters into the string, or to check whether certain character exist in the string
Other string operations include
Changing upper and lower case
Join function to glue any character into the string
Reversing string
Split string
"""

"""
Variables are referred to "envelop" or "buckets" where information can be maintained and referenced. Like any other programming language Python also uses a variable to store the information.
Variables can be declared by any name or even alphabets like a, aa, abc etc.
Variables can be re-declared even after you have declared it them for once
In Python you cannot concatenate string with number directly, you need to declare them as a separate variable and thereafter you can concatenate number with string
Declare local variable when you want to use it for current function
Declare Global variable when you want to use the same variable for rest of the program
To delete variable it uses keyword "del"
"""
