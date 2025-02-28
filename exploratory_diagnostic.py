
def longest_common_subsequence(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    lcs = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs = s1[i-1] + lcs
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs

# Test the function
s1 = "AGGTAB"
s2 = "GXTXAYB"
print("Longest common subsequence:", longest_common_subsequence(s1, s2))
