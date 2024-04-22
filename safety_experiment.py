
def longest_palindromic_substring(s):
    if len(s) < 2:
        return s
    
    longest_palindrome = ''
    
    for i in range(len(s)):
        palindrome = expand_around_center(s, i, i)
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome
            
        palindrome = expand_around_center(s, i, i + 1)
        if len(palindrome) > len(longest_palindrome):
            longest_palindrome = palindrome
            
    return longest_palindrome

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    return s[left+1:right]

# Test the function
s = "babad"
print(longest_palindromic_substring(s))
