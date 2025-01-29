
def correlation_coefficient(list1, list2):
    mean1 = sum(list1) / len(list1)
    mean2 = sum(list2) / len(list2)
    
    numerator = sum([(x - mean1) * (y - mean2) for x, y in zip(list1, list2)])
    
    sum_sq_diff1 = sum([(x - mean1) ** 2 for x in list1])
    sum_sq_diff2 = sum([(y - mean2) ** 2 for y in list2])
    
    denominator = (sum_sq_diff1 * sum_sq_diff2) ** 0.5
    
    if denominator == 0:
        return 0
    
    correlation = numerator / denominator
    
    return correlation

list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 5, 4, 6]

print(correlation_coefficient(list1, list2))
