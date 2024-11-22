
def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)
    
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    lcs_length = dp[m][n]
    
    lcs = [''] * lcs_length
    i = m
    j = n
    index = lcs_length - 1
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs[index] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(lcs)

# Test the function with two strings
str1 = "ABCDGH"
str2 = "AEDFHR"
print("Longest common subsequence:", longest_common_subsequence(str1, str2))
