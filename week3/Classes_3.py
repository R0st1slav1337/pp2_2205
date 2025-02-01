class Point(): # Class definition for Point
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self): # Method to show coordinates of point
        print(f"Coordinates of point are ({self.x}, {self.y})")

    def move(self, x, y): # Method to move point by x and y
        self.x += x
        self.y += y

    def dist(self, point): # Method to calculate distance between two points
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

point = Point(int(input("Enter x coordinate: ")), int(input("Enter y coordinate: "))) # Creating object of Point class
point.show() # Showing coordinates of point

point.move(int(input("Enter x to move: ")), int(input("Enter y to move: "))) # Moving point by x and y
print(f"New coordinates after moving are: ({point.x}, {point.y})") # Showing new coordinates of point

point2 = Point(int(input("Enter x coordinate: ")), int(input("Enter y coordinate: "))) # Creating another object of Point class

distance = point.dist(point2) # Calculating distance between two points
print(f"Distance between two points is {distance}") # Showing distance between two points