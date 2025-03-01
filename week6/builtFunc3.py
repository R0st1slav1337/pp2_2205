text = str(input("Enter a string: "))

text = text.lower().replace(" ", "") # convert to lowercase and remove spaces

if text == text[::-1]: # check if the string is a palindrome
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")