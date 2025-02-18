
import random

def get_weather_forecast():
    forecasts = ["sunny", "cloudy", "rainy", "stormy", "snowy"]
    return random.choice(forecasts)

def weather_forecasting_system():
    print("Welcome to the weather forecasting system!")
    while True:
        user_input = input("Enter 'predict' to get the weather forecast or 'exit' to stop: ")
        if user_input.lower() == 'predict':
            weather_forecast = get_weather_forecast()
            print(f"The weather forecast for today is: {weather_forecast}")
        elif user_input.lower() == 'exit':
            print("Thank you for using the weather forecasting system. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'predict' or 'exit'.")

weather_forecasting_system()
