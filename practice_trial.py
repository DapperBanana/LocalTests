letion(id='chatcmpl-9PJpOZcbJuuSC7OLbnoA8afD7WC5F', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import math

def sector_area(radius, angle):
    if angle > 360:
        return "Angle must be less than 360 degrees"
    
    sector_area = (math.pi * radius**2 * angle) / 360
    return sector_area

radius = float(input("Enter the radius of the sector: "))
angle = float(input("Enter the angle of the sector in degrees: "))

print("The area of the sector is: ", sector_area(radius, angle))', role='assistant', function_call=None, tool_calls=None))], created=1715821446, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=98, prompt_tokens=24, total_tokens=122)