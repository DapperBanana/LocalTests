
def roman_to_int(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    
    for i in range(len(roman)):
        if i > 0 and roman_dict[roman[i]] > roman_dict[roman[i-1]]:
            result += roman_dict[roman[i]] - 2 * roman_dict[roman[i-1]]
        else:
            result += roman_dict[roman[i]]
    
    return result

roman_numeral = input("Enter a Roman numeral: ")
integer_value = roman_to_int(roman_numeral)
print(f"The integer value of the Roman numeral {roman_numeral} is: {integer_value}")
