
def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""
    
    longest = s[0]
    
    for i in range(len(s)):
        odd_palindrome = expand_around_center(s, i, i)
        even_palindrome = expand_around_center(s, i, i + 1)
        
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest

# Test the program
input_string = "babad"
print("Longest palindromic substring in '{}' is '{}'".format(input_string,
                                                             longest_palindromic_substring(input_string)))
