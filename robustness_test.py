
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input temperature in Celsius
celsius_temp = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)

print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")
