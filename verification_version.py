
def roman_to_int(roman_numeral):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    
    for numeral in roman_numeral:
        value = roman_values[numeral]
        result += value
        
        if prev_value < value:
            result -= 2 * prev_value
        
        prev_value = value
    
    return result

roman_numeral = input("Enter a Roman numeral: ")
integer_value = roman_to_int(roman_numeral)
print("The integer value of the Roman numeral is:", integer_value)
