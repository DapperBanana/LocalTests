
import numpy as np

def correlation_coefficient(list1, list2):
    correlation_matrix = np.corrcoef(list1, list2)
    correlation_coeff = correlation_matrix[0, 1]
    return correlation_coeff

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

# Calculate correlation coefficient
corr_coefficient = correlation_coefficient(list1, list2)
print("Correlation coefficient:", corr_coefficient)
