letion(id='chatcmpl-98XHymTvOGdtNJ6WAV78UXaXeRQ4A', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import math

def calculate_distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    
    return distance

point1 = (1, 2, 3)
point2 = (4, 5, 6)

distance = calculate_distance(point1, point2)
print(f"The distance between {point1} and {point2} is: {distance}")', role='assistant', function_call=None, tool_calls=None))], created=1711821614, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_b28b39ffa8', usage=CompletionUsage(completion_tokens=128, prompt_tokens=24, total_tokens=152)