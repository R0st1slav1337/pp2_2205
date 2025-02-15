import math

def polygon_area(n, s): # Function to calculate the area of a regular polygon
    return (n * s ** 2) / (4 * math.tan(math.pi / n))
    # The formula for the area of a regular polygon is (n * s^2) / (4 * tan(pi / n))

# Input from the user
n = int(input("Enter the number of sides: "))
s = float(input("Enter the length of each side: "))

# Calculate the area
area = polygon_area(n, s)

# Print the result
print(f"The area of the polygon with {n} sides, each of length {s}, is {area:.1f}")