letion(id='chatcmpl-9N43qh7HGKxcFD2YkohoCwxrHMxWH', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def check_isogram(string):
    string = string.lower()
    seen = set()
    
    for char in string:
        if char.isalpha():
            if char in seen:
                return False
            seen.add(char)
    
    return True

# Test the function
print(check_isogram("algorithm"))
print(check_isogram("hello"))
print(check_isogram("Python"))
print(check_isogram("isogram"))', role='assistant', function_call=None, tool_calls=None))], created=1715284182, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=84, prompt_tokens=22, total_tokens=106)