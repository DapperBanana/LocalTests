
# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Read input temperature in Celsius from user
celsius = float(input("Enter temperature in Celsius: "))

# Convert temperature to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Display the converted temperature in Fahrenheit
print("Temperature in Fahrenheit: {:.2f}".format(fahrenheit))
