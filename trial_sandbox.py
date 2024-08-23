
def roman_to_int(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for letter in roman:
        curr_value = roman_dict[letter]
        if curr_value > prev_value:
            total += curr_value - 2 * prev_value
        else:
            total += curr_value
        prev_value = curr_value
        
    return total

roman_numeral = input("Enter a Roman numeral: ")
print("The integer value of the Roman numeral is:", roman_to_int(roman_numeral))
