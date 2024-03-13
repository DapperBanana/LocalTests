letion(id='chatcmpl-927Sm6ESkX9aGa8Wp5pbPBLTAJM7P', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    prime_sum = 0
    for i in range(start, end+1):
        if is_prime(i):
            prime_sum += i
    return prime_sum

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

result = sum_of_primes(start, end)
print(f"The sum of prime numbers in the range ({start}, {end}) is: {result}")', role='assistant', function_call=None, tool_calls=None))], created=1710292372, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_4f0b692a78', usage=CompletionUsage(completion_tokens=155, prompt_tokens=24, total_tokens=179)