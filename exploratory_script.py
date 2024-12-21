
def roman_to_int(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for numeral in roman_numeral:
        value = roman_dict[numeral]
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    
    return total

roman_numeral = input("Enter a Roman numeral: ")
print(f"The integer value of the Roman numeral {roman_numeral} is: {roman_to_int(roman_numeral)}")
