
import random

def get_weather():
    weather = ['Sunny', 'Cloudy', 'Rainy', 'Snowy']
    return random.choice(weather)

def get_temperature():
    return random.randint(50, 100)

def get_wind_speed():
    return random.randint(0, 20)

def get_humidity():
    return random.randint(0, 100)

def main():
    print("Welcome to the text-based weather forecasting system!")
    
    while True:
        user_input = input("Enter 'forecast' to get the weather forecast, or 'exit' to quit: ")
        
        if user_input.lower() == 'forecast':
            weather = get_weather()
            temperature = get_temperature()
            wind_speed = get_wind_speed()
            humidity = get_humidity()
            
            print(f"The weather forecast for today is: {weather}")
            print(f"Temperature: {temperature} F")
            print(f"Wind Speed: {wind_speed} mph")
            print(f"Humidity: {humidity}%")
        
        elif user_input.lower() == 'exit':
            print("Thank you for using the weather forecasting system. Goodbye!")
            break
        
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
