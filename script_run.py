
import numpy as np

# Generate some random data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add a column of ones to X for bias term
X_b = np.c_[np.ones((100, 1)), X]

# Calculate the optimal theta using the normal equation
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Make predictions
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta_best)

# Display the results
print("Optimal theta:")
print(theta_best)

print("\nPredictions:")
print(y_predict)
