
import numpy as np

def is_invertible(matrix):
    if np.linalg.matrix_rank(matrix) == len(matrix):
        return True
    else:
        return False

# Test the program
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[1, 2], [2, 4]])

if is_invertible(matrix1):
    print("Matrix 1 is invertible")
else:
    print("Matrix 1 is not invertible")

if is_invertible(matrix2):
    print("Matrix 2 is invertible")
else:
    print("Matrix 2 is not invertible")
