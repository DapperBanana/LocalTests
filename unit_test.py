
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Make predictions
predictions = model.predict(X)

# Print the model coefficients
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_[0])

# Print the predictions
print("Predictions:", predictions)
