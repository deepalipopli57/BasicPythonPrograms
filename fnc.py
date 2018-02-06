#Usings args
def a(*args):
    for x in enumerate(args):       #enumerate will return the index & member name
        print("Fnction", x)

a([1,2,3],[4,5,6])
a([1,2,3])

#Putting *args and/or **kwargs as the last items in our function definition's argument list allows that function to accept an arbitrary number of anonymous and/or keyword arguments.
#Those arguments are called Keyword Arguments. Actually, they are place holders for multiple arguments, and they are useful especially when we need to pass a different number of arguments each time we call the function.
#We may want to use *args when we're not sure how many arguments might be passed to our function, i.e. it allows us to pass an arbitrary number of arguments to our function.


#Using kwargs
#The ** is similar but it only works for keyword arguments. In other words, it collects them into a new dictionary. Actually, ** allows us to convert from keywords to dictionaries:
def b(**kwargs):
    print(kwargs)
b(a=10, b=50)



#while in fnctn
def main():
    x = 0
    while(x<4):
        print(x)
        x=x+1
if __name__ == main():
    main()


#for loop in fnctn
def main():
    for x in range(1,7):
        print(x)

if __name__ == main():
    main()


#for loop fnctn in string
def month():
    Months = ["Jan", "Feb", "Mar"]
    for month in Months:
        print(month)
if __name__ == month():
    month()


#break in for loop using function
def main():
    for x in range(10, 20):
        if (x == 15): break
        print(x)

if __name__ == "__main__":
    main()


#continue in function
def main():
    for x in range(10, 20):
        if (x % 5 == 0): continue
        print(x)

if __name__ == "__main__":
    main()


#enumerate function for for loop   (enumerate will return index)
def main():
    Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
    for i, m in enumerate(Months):
        print(i, m)


if __name__ == "__main__":
    main()

# return new list
def chng(lst):
    lst = [1,2,3,4]
    print ("Values are : ", lst)
    return


lst = [23,4,5,6,7]
chng(lst)
print("New list : ", lst)


#
def details(age):
    try:
        if age < 20:
            print("Young")
    except:
        if age >= 26:
            print("Mid")
    finally:
        print("Aged")

details(0)


#
def avrg(first, *args):
    return (first + sum(args) )

print(avrg(2,3,6,7))

#
def a():
    return 1,2,4

a,b,c = a()
print(a,b,c)




"""
Function in Python is a piece of reusable code that is used to perform single, related action. In this article, we will see

Function defined by the def statement
The code block within every function starts with a colon (:) and should be indented (space)
Any arguments or input parameters should be placed within these parentheses, etc.
At least one indent should be left before the code after declaring function
Same indent style should be maintained throughout the code within def function
For best practices three or four indents are considered best before the statement
You can use the "return" command to return values to the function call.
Python will print a random value like (0x021B2D30) when the argument is not supplied to the calling function. Example "print function."
On the calling side, it is an argument and on the function side it is a parameter
Default value in argument - When we supply only one argument while calling multiply function or any other function, Python assigns the other argument by default
Python enables you to reverse the order of the argument as well

"""