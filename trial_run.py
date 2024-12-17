
import numpy as np

def determinant(matrix):
    return np.linalg.det(matrix)

# Example matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

result = determinant(matrix)

print("The determinant of the matrix is:", result)
