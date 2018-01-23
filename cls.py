class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    print("Initial prog")

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * (self.x + self.y)

rectangle = Shape(100,45)
print (rectangle.area())
print (Shape(2,3).perimeter())


class DoubleSquare:
    def __init__(self, x, y):
        self.x = 2*x
        self.y = y

    def perimeter(self):
        return self.x + self.y

print(DoubleSquare(1,2).perimeter())


#class
class myClass():
    def method1(self):
        print("Good")

    def method2(self):
        print("V. Good")

def main():
    c = myClass()
    c.method1()
    c.method2()

if __name__=="__main()__":
    main()