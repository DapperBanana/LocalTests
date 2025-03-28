
import math

def mean(data):
    return sum(data) / len(data)

def correlation_coefficient(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    
    numerator = sum([(a - mean_x) * (b - mean_y) for a, b in zip(x, y)])
    
    sum_sq_x = sum([(a - mean_x) ** 2 for a in x])
    sum_sq_y = sum([(b - mean_y) ** 2 for b in y])
    
    denominator = math.sqrt(sum_sq_x) * math.sqrt(sum_sq_y)
    
    if denominator == 0:
        return 0
    
    return numerator / denominator

# Example usage
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

print("Correlation coefficient:", correlation_coefficient(x, y))
