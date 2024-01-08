letion(id='chatcmpl-8eXu1X5RpOCi30ykBNRpbWWgbMWhE', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import math

def calculate_distance(point1, point2):
    distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)
    return distance

# Testing the program
point1 = (1, 2, 3)
point2 = (4, 5, 6)
distance = calculate_distance(point1, point2)
print("The distance between", point1, "and", point2, "is", distance)', role='assistant', function_call=None, tool_calls=None))], created=1704674133, model='gpt-3.5-turbo-0613', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=122, prompt_tokens=24, total_tokens=146)