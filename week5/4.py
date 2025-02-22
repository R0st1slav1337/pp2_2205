import re

def find_sequences(text):
    # Matches sequences of uppercase and lowercase letters
    matches = re.findall(r'[A-Z][a-z]+', text)
    return matches

# Example usage
text = "Hello World! This is a Test String with Uppercase and lowercase Letters."
sequences = find_sequences(text)
print("Matches:", sequences)