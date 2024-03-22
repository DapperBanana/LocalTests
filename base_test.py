letion(id='chatcmpl-95dCQUE7dp2un30FYvvXet4PVEKSq', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Function to check if a given number is a narcissistic number
def is_narcissistic_number(num):
    num_str = str(num)
    n = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** n
        
    if total == num:
        return True
    else:
        return False

# Main program
num = int(input("Enter a number: "))
if is_narcissistic_number(num):
    print(f"{num} is a narcissistic number")
else:
    print(f"{num} is not a narcissistic number")', role='assistant', function_call=None, tool_calls=None))], created=1711129350, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3bc1b5746c', usage=CompletionUsage(completion_tokens=127, prompt_tokens=23, total_tokens=150)