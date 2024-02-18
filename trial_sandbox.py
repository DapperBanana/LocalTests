
def roman_to_int(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for letter in roman:
        value = roman_values[letter]
        if value > prev_value:
            result += value - 2 * prev_value
        else:
            result += value
        prev_value = value
    
    return result

roman_numeral = input("Enter a Roman numeral: ")
print(f"The integer value of the Roman numeral {roman_numeral} is: {roman_to_int(roman_numeral)}")
