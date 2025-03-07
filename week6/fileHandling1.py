import os

def list_directories_files(path): # Function to list directories and files in a given path
    directories = []
    files = []
    all_items = []

    for item in os.listdir(path): # Iterate over all items in the given path
        item_path = os.path.join(path, item) # Get the full path of the item
        if os.path.isdir(item_path): # Check if the item is a directory
            directories.append(item)
        elif os.path.isfile(item_path): # Check if the item is a file
            files.append(item)
        all_items.append(item) 

    print("Directories:")
    for directory in directories:
        print(directory)

    print("\nFiles:")
    for file in files:
        print(file)

    print("\nAll items:")
    for item in all_items:
        print(item)

if __name__ == "__main__": 
    specified_path = 'C:/Users/rasti/Desktop/pp2_2025'
    list_directories_files(specified_path)