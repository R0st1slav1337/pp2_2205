# re.fullmatch(r'[a-z]+(_[a-z]+)*', text) - snake case
# re.fullmatch(r'[a-z]+([A-Z][a-z]*)*', text) - CamelCase
import re

def replace_case(text):
    if re.fullmatch(r'[a-z]+(_[a-z]+)*', text):
        result = re.sub(r'(_[a-z])', lambda x: x.group(1).upper(), text)
        result = re.sub(r'_', '', result)
        return result
    
input_text = "hello_world_test"
output_text = replace_case(input_text)
print(input_text, "->", output_text)