letion(id='chatcmpl-9h3xXtJbMt6wHAkutu29EnBsUn8kg', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Using memoization to calculate the nth term of the Fibonacci sequence

fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]

    if n <= 1:
        return n
    else:
        fib_cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib_cache[n]

n = int(input("Enter the value of n: "))
result = fibonacci(n)
print(f"The {n}th term of the Fibonacci sequence is: {result}")', role='assistant', function_call=None, tool_calls=None))], created=1720050351, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=106, prompt_tokens=24, total_tokens=130)