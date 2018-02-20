class Animals:
    def eat(self):
       print("Eating,..")
class Birds(Animals):
    def brd(self):
        print("B'ful,....")


obj = Birds()
obj.eat()
obj.brd()