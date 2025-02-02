def FahrenheitToCelsius(F): # Function to convert Fahrenheit to Celsius
    C = (F - 32) * (5 / 9) 
    return C

temperature = FahrenheitToCelsius(float(input("Enter the temperature in Fahrenheit: "))) # get the temperature in Fahrenheit from the user

print(f"{temperature:.1f} Celsius")