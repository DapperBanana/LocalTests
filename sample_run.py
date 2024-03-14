
import random

def get_weather_forecast():
    weather_conditions = ['Sunny', 'Cloudy', 'Rainy', 'Stormy']
    return random.choice(weather_conditions)

def get_temperature():
    return random.randint(30, 100)

def get_wind_speed():
    return random.randint(0, 30)

def main():
    print("Welcome to the Basic Weather Forecasting System")
    print("Today's weather forecast:")
    forecast = get_weather_forecast()
    temperature = get_temperature()
    wind_speed = get_wind_speed()
    print(f"Weather: {forecast}")
    print(f"Temperature: {temperature}°F")
    print(f"Wind Speed: {wind_speed} mph")

if __name__ == "__main__":
    main()
