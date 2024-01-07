
def reverse_matrix(matrix):
    # Reverse the order of rows
    matrix = matrix[::-1]
    
    # Reverse the order of columns
    matrix = [row[::-1] for row in matrix]
    
    return matrix

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
reversed_matrix = reverse_matrix(matrix)
print(reversed_matrix)
