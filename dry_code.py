
import math

def mean(values):
    return sum(values) / len(values)

def correlation_coefficient(list1, list2):
    mean1 = mean(list1)
    mean2 = mean(list2)

    numerator = sum((x - mean1) * (y - mean2) for x, y in zip(list1, list2))
    denominator1 = math.sqrt(sum((x - mean1)**2 for x in list1))
    denominator2 = math.sqrt(sum((y - mean2)**2 for y in list2))

    correlation = numerator / (denominator1 * denominator2)

    return correlation

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

print("Correlation coefficient between list1 and list2:", correlation_coefficient(list1, list2))
