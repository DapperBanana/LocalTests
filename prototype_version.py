
import random

# Define possible weather conditions
weather_conditions = ['Sunny', 'Cloudy', 'Rainy', 'Stormy']

# Define probability distribution for each weather condition
weather_probabilities = [0.4, 0.3, 0.2, 0.1]

# Generate random weather condition based on probabilities
weather = random.choices(weather_conditions, weather_probabilities)[0]

# Define temperature range for each weather condition
temperature_ranges = {
    'Sunny': (70, 90),
    'Cloudy': (60, 80),
    'Rainy': (50, 70),
    'Stormy': (40, 60)
}

# Generate random temperature within range for the chosen weather condition
temperature = random.randint(temperature_ranges[weather][0], temperature_ranges[weather][1])

# Display weather forecast
print("Weather Forecast:")
print(f"Condition: {weather}")
print(f"Temperature: {temperature}F")
