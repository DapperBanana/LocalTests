
import random

def weather_forecast():
    weather_conditions = ["sunny", "cloudy", "rainy", "stormy", "snowy"]
    forecast = random.choice(weather_conditions)
    return forecast

def main():
    print("Welcome to the Weather Forecast System!")
    print("Fetching weather data...\n")
    
    current_weather = weather_forecast()
    
    print("The current weather forecast is:", current_weather)
    
if __name__ == "__main__":
    main()
