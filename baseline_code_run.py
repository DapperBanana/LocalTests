
import numpy as np

def is_invertible(matrix):
    if np.linalg.matrix_rank(matrix) == matrix.shape[0]:  # Check if matrix rank is equal to number of rows
        return True
    else:
        return False

# Example matrix
matrix = np.array([[1, 2], [3, 4]])

if is_invertible(matrix):
    print("The matrix is invertible.")
else:
    print("The matrix is not invertible.")
