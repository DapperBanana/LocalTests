letion(id='chatcmpl-99LQoJ7K9z4PXyWI9GGiXqArNylZC', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def calculate_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

base1 = float(input("Enter the length of the first base: "))
base2 = float(input("Enter the length of the second base: "))
height = float(input("Enter the height of the trapezoid: "))

area = calculate_area(base1, base2, height)
print("The area of the trapezoid is: ", area)', role='assistant', function_call=None, tool_calls=None))], created=1712014362, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_b28b39ffa8', usage=CompletionUsage(completion_tokens=107, prompt_tokens=22, total_tokens=129)