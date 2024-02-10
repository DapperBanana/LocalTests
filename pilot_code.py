
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample input data
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

# Initialize and fit the model
model = LinearRegression().fit(X, y)

# Predict the output
x_test = np.array([[3, 5]])
y_pred = model.predict(x_test)

# Print the coefficients and predicted output
print('Coefficients:', model.coef_)
print('Intercept:', model.intercept_)
print('Predicted output:', y_pred)
