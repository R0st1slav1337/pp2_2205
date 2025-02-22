import re

def split_string(text):
    # Split the string at every capital letter
    return re.split(r'(?=[A-Z])', text)

# Example usage
input_text = "helloWorldTest"
output_text = split_string(input_text)
print(input_text, "->", output_text)