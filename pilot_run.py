letion(id='chatcmpl-91gi8YmMWcJBXup0O9gGxZzwgDNKY', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="import matplotlib.pyplot as plt

# Dictionary of data
data = {
    'January': 100,
    'February': 150,
    'March': 120,
    'April': 200,
    'May': 180
}

# Extracting x and y values from the dictionary
months = list(data.keys())
values = list(data.values())

# Creating the line chart
plt.figure(figsize=(10, 5))
plt.plot(months, values, marker='o', color='blue', linestyle='solid')

# Adding labels and title
plt.xlabel('Months')
plt.ylabel('Values')
plt.title('Simple Line Chart')

# Display the chart
plt.show()", role='assistant', function_call=None, tool_calls=None))], created=1710189536, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_4f0b692a78', usage=CompletionUsage(completion_tokens=138, prompt_tokens=23, total_tokens=161)