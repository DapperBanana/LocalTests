letion(id='chatcmpl-9GvXWFUf9RRt2XxNCxgmKhIHQwPkM', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

# Take user input
num = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")', role='assistant', function_call=None, tool_calls=None))], created=1713821458, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_c2295e73ad', usage=CompletionUsage(completion_tokens=140, prompt_tokens=19, total_tokens=159)