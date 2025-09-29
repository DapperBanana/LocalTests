
def is_magic_square(matrix):
    n = len(matrix)
    
    # Calculate the sum of the first row as the magic sum
    magic_sum = sum(matrix[0])
    
    # Check if all rows have the same sum
    for i in range(n):
        if sum(matrix[i]) != magic_sum:
            return False
    
    # Check if all columns have the same sum
    for i in range(n):
        if sum(matrix[j][i] for j in range(n)) != magic_sum:
            return False
    
    # Check if the primary diagonal has the same sum
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False
    
    # Check if the secondary diagonal has the same sum
    if sum(matrix[i][n-i-1] for i in range(n)) != magic_sum:
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
