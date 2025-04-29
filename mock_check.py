
def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""
    
    longest_substring = ""
    for i in range(len(s)):
        # Check for odd length palindromes
        palindrome1 = expand_around_center(s, i, i)
        # Check for even length palindromes
        palindrome2 = expand_around_center(s, i, i + 1)
        
        if len(palindrome1) > len(longest_substring):
            longest_substring = palindrome1
        
        if len(palindrome2) > len(longest_substring):
            longest_substring = palindrome2
    
    return longest_substring

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

# Test the program
s = "babad"
print(longest_palindromic_substring(s))  # Output: "aba"

s = "cbbd"
print(longest_palindromic_substring(s))  # Output: "bb"
