
def edit_distance(s1, s2):
    m = len(s1) + 1
    n = len(s2) + 1
    
    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        dp[i][0] = i
        
    for j in range(n):
        dp[0][j] = j
        
    for i in range(1, m):
        for j in range(1, n):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                
    return dp[m-1][n-1]

# Test the program with sample strings
s1 = "kitten"
s2 = "sitting"
print(edit_distance(s1, s2))  # Output: 3
