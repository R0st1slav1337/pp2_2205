def has_33(nums): 
    for i in range(len(nums)-1): # loop through the list of numbers
        if nums[i] == 3 and nums[i+1] == 3: # check if the current number and the next number are 3
            print(True) # print True if the condition is met
            return True 
    print(False) # print False if the condition is not met
    return False

has_33([1, 3, 3])
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3]) 