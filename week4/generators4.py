def squares(a, b): # Generator function that yields the squares of numbers from a to b
    for i in range(a, b + 1):
        yield i * i

# Input from the user
a = int(input("Enter the start number (a): "))
b = int(input("Enter the end number (b): "))

for square in squares(a, b): # Iterate over the generator object
    print(square)