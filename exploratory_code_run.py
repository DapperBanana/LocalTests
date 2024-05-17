letion(id='chatcmpl-9PxmXBv0MvnS0WLNCyFFe6FmC2kbz', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import math

def area_of_heptagon(side_length):
    n = 7
    return (n * side_length ** 2) / (4 * math.tan(math.pi/n))

side_length = float(input("Enter the side length of the heptagon: "))
area = area_of_heptagon(side_length)
print("The area of the regular heptagon is:", area)', role='assistant', function_call=None, tool_calls=None))], created=1715975029, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=81, prompt_tokens=22, total_tokens=103)