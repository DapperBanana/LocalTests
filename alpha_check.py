
def is_magic_square(matrix):
    n = len(matrix)
    
    # Check if all rows have the same sum
    row_sum = sum(matrix[0])
    for row in matrix[1:]:
        if sum(row) != row_sum:
            return False
    
    # Check if all columns have the same sum
    for col in range(n):
        if sum(row[col] for row in matrix) != row_sum:
            return False
    
    # Check if the two diagonals have the same sum
    if sum(matrix[i][i] for i in range(n)) != row_sum:
        return False
    if sum(matrix[i][n-i-1] for i in range(n)) != row_sum:
        return False
    
    return True

# Example matrix
matrix = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
print(is_magic_square(matrix))
