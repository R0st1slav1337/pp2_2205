import math

# Function to convert degrees to radians
def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

# Input from the user
degrees = float(input("Enter degrees: "))

# Convert degrees to radians
radians = degrees_to_radians(degrees)

# Print the result
print(f"{degrees} degrees is equal to {radians:.6f} radians")