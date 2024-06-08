letion(id='chatcmpl-9XvYMw8Wlj0w726XBLVx1Dxyl6rqY', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def fibonacci(n):
    sequence = []
    
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

n = int(input("Enter the number of terms: "))
fibonacci_sequence = fibonacci(n)
print(f"Fibonacci sequence up to {n} terms: {fibonacci_sequence}")', role='assistant', function_call=None, tool_calls=None))], created=1717873086, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=84, prompt_tokens=24, total_tokens=108)