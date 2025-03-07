my_list = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# Open the file in write mode
with open('C:/Users/rasti/Desktop/pp2_2025/week6/example.txt', 'w') as file:
    for item in my_list: # Write each item in the list to the file
        file.write(item + '\n')