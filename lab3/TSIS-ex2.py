class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

k=int(input("Write the length of square:"))

square = Square(k)
print("Area of square with length :",k," is ", square.area())
