def generate_even_numbers(n): # Generator function that yields the even numbers from 0 to n
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

# Input from the user
n = int(input("Enter a number: "))

even_numbers_list = [] # Empty list to store the even numbers
for num in generate_even_numbers(n): # Iterate over the generator object
    even_numbers_list.append(str(num)) # Convert the number to a string and append it to the list
even_numbers = ", ".join(even_numbers_list) # Join the numbers with commas

# Print the result
print(even_numbers)