letion(id='chatcmpl-9aovWVKj7zX4iyIBvakDlD7cDOkuM', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import numpy as np

class LinearRegression:
    def fit(self, X, y):
        self.X = X
        self.y = y
        self.n = X.shape[0]
        
        X_b = np.c_[np.ones((self.n, 1)), X]
        self.theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    
    def predict(self, X):
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        return X_b.dot(self.theta)

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

predicted_values = model.predict(X)
print(predicted_values)', role='assistant', function_call=None, tool_calls=None))], created=1718562598, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=177, prompt_tokens=19, total_tokens=196)