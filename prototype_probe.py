
def romanToInt(s: str) -> int:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    prev_value = 0
    
    for char in s:
        current_value = roman_map[char]
        
        if current_value > prev_value:
            result += current_value - 2 * prev_value
        else:
            result += current_value
        
        prev_value = current_value
    
    return result

# Test the function
print(romanToInt("III")) # Output: 3
print(romanToInt("IV")) # Output: 4
print(romanToInt("IX")) # Output: 9
print(romanToInt("LVIII")) # Output: 58
print(romanToInt("MCMXCIV")) # Output: 1994
