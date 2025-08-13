
import numpy as np

# Function to calculate correlation coefficient
def correlation_coefficient(list1, list2):
    correlation = np.corrcoef(list1, list2)[0, 1]
    return correlation

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

# Calculate correlation coefficient
correlation = correlation_coefficient(list1, list2)

# Print correlation coefficient
print("Correlation Coefficient:", correlation)
