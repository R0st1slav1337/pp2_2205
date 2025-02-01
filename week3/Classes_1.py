class InputString():
    def __init__(self, string): # creating string 
        self.string = string
    
    def __str__(self): # returning string in upper case
        return self.string.upper()
    
str_1 = InputString(str(input()))
print(str_1)