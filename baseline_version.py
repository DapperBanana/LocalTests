letion(id='chatcmpl-8vEZPzQny7G9rKWSKluNllzrXF7e3', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="import json

# Read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Print the key-value pairs
for key, value in data.items():
    print(f'{key}: {value}')", role='assistant', function_call=None, tool_calls=None))], created=1708651395, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_cbdb91ce3f', usage=CompletionUsage(completion_tokens=52, prompt_tokens=23, total_tokens=75)