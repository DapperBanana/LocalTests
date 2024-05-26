
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    # Create a 2D table to store the length of LCS of substrings
    lcs_table = [[0] * (n+1) for _ in range(m+1)]
    
    # Fill the table using bottom-up dynamic programming approach
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                lcs_table[i][j] = 0
            elif X[i-1] == Y[j-1]:
                lcs_table[i][j] = lcs_table[i-1][j-1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i-1][j], lcs_table[i][j-1])
    
    # Find the longest common subsequence by tracing back the table
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs = X[i-1] + lcs
            i -= 1
            j -= 1
        elif lcs_table[i-1][j] > lcs_table[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return lcs

# Test the function with example strings
X = "ABCBDAB"
Y = "BDCAB"
print("Longest Common Subsequence:", lcs(X, Y))
