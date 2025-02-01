
import numpy as np

def determinant(matrix):
    return np.linalg.det(matrix)

# Define a square matrix
matrix = np.array([[1, 2],
                   [3, 4]])

# Calculate the determinant of the matrix
det = determinant(matrix)

print(f"The determinant of the matrix is: {det}")
