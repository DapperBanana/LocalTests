letion(id='chatcmpl-9FTeH9pCcSGmJ9aEg1z7U6XtPqmug', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def even_fibonacci_sum(limit):
    fib = [1, 1]
    even_sum = 0
    
    while True:
        next_num = fib[-1] + fib[-2]
        if next_num >= limit:
            break
        fib.append(next_num)
    
    for num in fib:
        if num % 2 == 0:
            even_sum += num
    
    return even_sum

limit = int(input("Enter the limit: "))
result = even_fibonacci_sum(limit)
print(f"The sum of all even Fibonacci numbers up to {limit} is: {result}")', role='assistant', function_call=None, tool_calls=None))], created=1713475917, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_d9767fc5b9', usage=CompletionUsage(completion_tokens=123, prompt_tokens=26, total_tokens=149)