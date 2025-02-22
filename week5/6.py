import re

def replace_characters(text):
    # Replace space, comma, or dot with a colon
    result = re.sub(r'[ ,.]', ':', text)
    return result

# Example usage
input_text = "Hello, world! This is a test."
output_text = replace_characters(input_text)
print(output_text)