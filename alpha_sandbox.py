
import math

def mean(numbers):
    return sum(numbers) / len(numbers)

def correlation_coefficient(list1, list2):
    mean1 = mean(list1)
    mean2 = mean(list2)
    cov_sum = 0
    var1_sum = 0
    var2_sum = 0

    for i in range(len(list1)):
        cov_sum += (list1[i] - mean1) * (list2[i] - mean2)
        var1_sum += (list1[i] - mean1) ** 2
        var2_sum += (list2[i] - mean2) ** 2

    corr_coef = cov_sum / math.sqrt(var1_sum * var2_sum)

    return corr_coef

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
print(correlation_coefficient(list1, list2))
