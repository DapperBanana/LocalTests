
# Importing the required libraries
import numpy as np
from sklearn.linear_model import LinearRegression

# Input features (X) and target variable (y)
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

# Creating a linear regression model
model = LinearRegression()

# Training the model
model.fit(X, y)

# Printing the coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Predicting on new data
new_data = np.array([[3, 3], [4, 5]])
predictions = model.predict(new_data)
print("Predictions:", predictions)
