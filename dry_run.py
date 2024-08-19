
import random

def weather_forecast():
    weather_conditions = ['sunny', 'cloudy', 'rainy', 'stormy', 'snowy']
    temperature = random.randint(-10, 40)
    
    current_weather = random.choice(weather_conditions)
    
    print("Today's weather forecast:")
    print(f"Weather conditions: {current_weather}")
    print(f"Temperature: {temperature} degrees Celsius")

weather_forecast()
