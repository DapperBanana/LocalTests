letion(id='chatcmpl-8yovtHvlI7ivKo1HNHbo0m8eEH7Vl', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

number = int(input("Enter a number to calculate its factorial: "))
result = factorial(number)
print("Factorial of", number, "is", result)', role='assistant', function_call=None, tool_calls=None))], created=1709506157, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_2b778c6b35', usage=CompletionUsage(completion_tokens=60, prompt_tokens=20, total_tokens=80)