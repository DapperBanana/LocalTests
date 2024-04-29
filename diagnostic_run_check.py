letion(id='chatcmpl-9JT2f3HIXnGX0J6FLlD8QFq93ayqh', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='def find_max_min(dictionary):
    values = list(dictionary.values())
    return max(values), min(values)

# test the function
dict_values = {'A': 10, 'B': 5, 'C': 15, 'D': 20, 'E': 1}
max_value, min_value = find_max_min(dict_values)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")', role='assistant', function_call=None, tool_calls=None))], created=1714426897, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_3b956da36b', usage=CompletionUsage(completion_tokens=91, prompt_tokens=22, total_tokens=113)