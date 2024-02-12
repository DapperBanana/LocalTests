letion(id='chatcmpl-8rFkoVhNahxBZZYtyQOKaJWApV94C', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import math

def calculate_cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

cone_volume = calculate_cone_volume(radius, height)
print("The volume of the cone is:", cone_volume)', role='assistant', function_call=None, tool_calls=None))], created=1707702634, model='gpt-3.5-turbo-0613', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=84, prompt_tokens=24, total_tokens=108)