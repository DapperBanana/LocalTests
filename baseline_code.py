
import numpy as np

def determinant(matrix):
    return np.linalg.det(matrix)

# Test the program with a sample matrix
matrix = np.array([[1, 2], [3, 4]])
det = determinant(matrix)
print("Determinant of the matrix:")
print(det)
