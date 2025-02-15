def numbers_in_reverse_order(n): # Generator function that yields the numbers from n to 0
    for i in range(n, 0-1, -1):
        yield i 

n = int(input("Enter a number: ")) # Input from the user

for number in numbers_in_reverse_order(n): # Iterate over the generator object
    print(number)