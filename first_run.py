letion(id='chatcmpl-97ANQ7aaKccIMULfq20hPwlUUe4tr', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import math

def area_of_heptagon(side_length):
    num_sides = 7
    apothem_length = side_length / (2 * math.tan(math.pi / num_sides))
    area = 0.5 * num_sides * side_length * apothem_length
    return area

side_length = float(input("Enter the side length of the heptagon: "))
print("The area of the regular heptagon is: ", area_of_heptagon(side_length))', role='assistant', function_call=None, tool_calls=None))], created=1711495212, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3bc1b5746c', usage=CompletionUsage(completion_tokens=104, prompt_tokens=22, total_tokens=126)