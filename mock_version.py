
import random

def get_weather_forecast():
    weather_options = ['Sunny', 'Cloudy', 'Rainy', 'Snowy']
    return random.choice(weather_options)

def get_temperature():
    return random.randint(60, 100)

def display_forecast():
    weather = get_weather_forecast()
    temperature = get_temperature()
    
    print("Today's weather forecast:")
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature} F")

def main():
    display_forecast()

if __name__ == "__main__":
    main()
