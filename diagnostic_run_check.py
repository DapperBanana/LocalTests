
import numpy as np

def calculate_determinant(matrix):
    determinant = np.linalg.det(matrix)
    return determinant

# Main program
matrix = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

determinant = calculate_determinant(matrix)

print("Matrix:")
print(matrix)
print("Determinant:", determinant)
