letion(id='chatcmpl-9lj0fGLTiv9qr2vF8zvb9A70adFTo', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Function to count the number of digits in 'n'
def count_digits(n):
    count = 0
    while n:
        count += 1
        n //= 10
    return count

# Function to check if 'n' is a vampire number
def is_vampire_number(n):
    fangs = []
    num_digits = count_digits(n)
    
    for i in range(10**(num_digits-1), 10**num_digits):
        if n % i == 0:
            quotient = n // i
            if sorted(str(i) + str(quotient)) == sorted(str(n)) and sorted(str(i)) != ['0'] and sorted(str(quotient)) != ['0']:
                fangs.append((i, quotient))
                
    if not fangs:
        return False
    else:
        for fang in fangs:
            print(f"{n} is a vampire number with fangs {fang[0]} and {fang[1]}")
        return True

# Main program
n = int(input("Enter a number to check if it's a vampire number: "))
if is_vampire_number(n):
    print(f"{n} is a vampire number")
else:
    print(f"{n} is not a vampire number")', role='assistant', function_call=None, tool_calls=None))], created=1721161461, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=263, prompt_tokens=22, total_tokens=285)