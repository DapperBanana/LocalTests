letion(id='chatcmpl-99fb0vcP5H0XGR1TI6tjRipM61kqe', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def calculate_area_of_trapezoid(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

base1 = float(input("Enter the length of base1: "))
base2 = float(input("Enter the length of base2: "))
height = float(input("Enter the height of the trapezoid: "))

area = calculate_area_of_trapezoid(base1, base2, height)
print("The area of the trapezoid is:", area)', role='assistant', function_call=None, tool_calls=None))], created=1712091874, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_b28b39ffa8', usage=CompletionUsage(completion_tokens=114, prompt_tokens=22, total_tokens=136)