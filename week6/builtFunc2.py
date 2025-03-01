text = str(input("Enter a string: "))

count1 = 0 # lowercase count
count2 = 0 # uppercase count

for i in text:
    if i.islower():
        count1 += 1
    elif i.isupper():
        count2 += 1

print("The number of lowercase letters is: ", count1)
print("The number of uppercase letters is: ", count2)