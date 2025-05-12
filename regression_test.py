
def correlation_coefficient(list1, list2):
    n = len(list1)
    
    # Calculate the mean of each list
    mean1 = sum(list1) / n
    mean2 = sum(list2) / n
    
    # Calculate the numerator and denominators of the correlation coefficient formula
    numerator = sum((x - mean1) * (y - mean2) for x, y in zip(list1, list2))
    denominator1 = sum((x - mean1) ** 2 for x in list1)
    denominator2 = sum((y - mean2) ** 2 for y in list2)
    
    # Calculate the correlation coefficient
    correlation_coefficient = numerator / (denominator1 ** 0.5 * denominator2 ** 0.5)
    
    return correlation_coefficient

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6]

print(correlation_coefficient(list1, list2))
