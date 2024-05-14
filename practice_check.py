letion(id='chatcmpl-9OsNuz3IvernyNTkqpYh8Aqfd2KEX', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def remove_punctuation(input_string):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    clean_string = ""
    
    for char in input_string:
        if char not in punctuation:
            clean_string += char
    
    return clean_string

input_string = "Hello, World!"
clean_string = remove_punctuation(input_string)
print(clean_string)', role='assistant', function_call=None, tool_calls=None))], created=1715715954, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=81, prompt_tokens=20, total_tokens=101)