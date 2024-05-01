
import numpy as np

class LinearRegression:
    def fit(self, X, y):
        ones = np.ones((X.shape[0], 1))
        X = np.concatenate((ones, X), axis=1)
        
        self.beta = np.linalg.inv(X.T @ X) @ X.T @ y
    
    def predict(self, X):
        ones = np.ones((X.shape[0], 1))
        X = np.concatenate((ones, X), axis=1)
        
        y_pred = X @ self.beta
        return y_pred

# Sample data
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

# Fit the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
X_test = np.array([[5], [6]])
y_pred = model.predict(X_test)

print("Predictions:", y_pred)
