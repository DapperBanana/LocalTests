
def roman_to_int(roman):
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

    for numeral in reversed(roman):
        value = roman_map[numeral]

        if value < prev_value:
            result -= value
        else:
            result += value

        prev_value = value

    return result

# Test the function
roman_numeral = 'XIV'
print(f'The integer value of {roman_numeral} is: {roman_to_int(roman_numeral)}')
