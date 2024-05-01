letion(id='chatcmpl-9KBRbMlPVsyU5xUZxL3vJL21OShCU', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def calculate_surface_area(side_length):
    # Calculate the surface area of a cube: 6 * side_length^2
    surface_area = 6 * side_length**2
    return surface_area

side_length = float(input("Enter the side length of the cube: "))
surface_area = calculate_surface_area(side_length)
print("The surface area of the cube is:", surface_area)', role='assistant', function_call=None, tool_calls=None))], created=1714597579, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3b956da36b', usage=CompletionUsage(completion_tokens=79, prompt_tokens=20, total_tokens=99)