letion(id='chatcmpl-8zBMMzs1UFIIkCVoKEz4swtbHlFaV', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Function to calculate the nth term of the Fibonacci sequence using memoization
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 1:
        result = n
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    
    memo[n] = result
    return result

# Taking input from the user
n = int(input("Enter the value of n: "))

# Calculating the nth Fibonacci number
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")', role='assistant', function_call=None, tool_calls=None))], created=1709592366, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_2b778c6b35', usage=CompletionUsage(completion_tokens=126, prompt_tokens=24, total_tokens=150)