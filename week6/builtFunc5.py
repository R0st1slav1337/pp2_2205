tup = (2, 5, True, 6, 3, "Meow")

for i in range(0, len(tup)):
    if bool(tup[i]) == True:
        continue
    else:
        print("False")
        exit()

print("True")