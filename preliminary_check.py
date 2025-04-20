
import math

def mean(values):
    return sum(values) / len(values)

def correlation_coefficient(x, y):
    mean_x = mean(x)
    mean_y = mean(y)

    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator = math.sqrt(sum((xi - mean_x)**2 for xi in x) * sum((yi - mean_y)**2 for yi in y))

    return numerator / denominator

# Example usage
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

print(correlation_coefficient(x, y))
