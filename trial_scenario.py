
import numpy as np

def determinant(matrix):
    # Convert the matrix to a numpy array for easier manipulation
    matrix = np.array(matrix)
    
    # Calculate the determinant using numpy's built-in function
    det = np.linalg.det(matrix)
    
    return det

# Test the function with a sample matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

det = determinant(matrix)
print("Determinant of the matrix:")
print(det)
