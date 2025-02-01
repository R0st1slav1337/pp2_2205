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

class Triangle(Shape): # Child class Triangle inheriting from Shape class
    def __init__(self, length, width):
        super().__init__(3)
        self.length = length
        self.width = width

    def area(self): # method to calculate area of triangle
        return (self.length * self.width)/2

square = Square(int(input("Enter side length of square: ")))
print(square.area())
triangle = Triangle(int(input("Enter length of triangle: ")), int(input("Enter width of triangle: ")))
print(triangle.area())