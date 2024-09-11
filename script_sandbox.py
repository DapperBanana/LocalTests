
import numpy as np

class LinearRegression:
    def __init__(self):
        self.coefficients = None

    def fit(self, X, y):
        X = np.insert(X, 0, 1, axis=1)  # Add a column of ones for the intercept term
        self.coefficients = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

    def predict(self, X):
        X = np.insert(X, 0, 1, axis=1)  # Add a column of ones for the intercept term
        return X.dot(self.coefficients)

# Example usage
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

X_test = np.array([[6], [7], [8]])
predictions = model.predict(X_test)

print(predictions)
