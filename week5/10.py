import re

def camel_to_snake(text):
    # Replace capital letters with _ followed by the lowercase letter
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    return result

# Example usage
input_text = "HelloWorldTest"
output_text = camel_to_snake(input_text)
print(input_text, "->", output_text)