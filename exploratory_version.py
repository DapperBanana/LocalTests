letion(id='chatcmpl-9WsukLcMAG6vbX69ywGyJrKNj7bRZ', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Function to find the union of two sets
def find_union(set1, set2):
    union_set = set1.union(set2)
    return union_set

# Input sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find the union of the two sets
union = find_union(set1, set2)

# Print the result
print("Union of set1 and set2 is:", union)', role='assistant', function_call=None, tool_calls=None))], created=1717624614, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=111, prompt_tokens=19, total_tokens=130)