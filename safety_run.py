
import numpy as np

# Function to calculate the correlation coefficient
def correlation_coefficient(list1, list2):
    return np.corrcoef(list1, list2)[0, 1]

# Input lists
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

# Calculate correlation coefficient
corr_coeff = correlation_coefficient(list1, list2)

print("Correlation Coefficient between list1 and list2:", corr_coeff)
