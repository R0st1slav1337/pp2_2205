def parallelogram_area(a, b): # Function to calculate the area of a parallelogram
    return a * b

a = float(input("Enter the length of the base: ")) # Input from the user
b = float(input("Enter the height: "))

# Calculate the area
area = parallelogram_area(a, b)
print(f"The area of the parallelogram is: {area:.1f}")