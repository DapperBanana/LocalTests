
def romanToInt(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_val = 0
    
    for char in s:
        current_val = roman_dict[char]
        
        if current_val > prev_val:
            result += current_val - 2 * prev_val
        else:
            result += current_val
        
        prev_val = current_val
        
    return result

# Test the function
print(romanToInt("III"))  # Output: 3
print(romanToInt("IV"))  # Output: 4
print(romanToInt("IX"))  # Output: 9
print(romanToInt("LVIII"))  # Output: 58
print(romanToInt("MCMXCIV"))  # Output: 1994
