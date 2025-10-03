
import math

def mean(numbers):
    return sum(numbers) / len(numbers)

def correlation_coefficient(list1, list2):
    mean1 = mean(list1)
    mean2 = mean(list2)
    
    numerator = sum((x - mean1) * (y - mean2) for x, y in zip(list1, list2))
    
    denominator1 = math.sqrt(sum((x - mean1) ** 2 for x in list1))
    denominator2 = math.sqrt(sum((y - mean2) ** 2 for y in list2))
    
    return numerator / (denominator1 * denominator2)

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]

print("Correlation coefficient:", correlation_coefficient(list1, list2))
