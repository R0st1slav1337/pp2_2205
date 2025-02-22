import re

# Define a function that takes a string as input and returns True if the string
# matches the pattern 'a*b*', otherwise returns False
def match_string(text):
    if re.fullmatch(r'a*b*', text):
        return True
    else:
        return False

# Test the function with some strings
test_strings = ["a", "ab", "aab", "b", "aaabbb", "ac", "aabbcc"]
for string in test_strings:
    result = match_string(string)
    print(f"'{string}': {result}")
