def unique_elements(input_list): # function to return a list of unique elements
    unique_list = [] # create an empty list to store the unique elements
    for element in input_list: # loop through the input list
        if element not in unique_list: # check if the element is not in the unique list
            unique_list.append(element) # add the element to the unique list
    return unique_list

input_list = [1, 7, 2, 3, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
print(unique_elements(input_list))