
def longest_palindrome(s):
    n = len(s)
    table = [[False for x in range(n)] for y in range(n)]
  
    # All substrings of length 1 are palindromes
    maxLength = 1
    for i in range(n):
        table[i][i] = True
  
    # Check for substring of length 2
    start = 0
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            table[i][i + 1] = True
            start = i
            maxLength = 2
  
    # Check for lengths greater than 2
    for k in range(3, n + 1):
        # Fix the starting index
        for i in range(n - k + 1):
            # Get the ending index of substring from
            # starting index i and length k
            j = i + k - 1
  
            # Checking for sub-string from ith index to
            # jth index, if str[i+1] to str[j-1] is a
            # palindrome
            if table[i + 1][j - 1] and s[i] == s[j]:
                table[i][j] = True
  
                if k > maxLength:
                    start = i
                    maxLength = k
  
    # Return the longest palindromic substring
    return s[start:start + maxLength]

# Test the function
input_string = "babad"
print("Longest palindromic substring is:", longest_palindrome(input_string))
