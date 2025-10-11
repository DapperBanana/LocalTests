
import numpy as np

def correlation_coefficient(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")
    
    mean1 = np.mean(list1)
    mean2 = np.mean(list2)
    
    numerator = sum((x - mean1) * (y - mean2) for x, y in zip(list1, list2))
    denominator1 = sum((x - mean1)**2 for x in list1)
    denominator2 = sum((y - mean2)**2 for y in list2)
    
    correlation_coeff = numerator / np.sqrt(denominator1 * denominator2)
    
    return correlation_coeff

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
coeff = correlation_coefficient(list1, list2)
print(f"Correlation coefficient: {coeff}")
