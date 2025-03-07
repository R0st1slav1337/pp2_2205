import os

def check_path_access(path):
    print(f"Checking access for path: {path}") # Print the path we are checking
    print(f"Exists: {os.path.exists(path)}") # Check if the path exists
    print(f"Readable: {os.access(path, os.R_OK)}") # Check if the path is readable
    print(f"Writable: {os.access(path, os.W_OK)}") # Check if the path is writable
    print(f"Executable: {os.access(path, os.X_OK)}") # Check if the path is executable

# Example usage
path_to_check = 'C:/Users/rasti/Desktop/pp2_2025/week5/3.py'
check_path_access(path_to_check)