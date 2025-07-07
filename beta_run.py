
def correlation_coefficient(list1, list2):
    # Calculate the mean of both lists
    mean_list1 = sum(list1) / len(list1)
    mean_list2 = sum(list2) / len(list2)

    # Calculate the covariance between the two lists
    covariance = sum([(x - mean_list1) * (y - mean_list2) for x, y in zip(list1, list2)]) / len(list1)

    # Calculate the standard deviation of both lists
    std_dev1 = (sum([(x - mean_list1) ** 2 for x in list1]) / len(list1)) ** 0.5
    std_dev2 = (sum([(y - mean_list2) ** 2 for y in list2]) / len(list2)) ** 0.5

    # Calculate the correlation coefficient
    correlation_coeff = covariance / (std_dev1 * std_dev2)

    return correlation_coeff

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 5, 4, 5]

print(correlation_coefficient(list1, list2))
