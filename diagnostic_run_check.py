
import random

def generate_weather():
    weather_options = ['sunny', 'cloudy', 'rainy', 'snowy']
    return random.choice(weather_options)

def get_temperature(weather):
    if weather == 'sunny':
        return random.randint(70, 100)
    elif weather == 'cloudy':
        return random.randint(60, 80)
    elif weather == 'rainy':
        return random.randint(50, 70)
    elif weather == 'snowy':
        return random.randint(0, 32)

def main():
    print("Welcome to the Weather Forecasting System\n")
    
    weather = generate_weather()
    temperature = get_temperature(weather)
    
    print(f"The weather today is {weather} with a temperature of {temperature} degrees Fahrenheit.")

if __name__ == "__main__":
    main()
