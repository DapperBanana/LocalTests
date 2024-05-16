letion(id='chatcmpl-9PeMS3Hzwi56BKVAGnIAlj62CMVzX', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def sum_digits(num):
    while num > 9:
        temp_sum = 0
        while num > 0:
            temp_sum += num % 10
            num = num // 10
        num = temp_sum
    return num

num = int(input("Enter a number: "))
print("Sum of digits until it becomes a single-digit number:", sum_digits(num))', role='assistant', function_call=None, tool_calls=None))], created=1715900376, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=80, prompt_tokens=29, total_tokens=109)