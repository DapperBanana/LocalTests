
def roman_to_int(roman):
    roman_dict = {
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
    
    for letter in roman:
        current_value = roman_dict[letter]
        
        if current_value > prev_value:
            result += current_value - 2 * prev_value  # Subtract twice the previous value if it appears before the current value
        else:
            result += current_value
        
        prev_value = current_value
    
    return result

# Test the function
roman_numeral = 'MCMXCIV'
print(roman_to_int(roman_numeral))  # Output: 1994
