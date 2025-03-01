import time
import math

num = int(input("Enter a number: "))
milsec = int(input("Enter the number of milliseconds: "))

def sqrt(num, milsec): 
    time.sleep(milsec/1000) # convert milliseconds to seconds
    return math.sqrt(num)

print(f"Square root of {num} after {milsec} milliseconds is {sqrt(num, milsec)}")