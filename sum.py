#Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
def sum(a,b,c):
    add = a+b+c
    if a==b==c:
        add=add*3
    return add

print(sum(1,2,3))
print(sum(2,2,2))


"""
Sample value of n is 5
Expected Result : 615
"""
n = int(input("Enter a no : "))
n1 = int("%s" %n)
n2 = int("%s%s" %(n,n))
n3 = int("%s%s%s" %(n,n,n))
print("O/p of n+nn+nnn of n1.n2,n3 : ", (n1+n2+n3))
