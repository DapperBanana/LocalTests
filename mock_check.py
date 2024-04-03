
def roman_to_int(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev_value = 0
    
    for letter in roman:
        current_value = roman_dict[letter]
        if current_value > prev_value:
            total += current_value - 2*prev_value
        else:
            total += current_value
        prev_value = current_value
        
    return total

# Test the function
print(roman_to_int('III'))  # Output: 3
print(roman_to_int('IV'))   # Output: 4
print(roman_to_int('IX'))   # Output: 9
print(roman_to_int('LVIII'))   # Output: 58
print(roman_to_int('MCMXCIV'))   # Output: 1994
