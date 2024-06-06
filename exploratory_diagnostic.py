letion(id='chatcmpl-9XFJ9pNLfREEI8dvosJJmyqutGoFi', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def sum_of_digits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num = num // 10
    return sum

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("The sum of digits in the number is:", result)', role='assistant', function_call=None, tool_calls=None))], created=1717710695, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=74, prompt_tokens=22, total_tokens=96)