letion(id='chatcmpl-927Lvic4LZbql3Tc4H6uCcOUr8Li7', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def convert_to_title_case(input_string):
    words = input_string.split()
    title_case_words = [word.capitalize() for word in words]
    return ' '.join(title_case_words)

# Example
input_string = "hello world"
output_string = convert_to_title_case(input_string)
print(output_string) # Output: "Hello World"', role='assistant', function_call=None, tool_calls=None))], created=1710291947, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_4f0b692a78', usage=CompletionUsage(completion_tokens=69, prompt_tokens=19, total_tokens=88)