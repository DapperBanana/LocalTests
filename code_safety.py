
def roman_to_int(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for i in range(len(roman_numeral) - 1, -1, -1):
        if roman_dict[roman_numeral[i]] < prev_value:
            result -= roman_dict[roman_numeral[i]]
        else:
            result += roman_dict[roman_numeral[i]]
        
        prev_value = roman_dict[roman_numeral[i]]
    
    return result

roman_numeral = input("Enter a Roman numeral: ")
print(roman_to_int(roman_numeral))
