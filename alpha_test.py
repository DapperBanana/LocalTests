
import math

def mean(numbers):
    return sum(numbers) / len(numbers)

def correlation_coefficient(list1, list2):
    mean1 = mean(list1)
    mean2 = mean(list2)
    
    num = sum((x - mean1) * (y - mean2) for x, y in zip(list1, list2))
    den = math.sqrt(sum((x - mean1)**2 for x in list1) * sum((y - mean2)**2 for y in list2))
    
    return num / den

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6]

# Calculate correlation coefficient
corr_coef = correlation_coefficient(list1, list2)
print("Correlation Coefficient:", corr_coef)
