letion(id='chatcmpl-9hi75EXvDnEXp6qVLd7WNnMjZpJz9', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def even_fibonacci_sum(limit):
    a = 1
    b = 1
    total_sum = 0

    while b <= limit:
        if b % 2 == 0:
            total_sum += b
        a, b = b, a + b

    return total_sum

limit = int(input("Enter the limit: "))
result = even_fibonacci_sum(limit)
print("The sum of all even Fibonacci numbers up to", limit, "is:", result)', role='assistant', function_call=None, tool_calls=None))], created=1720204703, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=103, prompt_tokens=26, total_tokens=129)