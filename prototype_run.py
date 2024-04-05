letion(id='chatcmpl-9AkXIPwEqjssAzXmV9BhWQObieCVd', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

weather_options = ["sunny", "cloudy", "rainy", "snowy"]

def generate_weather():
    return random.choice(weather_options)

def main():
    print("Welcome to the Weather Forecasting System!")
    
    while True:
        user_input = input("Enter 'forecast' to get weather forecast or 'exit' to quit: ")
        
        if user_input == 'forecast':
            weather = generate_weather()
            print("The weather today is", weather)
            
        elif user_input == 'exit':
            print("Goodbye!")
            break
        
        else:
            print("Invalid input. Please try again.")

if __name__ == '__main__':
    main()', role='assistant', function_call=None, tool_calls=None))], created=1712349192, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_b28b39ffa8', usage=CompletionUsage(completion_tokens=141, prompt_tokens=22, total_tokens=163)