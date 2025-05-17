
import numpy as np

def is_invertible(matrix):
    matrix_np = np.array(matrix)
    if np.linalg.matrix_rank(matrix_np) == len(matrix):
        return True
    else:
        return False

# Example matrix
matrix = [[1, 2],
          [3, 4]]

if is_invertible(matrix):
    print("The matrix is invertible.")
else:
    print("The matrix is not invertible.")
