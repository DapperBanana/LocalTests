
import math

def mean(values):
    return sum(values) / len(values)

def correlation_coefficient(x, y):
    n = len(x)
    x_mean = mean(x)
    y_mean = mean(y)
    
    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator_x = math.sqrt(sum((x[i] - x_mean) ** 2 for i in range(n)))
    denominator_y = math.sqrt(sum((y[i] - y_mean) ** 2 for i in range(n))
    
    correlation = numerator / (denominator_x * denominator_y)
    
    return correlation

# Example usage:
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

print(correlation_coefficient(x, y))
