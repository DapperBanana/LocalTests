letion(id='chatcmpl-9FTuRrglWph0RWLlm4nWCXfwNGAT9', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Function to check if a number is a perfect digital invariant
def is_perfect_digital_invariant(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Calculate the sum of digits raised to their respective powers
    num_sum = sum(int(digit)**i for i, digit in enumerate(num_str, 1))
    
    # Check if the sum is equal to the original number
    return num_sum == num

# Take user input
num = int(input("Enter a number: "))

# Check if the number is a perfect digital invariant
if is_perfect_digital_invariant(num):
    print(f"{num} is a perfect digital invariant.")
else:
    print(f"{num} is not a perfect digital invariant.")', role='assistant', function_call=None, tool_calls=None))], created=1713476919, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_d9767fc5b9', usage=CompletionUsage(completion_tokens=160, prompt_tokens=23, total_tokens=183)