letion(id='chatcmpl-8oGLtXvOTCkO7SdUiDXpdrDxBFTmA', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import math

def calculate_area_of_frustum_of_cone(top_radius, bottom_radius, height):
    # Calculate the slant height of the frustum
    slant_height = math.sqrt((top_radius - bottom_radius)**2 + height**2)
    
    # Calculate the surface area of the frustum
    area = math.pi * (top_radius + bottom_radius) * slant_height
    
    return area

# Example usage
top_radius = 4
bottom_radius = 8
height = 10

area = calculate_area_of_frustum_of_cone(top_radius, bottom_radius, height)
print("The area of the frustum of the cone is: ", area)', role='assistant', function_call=None, tool_calls=None))], created=1706989949, model='gpt-3.5-turbo-0613', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=143, prompt_tokens=23, total_tokens=166)