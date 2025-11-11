
import random

def get_weather_forecast():
    weather = ['sunny', 'cloudy', 'rainy', 'stormy', 'snowy']
    return random.choice(weather)

def main():
    print("Welcome to the Basic Weather Forecast System!")
    
    while True:
        user_input = input("Enter 'forecast' to get the weather forecast or 'exit' to quit: ")
        
        if user_input.lower() == 'forecast':
            forecast = get_weather_forecast()
            print(f"The weather forecast for today is: {forecast}")
        elif user_input.lower() == 'exit':
            print("Thank you for using the Weather Forecast System. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
