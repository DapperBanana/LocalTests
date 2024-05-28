
def roman_to_int(roman_numeral):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in roman_numeral:
        current_value = roman_dict[char]
        
        if current_value > prev_value:
            total = total - 2 * prev_value + current_value
        
        else:
            total += current_value
        
        prev_value = current_value
    
    return total

roman_numeral = input("Enter a Roman numeral: ")
print(f"The integer value of Roman numeral {roman_numeral} is: {roman_to_int(roman_numeral)}")
