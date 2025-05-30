
def roman_to_int(roman_numeral):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    
    for i in range(len(roman_numeral)):
        if i > 0 and roman_numerals[roman_numeral[i]] > roman_numerals[roman_numeral[i - 1]]:
            result += roman_numerals[roman_numeral[i]] - 2 * roman_numerals[roman_numeral[i - 1]]
        else:
            result += roman_numerals[roman_numeral[i]]
    
    return result

roman_numeral = input("Enter a Roman numeral: ")
print(f"The integer value of the Roman numeral {roman_numeral} is: {roman_to_int(roman_numeral)}")
