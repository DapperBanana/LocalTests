letion(id='chatcmpl-9WBPR3S72hAsfihqoUVjzWNuqrAg3', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

n = int(input("Enter the value of n: "))
result = fibonacci(n)
print(f"The {n}th term of the Fibonacci sequence is: {result}")', role='assistant', function_call=None, tool_calls=None))], created=1717457381, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=89, prompt_tokens=24, total_tokens=113)