
import numpy as np

def is_invertible(matrix):
    try:
        np.linalg.inv(matrix)
        return True
    except np.linalg.LinAlgError:
        return False

# Example usage
matrix = np.array([[1, 2], [3, 4]])
if is_invertible(matrix):
    print("The given matrix is invertible.")
else:
    print("The given matrix is not invertible.")
