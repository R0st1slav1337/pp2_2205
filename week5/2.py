import re

# Define a function that takes a string as input and returns True if the string
# matches the pattern 'ab{2,3}', otherwise returns False
def match_string(text):
    if re.fullmatch(r'ab{2,3}', text):
        return True
    else:
        return False

# Test the function with some strings
test_strings = ["ab", "abb", "abbb", "abbbb", "abbbbb",]
for string in test_strings:
    result = match_string(string)
    print(f"'{string}': {result}")