letion(id='chatcmpl-8wgK4SAskSf1BujGfi58AUoRJ5IWr', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def is_narcissistic_number(num):
    num_str = str(num)
    length = len(num_str)
    total = 0
    
    for digit in num_str:
        total += int(digit) ** length
        
    return total == num

num = int(input("Enter a number: "))
if is_narcissistic_number(num):
    print(f"{num} is a narcissistic number")
else:
    print(f"{num} is not a narcissistic number")', role='assistant', function_call=None, tool_calls=None))], created=1708996404, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_86156a94a0', usage=CompletionUsage(completion_tokens=98, prompt_tokens=23, total_tokens=121)