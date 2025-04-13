
import numpy as np

# Function to check if matrix is invertible
def is_invertible(matrix):
    if np.linalg.det(matrix) != 0:
        return True
    else:
        return False

# Input matrix
matrix = np.array([[1, 2], [3, 4]])

# Check if matrix is invertible
if is_invertible(matrix):
    print("The matrix is invertible")
else:
    print("The matrix is not invertible")
