
import random

# List of possible weather conditions
weather_conditions = ["sunny", "cloudy", "rainy", "stormy"]

# Function to generate random weather forecast
def generate_weather_forecast():
    return random.choice(weather_conditions)

# Main program loop
while True:
    user_input = input("Enter 'forecast' to get the weather forecast, or 'exit' to quit: ")

    if user_input == "forecast":
        weather_forecast = generate_weather_forecast()
        print("The weather forecast for today is:", weather_forecast)
    elif user_input == "exit":
        print("Exiting weather forecasting system...")
        break
    else:
        print("Invalid input. Please try again.")
