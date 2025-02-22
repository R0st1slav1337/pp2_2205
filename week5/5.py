import re

def match_string(text):
    # Check if the string starts with 'a' and ends with 'b'
    if re.search(r'a.*b$', text):
        return True
    else:
        return False

# Test the function with some strings
test_strings = ["a", "ab", "aab", "acdb", "aaabbb", "ac", "aabbcc"]
for string in test_strings:
    result = match_string(string)
    print(f"'{string}': {result}")