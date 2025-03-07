import os

def check_path(path):
    if os.path.exists(path): # Check if the path exists
        print(f"The path '{path}' exists.")
        directory, filename = os.path.split(path) # Split the path into directory and filename
        print(f"Directory: {directory}") # Print the directory
        print(f"Filename: {filename}") # Print the filename
    else:
        print(f"The path '{path}' does not exist.")

# Example usage
path = 'C:/Users/rasti/Desktop/pp2_2025/week1/3.py'
check_path(path)