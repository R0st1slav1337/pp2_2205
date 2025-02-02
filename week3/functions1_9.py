def Volume(r): # function to calculate the volume of a sphere
    return 4/3 * 3.14159 * r**3 # return the volume of the sphere

result = Volume(float(input("Enter the radius of the sphere: ")))
print(f"The volume of the sphere is {result:.2f}")