
import numpy as np

def calculate_determinant(matrix):
    return np.linalg.det(matrix)

# Input matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculate determinant
determinant = calculate_determinant(matrix)

print("Matrix:")
print(matrix)
print("Determinant:", determinant)
