letion(id='chatcmpl-97ALoGDLT7Wy8LbFEeVlCa4pWJ6dj', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def trapezoid_area(base1, base2, height):
    area = ((base1 + base2) / 2) * height
    return area

base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))
height = float(input("Enter the height of the trapezoid: "))

area = trapezoid_area(base1, base2, height)
print(f"The area of the trapezoid is: {area}")', role='assistant', function_call=None, tool_calls=None))], created=1711495112, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3bc1b5746c', usage=CompletionUsage(completion_tokens=112, prompt_tokens=22, total_tokens=134)