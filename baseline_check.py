
import numpy as np

# Input lists
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]

# Calculate correlation coefficient
correlation_coefficient = np.corrcoef(list1, list2)[0, 1]

print("Correlation Coefficient:", correlation_coefficient)
