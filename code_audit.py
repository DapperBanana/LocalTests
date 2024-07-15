letion(id='chatcmpl-9l3x6QohVf5i0bkexoocJAdjFs7y0', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        digit = number % 10
        sum_digits += digit
        number //= 10
    return sum_digits

number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))', role='assistant', function_call=None, tool_calls=None))], created=1721003636, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=66, prompt_tokens=22, total_tokens=88)