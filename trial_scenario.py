letion(id='chatcmpl-91ggvuGvmIxrs80t1RU5Aa6xvH3qx', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def calculate_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

base1 = float(input("Enter the length of the first base of the trapezoid: "))
base2 = float(input("Enter the length of the second base of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))

area = calculate_area(base1, base2, height)
print(f"The area of the trapezoid is: {area}")', role='assistant', function_call=None, tool_calls=None))], created=1710189461, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_4f0b692a78', usage=CompletionUsage(completion_tokens=119, prompt_tokens=22, total_tokens=141)