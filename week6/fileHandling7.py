def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src: # Open the source file in read mode
            content = src.read() # Read the content of the source file
        with open(destination_file, 'w') as dest: # Open the destination file in write mode
            dest.write(content) # Write the content to the destination file
        print(f"Contents copied from {source_file} to {destination_file} successfully.")
    except FileNotFoundError: # Handle the case when the source file does not exist
        print(f"The file {source_file} does not exist.")
    except Exception as e: # Handle any other exceptions
        print(f"An error occurred: {e}")

# Example usage
source_file = 'C:/Users/rasti/Desktop/pp2_2025/week6/source.txt'
destination_file = 'C:/Users/rasti/Desktop/pp2_2025/week6/destination.txt'
copy_file(source_file, destination_file)