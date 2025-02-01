class Shape(): # Parent class Shape 
    def __init__(self, sides):
        self.sides = sides
    
    def area(self): # method to calculate area by default
        return 0

class Square(Shape): # Child class Square inheriting from Shape class
    def __init__(self, side_length):
        super().__init__(4)
        self.side_length = side_length

    def area(self): # method to calculate area of square
        return self.side_length ** 2

square = Square(int(input()))
print(square.area())