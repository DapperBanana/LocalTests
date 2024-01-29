
import numpy as np

def is_invertible(matrix):
    try:
        np.linalg.inv(matrix)
        return True
    except np.linalg.LinAlgError:
        return False

# Example usage
matrix1 = np.array([[1, 2], [3, 4]])
print(is_invertible(matrix1))  # True

matrix2 = np.array([[1, 2], [2, 4]])
print(is_invertible(matrix2))  # False
