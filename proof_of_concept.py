
import numpy as np

class LinearRegression:
    def __init__(self):
        self.coef_ = None
        self.intercept_ = None

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        
        n = X.shape[0]
        _, d = X.shape

        X_bias = np.hstack((np.ones((n, 1)), X))
        A = np.dot(X_bias.T, X_bias)
        b = np.dot(X_bias.T, y)
        
        self.coef_ = np.linalg.solve(A, b)[1:]
        self.intercept_ = np.linalg.solve(A, b)[0]

    def predict(self, X):
        X = np.array(X)
        
        return np.dot(X, self.coef_) + self.intercept_

# Sample usage:
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 5, 4, 5]

model = LinearRegression()
model.fit(X, y)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
print("Predictions:", model.predict(X))
