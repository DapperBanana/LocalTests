letion(id='chatcmpl-9GvVLfkifEYU4c4KkWgJ3RwZ6UGLX', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def trapezoid_area(base1, base2, height):
    area = ((base1 + base2) / 2) * height
    return area

base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))
height = float(input("Enter the height of the trapezoid: "))

print("The area of the trapezoid is:", trapezoid_area(base1, base2, height))', role='assistant', function_call=None, tool_calls=None))], created=1713821323, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_c2295e73ad', usage=CompletionUsage(completion_tokens=107, prompt_tokens=22, total_tokens=129)