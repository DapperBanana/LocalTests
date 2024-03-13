letion(id='chatcmpl-92QaJCfsQNIS1NRT74XB7E7ScZEtk', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import math

def area_of_decagon(side_length):
    return (5 * side_length ** 2) / (4 * math.tan(math.pi / 10))

side_length = float(input("Enter the side length of the decagon: "))
area = area_of_decagon(side_length)
print(f"The area of the regular decagon is: {area}")', role='assistant', function_call=None, tool_calls=None))], created=1710365875, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_4f0b692a78', usage=CompletionUsage(completion_tokens=74, prompt_tokens=21, total_tokens=95)