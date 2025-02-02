from itertools import permutations # import permutations from itertools module

def print_permutations(s): # Function to print all permutations of a string
    perms = permutations(s) # get all permutations of the string
    for perm in perms: # loop through all permutations
        print(''.join(perm)) # print the permutation

user_input = input("Enter a string: ")
print_permutations(user_input)
