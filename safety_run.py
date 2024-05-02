letion(id='chatcmpl-9KZA57SbpH8yCbVg1gW5LlNYgJgAR', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Function to calculate the area of a trapezoid
def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

# Input the base1, base2 and height of the trapezoid
base1 = float(input("Enter the length of base1: "))
base2 = float(input("Enter the length of base2: "))
height = float(input("Enter the height of the trapezoid: "))

# Calculate the area of the trapezoid
area = trapezoid_area(base1, base2, height)

# Print the area of the trapezoid
print(f"The area of the trapezoid is: {area}")', role='assistant', function_call=None, tool_calls=None))], created=1714688749, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_a450710239', usage=CompletionUsage(completion_tokens=163, prompt_tokens=22, total_tokens=185)