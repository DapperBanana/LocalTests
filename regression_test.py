letion(id='chatcmpl-9NQdoeHNKoz8C1zhUVs5J3k5Gb8RO', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def sum_of_digits(num):
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))', role='assistant', function_call=None, tool_calls=None))], created=1715370980, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=51, prompt_tokens=22, total_tokens=73)