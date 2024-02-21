letion(id='chatcmpl-8ulcDjwbo7kIHNnCTIyVbROTczoeL', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def is_valid_isbn(isbn):
    isbn = isbn.replace('-', '')  # Remove hyphens
    if len(isbn) != 10:
        return False
    
    total = 0
    for i in range(10):
        if i == 9 and isbn[i] == 'X':
            total += 10
        elif not isbn[i].isdigit():
            return False
        else:
            total += int(isbn[i]) * (10 - i)
    
    return total % 11 == 0

# Test the function
print(is_valid_isbn("3-598-21508-0"))
print(is_valid_isbn("3-598-21507-X"))
print(is_valid_isbn("3-598-21507-XX"))', role='assistant', function_call=None, tool_calls=None))], created=1708540093, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_cbdb91ce3f', usage=CompletionUsage(completion_tokens=159, prompt_tokens=23, total_tokens=182)