letion(id='chatcmpl-9M2A3RCJqP9WU2fm762wKaiIJuxF9', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import numpy as np

class LinearRegression:
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None
        
    def fit(self, X, y):
        ones = np.ones((X.shape[0], 1))
        X = np.concatenate((ones, X), axis=1)
        
        # closed-form solution for linear regression
        self.coef_ = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
        self.intercept_ = self.coef_[0]
        self.coef_ = self.coef_[1:]
        
    def predict(self, X):
        return self.intercept_ + np.dot(X, self.coef_)
        
# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Predictions:", predictions)', role='assistant', function_call=None, tool_calls=None))], created=1715038551, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=243, prompt_tokens=19, total_tokens=262)