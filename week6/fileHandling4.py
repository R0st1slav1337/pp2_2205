def count_lines(file_path):
    try: 
        with open(file_path, 'r') as file: # Open the file in read mode
            lines = file.readlines() # Read all lines
            return len(lines) 
    except FileNotFoundError: # Handle the case when the file does not exist
        return "File not found."

# Example usage
file_path = 'C:/Users/rasti/Desktop/pp2_2025/week6/example.txt' 
print(f"Number of lines in the file: {count_lines(file_path)}")