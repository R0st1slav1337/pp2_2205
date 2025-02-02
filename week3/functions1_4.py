def is_prime(num): # Function to check if a number is prime or not
    if num < 2: # 0 and 1 are not prime numbers
        return False
    for i in range(2, int(num ** 0.5) + 1): # checking if number is divisible by any number from 2 to square root of number
        if num % i == 0: # if number is divisible by any number from 2 to square root of number, it is not prime
            return False
    return True

def filter_list(numbers): # Function to filter prime numbers from a list
    return list(filter(lambda x: is_prime(x), numbers)) # filtering prime numbers from list

numbers = list(map(int, input("Enter numbers separated by spaces: ").split())) # get the list of numbers from the user
prime_numbers = filter_list(numbers) # filtering prime numbers from list
print("Prime numbers:", prime_numbers) # print the prime numbers

