
import numpy as np

def determinant(matrix):
    return np.linalg.det(matrix)

# Test the program with a sample matrix
matrix = np.array([[1, 2], [3, 4]])
print("Matrix:")
print(matrix)
print("Determinant:", determinant(matrix))
