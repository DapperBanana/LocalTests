
import math

def correlation_coefficient(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_square = sum(map(lambda i: i ** 2, x))
    sum_y_square = sum(map(lambda i: i ** 2, y))
    sum_xy = sum([x[i] * y[i] for i in range(n)])

    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x_square - sum_x ** 2) * (n * sum_y_square - sum_y ** 2))

    correlation = numerator / denominator

    return correlation

# Example
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
print("Correlation coefficient:", correlation_coefficient(x, y))
