
import math

def mean(data):
    return sum(data) / len(data)

def correlation_coefficient(list1, list2):
    mean1 = mean(list1)
    mean2 = mean(list2)
    
    sum_xy = 0
    sum_xsq = 0
    sum_ysq = 0
    
    for x, y in zip(list1, list2):
        sum_xy += (x - mean1) * (y - mean2)
        sum_xsq += (x - mean1) ** 2
        sum_ysq += (y - mean2) ** 2
    
    correlation = sum_xy / math.sqrt(sum_xsq * sum_ysq)
    
    return correlation

# Test the program
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 6, 8, 10]

correlation = correlation_coefficient(list1, list2)
print("Correlation coefficient:", correlation)
