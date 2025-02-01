def is_prime(num): # Function to check if a number is prime or not
    if num < 2: # 0 and 1 are not prime numbers
        return False
    for i in range(2, int(num ** 0.5) + 1): # checking if number is divisible by any number from 2 to square root of number
        if num % i == 0: # if number is divisible by any number from 2 to square root of number, it is not prime
            return False
    return True

def filter_list(arr): # Function to filter prime numbers from a list
    arr = list(filter(lambda x: is_prime(x), arr)) # filtering prime numbers from list
    print(arr)

n = 100
arr1 = []
for i in range(1, n): # creating list of numbers from 1 to n
    arr1.append(i)

filter_list(arr1) # filtering prime numbers from list