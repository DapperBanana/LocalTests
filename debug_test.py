
import numpy as np

# Function to calculate correlation coefficient
def correlation_coefficient(list1, list2):
    corr_matrix = np.corrcoef(list1, list2)
    corr_coeff = corr_matrix[0, 1]
    return corr_coeff

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

# Calculate correlation coefficient
corr_coefficient_value = correlation_coefficient(list1, list2)
print(f"Correlation coefficient between list1 and list2: {corr_coefficient_value}")
