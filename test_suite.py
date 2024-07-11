letion(id='chatcmpl-9jsrJfoRZKU9M1KNIlVY5J7NdvX3I', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def sum_of_digits(num):
    total = 0
    
    while num > 0:
        total += num % 10
        num = num // 10
        
    return total

number = int(input("Enter a number: "))
print("The sum of digits in the number is:", sum_of_digits(number))', role='assistant', function_call=None, tool_calls=None))], created=1720722665, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=65, prompt_tokens=22, total_tokens=87)