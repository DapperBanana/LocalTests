
import numpy as np

def is_invertible(matrix):
    if np.linalg.matrix_rank(matrix) == len(matrix):
        return True
    else:
        return False

# Example matrix
matrix = np.array([[1, 2], [3, 4]])

if is_invertible(matrix):
    print("Matrix is invertible.")
else:
    print("Matrix is not invertible.")
