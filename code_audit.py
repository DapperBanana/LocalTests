
import random

def get_weather():
    weather_conditions = ['sunny', 'cloudy', 'rainy', 'snowy']
    return random.choice(weather_conditions)

def get_temperature():
    return random.randint(-10, 40)

def main():
    print("Welcome to the text-based weather forecasting system!")
    
    while True:
        user_input = input("Enter 'forecast' to get the weather forecast, or 'exit' to quit: ")
        
        if user_input == 'forecast':
            weather = get_weather()
            temperature = get_temperature()
            print(f"The weather forecast is {weather} with a temperature of {temperature} degrees.")
        elif user_input == 'exit':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
