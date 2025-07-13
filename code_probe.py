
import random

def get_weather_forecast():
    weather_conditions = ['sunny', 'cloudy', 'rainy', 'stormy', 'snowy']
    return random.choice(weather_conditions)

def main():
    print("Welcome to the Text-based Weather Forecasting System!")
    location = input("Enter your location: ")
    
    print(f"Fetching weather forecast for {location}...")
    
    weather_forecast = get_weather_forecast()
    
    print(f"The weather forecast for {location} is: {weather_forecast}")

if __name__ == "__main__":
    main()
