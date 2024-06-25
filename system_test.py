letion(id='chatcmpl-9e5tIgN5Hewzue253WBM4yVDMJmWH', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

def generate_weather():
    weather_options = ['sunny', 'rainy', 'cloudy', 'stormy', 'snowy']
    return random.choice(weather_options)

def get_user_input():
    user_input = input("Enter a location to get the weather forecast: ")
    return user_input

def main():
    location = get_user_input()
    weather = generate_weather()
    
    print(f"The weather forecast for {location} is: {weather}")
    
if __name__ == '__main__':
    main()', role='assistant', function_call=None, tool_calls=None))], created=1719342792, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=108, prompt_tokens=22, total_tokens=130)