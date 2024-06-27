
import numpy as np

# Generate some sample data
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Calculate the mean of X and y
mean_x = np.mean(X)
mean_y = np.mean(y)

# Calculate the slope and intercept of the regression line
numerator = np.sum((X - mean_x) * (y - mean_y))
denominator = np.sum((X - mean_x) ** 2)

slope = numerator / denominator
intercept = mean_y - (slope * mean_x)

# Predict some new values using the regression model
new_X = np.array([6, 7, 8, 9, 10])
predictions = slope * new_X + intercept

print("Slope:", slope)
print("Intercept:", intercept)
print("Predictions for new values:", predictions)
