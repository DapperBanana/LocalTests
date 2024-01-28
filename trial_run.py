
import numpy as np

def correlation_coefficient(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists should have the same length.")

    x = np.array(list1)
    y = np.array(list2)

    # Calculate the mean of the lists
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Calculate the differences from the mean
    diff_x = x - mean_x
    diff_y = y - mean_y

    # Calculate the covariance and variances
    covariance = np.mean(diff_x * diff_y)
    variance_x = np.mean(diff_x ** 2)
    variance_y = np.mean(diff_y ** 2)

    # Calculate the correlation coefficient
    correlation = covariance / (np.sqrt(variance_x) * np.sqrt(variance_y))
    
    return correlation

# Sample usage
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
print(correlation_coefficient(list1, list2))
