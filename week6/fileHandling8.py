import os

def delete_file(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # Check if the file is accessible
        if os.access(file_path, os.W_OK):
            try:
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted successfully.")
            except Exception as e: # Handle any exceptions that occur while deleting the file
                print(f"Error occurred while deleting the file: {e}")
        else:
            print(f"File '{file_path}' is not accessible.")
    else:
        print(f"File '{file_path}' does not exist.")

# Example usage
file_path = "C:/Users/rasti/Desktop/pp2_2025/week6/fileToDelete.txt"
delete_file(file_path)