
def roman_to_int(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for letter in roman:
        value = roman_dict[letter]

        # If the value of the current letter is greater than the value of the previous letter, subtract twice the previous value
        if value > prev_value:
            result += value - 2*prev_value
        else:
            result += value

        prev_value = value

    return result

print(roman_to_int('III')) # Output: 3
print(roman_to_int('IV')) # Output: 4
print(roman_to_int('IX')) # Output: 9
print(roman_to_int('LVIII')) # Output: 58
print(roman_to_int('MCMXCIV')) # Output: 1994
