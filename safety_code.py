letion(id='chatcmpl-9i7FnOO4VfFBjyJJFZ4XaECzsKYCK', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import math

def area_of_heptagon(side_length):
    num_sides = 7
    apothem_length = side_length / (2 * math.tan(math.pi / num_sides))
    area = (num_sides * side_length * apothem_length) / 2
    return area

side_length = float(input("Enter the length of a side of the heptagon: "))
area = area_of_heptagon(side_length)
print(f"The area of the regular heptagon is: {area}")', role='assistant', function_call=None, tool_calls=None))], created=1720301343, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=110, prompt_tokens=22, total_tokens=132)