
def is_magic_square(matrix):
    n = len(matrix)
    
    # Calculate the sum of the first row
    sum_val = sum(matrix[0])
    
    # Check if the sum of all rows and columns is equal to the sum of the first row
    for i in range(n):
        if sum(matrix[i]) != sum_val:
            return False
        if sum(row[i] for row in matrix) != sum_val:
            return False
    
    # Check the sum of the main diagonal
    if sum(matrix[i][i] for i in range(n)) != sum_val:
        return False
    
    # Check the sum of the other diagonal
    if sum(matrix[i][n-i-1] for i in range(n)) != sum_val:
        return False
    
    return True

# Example matrix
matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("The given matrix is a magic square.")
else:
    print("The given matrix is not a magic square.")
