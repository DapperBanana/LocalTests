
import random

def get_weather_forecast():
    weather_types = ['sunny', 'cloudy', 'rainy', 'snowy']
    return random.choice(weather_types)

def get_temperature():
    return random.randint(50, 100)

def get_wind_speed():
    return random.randint(0, 20)

def main():
    print("Welcome to the text-based weather forecasting system!")
    
    current_weather = get_weather_forecast()
    current_temperature = get_temperature()
    current_wind_speed = get_wind_speed()
    
    print("Today's weather forecast:")
    print("Weather: " + current_weather)
    print("Temperature: " + str(current_temperature) + " degrees Fahrenheit")
    print("Wind speed: " + str(current_wind_speed) + " mph")

if __name__ == "__main__":
    main()
