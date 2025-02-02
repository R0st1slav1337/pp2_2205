def spy_game(nums):
    code = [0, 0, 7]  # The sequence to look for
    for num in nums:
        if num == code[0]:  # Check if the current number matches the first number in the code
            code.pop(0)  # Remove the first number from the code
        if not code:  # If the code list is empty, the sequence has been found
            return True
    return False  # Return False if the sequence was not found

print(spy_game([1, 2, 4, 0, 0, 7, 5])) 
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  