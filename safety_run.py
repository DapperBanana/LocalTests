
def longest_palindromic_substring(s):
    n = len(s)
    start = 0
    max_len = 1
    
    for i in range(1, n):
        # Check for even length palindromes
        low = i - 1
        high = i
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1
        
        # Check for odd length palindromes
        low = i - 1
        high = i + 1
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1
    
    return s[start:start + max_len]

# Test the function
s = "babad"
print(longest_palindromic_substring(s))  # Output: "aba"

s = "cbbd"
print(longest_palindromic_substring(s))  # Output: "bb"
