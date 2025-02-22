import re

def find_sequences(text):
    # Matches sequences of lowercase letters joined with an underscore
    matches = re.findall(r'\b[a-z]+_[a-z]+\b', text)
    return matches

# Example usage
text = "Hello_world test_case example_228 not_matching this_one also_not1337"
result = find_sequences(text)
print("Matches:", result)
