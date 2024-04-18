letion(id='chatcmpl-9FTnnnthK7WdLQvGyEi9fi8BTyEFx', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    return total

# Test the function with a sample number
number = 12345
print(f"The sum of digits in {number} is: {sum_of_digits(number)}")', role='assistant', function_call=None, tool_calls=None))], created=1713476507, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_c2295e73ad', usage=CompletionUsage(completion_tokens=78, prompt_tokens=22, total_tokens=100)