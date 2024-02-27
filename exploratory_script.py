letion(id='chatcmpl-8wgLkii27L2u3MwA21uDjXxxDkLxs', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='from statistics import mean

def calculate_slope(x, y):
    n = len(x)
    x_mean = mean(x)
    y_mean = mean(y)
    
    numerator = sum([(x[i] - x_mean) * (y[i] - y_mean) for i in range(n)])
    denominator = sum([(x[i] - x_mean) ** 2 for i in range(n)])
    
    return numerator / denominator

def calculate_intercept(x, y):
    return mean(y) - calculate_slope(x, y) * mean(x)

def linear_regression(x, y, predict):
    slope = calculate_slope(x, y)
    intercept = calculate_intercept(x, y)
    
    predicted_y = [slope * xi + intercept for xi in predict]
    
    return predicted_y

# Example
x = [1, 2, 3, 4, 5]
y = [3, 4, 2, 5, 6]
predict = [6, 7, 8]

predicted_values = linear_regression(x, y, predict)
print(predicted_values)', role='assistant', function_call=None, tool_calls=None))], created=1708996508, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_86156a94a0', usage=CompletionUsage(completion_tokens=226, prompt_tokens=19, total_tokens=245)