def generate_squares(N): # generator function that yields the squares of numbers from 1 to N
    for i in range(1, N + 1):
        yield i * i

# Generate the squares of numbers from 1 to N
N = int(input("Enter a number: ")) # input from the user

for square in generate_squares(N): # iterate over the generator object
    print(square)