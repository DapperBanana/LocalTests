
import numpy as np

def calculate_determinant(matrix):
    det = np.linalg.det(matrix)
    return det

# Example usage
matrix = np.array([[1, 2], [3, 4]])
determinant = calculate_determinant(matrix)
print("Determinant:", determinant)
