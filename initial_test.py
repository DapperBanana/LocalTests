
def roman_to_int(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_val = 0

    for letter in roman:
        curr_val = roman_numerals[letter]

        if curr_val > prev_val:
            result += curr_val - 2*prev_val
        else:
            result += curr_val

        prev_val = curr_val

    return result

# Test the function
print(roman_to_int('III'))  # Output: 3
print(roman_to_int('IV'))   # Output: 4
print(roman_to_int('IX'))   # Output: 9
print(roman_to_int('LVIII'))  # Output: 58
print(roman_to_int('MCMXCIV'))  # Output: 1994
