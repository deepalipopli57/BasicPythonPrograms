class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def getData(self):
        print(self.real, "+",  self.imag,"i")


c1 = ComplexNumber(3,4)
c1.getData()