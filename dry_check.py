
import numpy as np

def correlation_coefficient(list1, list2):
    mean_list1 = np.mean(list1)
    mean_list2 = np.mean(list2)
    
    numerator = sum((x - mean_list1) * (y - mean_list2) for x, y in zip(list1, list2))
    
    denominator = np.sqrt(sum((x - mean_list1)**2 for x in list1)) * np.sqrt(sum((y - mean_list2)**2 for y in list2))
    
    correlation = numerator / denominator
    
    return correlation

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]

print("Correlation coefficient:", correlation_coefficient(list1, list2))
