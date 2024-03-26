letion(id='chatcmpl-97AVRKNLJ9co6sQg3O6as3OIJsIBq', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import math

def calculate_cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

volume = calculate_cone_volume(radius, height)
print(f"The volume of the cone is: {volume}")', role='assistant', function_call=None, tool_calls=None))], created=1711495709, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3bc1b5746c', usage=CompletionUsage(completion_tokens=83, prompt_tokens=24, total_tokens=107)