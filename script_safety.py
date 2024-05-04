letion(id='chatcmpl-9LG1jAHWIJuNdsIKw79DpVzou9JKs', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    return fib_sequence

n = int(input("Enter the number of terms: "))

fib_sequence = fibonacci(n)

print("Fibonacci sequence up to", n, "terms:")
print(fib_sequence)', role='assistant', function_call=None, tool_calls=None))], created=1714853523, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3b956da36b', usage=CompletionUsage(completion_tokens=93, prompt_tokens=24, total_tokens=117)