
import numpy as np

def calculate_determinant(matrix):
    det = np.linalg.det(matrix)
    return det

# Example usage

# Define a 3x3 matrix
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

# Calculate the determinant
determinant = calculate_determinant(matrix)

# Print the determinant
print("Determinant:", determinant)
