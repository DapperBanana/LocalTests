letion(id='chatcmpl-9dMPBIVDiki2TMtJxvZsH8QKhds85', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]

# Test the function
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False', role='assistant', function_call=None, tool_calls=None))], created=1719167945, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=60, prompt_tokens=20, total_tokens=80)