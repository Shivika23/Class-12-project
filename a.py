class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side) 


rectangle1 = Rectangle(5, 5)
print(f"Rectangle area: {rectangle1.area()}")  

square1 = Square(2)
print(f"Square area: {square1.area()}") 
