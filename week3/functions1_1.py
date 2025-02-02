def GramToOunce(gram): # convert gram to ounce
    return gram * 28.3495231

ounce = GramToOunce(float(input("Enter the number of gramms: "))) # get the number of gramms from the user

print(f"{ounce:.2f} ounces") # print the result with 2 decimal places