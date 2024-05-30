letion(id='chatcmpl-9UjYzeRlK4YgrgDNj3clSWr9tekO6', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")', role='assistant', function_call=None, tool_calls=None))], created=1717112013, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=55, prompt_tokens=20, total_tokens=75)