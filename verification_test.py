
import numpy as np

def is_invertible(matrix):
    try:
        inverse = np.linalg.inv(matrix)
        return True
    except np.linalg.LinAlgError:
        return False

# Example matrix
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[1, 2], [2, 4]])

print("Matrix 1 is invertible:", is_invertible(matrix1))
print("Matrix 2 is invertible:", is_invertible(matrix2))
