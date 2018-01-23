#Enter some values in list & tuple
print([input("Enter some items in list : ")])
print(input("Enter some values in tuple : ") )

colors_list = ["Red","Green","White" ,"Black"]
print(colors_list[0], colors_list[-1])


#Write a Python program to check whether a specified value is contained in a group of values.
def check_list(all_data, no):
    for value in all_data:
        if no == value:
            return True
    return False

print(check_list([1,2,3],3))
print(check_list([1,2,3],4))


#Write a Python program to create a histogram from a given list of integers.
def histogram(items):
    for n in items:
        output=''
        times=n
        while(times>0):
            output+= '*'
            times=times-1
        print(output)

histogram([2,4,6,4,2])


#tuple packing/unpacking
x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(emp)
print(profile)


#Compare tuple
a=(5,6)
b=(6,4)
if (a>b):print( "a is bigger")
else: print ("b is bigger")


# ===================dictionary======================
a = {'x':100, 'y':200}
b = a.items()
print(b)

x = ("a", "b","c", "d", "e")
print (x[2:4])


#copying dictionary
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
studentX=Boys.copy()
studentY=Girls.copy()
print (studentX)
print (studentY)



#updating dictionary
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Dict.update({"Sarah":9})
print (Dict)




"""
Python has tuple assignment feature which enables you to assign more than one variable at a time.

Packing and Unpacking of Tuples
In packing, we place value into a new tuple while in unpacking we extract those values back into variables.
A comparison operator in Python can work with tuples.
Using tuples as keys in dictionaries
Tuples are hashable, and list are not
We must use tuple as the key if we need to create a composite key to use in a dictionary
Dictionary can return the list of tuples by calling items, where each tuple is a key value pair
Tuples are immutable and cannot be deleted, but deleting tuple entirely is possible by using the keyword "del."
To fetch specific sets of sub-elements from tuple or list, we use this unique function called slicing
"""