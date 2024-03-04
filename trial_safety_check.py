
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Get temperature in Celsius from user
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
