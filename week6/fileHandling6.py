import string

for letter in string.ascii_uppercase: # Loop through the uppercase letters
    with open(f"{letter}.txt", "w") as file: # Open the file in write mode
        file.write(f"This is file {letter}.txt") # Write the content to the file