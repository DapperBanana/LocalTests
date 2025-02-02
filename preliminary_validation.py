
def longest_palindromic_substring(s):
    if s == '':
        return ''
    
    n = len(s)
    longest = ''
    
    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    for i in range(n):
        # For odd length palindromes
        palindrome1 = expand_around_center(i, i)
        # For even length palindromes
        palindrome2 = expand_around_center(i, i+1)
        
        longest = max(longest, palindrome1, palindrome2, key=len)
    
    return longest

# Test the function
s = "babad"
print(longest_palindromic_substring(s))  # Output: "aba"

s = "cbbd"
print(longest_palindromic_substring(s))  # Output: "bb"
