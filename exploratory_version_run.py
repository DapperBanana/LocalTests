letion(id='chatcmpl-94eoCnERNAgy5lPbqgXKlk7RxaLqS', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Function to find maximum and minimum values in a dictionary
def find_max_min(dictionary):
    values = list(dictionary.values())
    max_val = max(values)
    min_val = min(values)
    return max_val, min_val

# Test the function
dictionary = {'a': 5, 'b': 10, 'c': 3, 'd': 8}
max_val, min_val = find_max_min(dictionary)

print(f"Maximum value: {max_val}")
print(f"Minimum value: {min_val}")', role='assistant', function_call=None, tool_calls=None))], created=1710897208, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_4f0b692a78', usage=CompletionUsage(completion_tokens=109, prompt_tokens=22, total_tokens=131)