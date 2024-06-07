letion(id='chatcmpl-9XbKAxMJI5YPufZ1Px7QxTgspKqnG', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='# Function to find the union of two sets
def find_union(set1, set2):
    return set1.union(set2)

# Main code to test the function
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = find_union(set1, set2)
print("Union of set1 and set2:", union_set)', role='assistant', function_call=None, tool_calls=None))], created=1717795326, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=95, prompt_tokens=19, total_tokens=114)