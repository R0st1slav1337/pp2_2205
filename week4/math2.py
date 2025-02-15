def trapezoid_area(base1, base2, height): # Function to calculate the area of a trapezoid
    return 0.5 * (base1 + base2) * height

height = float(input("Enter the height: ")) # Input from the user
base1 = float(input("Enter the length of the first base: ")) 
base2 = float(input("Enter the length of the second base: "))

area = trapezoid_area(base1, base2, height)
print(f"The area of the trapezoid is: {area:.1f}") # Print the result