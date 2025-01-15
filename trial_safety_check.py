
def correlation_coefficient(list1, list2):
    n = len(list1)
    if n != len(list2):
        return "Lists must be of equal length"
    
    mean1 = sum(list1) / n
    mean2 = sum(list2) / n
    
    numerator = sum([(x - mean1)*(y - mean2) for x, y in zip(list1, list2)])
    denominator1 = sum([(x - mean1)**2 for x in list1])
    denominator2 = sum([(y - mean2)**2 for y in list2])
    
    correlation = numerator / ((denominator1 * denominator2)**0.5)
    
    return correlation

list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6]

print("Correlation coefficient:", correlation_coefficient(list1, list2))
