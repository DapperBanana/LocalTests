letion(id='chatcmpl-9iTBNov8DRlRGbSPpl8xAiWIrc7q6', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

def get_weather_forecast():
    weather_conditions = ["sunny", "cloudy", "rainy", "snowy"]
    return random.choice(weather_conditions)

def main():
    print("Welcome to the Weather Forecasting System!")
    while True:
        user_input = input("Would you like to get the weather forecast? (y/n): ")
        if user_input.lower() == "y":
            forecast = get_weather_forecast()
            print("The weather forecast for today is:", forecast)
        elif user_input.lower() == "n":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()', role='assistant', function_call=None, tool_calls=None))], created=1720385637, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=153, prompt_tokens=22, total_tokens=175)