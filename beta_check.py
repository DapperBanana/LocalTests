
# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input temperature in Celsius
celsius_temp = float(input("Enter temperature in Celsius: "))

# Convert temperature from Celsius to Fahrenheit
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)

# Display the converted temperature
print(f"Temperature in Fahrenheit: {fahrenheit_temp}")
