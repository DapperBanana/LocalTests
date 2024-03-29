letion(id='chatcmpl-98FY2fpycpaDpvPSmv2YlQtUYNO5Q', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

base1 = float(input("Enter the length of base1: "))
base2 = float(input("Enter the length of base2: "))
height = float(input("Enter the height of the trapezoid: "))

print("The area of the trapezoid is:", trapezoid_area(base1, base2, height))', role='assistant', function_call=None, tool_calls=None))], created=1711753418, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3bc1b5746c', usage=CompletionUsage(completion_tokens=106, prompt_tokens=22, total_tokens=128)