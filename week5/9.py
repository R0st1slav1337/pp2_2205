import re

def insert_spaces(text):
    # Insert spaces before capital letters
    return re.sub(r'([A-Z])', r' \1', text)

# Example usage
input_text = "helloWorldTest"
output_text = insert_spaces(input_text)
print(input_text, "->", output_text)