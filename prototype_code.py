
def roman_to_int(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for letter in roman:
        value = roman_dict[letter]
        if value > prev_value:
            result += value - 2 * prev_value
        else:
            result += value
        prev_value = value
    return result

roman_numeral = input("Enter a Roman numeral: ")
print("The integer value is:", roman_to_int(roman_numeral))
