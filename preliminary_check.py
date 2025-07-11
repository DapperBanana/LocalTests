
import random

def get_weather():
    weather = ['Sunny', 'Cloudy', 'Rainy', 'Snowy']
    return random.choice(weather)

def get_temperature():
    return random.randint(-10, 40)

def get_wind_speed():
    return random.randint(0, 30)

def get_humidity():
    return random.randint(0, 100)

def main():
    print("--- Weather Forecasting System ---")
    print("Today's Weather: " + get_weather())
    print("Temperature: " + str(get_temperature()) + "°C")
    print("Wind Speed: " + str(get_wind_speed()) + " km/h")
    print("Humidity: " + str(get_humidity()) + "%")

if __name__ == "__main__":
    main()
