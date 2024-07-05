letion(id='chatcmpl-9hiCNunJ4hdd7aXYc6jSck4UIzMmK', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def sum_of_digits(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    return total

number = int(input("Enter a number: "))
print("Sum of digits in", number, "is:", sum_of_digits(number))', role='assistant', function_call=None, tool_calls=None))], created=1720205031, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=57, prompt_tokens=22, total_tokens=79)