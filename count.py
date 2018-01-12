#Write a Python program to count the number 4 in a given list.
def count(no):
    count=0
    for item in no:
        if item == 4:
            count=count+1
    return count

print(count([1,2,4,4,3]))
print(count([1,2,3]))

