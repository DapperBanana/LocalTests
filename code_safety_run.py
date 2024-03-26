letion(id='chatcmpl-97A8wcvrGw6kxj0EvqmJQcYdWFRPK', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

base1 = float(input("Enter the length of base 1: "))
base2 = float(input("Enter the length of base 2: "))
height = float(input("Enter the height of the trapezoid: "))

area = trapezoid_area(base1, base2, height)
print(f"The area of the trapezoid is: {area}")', role='assistant', function_call=None, tool_calls=None))], created=1711494314, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3bc1b5746c', usage=CompletionUsage(completion_tokens=113, prompt_tokens=22, total_tokens=135)