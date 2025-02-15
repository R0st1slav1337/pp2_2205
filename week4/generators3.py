def divisible_by_3_and_4(n): # Generator function that yields the numbers divisible by 3 and 4 from 0 to n
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0: # Check if the number is divisible by 3 and 4
            yield i

n = int(input("Enter a number: ")) # Input from the user

for num in divisible_by_3_and_4(n): # Iterate over the generator object
    print(num)