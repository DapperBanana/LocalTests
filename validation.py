
import random

def generate_weather_forecast():
    weather_conditions = ['Sunny', 'Partly cloudy', 'Cloudy', 'Rainy', 'Thunderstorm']
    return random.choice(weather_conditions)

def main():
    print("Welcome to the Text-Based Weather Forecasting System!")
    
    while True:
        user_input = input("Enter 'forecast' to get the weather forecast or 'exit' to quit: ")
        
        if user_input.lower() == 'forecast':
            weather_forecast = generate_weather_forecast()
            print(f"The weather forecast for today is: {weather_forecast}")
        elif user_input.lower() == 'exit':
            print("Exiting the program. Thank you for using the Weather Forecasting System!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
