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