
import numpy as np

def is_invertible(matrix):
    try:
        np.linalg.inv(matrix)
        return True
    except np.linalg.LinAlgError:
        return False

# Example matrix
matrix = np.array([[1, 2], [3, 4]])

if is_invertible(matrix):
    print("The matrix is invertible.")
else:
    print("The matrix is not invertible.")
