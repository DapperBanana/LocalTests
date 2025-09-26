
import math

def mean(data):
    return sum(data) / len(data)

def correlation_coefficient(data1, data2):
    mean1 = mean(data1)
    mean2 = mean(data2)

    numerator = sum([(x - mean1) * (y - mean2) for x, y in zip(data1, data2)])
    denominator = math.sqrt(sum([(x - mean1)**2 for x in data1]) * sum([(y - mean2)**2 for y in data2]))

    return numerator / denominator

# Test the function
data1 = [1, 2, 3, 4, 5]
data2 = [2, 4, 6, 8, 10]

print(correlation_coefficient(data1, data2))
