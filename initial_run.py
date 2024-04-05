letion(id='chatcmpl-9AkYK7NgTFR7KbaS2gzZQIhljAS2E', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content="import matplotlib.pyplot as plt

# Dictionary of data
data = {
    'January': 100,
    'February': 150,
    'March': 120,
    'April': 180,
    'May': 200
}

# Extract keys and values from the dictionary
months = list(data.keys())
values = list(data.values())

# Create a line chart
plt.plot(months, values, marker='o')

# Add labels and title
plt.xlabel('Months')
plt.ylabel('Values')
plt.title('Simple Line Chart')

# Display the chart
plt.show()", role='assistant', function_call=None, tool_calls=None))], created=1712349256, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_b28b39ffa8', usage=CompletionUsage(completion_tokens=119, prompt_tokens=23, total_tokens=142)