def solve(numheads, numlegs): # define a function with two arguments
    for i in range(numheads+1): # i is the number of chickens
        j = numheads - i # j is the number of rabbits
        if 2*i + 4*j == numlegs: # 2 legs for chickens, 4 legs for rabbits
            return f"Number of chickens is {i} and rabbits is {j}" # return the number of chickens and rabbits
    return "No solutions" # if no solution is found

numheads = 35 
numlegs = 94 
solutions = solve(numheads, numlegs)
print(solutions)