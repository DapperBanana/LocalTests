letion(id='chatcmpl-8wg68m2wUnbyH3Vd03VK2IGuMz6F8', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import numpy as np

class LinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self, X, y):
        X_mean = np.mean(X)
        y_mean = np.mean(y)

        numerator = np.sum((X - X_mean) * (y - y_mean))
        denominator = np.sum((X - X_mean) ** 2)

        self.slope = numerator / denominator
        self.intercept = y_mean - self.slope * X_mean

    def predict(self, X):
        return self.slope * X + self.intercept

# Example usage
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])

model = LinearRegression()
model.fit(X, y)

x_test = np.array([6, 7, 8, 9, 10])
predictions = model.predict(x_test)

print(predictions) # Output: [ 7.  8.  9. 10. 11.]', role='assistant', function_call=None, tool_calls=None))], created=1708995540, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_86156a94a0', usage=CompletionUsage(completion_tokens=235, prompt_tokens=19, total_tokens=254)