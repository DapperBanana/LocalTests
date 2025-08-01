
import math

def mean(numbers):
    return sum(numbers) / len(numbers)

def correlation_coefficient(list1, list2):
    mean_list1 = mean(list1)
    mean_list2 = mean(list2)
    
    numerator = sum((x - mean_list1) * (y - mean_list2) for x, y in zip(list1, list2))
    denominator = math.sqrt(sum((x - mean_list1) ** 2 for x in list1)) * math.sqrt(sum((y - mean_list2) ** 2 for y in list2))
    
    correlation = numerator / denominator
    
    return correlation

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]

print("Correlation coefficient:", correlation_coefficient(list1, list2))
