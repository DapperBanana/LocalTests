
import random

def get_weather_forecast():
    weather_conditions = ['Sunny', 'Cloudy', 'Rainy', 'Snowy']
    random_weather = random.choice(weather_conditions)
    return random_weather

def main():
    print("Welcome to the Weather Forecasting System!")
    
    while True:
        user_input = input("Press enter to get today's weather forecast or type 'exit' to quit: ")
        
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
        else:
            weather_forecast = get_weather_forecast()
            print("Today's weather forecast is:", weather_forecast)

if __name__ == '__main__':
    main()
