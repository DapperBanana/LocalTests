
def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""
    
    dp = [[False for _ in range(n)] for _ in range(n)]
    
    start = 0
    max_length = 1
    
    for i in range(n):
        dp[i][i] = True
    
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if length == 2 and s[i] == s[j]:
                dp[i][j] = True
                start = i
                max_length = length
            elif s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                start = i
                max_length = length
                
    return s[start:start+max_length]

# Test the function
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab"

s = "cbbd"
print(longest_palindromic_substring(s))  # Output: "bb"
