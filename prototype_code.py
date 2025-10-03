
import random

def get_weather_forecast():
    weather_conditions = ['sunny', 'cloudy', 'rainy', 'snowy']
    return random.choice(weather_conditions)

def main():
    print("Welcome to the Weather Forecasting System!")
    
    while True:
        user_input = input("Enter 'Y' to get the weather forecast or 'N' to quit: ")
        
        if user_input.lower() == 'y':
            forecast = get_weather_forecast()
            print(f"The weather forecast for today is {forecast}.")
        elif user_input.lower() == 'n':
            print("Thank you for using the Weather Forecasting System!")
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    main()
