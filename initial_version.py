
def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""
    
    max_len = 1
    start = 0
    
    for i in range(len(s)):
        # Find palindromic substrings with center as s[i]
        l = i
        r = i
        
        while l > 0 and r < len(s) - 1 and s[l-1] == s[r+1]:
            l -= 1
            r += 1
        
        if r - l + 1 > max_len:
            start = l
            max_len = r - l + 1
        
        # Find palindromic substrings with center as s[i] and s[i+1]
        l = i
        r = i + 1
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        if r - l - 1 > max_len:
            start = l + 1
            max_len = r - l - 1
    
    return s[start:start + max_len]

# Test the function with a given string
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"

s = "cbbd"
print(longest_palindromic_substring(s))  # Output: "bb"
