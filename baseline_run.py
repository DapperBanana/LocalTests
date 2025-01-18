
import math

def correlation_coefficient(list1, list2):
    n = len(list1)
    
    # Calculate the mean of both lists
    mean1 = sum(list1) / n
    mean2 = sum(list2) / n
    
    # Calculate the numerator and denominators of the correlation coefficient formula
    numerator = sum((x - mean1) * (y - mean2) for x, y in zip(list1, list2))
    denominator1 = math.sqrt(sum((x - mean1)**2 for x in list1))
    denominator2 = math.sqrt(sum((y - mean2)**2 for y in list2))
    
    # Calculate the correlation coefficient
    correlation = numerator / (denominator1 * denominator2)
    
    return correlation

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]
print(correlation_coefficient(list1, list2))
